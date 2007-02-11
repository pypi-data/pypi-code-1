import unittest
import transaction

from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite
from plone.app.redirector.tests.base import RedirectorTestCase

from zope.component import getUtility
from plone.app.redirector.interfaces import IRedirectionStorage

class TestRedirectorEvents(RedirectorTestCase):
    """Ensure that the redirector event subscribers behave as expected.
    """
        
    @property
    def storage(self):
        return getUtility(IRedirectionStorage)
        
    def test_rename_updates_storage(self):
        self.folder.invokeFactory('Document', 'p1')
        transaction.savepoint(1)
        self.folder.manage_renameObject('p1', 'p2')
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/p1'), fp + '/p2')

    def test_cut_paste_updates_storage(self):
        self.folder.invokeFactory('Folder', 'f1')
        self.folder.invokeFactory('Document', 'p1')
        self.folder.invokeFactory('Document', 'p2')
        transaction.savepoint(1)
        cp = self.folder.manage_cutObjects(ids=('p1', 'p2',))
        self.folder.f1.manage_pasteObjects(cp)
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/p1'), fp + '/f1/p1')
        self.assertEquals(self.storage.get(fp + '/p2'), fp + '/f1/p2')
        
    def test_cut_paste_rename_updates_storage(self):
        self.folder.invokeFactory('Folder', 'f1')
        self.folder.invokeFactory('Document', 'p1')
        self.folder.invokeFactory('Document', 'p2')
        transaction.savepoint(1)
        cp = self.folder.manage_cutObjects(ids=('p1', 'p2',))
        self.folder.f1.manage_pasteObjects(cp)
        transaction.savepoint(1)
        self.folder.f1.manage_renameObject('p2', 'p3')
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/p1'), fp + '/f1/p1')
        self.assertEquals(self.storage.get(fp + '/p2'), fp + '/f1/p3')
        self.assertEquals(self.storage.get(fp + '/f1/p2'), fp + '/f1/p3')
        
    def test_delete_destroys_reference(self):
        self.folder.invokeFactory('Document', 'p1')
        transaction.savepoint(1)
        self.folder.manage_renameObject('p1', 'p2')
        transaction.savepoint(1)
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/p1'), fp + '/p2')
        
        self.folder._delObject('p2')
        
        self.assertEquals(self.storage.get(fp + '/p1'), None)
        
    def test_delete_destroys_child_reference(self):
        self.folder.invokeFactory('Folder', 'f1')
        self.folder.f1.invokeFactory('Document', 'p1')
        transaction.savepoint(1)
        self.folder.f1.manage_renameObject('p1', 'p2')
        transaction.savepoint(1)
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/f1/p1'), fp + '/f1/p2')
        
        self.folder._delObject('f1')
        
        self.assertEquals(self.storage.get(fp + '/f1/p1'), None)
        
    # XXX: These tests are disabled because OFS does not fire events for
    # children when a folder is renamed or moved. This means that our
    # redirection storage is not able to find sub-objects when they move.
    
    # We could get around this by recursing in subscribers.py, at a 
    # performance hit.
        
    def _DISABLED_test_rename_updates_parent_and_children(self):
        self.folder.invokeFactory('Folder', 'f1')
        self.folder.f1.invokeFactory('Document', 'p1')
        self.folder.f1.invokeFactory('Document', 'p2')
        transaction.savepoint(1)
        self.folder.manage_renameObject('f1', 'f2')
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/f1'), fp + '/f2')
        self.assertEquals(self.storage.get(fp + '/f1/p1'), fp + '/f2/p1')
        self.assertEquals(self.storage.get(fp + '/f1/p2'), fp + '/f2/p2')
        
    def _DISABLED_test_cut_paste_updates_parent_and_children(self):
        self.folder.invokeFactory('Folder', 'f1')
        self.folder.invokeFactory('Folder', 'f2')
        self.folder.f1.invokeFactory('Document', 'p1')
        self.folder.f1.invokeFactory('Document', 'p2')
        transaction.savepoint(1)
        cp = self.folder.manage_cutObjects(ids=('f1',))
        self.folder.f2.manage_pasteObjects(cp)
        
        fp = '/'.join(self.folder.getPhysicalPath())
        self.assertEquals(self.storage.get(fp + '/f1'), fp + '/f2/f1')
        self.assertEquals(self.storage.get(fp + '/f1/p1'), fp + '/f2/f1/p1')
        self.assertEquals(self.storage.get(fp + '/f1/p2'), fp + '/f2/f1/p2')

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRedirectorEvents))
    return suite
