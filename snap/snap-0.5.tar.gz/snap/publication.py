"""
$Id: publication.py 4257 2006-03-03 02:02:19Z sidnei $
"""

from snap.app import app
from zope import component
from zope.interface import implements
from zope.security.checker import ProxyFactory
from zope.security.proxy import removeSecurityProxy
from zope.publisher.browser import BrowserRequest
from zope.publisher.interfaces.browser import ISkin
from zope.app.publication.interfaces import IBrowserRequestFactory
from zope.app.publication.interfaces import IRequestPublicationFactory
from zope.app.publication.browser import BrowserPublication
from zope.app.publisher.browser import applySkin

class Publication(BrowserPublication):

    def getApplication(self, request):
        """Returns the object where traversal should commence.
        """
        # Look for a defined 'snap.skin' variable defined in the
        # request environment by the 'config' wsgi-filter and if
        # found, switch the skin to that.
        skin = request.get('snap.skin')
        if skin is not None:
            stack = request.getTraversalStack()
            # Check if a skin is not already setup.
            if not filter(None, ['++skin++' in part for part in stack]):
                skin = component.queryUtility(ISkin, skin, default=None)
                if skin is not None:
                    applySkin(request, skin)

        proxies = request.get('snap.security.proxies', None)
        if proxies in ('off', 'disable', 'false'):
            return app
        return ProxyFactory(app)

    def traverseName(self, request, ob, name):
        proxies = request.get('snap.security.proxies', None)
        remove_proxies = proxies in ('off', 'disable', 'false')
        if remove_proxies:
            ob = removeSecurityProxy(ob)
        subob = super(Publication, self).traverseName(request, ob, name)
        if remove_proxies:
            return removeSecurityProxy(subob)
        return subob

class PublicationFactory(object):

    implements(IRequestPublicationFactory)

    def canHandle(self, environment):
        return bool(environment.get('snap.enabled'))

    def __call__(self):
        request_class = component.queryUtility(
            IBrowserRequestFactory, default=BrowserRequest)
        return request_class, Publication
