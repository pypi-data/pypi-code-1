"""
  >>> import grok
  >>> grok.grok('grok.ftests.xmlrpc.xmlrpc')
  >>> from grok.ftests.xmlrpc.xmlrpc import Mammoth
  >>> getRootFolder()["Manfred"] = Mammoth()

  >>> from grok.ftests.xmlrpc_helper import ServerProxy

  >>> server = ServerProxy("http://localhost/")
  >>> server.Manfred.stomp()
  'Manfred stomped.'
  >>> server.Manfred.dance()
  "Manfred doesn't like to dance."

"""
import grok


class Mammoth(grok.Model):
    pass


class MammothRPC(grok.XMLRPC):

    def stomp(self):
        return '%s stomped.' % self.context.__name__

    def dance(self):
        return '%s doesn\'t like to dance.' % self.context.__name__
