"""
$Id: content.py 3965 2006-01-26 13:50:03Z sidnei $
"""

from snap.interface import IContent
from zope.interface import implements

class Content(object):
    implements(IContent)

    def __init__(self, path):
        self.path = path
