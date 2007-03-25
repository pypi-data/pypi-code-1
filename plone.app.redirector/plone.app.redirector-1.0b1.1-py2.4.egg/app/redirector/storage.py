from zope.interface import implements

from persistent import Persistent
from BTrees.OOBTree import OOBTree, OOSet

from plone.app.redirector.interfaces import IRedirectionStorage

class RedirectionStorage(Persistent):
    """Stores old paths to new paths.
    
    Note - instead of storing "new paths" it could store object ids or 
    similar. In general, there is a many-to-one relationship between 
    "old paths" and "new paths". An "old path" points to exactly one 
    "new path" (where the object is now to be found), but a "new path"
    can be pointed to by multiple different "old paths" (several objects
    that used to be distinct are now consolidated into one).
    
    The following tests (see test_storage.py) demonstrate its usage.
    
        >>> p = RedirectionStorage()
    
    Add one redirect
    
        >>> p.has_path('/foo')
        False
        >>> p.add('/foo', '/bar')
        >>> p.has_path('/foo')
        True
        >>> p.get('/foo')
        '/bar'
        >>> p.has_path('/bar')
        False
        >>> p.redirects('/bar')
        ['/foo']
        
    Note that trailing slashes are ignored:
    
        >>> p.has_path('/foo/')
        True
        >>> p.get('/foo/')
        '/bar'
        >>> p.redirects('/bar/')
        ['/foo']
    
    Circular references are ignored
    
        >>> p.add('/circle', '/circle')
        >>> p.has_path('/circle')
        False
        >>> p.get('/circle', '_marker_')
        '_marker_'
        >>> p.redirects('/circle')
        []
    
    Add another redirect
    
        >>> p.has_path('/baz')
        False
        >>> p.add('/baz', '/bar')
        >>> p.has_path('/baz')
        True
        >>> p.get('/baz')
        '/bar'
        >>> sorted(p.redirects('/bar'))
        ['/baz', '/foo']
        
    Update a redirect
    
        >>> p.add('/foo', '/quux')
        >>> p.has_path('/foo')
        True
        >>> p.get('/foo')
        '/quux'
        >>> p.redirects('/bar')
        ['/baz']
        >>> p.redirects('/quux')
        ['/foo']
    
    Remove a redirect
    
        >>> p.remove('/foo')
        >>> p.has_path('/foo')
        False
        >>> p.get('/foo', default='_notfound_')
        '_notfound_'
        >>> p.redirects('/quux')
        []
    
    Update a redirect in a chain
    
        >>> p.add('/fred', '/foo')
        >>> p.add('/fred', '/barney')
        >>> p.add('/barney', '/wilma')
        >>> p.get('/fred')
        '/wilma'
        >>> p.get('/barney')
        '/wilma'
        >>> sorted(p.redirects('/wilma'))
        ['/barney', '/fred']
        
    Destroy the target of a redirect
    
        >>> p.destroy('/wilma')
        >>> p.has_path('/barney')
        False
        >>> p.has_path('/fred')
        False
        >>> p.redirects('/wilma')
        []
    """
        
    implements(IRedirectionStorage)
    
    def __init__(self):
        self._paths = OOBTree()
        self._rpaths = OOBTree()
    
    def add(self, old_path, new_path):
        old_path = self._canonical(old_path)
        new_path = self._canonical(new_path)
        
        if old_path == new_path:
            return
        
        # Forget any existing reverse paths to old_path
        existing_target = self._paths.get(old_path, None)
        if existing_target is not None and self._rpaths.has_key(existing_target):
            if len(self._rpaths[existing_target]) == 1:
                del self._rpaths[existing_target]
            else:
                self._rpaths[existing_target].remove(old_path)
        
        # Update any references that pointed to old_path
        for p in self.redirects(old_path):
            self._paths[p] = new_path
            self._rpaths.setdefault(new_path, OOSet()).insert(p)
        
        self._paths[old_path] = new_path
        self._rpaths.setdefault(new_path, OOSet()).insert(old_path)
        
    def remove(self, old_path):
        old_path = self._canonical(old_path)
        new_path = self._paths.get(old_path, None)
        if new_path is not None and self._rpaths.has_key(new_path):
            if len(self._rpaths[new_path]) == 1:
                del self._rpaths[new_path]
            else:
                self._rpaths[new_path].remove(old_path)
        del self._paths[old_path]
        
    def destroy(self, new_path):
        new_path = self._canonical(new_path)
        for p in self._rpaths.get(new_path, []):
            if p in self._paths:
                del self._paths[p]
        if self._rpaths.has_key(new_path):
            if new_path in self._rpaths:
                del self._rpaths[new_path]

    def has_path(self, old_path):
        old_path = self._canonical(old_path)
        return bool(self._paths.has_key(old_path))

    def get(self, old_path, default=None):
        old_path = self._canonical(old_path)
        return self._paths.get(old_path, default)

    def redirects(self, new_path):
        new_path = self._canonical(new_path)
        return [a for a in self._rpaths.get(new_path, [])]

    def _canonical(self, path):
        if path.endswith('/'):
            path = path[:-1]
        return path