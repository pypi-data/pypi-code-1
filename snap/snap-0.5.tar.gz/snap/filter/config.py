"""
$Id: config.py 4067 2006-02-14 00:59:11Z sidnei $
"""

import sys
import warnings
from threading import local
from snap.path import Utility
from zope.app import zapi
from zope.app.rdb.interfaces import IZopeDatabaseAdapter

_import_chickens = {}, {}, ("*",) # dead chickens needed by __import__

def resolve(dottedname):

    name = dottedname.strip()
    if not name:
        raise ValueError("The given name is blank")

    names = name.split('.')
    if not names[-1]:
        raise ValueError(
            "Trailing dots are no longer supported in dotted names")

    if len(names) == 1:
        # Check for built-in objects
        marker = object()
        obj = __builtins__.get(names[0], marker)
        if obj is not marker:
            return obj

    if not names[0]:
        raise ValueError(
            "Can't use leading dots in dotted names")

    # Split off object name:
    oname, mname = names[-1], '.'.join(names[:-1])

    # Import the module
    if not mname:
        # Just got a single name. Must be a module
        mname = oname
        oname = ''

    try:
        mod = __import__(mname, *_import_chickens)
    except ImportError, v:
        raise

    if not oname:
        # see not mname case above
        return mod

    try:
        obj = getattr(mod, oname)
        return obj
    except AttributeError:
        # No such name, maybe it's a module that we still need to import
        try:
            return __import__(mname+'.'+oname, *_import_chickens)
        except ImportError:
            raise

class _Config(local): pass
config = _Config()

class Config:
    """WSGI application class wrapper which provides configuration for
    a snap application view.
    """

    def __init__(self, app, config):
        """Wrap a given WSGI app and stuff extra configuration into
        the environment.
        """
        self.app = app
        self.config = config

    def __call__(self, env, start_response):
        """Facilitate WSGI API by providing a callable hook.
        """
        entransit_data = self.config['entransit_data']
        self.config['path'] = Utility(data_prefix=(),
                                      entransit_prefix=entransit_data,
                                      package_prefix=entransit_data)
        for k, v in self.config.items():
            setattr(config, k, v)
            env['snap.%s' % k] = v
        return self.app(env, start_response)

def config_filter_factory(global_conf, **local_conf):
    appid = local_conf.get('appid')
    if not appid:
        # bomb if `appid` is missing.
        raise ValueError('Variable `appid` is required for paste.ini')
    connection_string = local_conf.get('connection_string')
    connection_factory = local_conf.get('connection_factory')
    if connection_string is not None and connection_factory is not None:
        # bomb if there's a existing `db_connection` setting.
        db_connection = local_conf.get('db_connection')
        if db_connection:
            raise ValueError('Variable `db_connection` is dead. Please '
                             'use `connection_string` and `connection_factory` '
                             'instead.')
        # resolve dotted name.
        connection_factory = resolve(connection_factory)

        # create a connection
        connection = connection_factory(connection_string)

        # register a global connection using `appid` as the name.
        gsm = zapi.getGlobalSiteManager()
        gsm.provideUtility(IZopeDatabaseAdapter, connection, appid)

        # fixup the `db_connection` argument.
        local_conf['db_connection'] = appid

    def filter(app):
        return Config(app, local_conf)
    return filter
