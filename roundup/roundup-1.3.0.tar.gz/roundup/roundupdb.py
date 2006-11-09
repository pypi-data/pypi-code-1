from __future__ import nested_scopes
#
# Copyright (c) 2001 Bizar Software Pty Ltd (http://www.bizarsoftware.com.au/)
# This module is free software, and you may redistribute it and/or modify
# under the same terms as Python, so long as this copyright message and
# disclaimer are retained in their original form.
#
# IN NO EVENT SHALL BIZAR SOFTWARE PTY LTD BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING
# OUT OF THE USE OF THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# BIZAR SOFTWARE PTY LTD SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS"
# BASIS, AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
# SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
#
# $Id$

"""Extending hyperdb with types specific to issue-tracking.
"""
__docformat__ = 'restructuredtext'

import re, os, smtplib, socket, time, random
import cStringIO, base64, quopri, mimetypes

from rfc2822 import encode_header

from roundup import password, date, hyperdb
from roundup.i18n import _

# MessageSendError is imported for backwards compatibility
from roundup.mailer import Mailer, straddr, MessageSendError

class Database:

    # remember the journal uid for the current journaltag so that:
    # a. we don't have to look it up every time we need it, and
    # b. if the journaltag disappears during a transaction, we don't barf
    #    (eg. the current user edits their username)
    journal_uid = None
    def getuid(self):
        """Return the id of the "user" node associated with the user
        that owns this connection to the hyperdatabase."""
        if self.journaltag is None:
            return None
        elif self.journaltag == 'admin':
            # admin user may not exist, but always has ID 1
            return '1'
        else:
            if (self.journal_uid is None or self.journal_uid[0] !=
                    self.journaltag):
                uid = self.user.lookup(self.journaltag)
                self.journal_uid = (self.journaltag, uid)
            return self.journal_uid[1]

    def setCurrentUser(self, username):
        """Set the user that is responsible for current database
        activities.
        """
        self.journaltag = username

    def isCurrentUser(self, username):
        """Check if a given username equals the already active user.
        """
        return self.journaltag == username

    def getUserTimezone(self):
        """Return user timezone defined in 'timezone' property of user class.
        If no such property exists return 0
        """
        userid = self.getuid()
        timezone = None
        try:
            tz = self.user.get(userid, 'timezone')
            date.get_timezone(tz)
            timezone = tz
        except KeyError:
            pass
        # If there is no class 'user' or current user doesn't have timezone
        # property or that property is not set assume he/she lives in
        # the timezone set in the tracker config.
        if timezone is None:
            timezone = self.config['TIMEZONE']
        return timezone

    def confirm_registration(self, otk):
        props = self.getOTKManager().getall(otk)
        for propname, proptype in self.user.getprops().items():
            value = props.get(propname, None)
            if value is None:
                pass
            elif isinstance(proptype, hyperdb.Date):
                props[propname] = date.Date(value)
            elif isinstance(proptype, hyperdb.Interval):
                props[propname] = date.Interval(value)
            elif isinstance(proptype, hyperdb.Password):
                props[propname] = password.Password()
                props[propname].unpack(value)

        # tag new user creation with 'admin'
        self.journaltag = 'admin'

        # create the new user
        cl = self.user

        props['roles'] = self.config.NEW_WEB_USER_ROLES
        userid = cl.create(**props)
        # clear the props from the otk database
        self.getOTKManager().destroy(otk)
        self.commit()

        return userid


class DetectorError(RuntimeError):
    """ Raised by detectors that want to indicate that something's amiss
    """
    pass

# deviation from spec - was called IssueClass
class IssueClass:
    """This class is intended to be mixed-in with a hyperdb backend
    implementation. The backend should provide a mechanism that
    enforces the title, messages, files, nosy and superseder
    properties:

    - title = hyperdb.String(indexme='yes')
    - messages = hyperdb.Multilink("msg")
    - files = hyperdb.Multilink("file")
    - nosy = hyperdb.Multilink("user")
    - superseder = hyperdb.Multilink(classname)
    """

    # The tuple below does not affect the class definition.
    # It just lists all names of all issue properties
    # marked for message extraction tool.
    #
    # XXX is there better way to get property names into message catalog??
    #
    # Note that this list also includes properties
    # defined in the classic template:
    # assignedto, topic, priority, status.
    (
        ''"title", ''"messages", ''"files", ''"nosy", ''"superseder",
        ''"assignedto", ''"topic", ''"priority", ''"status",
        # following properties are common for all hyperdb classes
        # they are listed here to keep things in one place
        ''"actor", ''"activity", ''"creator", ''"creation",
    )

    # New methods:
    def addmessage(self, nodeid, summary, text):
        """Add a message to an issue's mail spool.

        A new "msg" node is constructed using the current date, the user that
        owns the database connection as the author, and the specified summary
        text.

        The "files" and "recipients" fields are left empty.

        The given text is saved as the body of the message and the node is
        appended to the "messages" field of the specified issue.
        """

    def nosymessage(self, nodeid, msgid, oldvalues, whichnosy='nosy',
            from_address=None, cc=[], bcc=[]):
        """Send a message to the members of an issue's nosy list.

        The message is sent only to users on the nosy list who are not
        already on the "recipients" list for the message.

        These users are then added to the message's "recipients" list.

        If 'msgid' is None, the message gets sent only to the nosy
        list, and it's called a 'System Message'.

        The "cc" argument indicates additional recipients to send the
        message to that may not be specified in the message's recipients
        list.

        The "bcc" argument also indicates additional recipients to send the
        message to that may not be specified in the message's recipients
        list. These recipients will not be included in the To: or Cc:
        address lists.
        """
        if msgid:
            authid = self.db.msg.get(msgid, 'author')
            recipients = self.db.msg.get(msgid, 'recipients', [])
        else:
            # "system message"
            authid = None
            recipients = []

        sendto = []
        bcc_sendto = []
        seen_message = {}
        for recipient in recipients:
            seen_message[recipient] = 1

        def add_recipient(userid, to):
            # make sure they have an address
            address = self.db.user.get(userid, 'address')
            if address:
                to.append(address)
                recipients.append(userid)

        def good_recipient(userid):
            # Make sure we don't send mail to either the anonymous
            # user or a user who has already seen the message.
            return (userid and
                    (self.db.user.get(userid, 'username') != 'anonymous') and
                    not seen_message.has_key(userid))

        # possibly send the message to the author, as long as they aren't
        # anonymous
        if (good_recipient(authid) and
            (self.db.config.MESSAGES_TO_AUTHOR == 'yes' or
             (self.db.config.MESSAGES_TO_AUTHOR == 'new' and not oldvalues))):
            add_recipient(authid, sendto)

        if authid:
            seen_message[authid] = 1

        # now deal with the nosy and cc people who weren't recipients.
        for userid in cc + self.get(nodeid, whichnosy):
            if good_recipient(userid):
                add_recipient(userid, sendto)

        # now deal with bcc people.
        for userid in bcc:
            if good_recipient(userid):
                add_recipient(userid, bcc_sendto)

        if oldvalues:
            note = self.generateChangeNote(nodeid, oldvalues)
        else:
            note = self.generateCreateNote(nodeid)

        # If we have new recipients, update the message's recipients
        # and send the mail.
        if sendto or bcc_sendto:
            if msgid is not None:
                self.db.msg.set(msgid, recipients=recipients)
            self.send_message(nodeid, msgid, note, sendto, from_address,
                bcc_sendto)

    # backwards compatibility - don't remove
    sendmessage = nosymessage

    def send_message(self, nodeid, msgid, note, sendto, from_address=None,
            bcc_sendto=[]):
        '''Actually send the nominated message from this node to the sendto
           recipients, with the note appended.
        '''
        users = self.db.user
        messages = self.db.msg
        files = self.db.file

        if msgid is None:
            inreplyto = None
            messageid = None
        else:
            inreplyto = messages.get(msgid, 'inreplyto')
            messageid = messages.get(msgid, 'messageid')

        # make up a messageid if there isn't one (web edit)
        if not messageid:
            # this is an old message that didn't get a messageid, so
            # create one
            messageid = "<%s.%s.%s%s@%s>"%(time.time(), random.random(),
                                           self.classname, nodeid,
                                           self.db.config.MAIL_DOMAIN)
            if msgid is not None:
                messages.set(msgid, messageid=messageid)

        # compose title
        cn = self.classname
        title = self.get(nodeid, 'title') or '%s message copy'%cn

        # figure author information
        if msgid:
            authid = messages.get(msgid, 'author')
            authname = users.get(authid, 'realname')
            if not authname:
                authname = users.get(authid, 'username', '')
            authaddr = users.get(authid, 'address', '')
        else:
            # "system message"
            authid = None
            authname = 'admin'
            authaddr = self.db.config.ADMIN_EMAIL

        if authaddr:
            authaddr = " <%s>" % straddr( ('',authaddr) )

        # make the message body
        m = ['']

        # put in roundup's signature
        if self.db.config.EMAIL_SIGNATURE_POSITION == 'top':
            m.append(self.email_signature(nodeid, msgid))

        # add author information
        if authid:
            if len(self.get(nodeid,'messages')) == 1:
                m.append(_("New submission from %(authname)s%(authaddr)s:")
                    % locals())
            else:
                m.append(_("%(authname)s%(authaddr)s added the comment:")
                    % locals())
        else:
            m.append(_("System message:"))
        m.append('')

        # add the content
        if msgid is not None:
            m.append(messages.get(msgid, 'content', ''))

        # add the change note
        if note:
            m.append(note)

        # put in roundup's signature
        if self.db.config.EMAIL_SIGNATURE_POSITION == 'bottom':
            m.append(self.email_signature(nodeid, msgid))

        # encode the content as quoted-printable
        charset = getattr(self.db.config, 'EMAIL_CHARSET', 'utf-8')
        m = '\n'.join(m)
        if charset != 'utf-8':
            m = unicode(m, 'utf-8').encode(charset)
        content = cStringIO.StringIO(m)
        content_encoded = cStringIO.StringIO()
        quopri.encode(content, content_encoded, 0)
        content_encoded = content_encoded.getvalue()

        # get the files for this message
        if msgid is None:
            message_files = None
        else:
            message_files = messages.get(msgid, 'files')

        # make sure the To line is always the same (for testing mostly)
        sendto.sort()

        # make sure we have a from address
        if from_address is None:
            from_address = self.db.config.TRACKER_EMAIL

        # additional bit for after the From: "name"
        from_tag = getattr(self.db.config, 'EMAIL_FROM_TAG', '')
        if from_tag:
            from_tag = ' ' + from_tag

        subject = '[%s%s] %s'%(cn, nodeid, title)
        author = (authname + from_tag, from_address)

        # send an individual message per recipient?
        if self.db.config.NOSY_EMAIL_SENDING != 'single':
            sendto = [[address] for address in sendto]
        else:
            sendto = [sendto]

        # now send one or more messages
        # TODO: I believe we have to create a new message each time as we
        # can't fiddle the recipients in the message ... worth testing
        # and/or fixing some day
        first = True
        for sendto in sendto:
            # create the message
            mailer = Mailer(self.db.config)
            message, writer = mailer.get_standard_message(sendto, subject,
                author)

            # set reply-to to the tracker
            tracker_name = self.db.config.TRACKER_NAME
            if charset != 'utf-8':
                tracker = unicode(tracker_name, 'utf-8').encode(charset)
            tracker_name = encode_header(tracker_name, charset)
            writer.addheader('Reply-To', straddr((tracker_name, from_address)))

            # message ids
            if messageid:
                writer.addheader('Message-Id', messageid)
            if inreplyto:
                writer.addheader('In-Reply-To', inreplyto)

            # attach files
            if message_files:
                part = writer.startmultipartbody('mixed')
                part = writer.nextpart()
                part.addheader('Content-Transfer-Encoding', 'quoted-printable')
                body = part.startbody('text/plain; charset=%s'%charset)
                body.write(content_encoded)
                for fileid in message_files:
                    name = files.get(fileid, 'name')
                    mime_type = files.get(fileid, 'type')
                    content = files.get(fileid, 'content')
                    part = writer.nextpart()
                    if mime_type == 'text/plain':
                        part.addheader('Content-Disposition',
                            'attachment;\n filename="%s"'%name)
                        try:
                            content.decode('ascii')
                        except UnicodeError:
                            # the content cannot be 7bit-encoded.
                            # use quoted printable
                            part.addheader('Content-Transfer-Encoding',
                                'quoted-printable')
                            body = part.startbody('text/plain')
                            body.write(quopri.encodestring(content))
                        else:
                            part.addheader('Content-Transfer-Encoding', '7bit')
                            body = part.startbody('text/plain')
                            body.write(content)
                    else:
                        # some other type, so encode it
                        if not mime_type:
                            # this should have been done when the file was saved
                            mime_type = mimetypes.guess_type(name)[0]
                        if mime_type is None:
                            mime_type = 'application/octet-stream'
                        part.addheader('Content-Disposition',
                            'attachment;\n filename="%s"'%name)
                        part.addheader('Content-Transfer-Encoding', 'base64')
                        body = part.startbody(mime_type)
                        body.write(base64.encodestring(content))
                writer.lastpart()
            else:
                writer.addheader('Content-Transfer-Encoding',
                    'quoted-printable')
                body = writer.startbody('text/plain; charset=%s'%charset)
                body.write(content_encoded)

            if first:
                mailer.smtp_send(sendto + bcc_sendto, message)
            else:
                mailer.smtp_send(sendto, message)
            first = False

    def email_signature(self, nodeid, msgid):
        ''' Add a signature to the e-mail with some useful information
        '''
        # simplistic check to see if the url is valid,
        # then append a trailing slash if it is missing
        base = self.db.config.TRACKER_WEB
        if (not isinstance(base , type('')) or
            not (base.startswith('http://') or base.startswith('https://'))):
            web = "Configuration Error: TRACKER_WEB isn't a " \
                "fully-qualified URL"
        else:
            if not base.endswith('/'):
                base = base + '/'
            web = base + self.classname + nodeid

        # ensure the email address is properly quoted
        email = straddr((self.db.config.TRACKER_NAME,
            self.db.config.TRACKER_EMAIL))

        line = '_' * max(len(web)+2, len(email))
        return '\n%s\n%s\n<%s>\n%s'%(line, email, web, line)


    def generateCreateNote(self, nodeid):
        """Generate a create note that lists initial property values
        """
        cn = self.classname
        cl = self.db.classes[cn]
        props = cl.getprops(protected=0)

        # list the values
        m = []
        prop_items = props.items()
        prop_items.sort()
        for propname, prop in prop_items:
            value = cl.get(nodeid, propname, None)
            # skip boring entries
            if not value:
                continue
            if isinstance(prop, hyperdb.Link):
                link = self.db.classes[prop.classname]
                if value:
                    key = link.labelprop(default_to_id=1)
                    if key:
                        value = link.get(value, key)
                else:
                    value = ''
            elif isinstance(prop, hyperdb.Multilink):
                if value is None: value = []
                l = []
                link = self.db.classes[prop.classname]
                key = link.labelprop(default_to_id=1)
                if key:
                    value = [link.get(entry, key) for entry in value]
                value.sort()
                value = ', '.join(value)
            else:
                value = str(value)
                if '\n' in value:
                    value = '\n'+self.indentChangeNoteValue(value)
            m.append('%s: %s'%(propname, value))
        m.insert(0, '----------')
        m.insert(0, '')
        return '\n'.join(m)

    def generateChangeNote(self, nodeid, oldvalues):
        """Generate a change note that lists property changes
        """
        if not isinstance(oldvalues, type({})):
            raise TypeError("'oldvalues' must be dict-like, not %s."%
                type(oldvalues))

        cn = self.classname
        cl = self.db.classes[cn]
        changed = {}
        props = cl.getprops(protected=0)

        # determine what changed
        for key in oldvalues.keys():
            if key in ['files','messages']:
                continue
            if key in ('actor', 'activity', 'creator', 'creation'):
                continue
            # not all keys from oldvalues might be available in database
            # this happens when property was deleted
            try:
                new_value = cl.get(nodeid, key)
            except KeyError:
                continue
            # the old value might be non existent
            # this happens when property was added
            try:
                old_value = oldvalues[key]
                if type(new_value) is type([]):
                    new_value.sort()
                    old_value.sort()
                if new_value != old_value:
                    changed[key] = old_value
            except:
                changed[key] = new_value

        # list the changes
        m = []
        changed_items = changed.items()
        changed_items.sort()
        for propname, oldvalue in changed_items:
            prop = props[propname]
            value = cl.get(nodeid, propname, None)
            if isinstance(prop, hyperdb.Link):
                link = self.db.classes[prop.classname]
                key = link.labelprop(default_to_id=1)
                if key:
                    if value:
                        value = link.get(value, key)
                    else:
                        value = ''
                    if oldvalue:
                        oldvalue = link.get(oldvalue, key)
                    else:
                        oldvalue = ''
                change = '%s -> %s'%(oldvalue, value)
            elif isinstance(prop, hyperdb.Multilink):
                change = ''
                if value is None: value = []
                if oldvalue is None: oldvalue = []
                l = []
                link = self.db.classes[prop.classname]
                key = link.labelprop(default_to_id=1)
                # check for additions
                for entry in value:
                    if entry in oldvalue: continue
                    if key:
                        l.append(link.get(entry, key))
                    else:
                        l.append(entry)
                if l:
                    l.sort()
                    change = '+%s'%(', '.join(l))
                    l = []
                # check for removals
                for entry in oldvalue:
                    if entry in value: continue
                    if key:
                        l.append(link.get(entry, key))
                    else:
                        l.append(entry)
                if l:
                    l.sort()
                    change += ' -%s'%(', '.join(l))
            else:
                change = '%s -> %s'%(oldvalue, value)
                if '\n' in change:
                    value = self.indentChangeNoteValue(str(value))
                    oldvalue = self.indentChangeNoteValue(str(oldvalue))
                    change = '\nNow:\n%s\nWas:\n%s'%(value, oldvalue)
            m.append('%s: %s'%(propname, change))
        if m:
            m.insert(0, '----------')
            m.insert(0, '')
        return '\n'.join(m)

    def indentChangeNoteValue(self, text):
        lines = text.rstrip('\n').split('\n')
        lines = [ '  '+line for line in lines ]
        return '\n'.join(lines)

# vim: set filetype=python sts=4 sw=4 et si :
