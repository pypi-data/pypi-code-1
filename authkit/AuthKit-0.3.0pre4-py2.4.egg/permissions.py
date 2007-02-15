"""Permission objects

Permission objects are used to define which users should have access to a particular
resource. They are checked using some of the authorization objects either in the
``authkit.authorize`` module or ``authkit.pylons_adaptors`` module if you are using
Pylons.

Permissions objects are very similar to WSGI applications and can perform a
check based on the request or the response. Not all of the authorization
objects have access to the response because the permission might be checked as
part of a code block before the response is generated. This leads to two
classes of permissions, request-based (which can be checked anywhere) and
responce-based which can only be checked when the authorization object has
access to the response. 

All the built-in AuthKit permissions are request-based but you can use the
permissions objects defined in this module or create your own derived from
``authkit.permission.Permission``.

Permissions are described in detail in the AuthKit manual.
"""

from authkit.authorize import PermissionError, NotAuthenticatedError, NotAuthorizedError, middleware
from authkit.authenticate import no_authkit_users_in_environ 

# 
# Permission Classes
#

class PermissionSetupError(Exception):
    pass

class Permission:
    """
    The base class for all permissions objects. 

    The ``check()`` method is called by the authorization object to check the
    permission. Permissions should return the original status, headers and
    response or raise a ``NotAuthorizedError`` when their ``check()`` method is
    called. 

    .. Note ::
    
        The WSGI ``app`` can only be called once by the ``check()`` method.
        This means that you cannot write permisisons objects that perform
        logical ``not`` and ``or`` operations on other permissions objects
        since doing so might require the same app to be called multiple times.
        A permission object to perform an ``and`` operation is feasible and has
        been impleneted as the ``And`` permission class.  
        
   """

    def check(app, environ, start_response): 
        return app(environ, start_response)

class RequestPermission(Permission):
    """
    The base class for all request-based permissions
    """
    # XXX Is this line needed?
    require_response = False

class _TestBadlyLabelledResponseBasedPermission(RequestPermission):
    def check(self, app, environ, start_response):
        def start_response(a,b,c=None):
            return start_response(a,b,c)
        return app(environ, start_response)
        
class UserIn(RequestPermission):
    """
    Checks the ``REMOTE_USER`` is one of the users specified.
    
    Takes the following arguments:

    ``users``
        A list of usernames which are valid

    If there is no ``REMOTE_USER`` a ``NotAuthenticatedError`` is raised. If
    the ``REMOTE_USER`` is not in ``users`` a ``NotAuthorizedError`` is raised.

    Usernames supplied to ``users`` are treated case insensitively.
    """

    def __init__(self, users):
        if isinstance(users, list) or isinstance(users, tuple):
            users_ = []
            for user in users:
                users_.append(user.lower())
            self.users = users_
        elif isinstance(users, str):
            self.users = [users]
        else:
            raise PermissionSetupError('Expected users to be a list or a string, not %r'%users)
      
    def check(self, app, environ, start_response):
        if not environ.has_key('REMOTE_USER'):
            raise NotAuthenticatedError('Not Authenticated')
        if environ['REMOTE_USER'] not in self.users:
            raise NotAuthorizedError('You are not one of the users allowed to access this resource.')
        return app(environ, start_response)

class Exists(RequestPermission):
    """
    Checks the specified key is present in the ``environ``.
    
    Takes the following arguments:

    ``key``
        The required key

    ``error``
        The error to be raised if the key is missing. XXX This argument may be deprecated soon.

    """

    def __init__(self, key, error=NotAuthorizedError('Not Authorised')):
        self.key = key
        self.error = error
    
    def check(self, app, environ, start_response):
        if not environ.has_key(self.key):
            raise self.error
        return app(environ, start_response)
        
class And(RequestPermission):
    """
    Checks all the permission objects listed as keyword arguments in turn.
    Permissions are checked from left to right. The error raised by the ``And``
    permission is the error raised by the first permission check to fail.
    """

    def __init__(self, *permissions):
        if len(permissions) < 2:
            raise PermissionSetupError('Expected at least 2 permissions objects')
        list(permissions).reverse()
        self.permissions = permissions
        
    def check(self, app, environ, start_response):
        for permission in self.permissions:
            app = middleware(app, permission)
        #raise Exception(app, self.permissions)
        return app(environ, start_response)

class RemoteUser(RequestPermission):
    """
    Checks someone is signed in by checking for the presence of the
    ``REMOTE_USER``.
    
    If ``accept_empty`` is ``False`` (the default) then the value of the
    ``REMOTE_USER`` must evaluate to ``True`` in Python.
    """

    def __init__(self, accept_empty=False):
        self.accept_empty = accept_empty

    def check(self, app, environ, start_response):
        if not environ.has_key('REMOTE_USER'):
            raise NotAuthenticatedError('Not Authenticated')
        elif self.accept_empty==False and not environ['REMOTE_USER']:
            raise NotAuthorizedError('Not Authorised')
        return app(environ, start_response)

#
# Permissions to work with the AuthKit user management API
#

class HasAuthKitRole(RequestPermission):
    """
    Designed to work with the user management API described in the AuthKit manual.

    This permission checks that the signed in user has any if the roles specified
    in ``roles``. If ``all`` is ``True``, the user must have all the roles for
    the permission check to pass.
    """

    def __init__(self, roles, all=False, error=None):
        if isinstance(roles, str):
            roles = [roles]
        self.all = all
        self.roles = roles
        self.error = error
        
    def check(self, app, environ, start_response):
        """
        Should return True if the user has the role or
        False if the user doesn't exist or doesn't have the role.

        In this implementation role names are case insensitive.
        """
        if not environ.has_key('REMOTE_USER'):
            if self.error: 
                raise self.error
            raise NotAuthenticatedError('Not authenticated')
            
        if not environ.has_key('authkit.users'):
            raise no_authkit_users_in_environ
        users = environ['authkit.users']
        
        if not users.passwords.has_key(environ['REMOTE_USER']):
            raise NotAuthorizedError('No such user')

        if not users.roles.has_key(environ['REMOTE_USER']):
            if self.roles == None:
                return app(environ, start_response)
            else:
                raise NotAuthorizedError("User has no roles specified")
        
        if not self.all:
            for role in self.roles:
                if role.lower() in users.roles[environ['REMOTE_USER']]:
                    return app(environ, start_response)
            if self.error:
                raise self.error
            else:
                raise NotAuthorizedError("User doesn't have any of the specified roles")
        else:
            for role in self.roles:
                if role.lower() not in users.roles[environ['REMOTE_USER']]:
                    if self.error:
                        raise self.error
                    else:
                        raise NotAuthorizedError("User doesn't have the role %s"%role.lower())
            return app(environ, start_response)

    
class HasAuthKitGroup(RequestPermission):
    """
    Designed to work with the user management API described in the AuthKit manual.

    This permission checks that the signed in user is in one of the groups specified
    in ``groups``.
    """

    def __init__(self, groups, error=None):
        if isinstance(groups, str):
            groups = [groups]
        self.groups = groups
        self.error = error
        
    def check(self, app, environ, start_response):
        """
        Should return True if the user has the group or
        False if the user doesn't exist or doesn't have the group.

        In this implementation group names are case insensitive.
        """
        if not environ.has_key('REMOTE_USER'):
            if self.error: 
                raise self.error
            raise NotAuthenticatedError('Not authenticated')
            
        if not environ.has_key('authkit.users'):
            raise no_authkit_users_in_environ
        users = environ['authkit.users']
        if not users.passwords.has_key(environ['REMOTE_USER']):
            raise NotAuthorizedError('No such user')
        if not users.groups.has_key(environ['REMOTE_USER']) and self.groups == None:
            return app(environ, start_response)
        elif self.groups == None:
            if self.error:
                raise self.error
            else:
                raise NotAuthorizedError("User is not a member of any group")
        for group in self.groups:
            if users.groups[environ['REMOTE_USER']] == group.lower():
                return app(environ, start_response)
        if self.error:
            raise self.error
        else:
            raise NotAuthorizedError("User is not a member of the specified group(s) %r"%self.groups)
    
class ValidAuthKitUser(UserIn):
    """
    Checks that the signed in user is one of the users specified when setting up
    the user management API.
    """
    def __init__(self):
        pass
    
    def check(environ, start_response):
        if not environ.has_key('authkit.users'):
            raise no_authkit_users_in_environ
        self.users = environ['authkit.users'].usernames
        return UserIn.check(self, environ, start_response)

