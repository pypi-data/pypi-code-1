from zope.interface import implements, Interface
from zope.component import getUtility, getMultiAdapter

from plone.contentrules.engine.interfaces import IRuleStorage
from plone.contentrules.rule.interfaces import IRuleAction
from plone.contentrules.rule.interfaces import IExecutable

from plone.app.contentrules.actions.delete import DeleteAction

from plone.app.contentrules.rule import Rule

from plone.app.contentrules.tests.base import ContentRulesTestCase

from zope.component.interfaces import IObjectEvent

class DummyEvent(object):
    implements(IObjectEvent)
    
    def __init__(self, object):
        self.object = object

class TestDeleteAction(ContentRulesTestCase):

    def afterSetUp(self):
        self.setRoles(('Manager',))
        self.folder.invokeFactory('Document', 'd1')

    def testRegistered(self): 
        element = getUtility(IRuleAction, name='plone.actions.Delete')
        self.assertEquals('plone.actions.Delete', element.addview)
        self.assertEquals(None, element.editview)
        self.assertEquals(None, element.for_)
        self.assertEquals(IObjectEvent, element.event)
    
    def testInvokeAddView(self): 
        element = getUtility(IRuleAction, name='plone.actions.Delete')
        storage = IRuleStorage(self.folder)
        storage[u'foo'] = Rule()
        rule = self.folder.restrictedTraverse('++rule++foo')
        
        adding = rule.restrictedTraverse('+')
        addview = adding.restrictedTraverse(str(element.addview))
        
        addview()
        
        e = rule.elements[0].instance
        self.failUnless(isinstance(e, DeleteAction))
    
    def testExecute(self): 
        e = DeleteAction()
        
        ex = getMultiAdapter((self.folder, e, DummyEvent(self.folder.d1)), IExecutable)
        self.assertEquals(True, ex())
        
        self.failIf('d1' in self.folder.objectIds())
        
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestDeleteAction))
    return suite
