"""
$Id: utils.py 4141 2006-02-17 13:16:33Z sidnei $
"""

from os import stat
from stat import ST_MTIME
from snap.filter.config import config

_index = None

def parent(node):
    return getattr(node, '__parent__', None)

def traversal_path(context, *extra):
    parts = []
    current = context
    while parent(current) is not None:
        parts.append(getattr(current, '__name__', None))
        current = parent(current)
    parts.reverse()
    parts.extend(extra)
    return tuple(filter(None, parts))

def execute_query(context, query):
    from zope.app import zapi
    from zope.app.rdb import queryForResults
    from zope.app.rdb.interfaces import IZopeDatabaseAdapter
    conn = zapi.getUtility(IZopeDatabaseAdapter, config.db_connection,
                           context=context)()
    return queryForResults(conn, query)

def get_rdb_metadata(context, uid):
    query = "select * from cmf_meta where uid = '%s'" % uid
    results = execute_query(context, query)
    if results:
        return results[0]
    return None

class Proxy(object):

    def __init__(self, tgt, attr):
        self.tgt = tgt
        self.attr = attr

    def __getattribute__(self, name):
        if name in ('tgt', 'attr'):
            return object.__getattribute__(self, name)
        def func(*args, **kw):
            proxy = getattr(self.tgt, self.attr)
            return getattr(proxy, name)(*args, **kw)
        return func

proxy = Proxy(config, 'path')

join = proxy.join
content_path = proxy.content_path
translate_path = proxy.translate_path
package_path = proxy.package_path
metadata_path = proxy.metadata_path
exists = proxy.exists
isdir = proxy.isdir
get_metadata = proxy.get_metadata
