"""
$Id: metadata.py 3965 2006-01-26 13:50:03Z sidnei $
"""

from snap.interface import IMetadata
from zope.interface import implements

class Metadata(object):
    implements(IMetadata)

    def __init__(self, path):
        self.path = path
