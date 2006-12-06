"""
$Id: directory.py 4194 2006-02-22 17:31:34Z sidnei $
"""

import types
from snap.interface import IDirectory
from snap.utils import traversal_path, content_path, metadata_path
from snap.utils import exists, isdir
from snap.content import Content
from snap.metadata import Metadata
from zope.interface import implements
from zope.app.location import locate

class Directory(object):
    implements(IDirectory)

    def __init__(self, path):
        self.path = path

    def getChildren(self, spec=None):
        if type(spec) in types.StringTypes:
            spec = [spec]
        from snap.adapter import metadata_setup
        children = list()
        path = False
        sub = getattr(self, 'children', ())
        for name in sub:
            target_path = traversal_path(self, name)
            # Look for a sub-directory.
            for func, factory, setup in ((content_path, Directory, metadata_setup),):
                path = isdir(func(target_path))
                if path:
                    node = factory(path)
                    locate(node, self, name)
                    setup(node)
                    if spec is None or node.portal_type in spec:
                        children.append(node)
                    break
            if path:
                continue

            # Look for content or metadata.
            for func, factory, setup in ((content_path, Content,  metadata_setup),
                                         (metadata_path, Metadata, metadata_setup)):
                path = exists(func(target_path))
                if path:
                    node = factory(path)
                    locate(node, self, name)
                    setup(node)
                    if spec is None or node.portal_type in spec:
                        children.append(node)
                    break
        return children
