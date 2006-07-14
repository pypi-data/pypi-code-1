import sys

try:
    from paste.registry import StackedObjectProxy
    beaker_session = StackedObjectProxy()
except:
    pass
from myghtyutils.session import Session
from myghtyutils.util import PrefixArgs


class request(object):
    def __init__(self):
        class headers_out(object):
            def __init__(self):
                self.headers = {}
            def add(self, name, value):
                self.headers[name] = value
        self.headers_out = headers_out()

class SessionObject(object):
    """Session proxy/lazy creator
    
    This object proxies access to the actual session object, so that in the
    case that the session hasn't been used before, it will be setup. This
    avoid creating and loading the session from persistent storage unless
    its actually used during the request.
    
    """
    def __init__(self, environ, **params):
        self.__dict__['_params'] = params
        self.__dict__['_environ'] = environ
        self.__dict__['_sess'] = None
        self.__dict__['_headers'] = []
    
    def _session(self):
        """Lazy initial creation of session object"""
        if not self.__dict__['_sess']:
            params = self.__dict__['_params']
            environ = self.__dict__['_environ']
            req = request()
            self.__dict__['_headers'] = req.headers_out
            req.headers_in = dict(cookie=environ.get('HTTP_COOKIE'))
            self.__dict__['_sess'] = Session(req, use_cookies=True, **params)
        return self.__dict__['_sess']
    
    def __getattr__(self, attr):
        return getattr(self._session(), attr)
    
    def __setattr__(self, attr, value):
        setattr(self._session(), name, value)
    
    def __delattr__(self, name):
        self._session().__delattr__(name)
    
    def __getitem__(self, key):
        return self._session()[key]
    
    def __setitem__(self, key, value):
        self._session()[key] = value
    
    def __delitem__(self, key):
        self._session().__delitem__(key)
    
    def __repr__(self):
        return self._session().__repr__()
    
    def __iter__(self):
        """Only works for proxying to a dict"""
        return iter(self._session().keys())
    
    def __contains__(self, key):
        return self._session().has_key(key)
    

session_params = dict(invalidate_corrupt = False, type = None, data_dir = None,
    key = 'beaker_session_id', timeout = None, secret = None, log_file = None)

class SessionMiddleware(object):
    def __init__(self, wrap_app, global_conf={}, auto_register=True, **params):
        self.params = SessionArgs(**session_params)
        self.params.set_prefix_params(**global_conf)
        self.params.set_prefix_params(**params)
        self.auto_register = auto_register
        self.wrap_app = wrap_app
    
    def __call__(self, environ, start_response):
        session = SessionObject(environ, **self.params.params)
        if environ.get('paste.registry') and self.auto_register:
            environ['paste.registry'].register(beaker_session, session)
        environ['beaker.session'] = session
        
        def session_start_response(status, headers, exc_info = None):
            if session.__dict__['_sess']:
                cookie = session.__dict__['_headers'].headers.get('set-cookie')
                if cookie:
                    headers.append(('Set-cookie', cookie))
            return start_response(status, headers, exc_info)
        try:
            response = self.wrap_app(environ, session_start_response)
        except:
            ty, val = sys.exc_info()[:2]
            if isinstance(ty, str):
                raise ty, val, sys.exc_info()[2]
            if ty.__name__ == 'HTTPFound' and session.__dict__['_sess']:
                cookie = session.__dict__['_headers'].headers.get('set-cookie')
                val.headers.append(('Set-cookie', cookie))
            raise ty, val, sys.exc_info()[2]
        else:
            return response

def session_filter_factory(global_conf, **kwargs):
    def filter(app):
        return SessionMiddleware(app, global_conf, **kwargs)
    return filter

def session_filter_app_factory(app, global_conf, **kwargs):
    return SessionMiddleware(app, global_conf, **kwargs)

class SessionArgs(PrefixArgs):
    def __init__(self, **params):
        PrefixArgs.__init__(self, 'session_')
        self.set_prefix_params(**params)
        
    def clone(self, **params):
        p = self.get_params(**params)
        arg = CacheArgs()
        arg.params = p
        return arg
