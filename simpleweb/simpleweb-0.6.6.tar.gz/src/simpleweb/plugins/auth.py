import simpleweb.utils

class AuthUser(object):
	def __init__(self, username=None, roles=[]):
		self.username = username
		self.roles = roles


class SimpleAuth(object):
	def __init__(self):
		self.authuser_class = AuthUser

	def authenticated(self, request, username, roles=[]):
		user = AuthUser(username, roles)
		request.session[simpleweb.utils.ENV_KEY_AUTH_MIDDLEWARE] = user

	
	@staticmethod
	def require(users=[], roles=[]):

		def filter_inroles(arole):
			if arole in roles:
				return True
			else:
				return False

		def wrapper(func):

			def inner(*args, **kw):
				request = args[0]
				if request.session.user.username in users or filter(filter_inroles, request.session.user.roles):
					return func(*args, **kw)
				else:
					return "Username or UserRole insufficient to access this resource!"

			#after decorating the methods, the names change from GET, POST, etc, to inner(), 
			#this fixes that.

			inner.__name__ = func.__name__
			inner.__dict__ = func.__dict__
			inner.__doc__ = func.__doc__
			return inner

		return wrapper

