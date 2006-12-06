##############################################################################
#
# Enfold Enterprise Deployment - Remote Deployment of Content
# Copyright (C) 2005 Enfold Systems
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
##############################################################################
"""
$Id: __init__.py 5961 2006-08-11 02:26:09Z sidnei $
"""
import re
import os
import sys
import os.path
import types
import dateutil.parser

HTML4 = re.compile(
    '^[0-9]{4}-[0-9]{2}-[0-9]{2}'
    'T[0-9]{2}:[0-9]{2}:[0-9]{2}'
    '(Z|[+-][0-9]{2}:[0-9]{2})$')

def copy_file(infile, outfile):
    """ Read binary data from infile and write it to outfile. infile
    and outfile may be strings, in which case a file with that name is
    opened, or filehandles, in which case they are accessed directly.
    """

    if type(infile) is types.StringType:
        instream = open(infile, 'rb')
        read_in = instream.read
        close_in = instream.close
        seek_in = instream.seek
    elif type(infile) is types.IntType:
        # Maybe a file descriptor?
        def read(bytes):
            return os.read(infile, bytes)
        read_in = read
        def close():
            return os.close(infile)
        close_in = close
        def seek(pos, how):
            return os.lseek(infile, pos, how)
        seek_in = seek
    else:
        close_in = 0
        instream = infile
        read_in = instream.read
        seek_in = instream.seek

    if type(outfile) is types.StringType:
        outstream = open(outfile, 'wb')
        write_out = outstream.write
        close_out = outstream.close
    elif type(outfile) is types.IntType:
        # Maybe a file descriptor?
        def write(bytes):
            return os.write(outfile, bytes)
        write_out = write
        def close():
            return os.close(outfile)
        close_out = close
    else:
        close_out = 0
        outstream = outfile
        write_out = outstream.write

    try:
        blocksize = 2 << 16
        block = read_in(blocksize)
        write_out(block)
        while len(block) == blocksize:
            block = read_in(blocksize)
            write_out(block)
        seek_in(0)
    finally:
        if close_in: close_in()
        if close_out: close_out()

def make_target_path(originals, target):
    path = os.path.splitdrive(target)[-1]
    path = path.strip(os.path.sep)
    parts = os.path.split(path)
    destination = os.path.join(originals, *parts)
    return destination

def path2url(path):
    return path.replace(os.path.sep, '/')

def package_home(globals_dict):
    __name__ = globals_dict['__name__']
    m = sys.modules[__name__]
    if hasattr(m, '__path__'):
        r = m.__path__[0]
    elif "." in __name__:
        r = sys.modules[__name__[:__name__.rfind('.')]].__path__[0]
    else:
        r = __name__
    return os.path.abspath(r)

def SetFileSecurity(fname, mode):
    import pywintypes
    import ntsecuritycon

    # General "do the right thing for IIS" function.
    #
    # For early IIS versions that run as LocalSystem, it should
    # already be fine.  For later windows where IIS runs by default as
    # the NetworkService account, we are no good.  We could say either
    # "NT AUTHORITY\\NetworkService" or just "Users" - the latter
    # means we should work even if the IIS user is changed to an
    # explicit user.
    #
    # We just handle "Users" for now, could be expanded.
    #
    # And we can't use the literal 'Users' - it may have been renamed or
    # localized.  See Q157234.  So we use the well-known RID to make a SID.
    sid = pywintypes.SID()
    sid.Initialize(ntsecuritycon.SECURITY_NT_AUTHORITY, 2)
    sid.SetSubAuthority(0, ntsecuritycon.SECURITY_BUILTIN_DOMAIN_RID)
    sid.SetSubAuthority(1, ntsecuritycon.DOMAIN_ALIAS_RID_USERS)

    # Handle 'users' -> roughly equivalent to 'other'
    rights = 0
    if mode & int('0004', 8):
        rights |= ntsecuritycon.GENERIC_READ
    if mode & int('0002', 8):
        rights |= ntsecuritycon.GENERIC_WRITE
    if mode & int('0001', 8):
        rights |= ntsecuritycon.GENERIC_EXECUTE
    _SetFileSecurity(sid, fname, rights)

def _SetFileSecurity(username, fname, rights, inherit_flags=None):
    import win32security
    import pywintypes
    import ntsecuritycon

    # Returns None if no user, True if changed, False if already had
    # rights.
    if inherit_flags is None:
        inherit_flags = (
            ntsecuritycon.CONTAINER_INHERIT_ACE |
            ntsecuritycon.OBJECT_INHERIT_ACE # child objects inherit?
            )

    # Overload the 'username' param - allow it to already be a SID.
    if isinstance(username, pywintypes.SIDType):
        user_sid = username
    else:
        try:
            user_sid = win32security.LookupAccountName(None, username)[0]
        except win32security.error:
            return None

    sd = win32security.GetNamedSecurityInfo(
        fname, 
        win32security.SE_FILE_OBJECT, 
        win32security.DACL_SECURITY_INFORMATION)

    # Walk the dacl, looking for this entry.  Could maybe use
    # GetEffectiveRightsFromACL but that doesn't seem to give inherit
    # info.
    dacl = sd.GetSecurityDescriptorDacl()
    for i in range(dacl.GetAceCount()):
        ace = dacl.GetAce(i)
        ace_type, flags = ace[0]
        sid = ace[-1]
        
        if (ace_type == win32security.ACCESS_ALLOWED_ACE_TYPE and 
            flags & inherit_flags == inherit_flags and 
            ace[1] == rights and 
            sid == user_sid):
            return False

    dacl.AddAccessAllowedAceEx(dacl.GetAclRevision(), inherit_flags,
                               rights,
                               user_sid)
    sd = win32security.SetNamedSecurityInfo(
        fname, 
        win32security.SE_FILE_OBJECT, 
        win32security.DACL_SECURITY_INFORMATION,
        None, None, dacl, None)
    return True

class Utility:

    path = os.path

    def __init__(self, data_prefix, entransit_prefix,
                 package_prefix=None, globals_dict=None):
        if package_prefix is None:
            assert globals_dict is not None
            package_prefix = package_home(globals_dict)
        self.package_prefix = package_prefix
        self.data_prefix = data_prefix
        self.entransit_prefix = entransit_prefix
        self.data_path = self.package_path(*self.data_prefix)

    def join(self, *parts):
        return self.path.sep.join(filter(None, parts))

    def content_path(self, path):
        if isinstance(path, (tuple, list)):
            path = self.join(*path)
        path = self.translate_path(path)
        if path.startswith(self.data_path):
            return path
        parts = self.data_prefix + tuple(path.split('/'))
        path = self.package_path(*parts)
        return path

    def translate_path(self, p):
        p = p.replace(self.entransit_prefix, '').strip(self.path.sep)
        return '/' + '/'.join(filter(None, p.split(self.path.sep)))

    def package_path(self, *args):
        return self.join(self.package_prefix, *args)

    def metadata_path(self, path):
        path = self.content_path(path)
        path.strip(self.path.sep)
        if not path.endswith('.data'):
            path += '.data'
        return path

    def exists(self, path):
        if isinstance(path, unicode):
            path = path.encode('utf-8')
        return (self.path.isfile(path) and
                self.path.exists(path)) and path or False

    def isdir(self, path):
        if isinstance(path, unicode):
            path = path.encode('utf-8')
        return (self.path.isdir(path) and
                self.path.exists(path)) and path or False

    def get_metadata(self, path):
        from xmlrpclib import loads
        path = self.exists(self.metadata_path(path))
        if not path:
            return {}
        md = loads(open(path, 'rb').read())[0][0]
        for k, v in md.items():
            if isinstance(v, str) and HTML4.match(v):
                md[k] = dateutil.parser.parse(v)
        md['path'] = self.content_path(path)
        md['translated_path'] = self.translate_path(path)
        return md
