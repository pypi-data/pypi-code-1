"""
$Id: app.py 3965 2006-01-26 13:50:03Z sidnei $
"""
from snap.interface import IApplicationRoot
from snap.adapter import PublishTraverse
from zope.interface import implements
from zope.publisher.interfaces import IPublishTraverse

class Application(object):
    implements(IApplicationRoot, IPublishTraverse)

    def publishTraverse(self, request, name):
        return PublishTraverse(self, request).publishTraverse(request, name)

    def __call__(self):
        return 'Wee!'

app = Application()
