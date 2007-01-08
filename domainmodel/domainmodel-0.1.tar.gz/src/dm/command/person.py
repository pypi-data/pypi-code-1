from dm.command import *
import dm.re
import re
from dm.exceptions import *

class PersonCommand(Command):
    "Abstract person command."
        
    def __init__(self, name):
        super(PersonCommand, self).__init__(name=name)
        self.name = name
        self.person = None
        self.persons = self.registry.persons


class PersonCreate(DomainObjectCreate):
    "Command to create a new person."

    reservedNames = re.compile('^%s$' % dm.re.reservedPersonName)

    def __init__(self, name='', **kwds):
        super(PersonCreate, self).__init__(
            typeName='Person', objectId=name, objectKwds=kwds
        )
        self.person = None

    def execute(self):
        super(PersonCreate, self).execute()
        self.person = self.object


#class PersonCreate(PersonCommand):
#    "Command to create a new person."
#
#    reservedNames = re.compile('^%s$' % dm.re.reservedPersonName)
#
#    def __init__(self, name):
#        super(PersonCreate, self).__init__(name)
#
#    def execute(self):
#        "Make it so."
#        super(PersonCreate, self).execute()
#        if self.reservedNames.match(self.name):
#            message = "Name '%s' is reserved." % self.name
#            self.raiseError(message)
#        if self.name in self.persons.all:
#            message = "A person already exists with name '%s'." % self.name
#            self.raiseError(message)
#        self.person = self.persons.create(self.name)
#        self.commitSuccess()


class PersonDelete(PersonCommand):
    "Command to delete a registered person."

    def __init__(self, name):
        super(PersonDelete, self).__init__(name)

    def execute(self):
        "Make it so."
        super(PersonDelete, self).execute()
        if not self.name in self.persons:
            message = "No person found with name '%s'." % self.name
            self.raiseError(message)
        self.person = self.persons[self.name]
        self.person.delete()
        self.commitSuccess()


class PersonUndelete(PersonCommand):
    "Command to undelete a deleted registered person."

    def __init__(self, name):
        super(PersonUndelete, self).__init__(name)

    def execute(self):
        "Make it so."
        super(PersonUndelete, self).execute()
        if not self.name in self.persons.deleted:
            message = "No deleted person found with name '%s'." % self.name
            self.raiseError(message)
        person = self.persons.deleted[self.name]
        person.undelete()
        self.commitSuccess()


class PersonPurge(PersonCommand):
    "Command to purge a deleted registered person."

    def __init__(self, name):
        super(PersonPurge, self).__init__(name)

    def execute(self):
        "Make it so."
        super(PersonPurge, self).execute()
        if not self.name in self.persons.deleted:
            message = "No deleted person found with name '%s'." % self.name
            self.raiseError(message)
        person = self.persons.deleted[self.name]
        person.purge()
        self.commitSuccess()


class PersonRead(PersonCommand):
    "Command to read a registered person."

    def __init__(self, name):
        super(PersonRead, self).__init__(name)

    def execute(self):
        "Make it so."
        super(PersonRead, self).execute()
        try:
            person = self.persons[self.name]
            self.person = person
        except KforgeRegistryKeyError, inst:
            #message = "No person found with name '%s'." % self.name
            message = str(inst)
            self.raiseError(message)


class PersonAuthenticate(PersonCommand):
    "Command to authenticate a registered person."

    def __init__(self, name, password):
        super(PersonAuthenticate, self).__init__(name)
        self.password = password

    def execute(self):
        "Make it so."
        super(PersonAuthenticate, self).execute()
        reader = PersonRead(self.name)
        reader.execute()
        if not reader.person.isPassword(self.password):
            message = "No authorisation for name/password."
            self.raiseError(message)
        self.person = reader.person


class AllPersonRead(PersonRead):
    "Command to read any person, regardless of state."

    def __init__(self, name):
        super(AllPersonRead, self).__init__(name)
        self.persons = self.persons.all


class PersonList(PersonCommand):
    "Command to list registered persons."

    def __init__(self, userQuery='', startsWith='', startsWithAttributeName=''):
        super(PersonList, self).__init__('')
        self.userQuery = userQuery
        self.startsWith = startsWith
        self.startsWithAttributeName = startsWithAttributeName

    def execute(self):
        "Make it so."
        super(PersonList, self).execute()
        if self.startsWith:
            selection = self.persons.startsWith(
                value=self.startsWith,
                attributeName=self.startsWithAttributeName
            )
            self.results = [p for p in selection]
        elif self.userQuery:
            selection = self.persons.search(
                userQuery=self.userQuery
            )
            self.results = [p for p in selection]
        else:
            self.results = [p for p in self.persons]

