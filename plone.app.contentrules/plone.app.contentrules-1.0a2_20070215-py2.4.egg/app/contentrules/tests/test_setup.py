from zope.lifecycleevent.interfaces import IObjectModifiedEvent
#from zope.app.container.interfaces import IObjectAddedEvent
from zope.app.container.interfaces import IObjectRemovedEvent
from Products.Archetypes.interfaces import IObjectInitializedEvent

from plone.contentrules.engine.interfaces import IRuleContainer
from plone.contentrules.rule.interfaces import IRuleEventType

from plone.app.contentrules.tests.base import ContentRulesTestCase

class TestProductInstall(ContentRulesTestCase):

    def testRuleContainerInterfaces(self): 
        self.failUnless(IRuleContainer.providedBy(self.folder))
        self.failUnless(IRuleContainer.providedBy(self.portal))
        
    def testEventTypesMarked(self): 
        self.failUnless(IRuleEventType.providedBy(IObjectInitializedEvent))
        self.failUnless(IRuleEventType.providedBy(IObjectModifiedEvent))
        # self.failUnless(IRuleEventType.providedBy(IObjectAddedEvent))
        self.failUnless(IRuleEventType.providedBy(IObjectRemovedEvent))
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    return suite
