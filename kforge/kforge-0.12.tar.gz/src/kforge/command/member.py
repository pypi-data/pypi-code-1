from dm.command import *
from dm.command.person import PersonRead
from kforge.command.project import ProjectRead

class MemberCommand(Command):
    "Abstract member command."
        
    def __init__(self, projectName, personName):
        super(MemberCommand, self).__init__(
            projectName=projectName, personName=personName
        )
        self.projectName = projectName
        self.personName = personName
        self.project = None
        self.person = None
        self.member = None
        self.projects = self.registry.projects
        self.persons = self.registry.persons

    def loadProject(self):
        command = ProjectRead(self.projectName)
        command.execute()
        self.project = command.project
            
    def loadPerson(self):
        command = PersonRead(self.personName)
        command.execute()
        self.person = command.person
           
    def isMember(self):
        return self.person in self.project.members
           
    def isDeletedMember(self):
        return self.person in self.project.members.deleted
           
class MemberList(MemberCommand):
    "List members of project."

    def __init__(self, projectName):
        super(MemberList, self).__init__(projectName, '')

    def execute(self):
        "Make it so."
        super(MemberList, self).execute()
        self.loadProject()
        self.results = self.project.members


class MemberCreate(DomainObjectCreate):
    "Command to create a new member."

    def __init__(self, **kwds):
        super(MemberCreate, self).__init__(
            typeName='Member', objectKwds=kwds
        )
        self.member = None

    def execute(self):
        super(MemberCreate, self).execute()
        self.member = self.object


#class MemberCreate(MemberCommand):
#    "Command to create a new member."
#        
#    def __init__(self, projectName, personName, roleName=None):
#        super(MemberCreate, self).__init__(projectName, personName)
#        self.roleName = roleName
#
#    def execute(self):
#        "Make it so."
#        super(MemberCreate, self).execute()
#        self.loadProject()
#        self.loadPerson()
#        if self.isMember():
#            message = "'%s' is already a member of project '%s'." % (
#                self.personName, self.projectName)
#            self.raiseError(message)
#        if self.isDeletedMember():
#            self.member = self.project.members.deleted[self.person]
#            self.member.undelete()
#            self.member.save()
#        else:
#            self.member = self.project.members.create(self.person)
#            if self.roleName:
#                role = self.registry.roles[self.roleName]
#                self.member.role = role
#                self.member.save()
#        self.commitSuccess()
        
class MemberRead(MemberCommand):
    "Command to read a registered member."

    def __init__(self, projectName, personName):
        super(MemberRead, self).__init__(projectName, personName)

    def loadMember(self):
        self.loadProject()
        self.loadPerson()
        if not self.isMember():
            message = "Person '%s' isn't member of project '%s'." % (
                self.personName, self.projectName)
            self.raiseError(message)
        self.member = self.project.members[self.person]
            
    def execute(self):
        "Make it so."
        super(MemberRead, self).execute()
        self.loadMember()

class MemberDelete(MemberRead):
    "Command to delete a registered member."

    def __init__(self, projectName, personName):
        super(MemberDelete, self).__init__(projectName, personName)

    def execute(self):
        "Make it so."
        super(MemberDelete, self).execute()
        self.member.delete()

