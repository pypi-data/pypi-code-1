# (c) 2005 Ben Bangert
# This module is part of the Python Paste Project and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""Registry for handling request-local module globals sanely

Dealing with module globals in a thread-safe way is good if your
application is the sole responder in a thread, however that approach fails
to properly account for various scenarios that occur with WSGI applications
and middleware.

What is actually needed in the case where a module global is desired that
is always set properly depending on the current request, is a stacked
thread-local object. Such an object is popped or pushed during the request
cycle so that it properly represents the object that should be active for
the current request.

To make it easy to deal with such variables, this module provides a special
StackedObjectProxy class which you can instantiate and attach to your
module where you'd like others to access it. The object you'd like this to
actually "be" during the request is then registered with the
RegistryManager middleware, which ensures that for the scope of the current
WSGI application everything will work properly.

Example::
    
    #yourpackage/__init__.py
    
    from paste.registry import RegistryManager, StackedObjectProxy
    myglobal = StackedObjectProxy()
    
    #wsgi app stack
    app = RegistryManager(yourapp)
    
    #inside your wsgi app
    class yourapp(object):
        def __call__(self, environ, start_response):
            obj = someobject  # The request-local object you want to access
                              # via yourpackage.myglobal
            if environ.has_key('paste.registry'):
                environ['paste.registry'].register(myglobal, obj)

You will then be able to import yourpackage anywhere in your WSGI app or in
the calling stack below it and be assured that it is using the object you
registered with Registry.

RegisterManager can be in the WSGI stack multiple times, each time it
appears it registers a new request context.


Performance
===========

The overhead of the proxy object is very minimal, however if you are using
proxy objects extensively (Thousands of accesses per request or more), there
are some ways to avoid them. A proxy object runs approximately 3-20x slower
than direct access to the object, this is rarely your performance bottleneck
when developing web applications.

Should you be developing a system which may be accessing the proxy object
thousands of times per request, the performance of the proxy will start to
become more noticeabe. In that circumstance, the problem can be avoided by
getting at the actual object via the proxy with the ``curent_obj`` function::
    
    #sessions.py
    Session = StackedObjectProxy()
    # ... initialization code, etc.
    
    # somemodule.py
    import sessions
    
    def somefunc():
        session = sessions.Session.current_obj()
        # ... tons of session access

This way the proxy is used only once to retrieve the object for the current
context and the overhead is minimized while still making it easy to access
the underlying object.

**NOTE:** This is *highly* unlikely to be an issue in the vast majority of
cases, and requires incredibly large amounts of proxy object access before
one should consider the proxy object to be causing slow-downs. This section
is provided solely in the extremely rare case that it is an issue so that a
quick way to work around it is documented.

"""
import paste.util.threadinglocal as threadinglocal
from paste import wsgilib

__all__ = ['StackedObjectProxy', 'RegistryManager']

class StackedObjectProxy(object):
    """Track an object instance internally using a stack
    
    The StackedObjectProxy proxies access to an object internally using a
    stacked thread-local. This makes it safe for complex WSGI environments
    where access to the object may be desired in multiple places without
    having to pass the actual object around.
    
    New objects are added to the top of the stack with push_object while
    objects can be removed with pop_object. 
    
    """
    def __init__(self, default=None, name="Default"):
        """Create a new StackedObjectProxy
        
        If a default is given, its used in every thread if no other object
        has been pushed on.
        
        """
        self.__dict__['_name'] = name
        self.__dict__['local'] = threadinglocal.local()
        if default:
            self.__dict__['_default_object'] = default
    
    def __getattr__(self, attr):
        return getattr(self.current_obj(), attr)
    
    def __setattr__(self, attr, value):
        setattr(self.current_obj(), attr, value)
    
    def __delattr__(self, name):
        self.current_obj().__delattr__(name)
    
    def __getitem__(self, key):
        return self.current_obj()[key]
    
    def __setitem__(self, key, value):
        self.current_obj()[key] = value
    
    def __delitem__(self, key):
        self.current_obj().__delitem__(key)
    
    def __repr__(self):
        return self.current_obj().__repr__()
    
    def __iter__(self):
        """Only works for proxying to a dict"""
        return iter(self.current_obj().keys())
    
    def __len__(self):
        return len(self.current_obj())
    
    def __contains__(self, key):
        # I thought __getattr__ would catch this, but apparently not
        return self.current_obj().has_key(key)
    
    def current_obj(self):
        """Returns the current active object being proxied to
        
        In the event that no object was pushed, the default object if
        provided will be used. Otherwise, a TypeError will be raised.
        
        """
        objects = getattr(self.__dict__['local'], 'objects', None)
        if objects:
            return objects[-1]
        else:
            object = self.__dict__.get('_default_object')
            if object:
                return object
            else:
                raise TypeError(
                    "No object (Name: %s) has been registered for this \
                    thread" % self.__dict__['_name'])
    
    def push_object(self, obj):
        """Make ``obj`` the active object for this thread-local.
        
        This should be used like::

            obj = yourobject()
            module.glob = StackedObjectProxy()
            module.glob.push_object(obj)
            try:
                ... do stuff ...
            finally:
                module.glob.pop_object(conf)
        
        """
        if not hasattr(self.local, 'objects'):
            self.local.objects = []
        self.local.objects.append(obj)
    
    def pop_object(self, obj=None):
        """Remove a thread-local object.
        
        If ``obj`` is given, it is checked against the popped object and an
        error is emitted if they don't match.
        
        """
        if not hasattr(self.local, 'objects'):
            raise AssertionError("No object has been registered for this thread.")
        popped = self.local.objects.pop()
        if obj:
            if popped is not obj:
                raise AssertionError(
                    "The object popped (%s) is not the same as the object "
                    "expected (%s)"
                    % (popped, obj))

class Registry(object):
    """Track objects and stacked object proxies for removal
    
    The Registry object is instantiated a single time for the rquest no
    matter how many times the RegistryManager is used in a WSGI stack. Each
    RegistryManager must call ``prepare`` before continuing the call to
    start a new context for object registering.
    
    Each context is tracked with a dict inside a list. The last list
    element is the currently executing context. Each context dict is keyed
    by the id of the StackedObjectProxy instance being proxied, the value
    is a tuple of the StackedObjectProxy instance and the object being
    tracked.
    
    """
    def __init__(self):
        """Create a new Registry object
        
        ``prepare`` must still be called before this Registry object can be
        used to register objects.
        
        """
        self.reglist = []
    
    def prepare(self):
        """Used to create a new registry context
        
        Anytime a new RegistryManager is called, ``prepare`` needs to be
        called on the existing Registry object. This sets up a new context
        for registering objects.
        
        """
        self.reglist.append({})
    
    def register(self, stacked, obj):
        """Register an object with a StackedObjectProxy"""
        stacked.push_object(obj)
        myreglist = self.reglist[-1]
        myreglist[id(stacked)] = (stacked, obj)
    
    def cleanup(self):
        """Remove all objects from all StackedObjectProxy instances that
        were tracked at this Registry context"""
        for id, val in self.reglist[-1].iteritems():
            stacked, obj = val
            stacked.pop_object(obj)
        self.reglist.pop()
        
class RegistryManager(object):
    """Creates and maintains a Registry context
    
    RegistryManager creates a new registry context for the registration of
    StackedObjectProxy instances. Multiple RegistryManager's can be in a
    WSGI stack and will manage the context so that the StackedObjectProxies
    always proxy to the proper object.
    
    The object being registered can be any object sub-class, list, or dict.
    
    Registering objects is done inside a WSGI application under the
    RegistryManager instance, using the ``environ['paste.registry']``
    object which is a `Registry`_ instance.
        
    """
    def __init__(self, application):
        self.application = application
        
    def __call__(self, environ, start_response):
        app_iter = None
        reg = environ.setdefault('paste.registry', Registry())
        reg.prepare()
        try:
            app_iter = self.application(environ, start_response)
        finally:
            if app_iter is None:
                # An error occurred...
                reg.cleanup()
        if type(app_iter) in (list, tuple):
            # Because it is a concrete iterator (not a generator) we
            # know the configuration for this thread is no longer
            # needed:
            reg.cleanup()
            return app_iter
        else:
            new_app_iter = wsgilib.add_close(app_iter, reg.cleanup)
            return new_app_iter


