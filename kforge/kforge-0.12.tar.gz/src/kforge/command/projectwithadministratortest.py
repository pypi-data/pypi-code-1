import unittest
from kforge.testunit import TestCase
from kforge.command import *
from kforge.exceptions import *

def suite():
    suites = [
        unittest.makeSuite(TestProjectWithAdministratorCreate),
    ]
    return unittest.TestSuite(suites)

class TestProjectWithAdministratorCreate(TestCase):
    "TestCase for the ProjectWithAdministratorCreate command."

    projectName = 'TestProjectCreate'
    personName = 'TestProjectCreate'

    def setUp(self):
        super(TestProjectWithAdministratorCreate, self).setUp()
        self.registry.persons.create(self.personName)
        self.command = kforge.command.ProjectWithAdministratorCreate(
            self.projectName,
            self.personName
        )

    def tearDown(self):
        if self.projectName in self.registry.projects.all:
            project = self.registry.projects[self.projectName]
            project.delete()
            project.purge()
        if self.personName in self.registry.persons.all:
            person = self.registry.persons[self.personName]
            person.delete()
            person.purge()

    def testExecute(self):
        self.failUnless(self.personName in self.registry.persons)
        self.failIf(self.projectName in self.registry.projects)
        self.command.execute()
        self.failUnless(self.projectName in self.registry.projects)

    def testErrorProjectExists(self):
        self.command.execute()
        self.failUnlessRaises(KforgeCommandError, self.command.execute)

