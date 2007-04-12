# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _graphviz
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


agopen = _graphviz.agopen
def agraphnew(name,strict=False,directed=False):
    if strict:
       if directed:
            return _graphviz.agopen(name,cvar.Agstrictdirected,None)
       else:
            return _graphviz.agopen(name,cvar.Agstrictundirected,None)
    else:
        if directed:
            return _graphviz.agopen(name,cvar.Agdirected,None)
        else:		 
            return _graphviz.agopen(name,cvar.Agundirected,None)

agclose = _graphviz.agclose
agread = _graphviz.agread
agwrite = _graphviz.agwrite
agisundirected = _graphviz.agisundirected
agisdirected = _graphviz.agisdirected
agisstrict = _graphviz.agisstrict
agsubg = _graphviz.agsubg
agfstsubg = _graphviz.agfstsubg
agnxtsubg = _graphviz.agnxtsubg
agparent = _graphviz.agparent
agroot = _graphviz.agroot
agsubnode = _graphviz.agsubnode
agsubedge = _graphviz.agsubedge
agdelsubg = _graphviz.agdelsubg
agnode = _graphviz.agnode
agfstnode = _graphviz.agfstnode
agnxtnode = _graphviz.agnxtnode
agdelnode = _graphviz.agdelnode
agedge = _graphviz.agedge
aghead = _graphviz.aghead
agtail = _graphviz.agtail
agfstedge = _graphviz.agfstedge
agnxtedge = _graphviz.agnxtedge
agfstin = _graphviz.agfstin
agnxtin = _graphviz.agnxtin
agfstout = _graphviz.agfstout
agnxtout = _graphviz.agnxtout
agdeledge = _graphviz.agdeledge
agattr = _graphviz.agattr
agattrsym = _graphviz.agattrsym
agnxtattr = _graphviz.agnxtattr
agget = _graphviz.agget
agxget = _graphviz.agxget
agset = _graphviz.agset
agxset = _graphviz.agxset
agattrname = _graphviz.agattrname
agattrdefval = _graphviz.agattrdefval
agnnodes = _graphviz.agnnodes
agnedges = _graphviz.agnedges
agdegree = _graphviz.agdegree
agraphof = _graphviz.agraphof
agnameof = _graphviz.agnameof
def agnameof(handle):
  name=_graphviz.agnameof(handle)
  if name=='' or name.startswith('%'):
    return None
  else:
    return name 

AGRAPH = _graphviz.AGRAPH
AGNODE = _graphviz.AGNODE
AGOUTEDGE = _graphviz.AGOUTEDGE
AGINEDGE = _graphviz.AGINEDGE
AGEDGE = _graphviz.AGEDGE

cvar = _graphviz.cvar
Agdirected = cvar.Agdirected
Agstrictdirected = cvar.Agstrictdirected
Agundirected = cvar.Agundirected
Agstrictundirected = cvar.Agstrictundirected

