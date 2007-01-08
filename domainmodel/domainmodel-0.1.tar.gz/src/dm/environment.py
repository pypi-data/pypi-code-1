import os
from dm.exceptions import *

class SystemEnvironment(object):
    "Boundary object encapsulating environment variables."

    DJANGO_SETTINGS_MODULE = 'DJANGO_SETTINGS_MODULE'

    def __init__(self, systemName):
        self.systemName = systemName
        if self.systemName == 'domainmodel':
            self.systemPyName = 'dm'
        else:
            self.systemPyName = self.systemName

    def assertDjangoSettingsModule(self):
        "Raises exception if DJANGO_SETTINGS_MODULE not set in environment."
        if self.DJANGO_SETTINGS_MODULE in os.environ:
            djangoSettingsModuleName = os.environ[self.DJANGO_SETTINGS_MODULE]
        else:
            raise "Environment variable '%s' not set in environment." % (
                self.DJANGO_SETTINGS_MODULE
            )
        if djangoSettingsModuleName:
            firstPackageName = djangoSettingsModuleName.split('.')[0]
            if firstPackageName != self.systemPyName:
                msg = "In environment, %s %s looks wrong for %s system." % (
                    self.DJANGO_SETTINGS_MODULE, 
                    djangoSettingsModuleName, self.systemPyName
                )
                raise msg
        else:
            raise "%s value in environment not valid: '%s'" % (
                self.DJANGO_SETTINGS_MODULE,
                djangoSettingModuleName
            )

    def getConfigFilePath(self):
        "Reads path to system's configuration file from environment variable."
        name = self.getConfigFilePathEnvironmentVariableName()
        if name in os.environ:
            path = os.environ[name]
        else:
            message = "Environment variable '%s' not set." % name
            raise EnvironmentError, message
        return path
        
    def getConfigFilePathEnvironmentVariableName(self):
        name = self.systemName.upper() + '_SETTINGS'
        return name

