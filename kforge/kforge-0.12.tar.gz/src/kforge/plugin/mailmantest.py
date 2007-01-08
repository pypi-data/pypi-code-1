import unittest
from kforge.testunit import TestCase
import tempfile

import kforge.plugin.mailman

def suite():
    suites = [
            unittest.makeSuite(PluginTest),
        ]
    return unittest.TestSuite(suites)

# todo: extract abstract MailingListPlugin and MailingListUtils classes

class PluginTest(TestCase):
    """
    TestCase for the Mailman plugin.
    """
    
    def setUp(self):
        super(PluginTest, self).setUp()
        if not self.registry.plugins.has_key('mailman'):
            self.registry.plugins.create('mailman')
        self.plugin = self.registry.plugins['mailman']
        self.project = self.registry.projects['annakarenina']
        if 'mailman' in self.project.services:
            service = self.project.services['mailman']
            service.delete()
            service.purge()
        self.project.services.create('mailman', plugin=self.plugin)
        self.service = self.project.services['mailman']
        self.pathBuilder = kforge.filesystem.FileSystemPathBuilder()
    
    def tearDown(self):
        # do all of them to deal with errors elsewhere
        self.service.delete()
        self.service.purge()
    
    def testGetApacheConfig(self):
        self.plugin.getSystem().getApacheConfig(self.service)
    
    def testCreateAndDeleteMailingList(self):
        self.utils = self.plugin.getSystem()
        self.listName = 'annakarenina-dev'
        self.adminEmail = 'admin@someone.net'  # todo: fix addr
        self.adminPass = 'pass'
        self.utils.createMailingList(
            listName=self.listName,
            adminEmail=self.adminEmail,
            adminPass=self.adminPass
        )
        self.utils.deleteMailingList(
            listName=self.listName
        )

