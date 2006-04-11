from salamoia.h2o.object import Object
from salamoia.nacl.backend import Backend
from salamoia.h2o.exception import *
from salamoia.h2o.logioni import Ione
import salamoia.h2o.acl
from salamoia.h2o.attribute import *
import timing

class NACLObject(Object):
    hookMap = {}
    creationHooks = []
    modificationHooks = []
    
    def fetchOwner(self):
        if not hasattr(self, '_service'):
            return None
        c = self._service
        try:
            # if the object's container is a singleton don't fetch 
            # TODO: make singleton behave like normal objects ... but singleton
            if self.schema.containerClass.schema.absoluteDN():
                return None
            res =  c.fetch(self.ownerId())
            return res
        except FetchError:
            Ione.error("FEEEEEEEEETCH EEEEEEEEEEEEEEEEEERRROR")
            pass
        except:
            Ione.error("fetchOwner EXCEPTION")
        

    def ownerId(self):
        raise NotImplementedError, "to be overriden"

    def setIdHook(self):
        self.owner = self.fetchOwner()
        if self.owner:
            for i in self.owner.acl:
                self.acl.append(i) # TODO: maybe a copy is better?

    def typeSpec(self):
        raise NotImplementedError, "to be overriden"

    def __getstate__(self):
        Ione.log("GETTING STATE for pickle")
        return self.__dict__

    def __getattr__(self, name):
        #timing.start()
        #Ione.log("CALLING NACL GETATTR in", self.__class__, name)
        if name == '_attributes':
            state = self.__dict__
            attrs = {}
            for name in [x for x in state if x[0] != '_']:
                attrs[name] = Attribute(name, state[name], self.mapAttributeType(name))
            state['_attributes'] = attrs 
            #timing.finish()
            #Ione.log("GETATTR took msec:", timing.milli())
            return attrs
        # perche non c'era questa prima?
        try:
            return self.__dict__[name]
        except:
            raise AttributeError, name


# -- run the doc tests in this document if invoked as a script
from salamoia.tests import *; runDocTests()
# --
