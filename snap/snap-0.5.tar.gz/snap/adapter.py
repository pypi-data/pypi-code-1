"""
$Id: adapter.py 4142 2006-02-17 13:20:42Z sidnei $
"""
from sets import Set
from snap.utils import isdir, exists, parent, join
from snap.utils import get_metadata, get_rdb_metadata
from snap.utils import traversal_path
from snap.utils import content_path, metadata_path
from snap.content import Content
from snap.metadata import Metadata
from snap.registry import registry
from snap.directory import Directory
from snap.interface import ILocalRoles
from snap.interface import IMetadata

from zope.interface import implements, providedBy
from zope.interface import directlyProvides, directlyProvidedBy
from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces.browser import IBrowserPublisher
from zope.app import zapi
from zope.app.location import locate
from zope.app.traversing.interfaces import ITraversable
from zope.app.traversing.namespace import getResource
from zope.app.security.settings import Allow, Deny, Unset
from zope.app.securitypolicy.interfaces import IPrincipalRoleMap
from zope.app.traversing.interfaces import TraversalError

_marker = object()

class PublishTraverse(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def publishTraverse(self, request, name):
        adapter = ITraversable(self.context)
        if adapter is not None:
            try:
                return adapter.traverse(name, ())
            except TraversalError:
                pass
        view = zapi.queryMultiAdapter(
	    (self.context, request), name=name)
        if view is not None:
            return view
        return getResource(self.context, name, request)

class DirectoryTraverse(PublishTraverse):
    implements(IBrowserPublisher)

    def browserDefault(self, request):
        context = self.context
        path = context.path
        # Need to be sure we are looking at a directory.
        __traceback_info__ = (context, path)
        assert isdir(path), 'Path is not a directory or does not exist'
        fallbacks = ('default.html', 'content.html', 'index.html')
        for fb in fallbacks:
            if exists(content_path(join(path, fb))):
                return self.context, (fb,)
            if exists(metadata_path(join(path, fb))):
                return self.context, (fb,)
        return self.context, ('index.html',)

class ApplicationTraversable(object):
    implements(ITraversable)

    def __init__(self, context):
        self.context = context

    def traverse(self, name, furtherPath):
        node = DirectoryTraversable(self.context).traverse(name, furtherPath)
        marker = registry.get('top_level_markers', {}).get(name)
        if marker is not None:
            directlyProvides(node, marker, directlyProvidedBy(node))
        return node

def acquire_attr(node, attr, default=None):
    if getattr(node, attr, None) is not None:
        return
    current = node
    while parent(current) is not None:
        _parent = parent(current)
        value = getattr(_parent, attr, None)
        if value is not None:
            setattr(node, attr, value)
            return
        current = parent
    # Nothing has been found.
    setattr(node, attr, default)

def metadata_setup(node):
    path = metadata_path(node.path)
    if not exists(path):
        return
    meta = get_metadata(path)
    for key, value in meta.items():
        setattr(node, key, value)
        # XXX factor this out.
        if key in ('local_roles',) and value:
            directlyProvides(node, ILocalRoles, directlyProvidedBy(node))
    uid = getattr(node, 'uid', None)
    if uid is not None:
        record = get_rdb_metadata(node, uid)
        if record is not None:
            for key in record.__slots__:
                if hasattr(node, key):
                    continue
                setattr(node, key, getattr(record, key))
    if not IMetadata.providedBy(node):
        directlyProvides(node, IMetadata, directlyProvidedBy(node))
    # XXX factor this out.
    acquire_attr(node, 'right_column')
    portal_type = getattr(node, 'portal_type', None)
    interface = registry.get('type_markers', {}).get(portal_type)
    if portal_type is not None and interface is not None:
        directlyProvides(node, interface, directlyProvidedBy(node))
    parent_path = '/' + '/'.join(traversal_path(parent(node)))
    marker = registry.get('containment_markers', {}).get(parent_path)
    if marker is not None:
        directlyProvides(node, marker, directlyProvidedBy(node))

class DirectoryTraversable(object):
    implements(ITraversable)

    def __init__(self, context):
        self.context = context

    def traverse(self, name, furtherPath):
        attr = getattr(self.context, name, _marker)
        if attr is not _marker:
            return attr

        if hasattr(self.context, '__getitem__'):
            try:
                return self.context[name]
            except KeyError:
                pass

        # Look for a sub-directory.
        target_path = traversal_path(self.context, name)
        for func, factory, setup in ((content_path, Directory, metadata_setup),):
            path = isdir(func(target_path))
            if path:
                node = factory(path)
                locate(node, self.context, name)
                setup(node)
                return node

        # Look for content or metadata.
        for func, factory, setup in ((content_path, Content, metadata_setup),
                                     (metadata_path, Metadata, metadata_setup)):
            path = exists(func(target_path))
            if path:
                node = factory(path)
                locate(node, self.context, name)
                setup(node)
                return node

        raise TraversalError(self.context, name)

class PrincipalRoleMap(object):

    def __init__(self, context):
        self.context = context
        self.local_roles = getattr(context, 'local_roles', {})
        # Fixup group_ prefix coming from GRUF
        for pid, roles in self.local_roles.items():
            if pid.startswith('group_'):
                del self.local_roles[pid]
                pid = pid[6:]
                # XXX Do we care if there's a group with the same name
                # as a user?
                self.local_roles[pid] = roles
        # Build a reverse mapping to make the implementation saner.
        self.back = bk = {}
        self.exploded = expl = []
        for pid, roles in self.local_roles.items():
            for rid in roles:
                expl.append((rid, pid))
                role = bk.setdefault(rid, Set())
                role.add(pid)

    def getPrincipalsForRole(self, role_id):
        """Get the principals that have been granted a role.

        Return the list of (principal id, setting) who have been assigned or
        removed from a role.

        If no principals have been assigned this role,
        then the empty list is returned.
        """
        for principal_id in self.back.get(role_id, ()):
            yield principal_id, Allow

    def getRolesForPrincipal(self, principal_id):
        """Get the roles granted to a principal.

        Return the list of (role id, setting) assigned or removed from
        this principal.

        If no roles have been assigned to
        this principal, then the empty list is returned.
        """
        for role_id in self.local_roles.get(principal_id, ()):
            yield role_id, Allow

    def getSetting(self, role_id, principal_id):
        """Return the setting for this principal, role combination
        """
        roles = self.local_roles.get(principal_id, ())
        if role_id in roles:
            return Allow
        return Unset

    def getPrincipalsAndRoles(self):
        """Get all settings.

        Return all the principal/role combinations along with the
        setting for each combination as a sequence of tuples with the
        role id, principal id, and setting, in that order.
        """
        for rid, pid in self.exploded:
            yield rid, pid, Allow
