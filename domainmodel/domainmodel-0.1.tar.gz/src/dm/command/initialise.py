from dm.command import Command
from dm.command.state import *
from dm.command.accesscontrol import GrantStandardSystemAccess, GrantStandardProjectAccess
from dm.command.person import *

class InitialiseDomainModel(Command):
    """
    Creates default domain model objects.
    """
    
    def __init__(self):
        super(self.__class__, self).__init__()
    
    def execute(self):
        super(self.__class__, self).execute()
        self.createSystem()
        self.createStates()
        self.createRoles()
        self.createActions()
        self.createProtectionObjects()
        self.createGrants()
        self.createRefusals()
        self.createPersons()
        if self.dictionary['system_mode'] == 'development':
            self.createTestPlugins()
            self.setUpTestFixtures()
        # create plugins last so that apacheconfig is only created at the end
        self.createPlugins()
        self.commitSuccess()
    
    def createSystem(self):
        self.registry.systems.create()
        
    def createStates(self):
        self.registry.states.create('active')
        self.registry.states.create('deleted')
        
    def createRoles(self):
        roles = self.registry.roles
        self.adminRole     = roles.create('Administrator')
        self.developerRole = roles.create('Developer')
        self.friendRole    = roles.create('Friend')
        self.visitorRole   = roles.create('Visitor')
        
    def createActions(self):
        self.registry.actions.create('Create')
        self.registry.actions.create('Read')
        self.registry.actions.create('Update')
        self.registry.actions.create('Delete')
        self.registry.actions.create('Purge')
        
    def createProtectionObjects(self):
        self.registry.protectionObjects.create('Session')
        self.registry.protectionObjects.create('System')
        self.registry.protectionObjects.create('Person')
        self.registry.protectionObjects.create('Plugin')

    def createGrants(self):
        self.grantAdministratorAccess()
        self.grantRegistrationAccess()
        self.grantStandardSystemAccess('System')
        self.grantStandardSystemAccess('Person')

    def grantAdministratorAccess(self):
        for protectionObject in self.registry.protectionObjects:
            for permission in protectionObject.permissions:
                if not permission in self.adminRole.grants:
                    self.adminRole.grants.create(permission)

    def grantRegistrationAccess(self):
        create = self.registry.actions['Create']
        protectionObjects = self.registry.protectionObjects
        for role in self.registry.roles:
            personProtection = protectionObjects['Person']
            createPerson = personProtection.permissions[create]
            if not createPerson in role.grants:
                role.grants.create(createPerson)
            projectProtection = protectionObjects['Project']
            createProject = projectProtection.permissions[create]
            if not createProject in role.grants:
                role.grants.create(createProject)

    def grantStandardSystemAccess(self, protectedName):
        protectionObject = self.registry.protectionObjects[protectedName]
        cmd = GrantStandardSystemAccess(protectionObject)
        cmd.execute()

    def createRefusals(self):
        pass

    def createLicenses(self):
        licenses = self.registry.licenses
        licenses.create(name='Other/Proprietary License')
        licenses.create(name='General Public License (GPL)')
        licenses.create(name='BSD')
        licenses.create(name='Creative Commons (Attribution, Share Alike)')
        licenses.create(name='Creative Commons (Attribution, Derivatives)')

    def createPersons(self):
        cmd = PersonCreate('admin', 
            role=self.adminRole,
            fullname='Administrator'
        )
        cmd.execute()
        self.adminPerson = cmd.person
        self.adminPerson.setPassword('pass')
        self.adminPerson.save()
        
        visitorRoleName = self.dictionary['visitor_role']
        visitorRole = self.registry.roles[visitorRoleName]
        cmd = PersonCreate(self.dictionary['visitor'],
            role = visitorRole,
            fullname='Visitor',
        )
        cmd.execute()
        self.visitorPerson = cmd.person
        projectProtection = self.registry.protectionObjects['Project']
        create = self.registry.actions['Create']
        createProject = projectProtection.permissions[create]
        if not createProject in self.visitorPerson.bars:
                self.visitorPerson.bars.create(createProject)
        
    def createProjects(self):
        cmd = ProjectCreate('administration')
        cmd.execute()
        self.adminProject = cmd.project
        self.adminProject.title = 'Administration'
        self.adminProject.save()
        self.adminProject.members.create(
            self.adminPerson, role=self.adminRole
        )
        self.adminProject.members.create(
            self.visitorPerson, role=self.visitorRole
        )
    
    def createPlugins(self):
        plugins = self.registry.plugins
        plugins.create('accesscontrol')
        plugins.create('apacheconfig')
        plugins.create('svn')
        plugins.create('trac')
    
    def createTestPlugins(self):
        plugins = self.registry.plugins
        plugins.create('example')
        plugins.create('example_single_service')
    
    def setUpTestFixtures(self):
        personRoleName = self.dictionary['person_role']
        personRole = self.registry.roles[personRoleName]
        # do not reuse roles set in other methods as this method
        # should be callable on its own
        adminPerson = self.registry.persons['admin']
        adminRole = self.registry.roles['Administrator']
        friendRole = self.registry.roles['Friend']
        cmd = PersonCreate('levin',
            role = personRole,
            fullname='Levin',
        )
        cmd.execute()
        levin = cmd.person
        levin.setPassword('levin')
        levin.save()
        
        cmd = PersonCreate('natasha',
            role = personRole,
            fullname='Natasha',
        )
        cmd.execute()
        natasha = cmd.person
        natasha.setPassword('natasha')
        natasha.save()
        visitor = self.registry.persons[self.dictionary['visitor']]
        
        
        cmd = ProjectCreate('example')
        cmd.execute()
        exampleProject = cmd.project
        
        cmd = ProjectCreate('warandpeace')
        cmd.execute()
        warAndPeace = cmd.project
        warAndPeace.title = 'War and Peace'
        warAndPeace.save()
        cmd2 = ProjectCreate('annakarenina')
        cmd2.execute()
        annaKarenina = cmd2.project
        annaKarenina.title = 'Anna Karenina'
        annaKarenina.save()
        
        exampleProject.members.create(adminPerson,  role=adminRole)
        warAndPeace.members.create(  natasha,    role=adminRole)
        warAndPeace.members.create(  visitor,    role=friendRole)
        annaKarenina.members.create( levin,      role=adminRole)
        
        examplePlugin = self.registry.plugins['example']
        exampleSingleService = self.registry.plugins['example_single_service']
        for project in [warAndPeace, annaKarenina, exampleProject]:
            project.services.create('example', plugin=examplePlugin)
            project.services.create('example_single_service', plugin=exampleSingleService)
    
    def tearDownTestFixtures(self):
        # [[TODO: factor this out into a command class]]
        def purgeProject(projectName):
            if self.registry.projects.has_key(projectName):
                self.registry.projects[projectName].delete()
            if self.registry.projects.all.has_key(projectName):
                self.registry.projects.all[projectName].purge()
        purgeProject('warandpeace')
        purgeProject('annakarenina')
        
        def purgePerson(personName):
            if self.registry.persons.has_key(personName):
                self.registry.persons[personName].delete()
            if self.registry.persons.all.has_key(personName):
                self.registry.persons.all[personName].purge()
        purgePerson('natasha')
        purgePerson('levin')
        purgePerson('anna')
        purgePerson('bolskonski')

