from kforge.django.apps.kui.views.base import KforgeView
import kforge.command
import kforge.command.misc
from kforge.exceptions import KforgeCommandError
import random

class AuthenticateView(KforgeView):

    def __init__(self, **kwds):
        super(AuthenticateView, self).__init__(**kwds)
        self.isAuthenticateFail = False
        self.forgotPassword = False

    def setMinorNavigationItems(self):
        self.minorNavigation = [
            {'title': 'Welcome', 'url': '/'},
        ]
        if self.session:
            self.minorNavigation.append(
                {'title': 'Log out',      'url': '/logout/'},
            )
            self.minorNavigation.append(
                {'title': 'Join project', 'url': '/project/'},
            )
        else:
            self.minorNavigation.append(
                {'title': 'Log in',       'url': '/login/'},
            )
            self.minorNavigation.append(
                {'title': 'Register',     'url': '/person/create/'},
            )

    def canAccess(self):
        return True

    def authenticate(self):
        if self.session:
            return True
        params = self.request.POST.copy()
        name = params['name']
        forgotpassword = params.get('forgotpassword', False)
        if forgotpassword:
            # TODO: might want to indicate error if mailing fails
            self.forgotPassword = True
            cmd = kforge.command.misc.EmailNewPassword(name)
            try:
                cmd.execute()
            except KforgeCommandError, inst:
                msg = "EmailNewPassword failed for user: '%s' (%s)" % (name,
                        inst)
                self.logger.warn(msg)
            return # early out
        password = params['password']
        self.rememberme = params.get('rememberme', None)
        command = kforge.command.PersonAuthenticate(name, password)
        try:
            command.execute()
        except KforgeCommandError, inst:
            msg = "Login authentication failure for person name '%s'." % name
            self.logger.warn(msg)
        else:
            self.startSession(command.person)


    def setContext(self):
        super(AuthenticateView, self).setContext()
        self.setAuthenticationContext()
        self.context.update({
            'canCreatePerson': self.canCreatePerson(),
            'isAuthenticateFail': self.isAuthenticateFail,
            'forgotPassword': self.forgotPassword,
        })

    def setAuthenticationContext(self):
        if self.request.POST:
            params = self.request.POST.copy()
            self.context.update({
                'name': params.get('name', ''),
                'password': params.get('password', ''),
            })


class LoginView(AuthenticateView):

    templatePath = 'login'
    minorNavigationItem = '/login/'

    def login(self, returnPath=''):
        if self.request.POST:
            self.authenticate()
            params = self.request.POST.copy()
            returnPath = params.get('returnPath', '')
            if returnPath:
                self.returnPath = returnPath
            if self.session:
                if returnPath:
                    self.setRedirect(returnPath)
            else:
                self.isAuthenticateFail = True
        elif returnPath:
            self.returnPath = returnPath
        return self.getResponse()


class LogoutView(AuthenticateView):

    templatePath = 'logout'
    minorNavigationItem = '/logout/'

    def logout(self, redirectPath=''):
        self.redirectPath = redirectPath
        self.stopSession()
        return self.getResponse()


def login(request, returnPath=''):
    return LoginView(request=request).login(returnPath)

def logout(request, redirect=''):
    return LogoutView(request=request).logout(redirect)

