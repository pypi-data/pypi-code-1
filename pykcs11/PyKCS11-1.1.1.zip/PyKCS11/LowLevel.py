# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _LowLevel
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


cdata = _LowLevel.cdata
memmove = _LowLevel.memmove
class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _LowLevel.delete_PySwigIterator
    __del__ = lambda self : None;
    def value(*args): return _LowLevel.PySwigIterator_value(*args)
    def incr(*args): return _LowLevel.PySwigIterator_incr(*args)
    def decr(*args): return _LowLevel.PySwigIterator_decr(*args)
    def distance(*args): return _LowLevel.PySwigIterator_distance(*args)
    def equal(*args): return _LowLevel.PySwigIterator_equal(*args)
    def copy(*args): return _LowLevel.PySwigIterator_copy(*args)
    def next(*args): return _LowLevel.PySwigIterator_next(*args)
    def previous(*args): return _LowLevel.PySwigIterator_previous(*args)
    def advance(*args): return _LowLevel.PySwigIterator_advance(*args)
    def __eq__(*args): return _LowLevel.PySwigIterator___eq__(*args)
    def __ne__(*args): return _LowLevel.PySwigIterator___ne__(*args)
    def __iadd__(*args): return _LowLevel.PySwigIterator___iadd__(*args)
    def __isub__(*args): return _LowLevel.PySwigIterator___isub__(*args)
    def __add__(*args): return _LowLevel.PySwigIterator___add__(*args)
    def __sub__(*args): return _LowLevel.PySwigIterator___sub__(*args)
    def __iter__(self): return self
PySwigIterator_swigregister = _LowLevel.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)

class ckintlist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ckintlist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ckintlist, name)
    __repr__ = _swig_repr
    def iterator(*args): return _LowLevel.ckintlist_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _LowLevel.ckintlist___nonzero__(*args)
    def __len__(*args): return _LowLevel.ckintlist___len__(*args)
    def pop(*args): return _LowLevel.ckintlist_pop(*args)
    def __getslice__(*args): return _LowLevel.ckintlist___getslice__(*args)
    def __setslice__(*args): return _LowLevel.ckintlist___setslice__(*args)
    def __delslice__(*args): return _LowLevel.ckintlist___delslice__(*args)
    def __delitem__(*args): return _LowLevel.ckintlist___delitem__(*args)
    def __getitem__(*args): return _LowLevel.ckintlist___getitem__(*args)
    def __setitem__(*args): return _LowLevel.ckintlist___setitem__(*args)
    def append(*args): return _LowLevel.ckintlist_append(*args)
    def empty(*args): return _LowLevel.ckintlist_empty(*args)
    def size(*args): return _LowLevel.ckintlist_size(*args)
    def clear(*args): return _LowLevel.ckintlist_clear(*args)
    def swap(*args): return _LowLevel.ckintlist_swap(*args)
    def get_allocator(*args): return _LowLevel.ckintlist_get_allocator(*args)
    def begin(*args): return _LowLevel.ckintlist_begin(*args)
    def end(*args): return _LowLevel.ckintlist_end(*args)
    def rbegin(*args): return _LowLevel.ckintlist_rbegin(*args)
    def rend(*args): return _LowLevel.ckintlist_rend(*args)
    def pop_back(*args): return _LowLevel.ckintlist_pop_back(*args)
    def erase(*args): return _LowLevel.ckintlist_erase(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_ckintlist(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _LowLevel.ckintlist_push_back(*args)
    def front(*args): return _LowLevel.ckintlist_front(*args)
    def back(*args): return _LowLevel.ckintlist_back(*args)
    def assign(*args): return _LowLevel.ckintlist_assign(*args)
    def resize(*args): return _LowLevel.ckintlist_resize(*args)
    def insert(*args): return _LowLevel.ckintlist_insert(*args)
    def reserve(*args): return _LowLevel.ckintlist_reserve(*args)
    def capacity(*args): return _LowLevel.ckintlist_capacity(*args)
    __swig_destroy__ = _LowLevel.delete_ckintlist
    __del__ = lambda self : None;
ckintlist_swigregister = _LowLevel.ckintlist_swigregister
ckintlist_swigregister(ckintlist)

class ckbytelist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ckbytelist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ckbytelist, name)
    __repr__ = _swig_repr
    def iterator(*args): return _LowLevel.ckbytelist_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _LowLevel.ckbytelist___nonzero__(*args)
    def __len__(*args): return _LowLevel.ckbytelist___len__(*args)
    def pop(*args): return _LowLevel.ckbytelist_pop(*args)
    def __getslice__(*args): return _LowLevel.ckbytelist___getslice__(*args)
    def __setslice__(*args): return _LowLevel.ckbytelist___setslice__(*args)
    def __delslice__(*args): return _LowLevel.ckbytelist___delslice__(*args)
    def __delitem__(*args): return _LowLevel.ckbytelist___delitem__(*args)
    def __getitem__(*args): return _LowLevel.ckbytelist___getitem__(*args)
    def __setitem__(*args): return _LowLevel.ckbytelist___setitem__(*args)
    def append(*args): return _LowLevel.ckbytelist_append(*args)
    def empty(*args): return _LowLevel.ckbytelist_empty(*args)
    def size(*args): return _LowLevel.ckbytelist_size(*args)
    def clear(*args): return _LowLevel.ckbytelist_clear(*args)
    def swap(*args): return _LowLevel.ckbytelist_swap(*args)
    def get_allocator(*args): return _LowLevel.ckbytelist_get_allocator(*args)
    def begin(*args): return _LowLevel.ckbytelist_begin(*args)
    def end(*args): return _LowLevel.ckbytelist_end(*args)
    def rbegin(*args): return _LowLevel.ckbytelist_rbegin(*args)
    def rend(*args): return _LowLevel.ckbytelist_rend(*args)
    def pop_back(*args): return _LowLevel.ckbytelist_pop_back(*args)
    def erase(*args): return _LowLevel.ckbytelist_erase(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_ckbytelist(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _LowLevel.ckbytelist_push_back(*args)
    def front(*args): return _LowLevel.ckbytelist_front(*args)
    def back(*args): return _LowLevel.ckbytelist_back(*args)
    def assign(*args): return _LowLevel.ckbytelist_assign(*args)
    def resize(*args): return _LowLevel.ckbytelist_resize(*args)
    def insert(*args): return _LowLevel.ckbytelist_insert(*args)
    def reserve(*args): return _LowLevel.ckbytelist_reserve(*args)
    def capacity(*args): return _LowLevel.ckbytelist_capacity(*args)
    __swig_destroy__ = _LowLevel.delete_ckbytelist
    __del__ = lambda self : None;
ckbytelist_swigregister = _LowLevel.ckbytelist_swigregister
ckbytelist_swigregister(ckbytelist)

class ckattrlist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ckattrlist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ckattrlist, name)
    __repr__ = _swig_repr
    def iterator(*args): return _LowLevel.ckattrlist_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _LowLevel.ckattrlist___nonzero__(*args)
    def __len__(*args): return _LowLevel.ckattrlist___len__(*args)
    def pop(*args): return _LowLevel.ckattrlist_pop(*args)
    def __getslice__(*args): return _LowLevel.ckattrlist___getslice__(*args)
    def __setslice__(*args): return _LowLevel.ckattrlist___setslice__(*args)
    def __delslice__(*args): return _LowLevel.ckattrlist___delslice__(*args)
    def __delitem__(*args): return _LowLevel.ckattrlist___delitem__(*args)
    def __getitem__(*args): return _LowLevel.ckattrlist___getitem__(*args)
    def __setitem__(*args): return _LowLevel.ckattrlist___setitem__(*args)
    def append(*args): return _LowLevel.ckattrlist_append(*args)
    def empty(*args): return _LowLevel.ckattrlist_empty(*args)
    def size(*args): return _LowLevel.ckattrlist_size(*args)
    def clear(*args): return _LowLevel.ckattrlist_clear(*args)
    def swap(*args): return _LowLevel.ckattrlist_swap(*args)
    def get_allocator(*args): return _LowLevel.ckattrlist_get_allocator(*args)
    def begin(*args): return _LowLevel.ckattrlist_begin(*args)
    def end(*args): return _LowLevel.ckattrlist_end(*args)
    def rbegin(*args): return _LowLevel.ckattrlist_rbegin(*args)
    def rend(*args): return _LowLevel.ckattrlist_rend(*args)
    def pop_back(*args): return _LowLevel.ckattrlist_pop_back(*args)
    def erase(*args): return _LowLevel.ckattrlist_erase(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_ckattrlist(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _LowLevel.ckattrlist_push_back(*args)
    def front(*args): return _LowLevel.ckattrlist_front(*args)
    def back(*args): return _LowLevel.ckattrlist_back(*args)
    def assign(*args): return _LowLevel.ckattrlist_assign(*args)
    def resize(*args): return _LowLevel.ckattrlist_resize(*args)
    def insert(*args): return _LowLevel.ckattrlist_insert(*args)
    def reserve(*args): return _LowLevel.ckattrlist_reserve(*args)
    def capacity(*args): return _LowLevel.ckattrlist_capacity(*args)
    __swig_destroy__ = _LowLevel.delete_ckattrlist
    __del__ = lambda self : None;
ckattrlist_swigregister = _LowLevel.ckattrlist_swigregister
ckattrlist_swigregister(ckattrlist)

class ckobjlist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ckobjlist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ckobjlist, name)
    __repr__ = _swig_repr
    def iterator(*args): return _LowLevel.ckobjlist_iterator(*args)
    def __iter__(self): return self.iterator()
    def __nonzero__(*args): return _LowLevel.ckobjlist___nonzero__(*args)
    def __len__(*args): return _LowLevel.ckobjlist___len__(*args)
    def pop(*args): return _LowLevel.ckobjlist_pop(*args)
    def __getslice__(*args): return _LowLevel.ckobjlist___getslice__(*args)
    def __setslice__(*args): return _LowLevel.ckobjlist___setslice__(*args)
    def __delslice__(*args): return _LowLevel.ckobjlist___delslice__(*args)
    def __delitem__(*args): return _LowLevel.ckobjlist___delitem__(*args)
    def __getitem__(*args): return _LowLevel.ckobjlist___getitem__(*args)
    def __setitem__(*args): return _LowLevel.ckobjlist___setitem__(*args)
    def append(*args): return _LowLevel.ckobjlist_append(*args)
    def empty(*args): return _LowLevel.ckobjlist_empty(*args)
    def size(*args): return _LowLevel.ckobjlist_size(*args)
    def clear(*args): return _LowLevel.ckobjlist_clear(*args)
    def swap(*args): return _LowLevel.ckobjlist_swap(*args)
    def get_allocator(*args): return _LowLevel.ckobjlist_get_allocator(*args)
    def begin(*args): return _LowLevel.ckobjlist_begin(*args)
    def end(*args): return _LowLevel.ckobjlist_end(*args)
    def rbegin(*args): return _LowLevel.ckobjlist_rbegin(*args)
    def rend(*args): return _LowLevel.ckobjlist_rend(*args)
    def pop_back(*args): return _LowLevel.ckobjlist_pop_back(*args)
    def erase(*args): return _LowLevel.ckobjlist_erase(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_ckobjlist(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(*args): return _LowLevel.ckobjlist_push_back(*args)
    def front(*args): return _LowLevel.ckobjlist_front(*args)
    def back(*args): return _LowLevel.ckobjlist_back(*args)
    def assign(*args): return _LowLevel.ckobjlist_assign(*args)
    def resize(*args): return _LowLevel.ckobjlist_resize(*args)
    def insert(*args): return _LowLevel.ckobjlist_insert(*args)
    def reserve(*args): return _LowLevel.ckobjlist_reserve(*args)
    def capacity(*args): return _LowLevel.ckobjlist_capacity(*args)
    __swig_destroy__ = _LowLevel.delete_ckobjlist
    __del__ = lambda self : None;
ckobjlist_swigregister = _LowLevel.ckobjlist_swigregister
ckobjlist_swigregister(ckobjlist)

class CK_SESSION_HANDLE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_SESSION_HANDLE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_SESSION_HANDLE, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LowLevel.new_CK_SESSION_HANDLE(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_SESSION_HANDLE
    __del__ = lambda self : None;
    def assign(*args): return _LowLevel.CK_SESSION_HANDLE_assign(*args)
    def value(*args): return _LowLevel.CK_SESSION_HANDLE_value(*args)
    def cast(*args): return _LowLevel.CK_SESSION_HANDLE_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _LowLevel.CK_SESSION_HANDLE_frompointer
    if _newclass:frompointer = staticmethod(_LowLevel.CK_SESSION_HANDLE_frompointer)
CK_SESSION_HANDLE_swigregister = _LowLevel.CK_SESSION_HANDLE_swigregister
CK_SESSION_HANDLE_swigregister(CK_SESSION_HANDLE)
CK_SESSION_HANDLE_frompointer = _LowLevel.CK_SESSION_HANDLE_frompointer

class CK_OBJECT_HANDLE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_OBJECT_HANDLE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_OBJECT_HANDLE, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LowLevel.new_CK_OBJECT_HANDLE(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_OBJECT_HANDLE
    __del__ = lambda self : None;
    def assign(*args): return _LowLevel.CK_OBJECT_HANDLE_assign(*args)
    def value(*args): return _LowLevel.CK_OBJECT_HANDLE_value(*args)
    def cast(*args): return _LowLevel.CK_OBJECT_HANDLE_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _LowLevel.CK_OBJECT_HANDLE_frompointer
    if _newclass:frompointer = staticmethod(_LowLevel.CK_OBJECT_HANDLE_frompointer)
CK_OBJECT_HANDLE_swigregister = _LowLevel.CK_OBJECT_HANDLE_swigregister
CK_OBJECT_HANDLE_swigregister(CK_OBJECT_HANDLE)
CK_OBJECT_HANDLE_frompointer = _LowLevel.CK_OBJECT_HANDLE_frompointer

class byteArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, byteArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, byteArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LowLevel.new_byteArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_byteArray
    __del__ = lambda self : None;
    def __getitem__(*args): return _LowLevel.byteArray___getitem__(*args)
    def __setitem__(*args): return _LowLevel.byteArray___setitem__(*args)
    def cast(*args): return _LowLevel.byteArray_cast(*args)
    __swig_getmethods__["frompointer"] = lambda x: _LowLevel.byteArray_frompointer
    if _newclass:frompointer = staticmethod(_LowLevel.byteArray_frompointer)
byteArray_swigregister = _LowLevel.byteArray_swigregister
byteArray_swigregister(byteArray)
byteArray_frompointer = _LowLevel.byteArray_frompointer

class CK_VERSION(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_VERSION, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_VERSION, name)
    __repr__ = _swig_repr
    __swig_getmethods__["major"] = _LowLevel.CK_VERSION_major_get
    if _newclass:major = property(_LowLevel.CK_VERSION_major_get)
    __swig_getmethods__["minor"] = _LowLevel.CK_VERSION_minor_get
    if _newclass:minor = property(_LowLevel.CK_VERSION_minor_get)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_VERSION(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_VERSION
    __del__ = lambda self : None;
CK_VERSION_swigregister = _LowLevel.CK_VERSION_swigregister
CK_VERSION_swigregister(CK_VERSION)

class CK_INFO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_INFO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_INFO, name)
    __repr__ = _swig_repr
    __swig_getmethods__["cryptokiVersion"] = _LowLevel.CK_INFO_cryptokiVersion_get
    if _newclass:cryptokiVersion = property(_LowLevel.CK_INFO_cryptokiVersion_get)
    __swig_getmethods__["manufacturerID"] = _LowLevel.CK_INFO_manufacturerID_get
    if _newclass:manufacturerID = property(_LowLevel.CK_INFO_manufacturerID_get)
    __swig_getmethods__["flags"] = _LowLevel.CK_INFO_flags_get
    if _newclass:flags = property(_LowLevel.CK_INFO_flags_get)
    __swig_getmethods__["libraryDescription"] = _LowLevel.CK_INFO_libraryDescription_get
    if _newclass:libraryDescription = property(_LowLevel.CK_INFO_libraryDescription_get)
    __swig_getmethods__["libraryVersion"] = _LowLevel.CK_INFO_libraryVersion_get
    if _newclass:libraryVersion = property(_LowLevel.CK_INFO_libraryVersion_get)
    def GetManufacturerID(*args): return _LowLevel.CK_INFO_GetManufacturerID(*args)
    def GetLibraryDescription(*args): return _LowLevel.CK_INFO_GetLibraryDescription(*args)
    def GetLibraryVersion(*args): return _LowLevel.CK_INFO_GetLibraryVersion(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_INFO(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_INFO
    __del__ = lambda self : None;
CK_INFO_swigregister = _LowLevel.CK_INFO_swigregister
CK_INFO_swigregister(CK_INFO)

class CK_SLOT_INFO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_SLOT_INFO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_SLOT_INFO, name)
    __repr__ = _swig_repr
    __swig_getmethods__["flags"] = _LowLevel.CK_SLOT_INFO_flags_get
    if _newclass:flags = property(_LowLevel.CK_SLOT_INFO_flags_get)
    __swig_getmethods__["hardwareVersion"] = _LowLevel.CK_SLOT_INFO_hardwareVersion_get
    if _newclass:hardwareVersion = property(_LowLevel.CK_SLOT_INFO_hardwareVersion_get)
    __swig_getmethods__["firmwareVersion"] = _LowLevel.CK_SLOT_INFO_firmwareVersion_get
    if _newclass:firmwareVersion = property(_LowLevel.CK_SLOT_INFO_firmwareVersion_get)
    def GetManufacturerID(*args): return _LowLevel.CK_SLOT_INFO_GetManufacturerID(*args)
    def GetSlotDescription(*args): return _LowLevel.CK_SLOT_INFO_GetSlotDescription(*args)
    def GetHardwareVersion(*args): return _LowLevel.CK_SLOT_INFO_GetHardwareVersion(*args)
    def GetFirmwareVersion(*args): return _LowLevel.CK_SLOT_INFO_GetFirmwareVersion(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_SLOT_INFO(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_SLOT_INFO
    __del__ = lambda self : None;
CK_SLOT_INFO_swigregister = _LowLevel.CK_SLOT_INFO_swigregister
CK_SLOT_INFO_swigregister(CK_SLOT_INFO)

class CK_TOKEN_INFO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_TOKEN_INFO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_TOKEN_INFO, name)
    __repr__ = _swig_repr
    __swig_getmethods__["flags"] = _LowLevel.CK_TOKEN_INFO_flags_get
    if _newclass:flags = property(_LowLevel.CK_TOKEN_INFO_flags_get)
    __swig_getmethods__["ulMaxSessionCount"] = _LowLevel.CK_TOKEN_INFO_ulMaxSessionCount_get
    if _newclass:ulMaxSessionCount = property(_LowLevel.CK_TOKEN_INFO_ulMaxSessionCount_get)
    __swig_getmethods__["ulSessionCount"] = _LowLevel.CK_TOKEN_INFO_ulSessionCount_get
    if _newclass:ulSessionCount = property(_LowLevel.CK_TOKEN_INFO_ulSessionCount_get)
    __swig_getmethods__["ulMaxRwSessionCount"] = _LowLevel.CK_TOKEN_INFO_ulMaxRwSessionCount_get
    if _newclass:ulMaxRwSessionCount = property(_LowLevel.CK_TOKEN_INFO_ulMaxRwSessionCount_get)
    __swig_getmethods__["ulRwSessionCount"] = _LowLevel.CK_TOKEN_INFO_ulRwSessionCount_get
    if _newclass:ulRwSessionCount = property(_LowLevel.CK_TOKEN_INFO_ulRwSessionCount_get)
    __swig_getmethods__["ulMaxPinLen"] = _LowLevel.CK_TOKEN_INFO_ulMaxPinLen_get
    if _newclass:ulMaxPinLen = property(_LowLevel.CK_TOKEN_INFO_ulMaxPinLen_get)
    __swig_getmethods__["ulMinPinLen"] = _LowLevel.CK_TOKEN_INFO_ulMinPinLen_get
    if _newclass:ulMinPinLen = property(_LowLevel.CK_TOKEN_INFO_ulMinPinLen_get)
    __swig_getmethods__["ulTotalPublicMemory"] = _LowLevel.CK_TOKEN_INFO_ulTotalPublicMemory_get
    if _newclass:ulTotalPublicMemory = property(_LowLevel.CK_TOKEN_INFO_ulTotalPublicMemory_get)
    __swig_getmethods__["ulFreePublicMemory"] = _LowLevel.CK_TOKEN_INFO_ulFreePublicMemory_get
    if _newclass:ulFreePublicMemory = property(_LowLevel.CK_TOKEN_INFO_ulFreePublicMemory_get)
    __swig_getmethods__["ulTotalPrivateMemory"] = _LowLevel.CK_TOKEN_INFO_ulTotalPrivateMemory_get
    if _newclass:ulTotalPrivateMemory = property(_LowLevel.CK_TOKEN_INFO_ulTotalPrivateMemory_get)
    __swig_getmethods__["ulFreePrivateMemory"] = _LowLevel.CK_TOKEN_INFO_ulFreePrivateMemory_get
    if _newclass:ulFreePrivateMemory = property(_LowLevel.CK_TOKEN_INFO_ulFreePrivateMemory_get)
    __swig_getmethods__["hardwareVersion"] = _LowLevel.CK_TOKEN_INFO_hardwareVersion_get
    if _newclass:hardwareVersion = property(_LowLevel.CK_TOKEN_INFO_hardwareVersion_get)
    __swig_getmethods__["firmwareVersion"] = _LowLevel.CK_TOKEN_INFO_firmwareVersion_get
    if _newclass:firmwareVersion = property(_LowLevel.CK_TOKEN_INFO_firmwareVersion_get)
    def GetLabel(*args): return _LowLevel.CK_TOKEN_INFO_GetLabel(*args)
    def GetManufacturerID(*args): return _LowLevel.CK_TOKEN_INFO_GetManufacturerID(*args)
    def GetModel(*args): return _LowLevel.CK_TOKEN_INFO_GetModel(*args)
    def GetSerialNumber(*args): return _LowLevel.CK_TOKEN_INFO_GetSerialNumber(*args)
    def GetFirmwareVersion(*args): return _LowLevel.CK_TOKEN_INFO_GetFirmwareVersion(*args)
    def GetUtcTime(*args): return _LowLevel.CK_TOKEN_INFO_GetUtcTime(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_TOKEN_INFO(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_TOKEN_INFO
    __del__ = lambda self : None;
CK_TOKEN_INFO_swigregister = _LowLevel.CK_TOKEN_INFO_swigregister
CK_TOKEN_INFO_swigregister(CK_TOKEN_INFO)

class CK_SESSION_INFO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_SESSION_INFO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_SESSION_INFO, name)
    __repr__ = _swig_repr
    __swig_getmethods__["slotID"] = _LowLevel.CK_SESSION_INFO_slotID_get
    if _newclass:slotID = property(_LowLevel.CK_SESSION_INFO_slotID_get)
    __swig_getmethods__["state"] = _LowLevel.CK_SESSION_INFO_state_get
    if _newclass:state = property(_LowLevel.CK_SESSION_INFO_state_get)
    __swig_getmethods__["flags"] = _LowLevel.CK_SESSION_INFO_flags_get
    if _newclass:flags = property(_LowLevel.CK_SESSION_INFO_flags_get)
    __swig_getmethods__["ulDeviceError"] = _LowLevel.CK_SESSION_INFO_ulDeviceError_get
    if _newclass:ulDeviceError = property(_LowLevel.CK_SESSION_INFO_ulDeviceError_get)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_SESSION_INFO(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_SESSION_INFO
    __del__ = lambda self : None;
CK_SESSION_INFO_swigregister = _LowLevel.CK_SESSION_INFO_swigregister
CK_SESSION_INFO_swigregister(CK_SESSION_INFO)

class CK_DATE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_DATE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_DATE, name)
    __repr__ = _swig_repr
    def GetYear(*args): return _LowLevel.CK_DATE_GetYear(*args)
    def GetMonth(*args): return _LowLevel.CK_DATE_GetMonth(*args)
    def GetDay(*args): return _LowLevel.CK_DATE_GetDay(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_DATE(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_DATE
    __del__ = lambda self : None;
CK_DATE_swigregister = _LowLevel.CK_DATE_swigregister
CK_DATE_swigregister(CK_DATE)

class CK_MECHANISM(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_MECHANISM, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_MECHANISM, name)
    __repr__ = _swig_repr
    __swig_setmethods__["mechanism"] = _LowLevel.CK_MECHANISM_mechanism_set
    __swig_getmethods__["mechanism"] = _LowLevel.CK_MECHANISM_mechanism_get
    if _newclass:mechanism = property(_LowLevel.CK_MECHANISM_mechanism_get, _LowLevel.CK_MECHANISM_mechanism_set)
    __swig_setmethods__["pParameter"] = _LowLevel.CK_MECHANISM_pParameter_set
    __swig_getmethods__["pParameter"] = _LowLevel.CK_MECHANISM_pParameter_get
    if _newclass:pParameter = property(_LowLevel.CK_MECHANISM_pParameter_get, _LowLevel.CK_MECHANISM_pParameter_set)
    __swig_setmethods__["ulParameterLen"] = _LowLevel.CK_MECHANISM_ulParameterLen_set
    __swig_getmethods__["ulParameterLen"] = _LowLevel.CK_MECHANISM_ulParameterLen_get
    if _newclass:ulParameterLen = property(_LowLevel.CK_MECHANISM_ulParameterLen_get, _LowLevel.CK_MECHANISM_ulParameterLen_set)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_MECHANISM(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_MECHANISM
    __del__ = lambda self : None;
CK_MECHANISM_swigregister = _LowLevel.CK_MECHANISM_swigregister
CK_MECHANISM_swigregister(CK_MECHANISM)

class CK_MECHANISM_INFO(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_MECHANISM_INFO, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_MECHANISM_INFO, name)
    __repr__ = _swig_repr
    __swig_getmethods__["ulMinKeySize"] = _LowLevel.CK_MECHANISM_INFO_ulMinKeySize_get
    if _newclass:ulMinKeySize = property(_LowLevel.CK_MECHANISM_INFO_ulMinKeySize_get)
    __swig_getmethods__["ulMaxKeySize"] = _LowLevel.CK_MECHANISM_INFO_ulMaxKeySize_get
    if _newclass:ulMaxKeySize = property(_LowLevel.CK_MECHANISM_INFO_ulMaxKeySize_get)
    __swig_getmethods__["flags"] = _LowLevel.CK_MECHANISM_INFO_flags_get
    if _newclass:flags = property(_LowLevel.CK_MECHANISM_INFO_flags_get)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_MECHANISM_INFO(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_MECHANISM_INFO
    __del__ = lambda self : None;
CK_MECHANISM_INFO_swigregister = _LowLevel.CK_MECHANISM_INFO_swigregister
CK_MECHANISM_INFO_swigregister(CK_MECHANISM_INFO)

FALSE = _LowLevel.FALSE
TRUE = _LowLevel.TRUE
CK_TRUE = _LowLevel.CK_TRUE
CK_FALSE = _LowLevel.CK_FALSE
CK_UNAVAILABLE_INFORMATION = _LowLevel.CK_UNAVAILABLE_INFORMATION
CK_EFFECTIVELY_INFINITE = _LowLevel.CK_EFFECTIVELY_INFINITE
CK_INVALID_HANDLE = _LowLevel.CK_INVALID_HANDLE
CKN_SURRENDER = _LowLevel.CKN_SURRENDER
CKF_TOKEN_PRESENT = _LowLevel.CKF_TOKEN_PRESENT
CKF_REMOVABLE_DEVICE = _LowLevel.CKF_REMOVABLE_DEVICE
CKF_HW_SLOT = _LowLevel.CKF_HW_SLOT
CKF_RNG = _LowLevel.CKF_RNG
CKF_WRITE_PROTECTED = _LowLevel.CKF_WRITE_PROTECTED
CKF_LOGIN_REQUIRED = _LowLevel.CKF_LOGIN_REQUIRED
CKF_USER_PIN_INITIALIZED = _LowLevel.CKF_USER_PIN_INITIALIZED
CKF_RESTORE_KEY_NOT_NEEDED = _LowLevel.CKF_RESTORE_KEY_NOT_NEEDED
CKF_CLOCK_ON_TOKEN = _LowLevel.CKF_CLOCK_ON_TOKEN
CKF_PROTECTED_AUTHENTICATION_PATH = _LowLevel.CKF_PROTECTED_AUTHENTICATION_PATH
CKF_DUAL_CRYPTO_OPERATIONS = _LowLevel.CKF_DUAL_CRYPTO_OPERATIONS
CKF_TOKEN_INITIALIZED = _LowLevel.CKF_TOKEN_INITIALIZED
CKF_SECONDARY_AUTHENTICATION = _LowLevel.CKF_SECONDARY_AUTHENTICATION
CKF_USER_PIN_COUNT_LOW = _LowLevel.CKF_USER_PIN_COUNT_LOW
CKF_USER_PIN_FINAL_TRY = _LowLevel.CKF_USER_PIN_FINAL_TRY
CKF_USER_PIN_LOCKED = _LowLevel.CKF_USER_PIN_LOCKED
CKF_USER_PIN_TO_BE_CHANGED = _LowLevel.CKF_USER_PIN_TO_BE_CHANGED
CKF_SO_PIN_COUNT_LOW = _LowLevel.CKF_SO_PIN_COUNT_LOW
CKF_SO_PIN_FINAL_TRY = _LowLevel.CKF_SO_PIN_FINAL_TRY
CKF_SO_PIN_LOCKED = _LowLevel.CKF_SO_PIN_LOCKED
CKF_SO_PIN_TO_BE_CHANGED = _LowLevel.CKF_SO_PIN_TO_BE_CHANGED
CKU_SO = _LowLevel.CKU_SO
CKU_USER = _LowLevel.CKU_USER
CKS_RO_PUBLIC_SESSION = _LowLevel.CKS_RO_PUBLIC_SESSION
CKS_RO_USER_FUNCTIONS = _LowLevel.CKS_RO_USER_FUNCTIONS
CKS_RW_PUBLIC_SESSION = _LowLevel.CKS_RW_PUBLIC_SESSION
CKS_RW_USER_FUNCTIONS = _LowLevel.CKS_RW_USER_FUNCTIONS
CKS_RW_SO_FUNCTIONS = _LowLevel.CKS_RW_SO_FUNCTIONS
CKF_RW_SESSION = _LowLevel.CKF_RW_SESSION
CKF_SERIAL_SESSION = _LowLevel.CKF_SERIAL_SESSION
CKO_DATA = _LowLevel.CKO_DATA
CKO_CERTIFICATE = _LowLevel.CKO_CERTIFICATE
CKO_PUBLIC_KEY = _LowLevel.CKO_PUBLIC_KEY
CKO_PRIVATE_KEY = _LowLevel.CKO_PRIVATE_KEY
CKO_SECRET_KEY = _LowLevel.CKO_SECRET_KEY
CKO_HW_FEATURE = _LowLevel.CKO_HW_FEATURE
CKO_DOMAIN_PARAMETERS = _LowLevel.CKO_DOMAIN_PARAMETERS
CKO_MECHANISM = _LowLevel.CKO_MECHANISM
CKO_VENDOR_DEFINED = _LowLevel.CKO_VENDOR_DEFINED
CKH_MONOTONIC_COUNTER = _LowLevel.CKH_MONOTONIC_COUNTER
CKH_CLOCK = _LowLevel.CKH_CLOCK
CKH_VENDOR_DEFINED = _LowLevel.CKH_VENDOR_DEFINED
CKK_RSA = _LowLevel.CKK_RSA
CKK_DSA = _LowLevel.CKK_DSA
CKK_DH = _LowLevel.CKK_DH
CKK_ECDSA = _LowLevel.CKK_ECDSA
CKK_EC = _LowLevel.CKK_EC
CKK_X9_42_DH = _LowLevel.CKK_X9_42_DH
CKK_KEA = _LowLevel.CKK_KEA
CKK_GENERIC_SECRET = _LowLevel.CKK_GENERIC_SECRET
CKK_RC2 = _LowLevel.CKK_RC2
CKK_RC4 = _LowLevel.CKK_RC4
CKK_DES = _LowLevel.CKK_DES
CKK_DES2 = _LowLevel.CKK_DES2
CKK_DES3 = _LowLevel.CKK_DES3
CKK_CAST = _LowLevel.CKK_CAST
CKK_CAST3 = _LowLevel.CKK_CAST3
CKK_CAST5 = _LowLevel.CKK_CAST5
CKK_CAST128 = _LowLevel.CKK_CAST128
CKK_RC5 = _LowLevel.CKK_RC5
CKK_IDEA = _LowLevel.CKK_IDEA
CKK_SKIPJACK = _LowLevel.CKK_SKIPJACK
CKK_BATON = _LowLevel.CKK_BATON
CKK_JUNIPER = _LowLevel.CKK_JUNIPER
CKK_CDMF = _LowLevel.CKK_CDMF
CKK_AES = _LowLevel.CKK_AES
CKK_BLOWFISH = _LowLevel.CKK_BLOWFISH
CKK_TWOFISH = _LowLevel.CKK_TWOFISH
CKK_VENDOR_DEFINED = _LowLevel.CKK_VENDOR_DEFINED
CKC_X_509 = _LowLevel.CKC_X_509
CKC_X_509_ATTR_CERT = _LowLevel.CKC_X_509_ATTR_CERT
CKC_WTLS = _LowLevel.CKC_WTLS
CKC_VENDOR_DEFINED = _LowLevel.CKC_VENDOR_DEFINED
CKA_CLASS = _LowLevel.CKA_CLASS
CKA_TOKEN = _LowLevel.CKA_TOKEN
CKA_PRIVATE = _LowLevel.CKA_PRIVATE
CKA_LABEL = _LowLevel.CKA_LABEL
CKA_APPLICATION = _LowLevel.CKA_APPLICATION
CKA_VALUE = _LowLevel.CKA_VALUE
CKA_OBJECT_ID = _LowLevel.CKA_OBJECT_ID
CKA_CERTIFICATE_TYPE = _LowLevel.CKA_CERTIFICATE_TYPE
CKA_ISSUER = _LowLevel.CKA_ISSUER
CKA_SERIAL_NUMBER = _LowLevel.CKA_SERIAL_NUMBER
CKA_AC_ISSUER = _LowLevel.CKA_AC_ISSUER
CKA_OWNER = _LowLevel.CKA_OWNER
CKA_ATTR_TYPES = _LowLevel.CKA_ATTR_TYPES
CKA_TRUSTED = _LowLevel.CKA_TRUSTED
CKA_KEY_TYPE = _LowLevel.CKA_KEY_TYPE
CKA_SUBJECT = _LowLevel.CKA_SUBJECT
CKA_ID = _LowLevel.CKA_ID
CKA_SENSITIVE = _LowLevel.CKA_SENSITIVE
CKA_ENCRYPT = _LowLevel.CKA_ENCRYPT
CKA_DECRYPT = _LowLevel.CKA_DECRYPT
CKA_WRAP = _LowLevel.CKA_WRAP
CKA_UNWRAP = _LowLevel.CKA_UNWRAP
CKA_SIGN = _LowLevel.CKA_SIGN
CKA_SIGN_RECOVER = _LowLevel.CKA_SIGN_RECOVER
CKA_VERIFY = _LowLevel.CKA_VERIFY
CKA_VERIFY_RECOVER = _LowLevel.CKA_VERIFY_RECOVER
CKA_DERIVE = _LowLevel.CKA_DERIVE
CKA_START_DATE = _LowLevel.CKA_START_DATE
CKA_END_DATE = _LowLevel.CKA_END_DATE
CKA_MODULUS = _LowLevel.CKA_MODULUS
CKA_MODULUS_BITS = _LowLevel.CKA_MODULUS_BITS
CKA_PUBLIC_EXPONENT = _LowLevel.CKA_PUBLIC_EXPONENT
CKA_PRIVATE_EXPONENT = _LowLevel.CKA_PRIVATE_EXPONENT
CKA_PRIME_1 = _LowLevel.CKA_PRIME_1
CKA_PRIME_2 = _LowLevel.CKA_PRIME_2
CKA_EXPONENT_1 = _LowLevel.CKA_EXPONENT_1
CKA_EXPONENT_2 = _LowLevel.CKA_EXPONENT_2
CKA_COEFFICIENT = _LowLevel.CKA_COEFFICIENT
CKA_PRIME = _LowLevel.CKA_PRIME
CKA_SUBPRIME = _LowLevel.CKA_SUBPRIME
CKA_BASE = _LowLevel.CKA_BASE
CKA_PRIME_BITS = _LowLevel.CKA_PRIME_BITS
CKA_SUBPRIME_BITS = _LowLevel.CKA_SUBPRIME_BITS
CKA_SUB_PRIME_BITS = _LowLevel.CKA_SUB_PRIME_BITS
CKA_VALUE_BITS = _LowLevel.CKA_VALUE_BITS
CKA_VALUE_LEN = _LowLevel.CKA_VALUE_LEN
CKA_EXTRACTABLE = _LowLevel.CKA_EXTRACTABLE
CKA_LOCAL = _LowLevel.CKA_LOCAL
CKA_NEVER_EXTRACTABLE = _LowLevel.CKA_NEVER_EXTRACTABLE
CKA_ALWAYS_SENSITIVE = _LowLevel.CKA_ALWAYS_SENSITIVE
CKA_KEY_GEN_MECHANISM = _LowLevel.CKA_KEY_GEN_MECHANISM
CKA_MODIFIABLE = _LowLevel.CKA_MODIFIABLE
CKA_ECDSA_PARAMS = _LowLevel.CKA_ECDSA_PARAMS
CKA_EC_PARAMS = _LowLevel.CKA_EC_PARAMS
CKA_EC_POINT = _LowLevel.CKA_EC_POINT
CKA_SECONDARY_AUTH = _LowLevel.CKA_SECONDARY_AUTH
CKA_AUTH_PIN_FLAGS = _LowLevel.CKA_AUTH_PIN_FLAGS
CKA_HW_FEATURE_TYPE = _LowLevel.CKA_HW_FEATURE_TYPE
CKA_RESET_ON_INIT = _LowLevel.CKA_RESET_ON_INIT
CKA_HAS_RESET = _LowLevel.CKA_HAS_RESET
CKA_VENDOR_DEFINED = _LowLevel.CKA_VENDOR_DEFINED
CKM_RSA_PKCS_KEY_PAIR_GEN = _LowLevel.CKM_RSA_PKCS_KEY_PAIR_GEN
CKM_RSA_PKCS = _LowLevel.CKM_RSA_PKCS
CKM_RSA_9796 = _LowLevel.CKM_RSA_9796
CKM_RSA_X_509 = _LowLevel.CKM_RSA_X_509
CKM_MD2_RSA_PKCS = _LowLevel.CKM_MD2_RSA_PKCS
CKM_MD5_RSA_PKCS = _LowLevel.CKM_MD5_RSA_PKCS
CKM_SHA1_RSA_PKCS = _LowLevel.CKM_SHA1_RSA_PKCS
CKM_RIPEMD128_RSA_PKCS = _LowLevel.CKM_RIPEMD128_RSA_PKCS
CKM_RIPEMD160_RSA_PKCS = _LowLevel.CKM_RIPEMD160_RSA_PKCS
CKM_RSA_PKCS_OAEP = _LowLevel.CKM_RSA_PKCS_OAEP
CKM_RSA_X9_31_KEY_PAIR_GEN = _LowLevel.CKM_RSA_X9_31_KEY_PAIR_GEN
CKM_RSA_X9_31 = _LowLevel.CKM_RSA_X9_31
CKM_SHA1_RSA_X9_31 = _LowLevel.CKM_SHA1_RSA_X9_31
CKM_RSA_PKCS_PSS = _LowLevel.CKM_RSA_PKCS_PSS
CKM_SHA1_RSA_PKCS_PSS = _LowLevel.CKM_SHA1_RSA_PKCS_PSS
CKM_DSA_KEY_PAIR_GEN = _LowLevel.CKM_DSA_KEY_PAIR_GEN
CKM_DSA = _LowLevel.CKM_DSA
CKM_DSA_SHA1 = _LowLevel.CKM_DSA_SHA1
CKM_DH_PKCS_KEY_PAIR_GEN = _LowLevel.CKM_DH_PKCS_KEY_PAIR_GEN
CKM_DH_PKCS_DERIVE = _LowLevel.CKM_DH_PKCS_DERIVE
CKM_X9_42_DH_KEY_PAIR_GEN = _LowLevel.CKM_X9_42_DH_KEY_PAIR_GEN
CKM_X9_42_DH_DERIVE = _LowLevel.CKM_X9_42_DH_DERIVE
CKM_X9_42_DH_HYBRID_DERIVE = _LowLevel.CKM_X9_42_DH_HYBRID_DERIVE
CKM_X9_42_MQV_DERIVE = _LowLevel.CKM_X9_42_MQV_DERIVE
CKM_SHA256_RSA_PKCS = _LowLevel.CKM_SHA256_RSA_PKCS
CKM_SHA384_RSA_PKCS = _LowLevel.CKM_SHA384_RSA_PKCS
CKM_SHA512_RSA_PKCS = _LowLevel.CKM_SHA512_RSA_PKCS
CKM_SHA256_RSA_PKCS_PSS = _LowLevel.CKM_SHA256_RSA_PKCS_PSS
CKM_SHA384_RSA_PKCS_PSS = _LowLevel.CKM_SHA384_RSA_PKCS_PSS
CKM_SHA512_RSA_PKCS_PSS = _LowLevel.CKM_SHA512_RSA_PKCS_PSS
CKM_RC2_KEY_GEN = _LowLevel.CKM_RC2_KEY_GEN
CKM_RC2_ECB = _LowLevel.CKM_RC2_ECB
CKM_RC2_CBC = _LowLevel.CKM_RC2_CBC
CKM_RC2_MAC = _LowLevel.CKM_RC2_MAC
CKM_RC2_MAC_GENERAL = _LowLevel.CKM_RC2_MAC_GENERAL
CKM_RC2_CBC_PAD = _LowLevel.CKM_RC2_CBC_PAD
CKM_RC4_KEY_GEN = _LowLevel.CKM_RC4_KEY_GEN
CKM_RC4 = _LowLevel.CKM_RC4
CKM_DES_KEY_GEN = _LowLevel.CKM_DES_KEY_GEN
CKM_DES_ECB = _LowLevel.CKM_DES_ECB
CKM_DES_CBC = _LowLevel.CKM_DES_CBC
CKM_DES_MAC = _LowLevel.CKM_DES_MAC
CKM_DES_MAC_GENERAL = _LowLevel.CKM_DES_MAC_GENERAL
CKM_DES_CBC_PAD = _LowLevel.CKM_DES_CBC_PAD
CKM_DES2_KEY_GEN = _LowLevel.CKM_DES2_KEY_GEN
CKM_DES3_KEY_GEN = _LowLevel.CKM_DES3_KEY_GEN
CKM_DES3_ECB = _LowLevel.CKM_DES3_ECB
CKM_DES3_CBC = _LowLevel.CKM_DES3_CBC
CKM_DES3_MAC = _LowLevel.CKM_DES3_MAC
CKM_DES3_MAC_GENERAL = _LowLevel.CKM_DES3_MAC_GENERAL
CKM_DES3_CBC_PAD = _LowLevel.CKM_DES3_CBC_PAD
CKM_CDMF_KEY_GEN = _LowLevel.CKM_CDMF_KEY_GEN
CKM_CDMF_ECB = _LowLevel.CKM_CDMF_ECB
CKM_CDMF_CBC = _LowLevel.CKM_CDMF_CBC
CKM_CDMF_MAC = _LowLevel.CKM_CDMF_MAC
CKM_CDMF_MAC_GENERAL = _LowLevel.CKM_CDMF_MAC_GENERAL
CKM_CDMF_CBC_PAD = _LowLevel.CKM_CDMF_CBC_PAD
CKM_DES_OFB64 = _LowLevel.CKM_DES_OFB64
CKM_DES_OFB8 = _LowLevel.CKM_DES_OFB8
CKM_DES_CFB64 = _LowLevel.CKM_DES_CFB64
CKM_DES_CFB8 = _LowLevel.CKM_DES_CFB8
CKM_MD2 = _LowLevel.CKM_MD2
CKM_MD2_HMAC = _LowLevel.CKM_MD2_HMAC
CKM_MD2_HMAC_GENERAL = _LowLevel.CKM_MD2_HMAC_GENERAL
CKM_MD5 = _LowLevel.CKM_MD5
CKM_MD5_HMAC = _LowLevel.CKM_MD5_HMAC
CKM_MD5_HMAC_GENERAL = _LowLevel.CKM_MD5_HMAC_GENERAL
CKM_SHA_1 = _LowLevel.CKM_SHA_1
CKM_SHA_1_HMAC = _LowLevel.CKM_SHA_1_HMAC
CKM_SHA_1_HMAC_GENERAL = _LowLevel.CKM_SHA_1_HMAC_GENERAL
CKM_RIPEMD128 = _LowLevel.CKM_RIPEMD128
CKM_RIPEMD128_HMAC = _LowLevel.CKM_RIPEMD128_HMAC
CKM_RIPEMD128_HMAC_GENERAL = _LowLevel.CKM_RIPEMD128_HMAC_GENERAL
CKM_RIPEMD160 = _LowLevel.CKM_RIPEMD160
CKM_RIPEMD160_HMAC = _LowLevel.CKM_RIPEMD160_HMAC
CKM_RIPEMD160_HMAC_GENERAL = _LowLevel.CKM_RIPEMD160_HMAC_GENERAL
CKM_SHA256 = _LowLevel.CKM_SHA256
CKM_SHA256_HMAC = _LowLevel.CKM_SHA256_HMAC
CKM_SHA256_HMAC_GENERAL = _LowLevel.CKM_SHA256_HMAC_GENERAL
CKM_SHA384 = _LowLevel.CKM_SHA384
CKM_SHA384_HMAC = _LowLevel.CKM_SHA384_HMAC
CKM_SHA384_HMAC_GENERAL = _LowLevel.CKM_SHA384_HMAC_GENERAL
CKM_SHA512 = _LowLevel.CKM_SHA512
CKM_SHA512_HMAC = _LowLevel.CKM_SHA512_HMAC
CKM_SHA512_HMAC_GENERAL = _LowLevel.CKM_SHA512_HMAC_GENERAL
CKM_CAST_KEY_GEN = _LowLevel.CKM_CAST_KEY_GEN
CKM_CAST_ECB = _LowLevel.CKM_CAST_ECB
CKM_CAST_CBC = _LowLevel.CKM_CAST_CBC
CKM_CAST_MAC = _LowLevel.CKM_CAST_MAC
CKM_CAST_MAC_GENERAL = _LowLevel.CKM_CAST_MAC_GENERAL
CKM_CAST_CBC_PAD = _LowLevel.CKM_CAST_CBC_PAD
CKM_CAST3_KEY_GEN = _LowLevel.CKM_CAST3_KEY_GEN
CKM_CAST3_ECB = _LowLevel.CKM_CAST3_ECB
CKM_CAST3_CBC = _LowLevel.CKM_CAST3_CBC
CKM_CAST3_MAC = _LowLevel.CKM_CAST3_MAC
CKM_CAST3_MAC_GENERAL = _LowLevel.CKM_CAST3_MAC_GENERAL
CKM_CAST3_CBC_PAD = _LowLevel.CKM_CAST3_CBC_PAD
CKM_CAST5_KEY_GEN = _LowLevel.CKM_CAST5_KEY_GEN
CKM_CAST128_KEY_GEN = _LowLevel.CKM_CAST128_KEY_GEN
CKM_CAST5_ECB = _LowLevel.CKM_CAST5_ECB
CKM_CAST128_ECB = _LowLevel.CKM_CAST128_ECB
CKM_CAST5_CBC = _LowLevel.CKM_CAST5_CBC
CKM_CAST128_CBC = _LowLevel.CKM_CAST128_CBC
CKM_CAST5_MAC = _LowLevel.CKM_CAST5_MAC
CKM_CAST128_MAC = _LowLevel.CKM_CAST128_MAC
CKM_CAST5_MAC_GENERAL = _LowLevel.CKM_CAST5_MAC_GENERAL
CKM_CAST128_MAC_GENERAL = _LowLevel.CKM_CAST128_MAC_GENERAL
CKM_CAST5_CBC_PAD = _LowLevel.CKM_CAST5_CBC_PAD
CKM_CAST128_CBC_PAD = _LowLevel.CKM_CAST128_CBC_PAD
CKM_RC5_KEY_GEN = _LowLevel.CKM_RC5_KEY_GEN
CKM_RC5_ECB = _LowLevel.CKM_RC5_ECB
CKM_RC5_CBC = _LowLevel.CKM_RC5_CBC
CKM_RC5_MAC = _LowLevel.CKM_RC5_MAC
CKM_RC5_MAC_GENERAL = _LowLevel.CKM_RC5_MAC_GENERAL
CKM_RC5_CBC_PAD = _LowLevel.CKM_RC5_CBC_PAD
CKM_IDEA_KEY_GEN = _LowLevel.CKM_IDEA_KEY_GEN
CKM_IDEA_ECB = _LowLevel.CKM_IDEA_ECB
CKM_IDEA_CBC = _LowLevel.CKM_IDEA_CBC
CKM_IDEA_MAC = _LowLevel.CKM_IDEA_MAC
CKM_IDEA_MAC_GENERAL = _LowLevel.CKM_IDEA_MAC_GENERAL
CKM_IDEA_CBC_PAD = _LowLevel.CKM_IDEA_CBC_PAD
CKM_GENERIC_SECRET_KEY_GEN = _LowLevel.CKM_GENERIC_SECRET_KEY_GEN
CKM_CONCATENATE_BASE_AND_KEY = _LowLevel.CKM_CONCATENATE_BASE_AND_KEY
CKM_CONCATENATE_BASE_AND_DATA = _LowLevel.CKM_CONCATENATE_BASE_AND_DATA
CKM_CONCATENATE_DATA_AND_BASE = _LowLevel.CKM_CONCATENATE_DATA_AND_BASE
CKM_XOR_BASE_AND_DATA = _LowLevel.CKM_XOR_BASE_AND_DATA
CKM_EXTRACT_KEY_FROM_KEY = _LowLevel.CKM_EXTRACT_KEY_FROM_KEY
CKM_SSL3_PRE_MASTER_KEY_GEN = _LowLevel.CKM_SSL3_PRE_MASTER_KEY_GEN
CKM_SSL3_MASTER_KEY_DERIVE = _LowLevel.CKM_SSL3_MASTER_KEY_DERIVE
CKM_SSL3_KEY_AND_MAC_DERIVE = _LowLevel.CKM_SSL3_KEY_AND_MAC_DERIVE
CKM_SSL3_MASTER_KEY_DERIVE_DH = _LowLevel.CKM_SSL3_MASTER_KEY_DERIVE_DH
CKM_TLS_PRE_MASTER_KEY_GEN = _LowLevel.CKM_TLS_PRE_MASTER_KEY_GEN
CKM_TLS_MASTER_KEY_DERIVE = _LowLevel.CKM_TLS_MASTER_KEY_DERIVE
CKM_TLS_KEY_AND_MAC_DERIVE = _LowLevel.CKM_TLS_KEY_AND_MAC_DERIVE
CKM_TLS_MASTER_KEY_DERIVE_DH = _LowLevel.CKM_TLS_MASTER_KEY_DERIVE_DH
CKM_TLS_PRF = _LowLevel.CKM_TLS_PRF
CKM_SSL3_MD5_MAC = _LowLevel.CKM_SSL3_MD5_MAC
CKM_SSL3_SHA1_MAC = _LowLevel.CKM_SSL3_SHA1_MAC
CKM_MD5_KEY_DERIVATION = _LowLevel.CKM_MD5_KEY_DERIVATION
CKM_MD2_KEY_DERIVATION = _LowLevel.CKM_MD2_KEY_DERIVATION
CKM_SHA1_KEY_DERIVATION = _LowLevel.CKM_SHA1_KEY_DERIVATION
CKM_SHA256_KEY_DERIVATION = _LowLevel.CKM_SHA256_KEY_DERIVATION
CKM_SHA384_KEY_DERIVATION = _LowLevel.CKM_SHA384_KEY_DERIVATION
CKM_SHA512_KEY_DERIVATION = _LowLevel.CKM_SHA512_KEY_DERIVATION
CKM_PBE_MD2_DES_CBC = _LowLevel.CKM_PBE_MD2_DES_CBC
CKM_PBE_MD5_DES_CBC = _LowLevel.CKM_PBE_MD5_DES_CBC
CKM_PBE_MD5_CAST_CBC = _LowLevel.CKM_PBE_MD5_CAST_CBC
CKM_PBE_MD5_CAST3_CBC = _LowLevel.CKM_PBE_MD5_CAST3_CBC
CKM_PBE_MD5_CAST5_CBC = _LowLevel.CKM_PBE_MD5_CAST5_CBC
CKM_PBE_MD5_CAST128_CBC = _LowLevel.CKM_PBE_MD5_CAST128_CBC
CKM_PBE_SHA1_CAST5_CBC = _LowLevel.CKM_PBE_SHA1_CAST5_CBC
CKM_PBE_SHA1_CAST128_CBC = _LowLevel.CKM_PBE_SHA1_CAST128_CBC
CKM_PBE_SHA1_RC4_128 = _LowLevel.CKM_PBE_SHA1_RC4_128
CKM_PBE_SHA1_RC4_40 = _LowLevel.CKM_PBE_SHA1_RC4_40
CKM_PBE_SHA1_DES3_EDE_CBC = _LowLevel.CKM_PBE_SHA1_DES3_EDE_CBC
CKM_PBE_SHA1_DES2_EDE_CBC = _LowLevel.CKM_PBE_SHA1_DES2_EDE_CBC
CKM_PBE_SHA1_RC2_128_CBC = _LowLevel.CKM_PBE_SHA1_RC2_128_CBC
CKM_PBE_SHA1_RC2_40_CBC = _LowLevel.CKM_PBE_SHA1_RC2_40_CBC
CKM_PKCS5_PBKD2 = _LowLevel.CKM_PKCS5_PBKD2
CKM_PBA_SHA1_WITH_SHA1_HMAC = _LowLevel.CKM_PBA_SHA1_WITH_SHA1_HMAC
CKM_WTLS_PRE_MASTER_KEY_GEN = _LowLevel.CKM_WTLS_PRE_MASTER_KEY_GEN
CKM_WTLS_MASTER_KEY_DERIVE = _LowLevel.CKM_WTLS_MASTER_KEY_DERIVE
CKM_WTLS_MASTER_KEY_DERIVE_DH_ECC = _LowLevel.CKM_WTLS_MASTER_KEY_DERIVE_DH_ECC
CKM_WTLS_PRF = _LowLevel.CKM_WTLS_PRF
CKM_WTLS_SERVER_KEY_AND_MAC_DERIVE = _LowLevel.CKM_WTLS_SERVER_KEY_AND_MAC_DERIVE
CKM_WTLS_CLIENT_KEY_AND_MAC_DERIVE = _LowLevel.CKM_WTLS_CLIENT_KEY_AND_MAC_DERIVE
CKM_KEY_WRAP_LYNKS = _LowLevel.CKM_KEY_WRAP_LYNKS
CKM_KEY_WRAP_SET_OAEP = _LowLevel.CKM_KEY_WRAP_SET_OAEP
CKM_CMS_SIG = _LowLevel.CKM_CMS_SIG
CKM_SKIPJACK_KEY_GEN = _LowLevel.CKM_SKIPJACK_KEY_GEN
CKM_SKIPJACK_ECB64 = _LowLevel.CKM_SKIPJACK_ECB64
CKM_SKIPJACK_CBC64 = _LowLevel.CKM_SKIPJACK_CBC64
CKM_SKIPJACK_OFB64 = _LowLevel.CKM_SKIPJACK_OFB64
CKM_SKIPJACK_CFB64 = _LowLevel.CKM_SKIPJACK_CFB64
CKM_SKIPJACK_CFB32 = _LowLevel.CKM_SKIPJACK_CFB32
CKM_SKIPJACK_CFB16 = _LowLevel.CKM_SKIPJACK_CFB16
CKM_SKIPJACK_CFB8 = _LowLevel.CKM_SKIPJACK_CFB8
CKM_SKIPJACK_WRAP = _LowLevel.CKM_SKIPJACK_WRAP
CKM_SKIPJACK_PRIVATE_WRAP = _LowLevel.CKM_SKIPJACK_PRIVATE_WRAP
CKM_SKIPJACK_RELAYX = _LowLevel.CKM_SKIPJACK_RELAYX
CKM_KEA_KEY_PAIR_GEN = _LowLevel.CKM_KEA_KEY_PAIR_GEN
CKM_KEA_KEY_DERIVE = _LowLevel.CKM_KEA_KEY_DERIVE
CKM_FORTEZZA_TIMESTAMP = _LowLevel.CKM_FORTEZZA_TIMESTAMP
CKM_BATON_KEY_GEN = _LowLevel.CKM_BATON_KEY_GEN
CKM_BATON_ECB128 = _LowLevel.CKM_BATON_ECB128
CKM_BATON_ECB96 = _LowLevel.CKM_BATON_ECB96
CKM_BATON_CBC128 = _LowLevel.CKM_BATON_CBC128
CKM_BATON_COUNTER = _LowLevel.CKM_BATON_COUNTER
CKM_BATON_SHUFFLE = _LowLevel.CKM_BATON_SHUFFLE
CKM_BATON_WRAP = _LowLevel.CKM_BATON_WRAP
CKM_ECDSA_KEY_PAIR_GEN = _LowLevel.CKM_ECDSA_KEY_PAIR_GEN
CKM_EC_KEY_PAIR_GEN = _LowLevel.CKM_EC_KEY_PAIR_GEN
CKM_ECDSA = _LowLevel.CKM_ECDSA
CKM_ECDSA_SHA1 = _LowLevel.CKM_ECDSA_SHA1
CKM_ECDH1_DERIVE = _LowLevel.CKM_ECDH1_DERIVE
CKM_ECDH1_COFACTOR_DERIVE = _LowLevel.CKM_ECDH1_COFACTOR_DERIVE
CKM_ECMQV_DERIVE = _LowLevel.CKM_ECMQV_DERIVE
CKM_JUNIPER_KEY_GEN = _LowLevel.CKM_JUNIPER_KEY_GEN
CKM_JUNIPER_ECB128 = _LowLevel.CKM_JUNIPER_ECB128
CKM_JUNIPER_CBC128 = _LowLevel.CKM_JUNIPER_CBC128
CKM_JUNIPER_COUNTER = _LowLevel.CKM_JUNIPER_COUNTER
CKM_JUNIPER_SHUFFLE = _LowLevel.CKM_JUNIPER_SHUFFLE
CKM_JUNIPER_WRAP = _LowLevel.CKM_JUNIPER_WRAP
CKM_FASTHASH = _LowLevel.CKM_FASTHASH
CKM_AES_KEY_GEN = _LowLevel.CKM_AES_KEY_GEN
CKM_AES_ECB = _LowLevel.CKM_AES_ECB
CKM_AES_CBC = _LowLevel.CKM_AES_CBC
CKM_AES_MAC = _LowLevel.CKM_AES_MAC
CKM_AES_MAC_GENERAL = _LowLevel.CKM_AES_MAC_GENERAL
CKM_AES_CBC_PAD = _LowLevel.CKM_AES_CBC_PAD
CKM_BLOWFISH_KEY_GEN = _LowLevel.CKM_BLOWFISH_KEY_GEN
CKM_BLOWFISH_CBC = _LowLevel.CKM_BLOWFISH_CBC
CKM_TWOFISH_KEY_GEN = _LowLevel.CKM_TWOFISH_KEY_GEN
CKM_TWOFISH_CBC = _LowLevel.CKM_TWOFISH_CBC
CKM_DES_ECB_ENCRYPT_DATA = _LowLevel.CKM_DES_ECB_ENCRYPT_DATA
CKM_DES_CBC_ENCRYPT_DATA = _LowLevel.CKM_DES_CBC_ENCRYPT_DATA
CKM_DES3_ECB_ENCRYPT_DATA = _LowLevel.CKM_DES3_ECB_ENCRYPT_DATA
CKM_DES3_CBC_ENCRYPT_DATA = _LowLevel.CKM_DES3_CBC_ENCRYPT_DATA
CKM_AES_ECB_ENCRYPT_DATA = _LowLevel.CKM_AES_ECB_ENCRYPT_DATA
CKM_AES_CBC_ENCRYPT_DATA = _LowLevel.CKM_AES_CBC_ENCRYPT_DATA
CKM_DSA_PARAMETER_GEN = _LowLevel.CKM_DSA_PARAMETER_GEN
CKM_DH_PKCS_PARAMETER_GEN = _LowLevel.CKM_DH_PKCS_PARAMETER_GEN
CKM_X9_42_DH_PARAMETER_GEN = _LowLevel.CKM_X9_42_DH_PARAMETER_GEN
CKM_VENDOR_DEFINED = _LowLevel.CKM_VENDOR_DEFINED
CKF_HW = _LowLevel.CKF_HW
CKF_ENCRYPT = _LowLevel.CKF_ENCRYPT
CKF_DECRYPT = _LowLevel.CKF_DECRYPT
CKF_DIGEST = _LowLevel.CKF_DIGEST
CKF_SIGN = _LowLevel.CKF_SIGN
CKF_SIGN_RECOVER = _LowLevel.CKF_SIGN_RECOVER
CKF_VERIFY = _LowLevel.CKF_VERIFY
CKF_VERIFY_RECOVER = _LowLevel.CKF_VERIFY_RECOVER
CKF_GENERATE = _LowLevel.CKF_GENERATE
CKF_GENERATE_KEY_PAIR = _LowLevel.CKF_GENERATE_KEY_PAIR
CKF_WRAP = _LowLevel.CKF_WRAP
CKF_UNWRAP = _LowLevel.CKF_UNWRAP
CKF_DERIVE = _LowLevel.CKF_DERIVE
CKF_EC_F_P = _LowLevel.CKF_EC_F_P
CKF_EC_F_2M = _LowLevel.CKF_EC_F_2M
CKF_EC_ECPARAMETERS = _LowLevel.CKF_EC_ECPARAMETERS
CKF_EC_NAMEDCURVE = _LowLevel.CKF_EC_NAMEDCURVE
CKF_EC_UNCOMPRESS = _LowLevel.CKF_EC_UNCOMPRESS
CKF_EC_COMPRESS = _LowLevel.CKF_EC_COMPRESS
CKF_EXTENSION = _LowLevel.CKF_EXTENSION
CKR_OK = _LowLevel.CKR_OK
CKR_CANCEL = _LowLevel.CKR_CANCEL
CKR_HOST_MEMORY = _LowLevel.CKR_HOST_MEMORY
CKR_SLOT_ID_INVALID = _LowLevel.CKR_SLOT_ID_INVALID
CKR_GENERAL_ERROR = _LowLevel.CKR_GENERAL_ERROR
CKR_FUNCTION_FAILED = _LowLevel.CKR_FUNCTION_FAILED
CKR_ARGUMENTS_BAD = _LowLevel.CKR_ARGUMENTS_BAD
CKR_NO_EVENT = _LowLevel.CKR_NO_EVENT
CKR_NEED_TO_CREATE_THREADS = _LowLevel.CKR_NEED_TO_CREATE_THREADS
CKR_CANT_LOCK = _LowLevel.CKR_CANT_LOCK
CKR_ATTRIBUTE_READ_ONLY = _LowLevel.CKR_ATTRIBUTE_READ_ONLY
CKR_ATTRIBUTE_SENSITIVE = _LowLevel.CKR_ATTRIBUTE_SENSITIVE
CKR_ATTRIBUTE_TYPE_INVALID = _LowLevel.CKR_ATTRIBUTE_TYPE_INVALID
CKR_ATTRIBUTE_VALUE_INVALID = _LowLevel.CKR_ATTRIBUTE_VALUE_INVALID
CKR_DATA_INVALID = _LowLevel.CKR_DATA_INVALID
CKR_DATA_LEN_RANGE = _LowLevel.CKR_DATA_LEN_RANGE
CKR_DEVICE_ERROR = _LowLevel.CKR_DEVICE_ERROR
CKR_DEVICE_MEMORY = _LowLevel.CKR_DEVICE_MEMORY
CKR_DEVICE_REMOVED = _LowLevel.CKR_DEVICE_REMOVED
CKR_ENCRYPTED_DATA_INVALID = _LowLevel.CKR_ENCRYPTED_DATA_INVALID
CKR_ENCRYPTED_DATA_LEN_RANGE = _LowLevel.CKR_ENCRYPTED_DATA_LEN_RANGE
CKR_FUNCTION_CANCELED = _LowLevel.CKR_FUNCTION_CANCELED
CKR_FUNCTION_NOT_PARALLEL = _LowLevel.CKR_FUNCTION_NOT_PARALLEL
CKR_FUNCTION_NOT_SUPPORTED = _LowLevel.CKR_FUNCTION_NOT_SUPPORTED
CKR_KEY_HANDLE_INVALID = _LowLevel.CKR_KEY_HANDLE_INVALID
CKR_KEY_SIZE_RANGE = _LowLevel.CKR_KEY_SIZE_RANGE
CKR_KEY_TYPE_INCONSISTENT = _LowLevel.CKR_KEY_TYPE_INCONSISTENT
CKR_KEY_NOT_NEEDED = _LowLevel.CKR_KEY_NOT_NEEDED
CKR_KEY_CHANGED = _LowLevel.CKR_KEY_CHANGED
CKR_KEY_NEEDED = _LowLevel.CKR_KEY_NEEDED
CKR_KEY_INDIGESTIBLE = _LowLevel.CKR_KEY_INDIGESTIBLE
CKR_KEY_FUNCTION_NOT_PERMITTED = _LowLevel.CKR_KEY_FUNCTION_NOT_PERMITTED
CKR_KEY_NOT_WRAPPABLE = _LowLevel.CKR_KEY_NOT_WRAPPABLE
CKR_KEY_UNEXTRACTABLE = _LowLevel.CKR_KEY_UNEXTRACTABLE
CKR_MECHANISM_INVALID = _LowLevel.CKR_MECHANISM_INVALID
CKR_MECHANISM_PARAM_INVALID = _LowLevel.CKR_MECHANISM_PARAM_INVALID
CKR_OBJECT_HANDLE_INVALID = _LowLevel.CKR_OBJECT_HANDLE_INVALID
CKR_OPERATION_ACTIVE = _LowLevel.CKR_OPERATION_ACTIVE
CKR_OPERATION_NOT_INITIALIZED = _LowLevel.CKR_OPERATION_NOT_INITIALIZED
CKR_PIN_INCORRECT = _LowLevel.CKR_PIN_INCORRECT
CKR_PIN_INVALID = _LowLevel.CKR_PIN_INVALID
CKR_PIN_LEN_RANGE = _LowLevel.CKR_PIN_LEN_RANGE
CKR_PIN_EXPIRED = _LowLevel.CKR_PIN_EXPIRED
CKR_PIN_LOCKED = _LowLevel.CKR_PIN_LOCKED
CKR_SESSION_CLOSED = _LowLevel.CKR_SESSION_CLOSED
CKR_SESSION_COUNT = _LowLevel.CKR_SESSION_COUNT
CKR_SESSION_HANDLE_INVALID = _LowLevel.CKR_SESSION_HANDLE_INVALID
CKR_SESSION_PARALLEL_NOT_SUPPORTED = _LowLevel.CKR_SESSION_PARALLEL_NOT_SUPPORTED
CKR_SESSION_READ_ONLY = _LowLevel.CKR_SESSION_READ_ONLY
CKR_SESSION_EXISTS = _LowLevel.CKR_SESSION_EXISTS
CKR_SESSION_READ_ONLY_EXISTS = _LowLevel.CKR_SESSION_READ_ONLY_EXISTS
CKR_SESSION_READ_WRITE_SO_EXISTS = _LowLevel.CKR_SESSION_READ_WRITE_SO_EXISTS
CKR_SIGNATURE_INVALID = _LowLevel.CKR_SIGNATURE_INVALID
CKR_SIGNATURE_LEN_RANGE = _LowLevel.CKR_SIGNATURE_LEN_RANGE
CKR_TEMPLATE_INCOMPLETE = _LowLevel.CKR_TEMPLATE_INCOMPLETE
CKR_TEMPLATE_INCONSISTENT = _LowLevel.CKR_TEMPLATE_INCONSISTENT
CKR_TOKEN_NOT_PRESENT = _LowLevel.CKR_TOKEN_NOT_PRESENT
CKR_TOKEN_NOT_RECOGNIZED = _LowLevel.CKR_TOKEN_NOT_RECOGNIZED
CKR_TOKEN_WRITE_PROTECTED = _LowLevel.CKR_TOKEN_WRITE_PROTECTED
CKR_UNWRAPPING_KEY_HANDLE_INVALID = _LowLevel.CKR_UNWRAPPING_KEY_HANDLE_INVALID
CKR_UNWRAPPING_KEY_SIZE_RANGE = _LowLevel.CKR_UNWRAPPING_KEY_SIZE_RANGE
CKR_UNWRAPPING_KEY_TYPE_INCONSISTENT = _LowLevel.CKR_UNWRAPPING_KEY_TYPE_INCONSISTENT
CKR_USER_ALREADY_LOGGED_IN = _LowLevel.CKR_USER_ALREADY_LOGGED_IN
CKR_USER_NOT_LOGGED_IN = _LowLevel.CKR_USER_NOT_LOGGED_IN
CKR_USER_PIN_NOT_INITIALIZED = _LowLevel.CKR_USER_PIN_NOT_INITIALIZED
CKR_USER_TYPE_INVALID = _LowLevel.CKR_USER_TYPE_INVALID
CKR_USER_ANOTHER_ALREADY_LOGGED_IN = _LowLevel.CKR_USER_ANOTHER_ALREADY_LOGGED_IN
CKR_USER_TOO_MANY_TYPES = _LowLevel.CKR_USER_TOO_MANY_TYPES
CKR_WRAPPED_KEY_INVALID = _LowLevel.CKR_WRAPPED_KEY_INVALID
CKR_WRAPPED_KEY_LEN_RANGE = _LowLevel.CKR_WRAPPED_KEY_LEN_RANGE
CKR_WRAPPING_KEY_HANDLE_INVALID = _LowLevel.CKR_WRAPPING_KEY_HANDLE_INVALID
CKR_WRAPPING_KEY_SIZE_RANGE = _LowLevel.CKR_WRAPPING_KEY_SIZE_RANGE
CKR_WRAPPING_KEY_TYPE_INCONSISTENT = _LowLevel.CKR_WRAPPING_KEY_TYPE_INCONSISTENT
CKR_RANDOM_SEED_NOT_SUPPORTED = _LowLevel.CKR_RANDOM_SEED_NOT_SUPPORTED
CKR_RANDOM_NO_RNG = _LowLevel.CKR_RANDOM_NO_RNG
CKR_DOMAIN_PARAMS_INVALID = _LowLevel.CKR_DOMAIN_PARAMS_INVALID
CKR_BUFFER_TOO_SMALL = _LowLevel.CKR_BUFFER_TOO_SMALL
CKR_SAVED_STATE_INVALID = _LowLevel.CKR_SAVED_STATE_INVALID
CKR_INFORMATION_SENSITIVE = _LowLevel.CKR_INFORMATION_SENSITIVE
CKR_STATE_UNSAVEABLE = _LowLevel.CKR_STATE_UNSAVEABLE
CKR_CRYPTOKI_NOT_INITIALIZED = _LowLevel.CKR_CRYPTOKI_NOT_INITIALIZED
CKR_CRYPTOKI_ALREADY_INITIALIZED = _LowLevel.CKR_CRYPTOKI_ALREADY_INITIALIZED
CKR_MUTEX_BAD = _LowLevel.CKR_MUTEX_BAD
CKR_MUTEX_NOT_LOCKED = _LowLevel.CKR_MUTEX_NOT_LOCKED
CKR_VENDOR_DEFINED = _LowLevel.CKR_VENDOR_DEFINED
CKF_LIBRARY_CANT_CREATE_OS_THREADS = _LowLevel.CKF_LIBRARY_CANT_CREATE_OS_THREADS
CKF_OS_LOCKING_OK = _LowLevel.CKF_OS_LOCKING_OK
CKF_DONT_BLOCK = _LowLevel.CKF_DONT_BLOCK
CKG_MGF1_SHA1 = _LowLevel.CKG_MGF1_SHA1
CKZ_DATA_SPECIFIED = _LowLevel.CKZ_DATA_SPECIFIED
CKD_NULL = _LowLevel.CKD_NULL
CKD_SHA1_KDF = _LowLevel.CKD_SHA1_KDF
CKD_SHA1_KDF_ASN1 = _LowLevel.CKD_SHA1_KDF_ASN1
CKD_SHA1_KDF_CONCATENATE = _LowLevel.CKD_SHA1_KDF_CONCATENATE
CKP_PKCS5_PBKD2_HMAC_SHA1 = _LowLevel.CKP_PKCS5_PBKD2_HMAC_SHA1
CKZ_SALT_SPECIFIED = _LowLevel.CKZ_SALT_SPECIFIED
class CPKCS11Lib(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CPKCS11Lib, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CPKCS11Lib, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LowLevel.new_CPKCS11Lib(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CPKCS11Lib
    __del__ = lambda self : None;
    def Load(*args): return _LowLevel.CPKCS11Lib_Load(*args)
    def Unload(*args): return _LowLevel.CPKCS11Lib_Unload(*args)
    def C_Initialize(*args): return _LowLevel.CPKCS11Lib_C_Initialize(*args)
    def C_Finalize(*args): return _LowLevel.CPKCS11Lib_C_Finalize(*args)
    def C_GetInfo(*args): return _LowLevel.CPKCS11Lib_C_GetInfo(*args)
    def C_GetSlotList(*args): return _LowLevel.CPKCS11Lib_C_GetSlotList(*args)
    def C_GetSlotInfo(*args): return _LowLevel.CPKCS11Lib_C_GetSlotInfo(*args)
    def C_GetTokenInfo(*args): return _LowLevel.CPKCS11Lib_C_GetTokenInfo(*args)
    def C_InitToken(*args): return _LowLevel.CPKCS11Lib_C_InitToken(*args)
    def C_InitPIN(*args): return _LowLevel.CPKCS11Lib_C_InitPIN(*args)
    def C_SetPIN(*args): return _LowLevel.CPKCS11Lib_C_SetPIN(*args)
    def C_OpenSession(*args): return _LowLevel.CPKCS11Lib_C_OpenSession(*args)
    def C_CloseSession(*args): return _LowLevel.CPKCS11Lib_C_CloseSession(*args)
    def C_CloseAllSessions(*args): return _LowLevel.CPKCS11Lib_C_CloseAllSessions(*args)
    def C_GetSessionInfo(*args): return _LowLevel.CPKCS11Lib_C_GetSessionInfo(*args)
    def C_Login(*args): return _LowLevel.CPKCS11Lib_C_Login(*args)
    def C_Logout(*args): return _LowLevel.CPKCS11Lib_C_Logout(*args)
    def C_CreateObject(*args): return _LowLevel.CPKCS11Lib_C_CreateObject(*args)
    def C_DestroyObject(*args): return _LowLevel.CPKCS11Lib_C_DestroyObject(*args)
    def C_GetObjectSize(*args): return _LowLevel.CPKCS11Lib_C_GetObjectSize(*args)
    def C_GetAttributeValue(*args): return _LowLevel.CPKCS11Lib_C_GetAttributeValue(*args)
    def C_SetAttributeValue(*args): return _LowLevel.CPKCS11Lib_C_SetAttributeValue(*args)
    def C_FindObjectsInit(*args): return _LowLevel.CPKCS11Lib_C_FindObjectsInit(*args)
    def C_FindObjects(*args): return _LowLevel.CPKCS11Lib_C_FindObjects(*args)
    def C_FindObjectsFinal(*args): return _LowLevel.CPKCS11Lib_C_FindObjectsFinal(*args)
    def C_EncryptInit(*args): return _LowLevel.CPKCS11Lib_C_EncryptInit(*args)
    def C_Encrypt(*args): return _LowLevel.CPKCS11Lib_C_Encrypt(*args)
    def C_EncryptUpdate(*args): return _LowLevel.CPKCS11Lib_C_EncryptUpdate(*args)
    def C_EncryptFinal(*args): return _LowLevel.CPKCS11Lib_C_EncryptFinal(*args)
    def C_DecryptInit(*args): return _LowLevel.CPKCS11Lib_C_DecryptInit(*args)
    def C_Decrypt(*args): return _LowLevel.CPKCS11Lib_C_Decrypt(*args)
    def C_DecryptUpdate(*args): return _LowLevel.CPKCS11Lib_C_DecryptUpdate(*args)
    def C_DecryptFinal(*args): return _LowLevel.CPKCS11Lib_C_DecryptFinal(*args)
    def C_DigestInit(*args): return _LowLevel.CPKCS11Lib_C_DigestInit(*args)
    def C_Digest(*args): return _LowLevel.CPKCS11Lib_C_Digest(*args)
    def C_DigestUpdate(*args): return _LowLevel.CPKCS11Lib_C_DigestUpdate(*args)
    def C_DigestKey(*args): return _LowLevel.CPKCS11Lib_C_DigestKey(*args)
    def C_DigestFinal(*args): return _LowLevel.CPKCS11Lib_C_DigestFinal(*args)
    def C_SignInit(*args): return _LowLevel.CPKCS11Lib_C_SignInit(*args)
    def C_Sign(*args): return _LowLevel.CPKCS11Lib_C_Sign(*args)
    def C_SignUpdate(*args): return _LowLevel.CPKCS11Lib_C_SignUpdate(*args)
    def C_SignFinal(*args): return _LowLevel.CPKCS11Lib_C_SignFinal(*args)
    def C_VerifyInit(*args): return _LowLevel.CPKCS11Lib_C_VerifyInit(*args)
    def C_Verify(*args): return _LowLevel.CPKCS11Lib_C_Verify(*args)
    def C_VerifyUpdate(*args): return _LowLevel.CPKCS11Lib_C_VerifyUpdate(*args)
    def C_VerifyFinal(*args): return _LowLevel.CPKCS11Lib_C_VerifyFinal(*args)
    def C_GenerateKey(*args): return _LowLevel.CPKCS11Lib_C_GenerateKey(*args)
    def C_GenerateKeyPair(*args): return _LowLevel.CPKCS11Lib_C_GenerateKeyPair(*args)
    def C_WrapKey(*args): return _LowLevel.CPKCS11Lib_C_WrapKey(*args)
    def C_UnwrapKey(*args): return _LowLevel.CPKCS11Lib_C_UnwrapKey(*args)
    def C_SeedRandom(*args): return _LowLevel.CPKCS11Lib_C_SeedRandom(*args)
    def C_GenerateRandom(*args): return _LowLevel.CPKCS11Lib_C_GenerateRandom(*args)
    def C_WaitForSlotEvent(*args): return _LowLevel.CPKCS11Lib_C_WaitForSlotEvent(*args)
CPKCS11Lib_swigregister = _LowLevel.CPKCS11Lib_swigregister
CPKCS11Lib_swigregister(CPKCS11Lib)

class CK_ATTRIBUTE_SMART(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CK_ATTRIBUTE_SMART, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CK_ATTRIBUTE_SMART, name)
    __repr__ = _swig_repr
    def Reset(*args): return _LowLevel.CK_ATTRIBUTE_SMART_Reset(*args)
    def ResetValue(*args): return _LowLevel.CK_ATTRIBUTE_SMART_ResetValue(*args)
    def Reserve(*args): return _LowLevel.CK_ATTRIBUTE_SMART_Reserve(*args)
    def GetType(*args): return _LowLevel.CK_ATTRIBUTE_SMART_GetType(*args)
    def SetType(*args): return _LowLevel.CK_ATTRIBUTE_SMART_SetType(*args)
    def GetLen(*args): return _LowLevel.CK_ATTRIBUTE_SMART_GetLen(*args)
    def IsString(*args): return _LowLevel.CK_ATTRIBUTE_SMART_IsString(*args)
    def IsBool(*args): return _LowLevel.CK_ATTRIBUTE_SMART_IsBool(*args)
    def IsNum(*args): return _LowLevel.CK_ATTRIBUTE_SMART_IsNum(*args)
    def IsBin(*args): return _LowLevel.CK_ATTRIBUTE_SMART_IsBin(*args)
    def GetString(*args): return _LowLevel.CK_ATTRIBUTE_SMART_GetString(*args)
    def SetString(*args): return _LowLevel.CK_ATTRIBUTE_SMART_SetString(*args)
    def GetNum(*args): return _LowLevel.CK_ATTRIBUTE_SMART_GetNum(*args)
    def SetNum(*args): return _LowLevel.CK_ATTRIBUTE_SMART_SetNum(*args)
    def GetBool(*args): return _LowLevel.CK_ATTRIBUTE_SMART_GetBool(*args)
    def SetBool(*args): return _LowLevel.CK_ATTRIBUTE_SMART_SetBool(*args)
    def GetBin(*args): return _LowLevel.CK_ATTRIBUTE_SMART_GetBin(*args)
    def SetBin(*args): return _LowLevel.CK_ATTRIBUTE_SMART_SetBin(*args)
    def __init__(self, *args): 
        this = _LowLevel.new_CK_ATTRIBUTE_SMART(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LowLevel.delete_CK_ATTRIBUTE_SMART
    __del__ = lambda self : None;
CK_ATTRIBUTE_SMART_swigregister = _LowLevel.CK_ATTRIBUTE_SMART_swigregister
CK_ATTRIBUTE_SMART_swigregister(CK_ATTRIBUTE_SMART)



