# runtime.py
# Copyright (C) 2006, 2007 Michael Bayer mike_mp@zzzcomputing.com
#
# This module is part of Mako and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""provides runtime services for templates, including Context, Namespace, and various helper functions."""

from mako import exceptions, util
import inspect, sys

class Context(object):
    """provides runtime namespace, output buffer, and various callstacks for templates."""
    def __init__(self, buffer, **data):
        self._buffer_stack = [buffer]
        self._data = data
        self._kwargs = data.copy()
        self._with_template = None
        self.namespaces = {}
        
        # "capture" function which proxies to the generic "capture" function
        data['capture'] = lambda x, *args, **kwargs: capture(self, x, *args, **kwargs)
        
        # "caller" stack used by def calls with content
        self.caller_stack = [Undefined]
        data['caller'] = _StackFacade(self.caller_stack)
    lookup = property(lambda self:self._with_template.lookup)
    kwargs = property(lambda self:self._kwargs.copy())
    def keys(self):
        return self._data.keys()
    def __getitem__(self, key):
        return self._data[key]
    def push_buffer(self):
        """push a capturing buffer onto this Context."""
        self._buffer_stack.append(util.FastEncodingBuffer())
    def pop_buffer(self):
        """pop the most recent capturing buffer from this Context."""
        return self._buffer_stack.pop()
    def get(self, key, default=None):
        return self._data.get(key, default)
    def write(self, string):
        """write a string to this Context's underlying output buffer."""
        self._buffer_stack[-1].write(string)
    def _copy(self):
        c = Context.__new__(Context)
        c._buffer_stack = self._buffer_stack
        c._data = self._data.copy()
        c._kwargs = self._kwargs
        c._with_template = self._with_template
        c.namespaces = self.namespaces
        c.caller_stack = self.caller_stack
        return c
    def locals_(self, d):
        """create a new Context with a copy of this Context's current state, updated with the given dictionary."""
        if len(d) == 0:
            return self
        c = self._copy()
        c._data.update(d)
        return c
    def _clean_inheritance_tokens(self):
        """create a new copy of this Context with tokens related to inheritance state removed."""
        c = self._copy()
        x = c._data
        x.pop('self', None)
        x.pop('parent', None)
        x.pop('next', None)
        return c

class _StackFacade(object):
    def __init__(self, stack):
        self.target = stack
    def __getattr__(self, key):
        return getattr(self.target[-1], key)
        
class Undefined(object):
    """represents an undefined value in a template."""
    def __str__(self):
        raise NameError("Undefined")
UNDEFINED = Undefined()

    
class Namespace(object):
    """provides access to collections of rendering methods, which can be local, from other templates, or from imported modules"""
    def __init__(self, name, context, module=None, template=None, templateuri=None, callables=None, inherits=None, populate_self=True, calling_uri=None):
        self.name = name
        if module is not None:
            mod = __import__(module)
            for token in module.split('.')[1:]:
                mod = getattr(mod, token)
            self._module = mod
        else:
            self._module = None
        if templateuri is not None:
            self.template = _lookup_template(context, templateuri, calling_uri)
            self._templateuri = self.template.module._template_uri
        else:
            self.template = template
            if self.template is not None:
                self._templateuri = self.template.module._template_uri
        self.context = context
        self.inherits = inherits
        if callables is not None:
            self.callables = dict([(c.func_name, c) for c in callables])
        else:
            self.callables = None
        if populate_self and self.template is not None:
            (lclcallable, self.context) = _populate_self_namespace(context, self.template, self_ns=self)

    module = property(lambda s:s._module or s.template.module)
    filename = property(lambda s:s._module and s._module.__file__ or s.template.filename)
    uri = property(lambda s:s.template.uri)
    
    def get_namespace(self, uri):
        """return a namespace corresponding to the given template uri.
        
        if a relative uri, it is adjusted to that of the template of this namespace"""
        key = (self, uri)
        if self.context.namespaces.has_key(key):
            return self.context.namespaces[key]
        else:
            ns = Namespace(uri, self.context, templateuri=uri, calling_uri=self._templateuri) 
            self.context.namespaces[key] = ns
            return ns
    
    def get_template(self, uri):
        return _lookup_template(self.context, uri, self._templateuri)
        
    def get_cached(self, key, **kwargs):
        if self.template:
            if self.template.cache_dir:
                kwargs.setdefault('data_dir', self.template.cache_dir)
            if self.template.cache_type:
                kwargs.setdefault('type', self.template.cache_type)
        return self.template.module._template_cache.get(key, **kwargs)
        
    def include_file(self, uri):
        """include a file at the given uri"""
        _include_file(self.context, uri, self._templateuri)
        
    def _populate(self, d, l):
        for ident in l:
            if ident == '*':
                for (k, v) in self._get_star():
                    d[k] = v
            else:
                d[ident] = getattr(self, ident)
    
    def _get_star(self):
        if self.callables is not None:
            for k in self.callables:
                yield (k, self.callables[key])
        if self.template is not None:
            def get(key):
                callable_ = self.template.get_def(key).callable_
                return lambda *args, **kwargs:callable_(self.context, *args, **kwargs)
            for k in self.template.module._exports:
                yield (k, get(k))
        if self._module is not None:
            def get(key):
                callable_ = getattr(self._module, key)
                return lambda *args, **kwargs:callable_(self.context, *args, **kwargs)
            for k in dir(self._module):
                if k[0] != '_':
                    yield (k, get(k))
                            
    def __getattr__(self, key):
        if self.callables is not None:
            try:
                return self.callables[key]
            except KeyError:
                pass
        if self.template is not None:
            try:
                callable_ = self.template.get_def(key).callable_
                return lambda *args, **kwargs:callable_(self.context, *args, **kwargs)
            except AttributeError:
                pass
        if self._module is not None:
            try:
                callable_ = getattr(self._module, key)
                return lambda *args, **kwargs:callable_(self.context, *args, **kwargs)
            except AttributeError:
                pass
        if self.inherits is not None:
            return getattr(self.inherits, key)
        raise exceptions.RuntimeException("Namespace '%s' has no member '%s'" % (self.name, key))

def capture(context, callable_, *args, **kwargs):
    """execute the given template def, capturing the output into a buffer."""
    if not callable(callable_):
        raise exceptions.RuntimeException("capture() function expects a callable as its argument (i.e. capture(func, *args, **kwargs))")
    context.push_buffer()
    try:
        callable_(*args, **kwargs)
    finally:
        buf = context.pop_buffer()
    return buf.getvalue()
        
def _include_file(context, uri, calling_uri):
    """locate the template from the given uri and include it in the current output."""
    template = _lookup_template(context, uri, calling_uri)
    (callable_, ctx) = _populate_self_namespace(context._clean_inheritance_tokens(), template)
    callable_(ctx, **_kwargs_for_callable(callable_, context._data))
        
def _inherit_from(context, uri, calling_uri):
    """called by the _inherit method in template modules to set up the inheritance chain at the start
    of a template's execution."""
    if uri is None:
        return None
    template = _lookup_template(context, uri, calling_uri)
    self_ns = context['self']
    ih = self_ns
    while ih.inherits is not None:
        ih = ih.inherits
    lclcontext = context.locals_({'next':ih})
    ih.inherits = Namespace("self:%s" % template.uri, lclcontext, template = template, populate_self=False)
    context._data['parent'] = lclcontext._data['local'] = ih.inherits
    callable_ = getattr(template.module, '_mako_inherit', None)
    if callable_ is not None:
        ret = callable_(template, lclcontext)
        if ret:
            return ret

    gen_ns = getattr(template.module, '_mako_generate_namespaces', None)
    if gen_ns is not None:
        gen_ns(context)
    return (template.callable_, lclcontext)

def _lookup_template(context, uri, relativeto):
    lookup = context._with_template.lookup
    if lookup is None:
        raise exceptions.TemplateLookupException("Template '%s' has no TemplateLookup associated" % context._with_template.uri)
    uri = lookup.adjust_uri(uri, relativeto)
    try:
        return lookup.get_template(uri)
    except exceptions.TopLevelLookupException, e:
        raise exceptions.TemplateLookupException(str(e))

def _populate_self_namespace(context, template, self_ns=None):
    if self_ns is None:
        self_ns = Namespace('self:%s' % template.uri, context, template=template, populate_self=False)
    context._data['self'] = context._data['local'] = self_ns
    if hasattr(template.module, '_mako_inherit'):
        ret = template.module._mako_inherit(template, context)
        if ret:
            return ret
    return (template.callable_, context)

def _render(template, callable_, args, data, as_unicode=False):
    """create a Context and return the string output of the given template and template callable."""
    if as_unicode:
        buf = util.FastEncodingBuffer()
    elif template.output_encoding:
        buf = util.FastEncodingBuffer(template.output_encoding)
    else:
        buf = util.StringIO()
    context = Context(buf, **data)
    context._with_template = template
    _render_context(template, callable_, context, *args, **_kwargs_for_callable(callable_, data))
    return context.pop_buffer().getvalue()

def _kwargs_for_callable(callable_, data):
    kwargs = {}
    argspec = inspect.getargspec(callable_)
    namedargs = argspec[0] + [v for v in argspec[1:3] if v is not None]
    for arg in namedargs:
        if arg != 'context' and arg in data:
            kwargs[arg] = data[arg]
    return kwargs
    
def _render_context(tmpl, callable_, context, *args, **kwargs):
    import mako.template as template
    # create polymorphic 'self' namespace for this template with possibly updated context
    if not isinstance(tmpl, template.DefTemplate):
        # if main render method, call from the base of the inheritance stack
        (inherit, lclcontext) = _populate_self_namespace(context, tmpl)
        _exec_template(inherit, lclcontext, args=args, kwargs=kwargs)
    else:
        # otherwise, call the actual rendering method specified
        (inherit, lclcontext) = _populate_self_namespace(context, tmpl.parent)
        _exec_template(callable_, context, args=args, kwargs=kwargs)
        
def _exec_template(callable_, context, args=None, kwargs=None):
    """execute a rendering callable given the callable, a Context, and optional explicit arguments

    the contextual Template will be located if it exists, and the error handling options specified
    on that Template will be interpreted here.
    """
    template = context._with_template
    if template is not None and (template.format_exceptions or template.error_handler):
        error = None
        try:
            callable_(context, *args, **kwargs)
        except Exception, e:
            error = e
        except:                
            e = sys.exc_info()[0]
            error = e
        if error:
            if template.error_handler:
                result = template.error_handler(context, error)
                if not result:
                    raise error
            else:
                context._buffer_stack = [util.StringIO()]
                error_template = exceptions.html_error_template()
                context._with_template = error_template
                error_template.render_context(context, error=error)
    else:
        callable_(context, *args, **kwargs)
