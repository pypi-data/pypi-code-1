import unittest
from kforge.handlers.modpythontest import ModPythonHandlerTestCase
from kforge.handlers.modpythontest import MockModPythonRequest
from kforge.handlers.projecthost import ProjectAccessHandler
from kforge.handlers.projecthost import ProjectAuthenHandler
from kforge.handlers.apachecodes import *
from kforge.dictionarywords import *


def suite():
    suites = [
        unittest.makeSuite(TestProjectAccessHandler),
        unittest.makeSuite(TestProjectAccessHandler_WithCookie),
        unittest.makeSuite(TestProjectAuthenHandler),
    ]
    return unittest.TestSuite(suites)


class MockProjectAccessRequest(MockModPythonRequest):

    def __init__(self):
        super(MockProjectAccessRequest, self).__init__()
        self.subprocess_env.add('HTTP_USER_AGENT', 'Mozilla')
    

class TestProjectAccessHandler(ModPythonHandlerTestCase):

    requestClass = MockProjectAccessRequest
    handlerClass = ProjectAccessHandler

    def test_isCookieClient(self):
        self.handler.authorise()
        self.failUnless(self.handler.isCookieClient())

    def test_authorise_OK(self):
        self.failUnlessEqual(
            self.handler.authorise(),
            OK
        )
        self.failUnless(self.handler.isAccessAllowed)
        self.failIf(self.handler.session)

    def test_authorise_DENY(self):
        self.request.method = 'POST'
        self.failUnlessEqual(
            self.handler.authorise(),
            OK
        )
        self.failIf(self.handler.isAccessAllowed)
        self.failUnlessEqual(
            self.request.status,
            HTTP_MOVED_TEMPORARILY
        )
        self.failUnless(self.request.err_headers_out.has_key('Location'))
        self.request.uri = '/annakarenina/example'  # visitor is member
        self.request.method = 'GET'
        self.failUnlessEqual(
            self.handler.authorise(),
            OK
        )
        self.failUnlessEqual(
            self.request.status,
            HTTP_MOVED_TEMPORARILY
        )
        self.request.method = 'POST'
        self.failUnlessEqual(
            self.handler.authorise(),
            OK
        )
        self.failUnlessEqual(
            self.request.status,
            HTTP_MOVED_TEMPORARILY
        )
        
    def test_authorise_DEFER(self):
        self.request.method = 'POST'
        self.request.subprocess_env['HTTP_USER_AGENT'] = 'SVN'
        self.failUnlessEqual(
            self.handler.authorise(),
            HTTP_UNAUTHORIZED
        )


class MockProjectAccessRequest_WithCookie(MockProjectAccessRequest):

    def __init__(self):
        super(MockProjectAccessRequest_WithCookie, self).__init__()
        self.addSessionCookie()

    def addSessionCookie(self):
        import dm.view.base
        view = dm.view.base.ControlledAccessView(None)
        person = view.registry.persons['natasha']  # admin for warandpeace
        session = person.sessions.create()
        cookieString = view.makeCookieStringFromSessionKey(session.key)
        cookieName = view.dictionary[AUTH_COOKIE_NAME]
        self.headers_in.add('Cookie', "%s=%s" % (cookieName, cookieString))

        # so we can delete the session after the test
        self.sessionFixture = session


class TestProjectAccessHandler_WithCookie(ModPythonHandlerTestCase):

    requestClass = MockProjectAccessRequest_WithCookie
    handlerClass = ProjectAccessHandler

    def tearDown(self):
        self.request.sessionFixture.delete()
        super(TestProjectAccessHandler_WithCookie, self).tearDown()

    def test_authorise_OK(self):
        self.failUnlessEqual(
            self.handler.authorise(),
            OK
        )
        self.failUnlessEqual(
            self.handler.isAccessAllowed,
            True
        )
        self.failUnless(self.handler.session)
        
    def test_authorise_REDIRECT(self):
        self.request.method = 'POST'
        self.request.uri = '/annakarenina/example'   # natasha not member
        
        self.failUnlessEqual(
            self.handler.authorise(),
            OK
        )
        self.failUnlessEqual(
            self.handler.isAccessAllowed,
            False
        )
        self.failUnless(self.handler.session)
        self.failUnlessEqual(
            self.request.status,
            HTTP_MOVED_TEMPORARILY
        )
        

class MockProjectAuthenRequest(MockModPythonRequest):

    def __init__(self):
        super(MockProjectAuthenRequest, self).__init__()
        self.subprocess_env = {'HTTP_USER_AGENT': 'SVN'}
        self.user = 'admin'
        self.basicAuthPass = 'pass'

    def get_basic_auth_pw(self):
        return self.basicAuthPass


class TestProjectAuthenHandler(ModPythonHandlerTestCase):

    requestClass = MockProjectAuthenRequest
    handlerClass = ProjectAuthenHandler

    def test_isCookieClient(self):
        self.handler.authorise()
        self.failIf(self.handler.isCookieClient())

    def test_authorise_OK(self):
        self.failUnlessEqual(self.handler.authorise(), OK)
        self.request.method = 'POST'
        self.failUnlessEqual(self.handler.authorise(), OK)

    def test_authorise_DENY_visitor(self):
        self.request.method = 'POST'
        self.request.user = ''
        self.failUnlessEqual(
            self.handler.authorise(),
            HTTP_UNAUTHORIZED
        )
        
    def test_authorise_DENY_Mozilla(self):
        self.request.method = 'POST'
        self.request.subprocess_env['HTTP_USER_AGENT'] = 'Mozilla'
        self.failUnlessEqual(
            self.handler.authorise(),
            HTTP_UNAUTHORIZED
        )


