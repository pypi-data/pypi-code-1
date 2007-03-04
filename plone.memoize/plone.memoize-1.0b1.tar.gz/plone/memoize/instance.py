"""
Memoize decorators for instances.

Stores values in a property on the instance. See instance.txt.

Stolen from Whit Morriss' memojito package. 
"""

_marker = object()
class Memojito(object):
    propname = '_memojito_'
    def clear(self, inst):
        if hasattr(inst, self.propname):
            delattr(inst, self.propname)
        
    def clearbefore(self, func):
        def clear(*args, **kwargs):
            inst=args[0]
            self.clear(inst)
            return func(*args, **kwargs)
        return clear

    def clearafter(self, func):
        def clear(*args, **kwargs):
            inst=args[0]
            val = func(*args, **kwargs)
            self.clear(inst)
            return val 
        return clear

    def memoize(self, func):
        def memogetter(*args, **kwargs):
            inst = args[0]
            cache = getattr(inst, self.propname, dict())

            # XXX this could be improved to unfold unhashables
            # and optimized with pyrex
            
            key = (func.__name__, args, frozenset(kwargs.items()))
            key=hash(key)
            val = cache.get(key, _marker)
            if val is _marker:
                val=func(*args, **kwargs)
                cache[key]=val
                setattr(inst, self.propname, cache)
            return val
        return memogetter

_m = Memojito()
memoize = _m.memoize
clearbefore = _m.clearbefore
clearafter = _m.clearafter

__all__ = (memoize, clearbefore, clearafter)