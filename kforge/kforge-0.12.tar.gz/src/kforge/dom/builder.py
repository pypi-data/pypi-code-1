import dm.dom.builder

class ModelBuilder(dm.dom.builder.ModelBuilder):

    def construct(self):
        super(ModelBuilder, self).construct()
        self.loadProject()
        self.loadLicense()
        self.loadService()
        self.loadMember()

    def loadPerson(self):  # override core model's Person
        from kforge.dom.person import Person
        self.registry.registerDomainClass(Person)
        self.registry.persons = Person.createRegister()

    def loadProject(self):
        from kforge.dom.project import Project 
        self.registry.registerDomainClass(Project)
        self.registry.projects = Project.createRegister()

    def loadLicense(self):
        from kforge.dom.license import License  
        self.registry.registerDomainClass(License)
        from kforge.dom.license import ProjectLicense  
        self.registry.registerDomainClass(ProjectLicense)
        self.registry.licenses = License.createRegister()
        self.registry.loadBackgroundRegister(self.registry.licenses)

    def loadService(self):
        from kforge.dom.service import Service
        self.registry.registerDomainClass(Service)
        self.registry.services = Service.createRegister()

    def loadMember(self):
        from kforge.dom.member import Member
        self.registry.registerDomainClass(Member)
        self.registry.members = Member.createRegister()

