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

"""Command-line script stub that calls the roundup.mailgw.
"""
__docformat__ = 'restructuredtext'

# python version check
from roundup import version_check
from roundup import __version__ as roundup_version

import sys, os, re, cStringIO, getopt

from roundup.mailgw import Message
from roundup.i18n import _

def usage(args, message=None):
    if message is not None:
        print message
    print _('Usage: %(program)s [-v] [-c] [[-C class] -S field=value]* '
        '<instance home> [method]')%{'program': args[0]}
    print _('''
Options:
 -v: print version and exit
 -c: default class of item to create (else the tracker's MAIL_DEFAULT_CLASS)
 -C / -S: see below

The roundup mail gateway may be called in one of four ways:
 . with an instance home as the only argument,
 . with both an instance home and a mail spool file, or
 . with both an instance home and a POP/APOP server account.
 . with both an instance home and a IMAP/IMAPS server account.
 
It also supports optional -C and -S arguments that allows you to set a
fields for a class created by the roundup-mailgw. The default class if
not specified is msg, but the other classes: issue, file, user can
also be used. The -S or --set options uses the same
property=value[;property=value] notation accepted by the command line
roundup command or the commands that can be given on the Subject line
of an email message.

It can let you set the type of the message on a per email address basis.

PIPE:
 In the first case, the mail gateway reads a single message from the
 standard input and submits the message to the roundup.mailgw module.

UNIX mailbox:
 In the second case, the gateway reads all messages from the mail spool
 file and submits each in turn to the roundup.mailgw module. The file is
 emptied once all messages have been successfully handled. The file is
 specified as:
   mailbox /path/to/mailbox

POP:
 In the third case, the gateway reads all messages from the POP server
 specified and submits each in turn to the roundup.mailgw module. The
 server is specified as:
    pop username:password@server
 The username and password may be omitted:
    pop username@server
    pop server
 are both valid. The username and/or password will be prompted for if
 not supplied on the command-line.

APOP:
 Same as POP, but using Authenticated POP:
    apop username:password@server

IMAP:
 Connect to an IMAP server. This supports the same notation as that of
 POP mail.
    imap username:password@server
 It also allows you to specify a specific mailbox other than INBOX using
 this format:
    imap username:password@server mailbox
 
IMAPS:
 Connect to an IMAP server over ssl. 
 This supports the same notation as IMAP.
    imaps username:password@server [mailbox]
 
''')
    return 1

def main(argv):
    '''Handle the arguments to the program and initialise environment.
    '''
    # take the argv array and parse it leaving the non-option
    # arguments in the args array.
    try:
        optionsList, args = getopt.getopt(argv[1:], 'vc:C:S:', ['set=',
            'class='])
    except getopt.GetoptError:
        # print help information and exit:
        usage(argv)
        sys.exit(2)

    for (opt, arg) in optionsList:
        if opt == '-v':
            print '%s (python %s)'%(roundup_version, sys.version.split()[0])
            return

    # figure the instance home
    if len(args) > 0:
        instance_home = args[0]
    else:
        instance_home = os.environ.get('ROUNDUP_INSTANCE', '')
    if not instance_home:
        return usage(argv)

    # get the instance
    import roundup.instance
    instance = roundup.instance.open(instance_home)

    # get a mail handler
    db = instance.open('admin')

    # now wrap in try/finally so we always close the database
    try:
        handler = instance.MailGW(instance, db, optionsList)

        # if there's no more arguments, read a single message from stdin
        if len(args) == 1:
            return handler.do_pipe()

        # otherwise, figure what sort of mail source to handle
        if len(args) < 3:
            return usage(argv, _('Error: not enough source specification information'))
        source, specification = args[1:3]
        if source == 'mailbox':
            return handler.do_mailbox(specification)
        elif source == 'pop':
            m = re.match(r'((?P<user>[^:]+)(:(?P<pass>.+))?@)?(?P<server>.+)',
                specification)
            if m:
                return handler.do_pop(m.group('server'), m.group('user'),
                    m.group('pass'))
            return usage(argv, _('Error: pop specification not valid'))
        elif source == 'apop':
            m = re.match(r'((?P<user>[^:]+)(:(?P<pass>.+))?@)?(?P<server>.+)',
                specification)
            if m:
                return handler.do_apop(m.group('server'), m.group('user'),
                    m.group('pass'))
            return usage(argv, _('Error: apop specification not valid'))
        elif source == 'imap' or source == 'imaps':
            m = re.match(r'((?P<user>[^:]+)(:(?P<pass>.+))?@)?(?P<server>.+)',
                specification)
            if m:
                ssl = 0
                if source == 'imaps':
                    ssl = 1
                mailbox = ''
                if len(args) > 3:
                    mailbox = args[3]
                return handler.do_imap(m.group('server'), m.group('user'),
                    m.group('pass'), mailbox, ssl)

        return usage(argv, _('Error: The source must be either "mailbox",'
            ' "pop", "apop", "imap" or "imaps"'))
    finally:
        handler.db.close()

def run():
    # time out after a minute if we can
    import socket
    if hasattr(socket, 'setdefaulttimeout'):
        socket.setdefaulttimeout(60)
    sys.exit(main(sys.argv))

# call main
if __name__ == '__main__':
    run()

# vim: set filetype=python ts=4 sw=4 et si
