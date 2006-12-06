"""
$Id: registry.py 3967 2006-01-26 19:06:28Z sidnei $
"""

from snap.filter.config import config

_marker = object()

class Registry(object):

    def __init__(self):
        self.__apps = {}

    def __getitem__(self, name):
        got = self.get(name, _marker)
        if got is _marker:
            raise KeyError, name
        return got

    def get(self, name, default=None):
        appid = config.appid
        app = self.__apps.get(appid, default)
        if app is default:
            return default
        return app.get(name, default)

    def __setitem__(self, name, value):
        appid = config.appid
        self.register(appid, name, value)

    def register(self, appid, name, value):
        app = self.__apps.get(appid)
        if app is None:
            app = self.__apps[appid] = {}
        app[name] = value

registry = Registry()

def registerTypeMarkers(appid, _map):
    registry.register(appid, 'type_markers', _map)

def registerTopLevelMarkers(appid, _map):
    registry.register(appid, 'top_level_markers', _map)

def registerContainmentMarkers(appid, _map):
    registry.register(appid, 'containment_markers', _map)
