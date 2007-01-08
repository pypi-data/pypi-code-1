import dm.command
import kforge.utils.backup
from kforge.ioc import *
import os

class Backup(dm.command.Command):
    
    def __init__(self, baseBackupPath):
        super(Backup, self).__init__()
        self.backupPathBuilder = BackupPathBuilder(baseBackupPath)
    
    def execute(self):
        super(Backup, self).execute()
        if os.path.exists(self.backupPathBuilder.miscBackupPath):
            shutil.rmtree(self.backupPathBuilder.miscBackupPath)
        os.makedirs(self.backupPathBuilder.miscBackupPath)
        self.backupDatabase()
        # todo backup non-service plugins
        for project in self.registry.projects:
            self.backupProject(project)
    
    def backupDatabase(self):
        """
        Backup up the central kforge database.
        [[TODO: support db types other than postgres]]
        """
        dbType = self.dictionary['db.type']
        if dbType == 'postgres':
            backupCmd = kforge.utils.backup.BackupItemDbPgsql(self.backupPathBuilder.miscBackupPath, 'db.sql')
            backupCmd.dbName = self.dictionary['db.name']
            backupCmd.username = 'postgres'
            backupCmd.doBackup()
        else:
            self.raiseError('Database type: %s is not supported' % dbType)
    
    def backupProject(self, project):
        projectBackupPath = self.backupPathBuilder.getProjectPath(project)
        if os.path.exists(projectBackupPath):
            shutil.rmtree(projectBackupPath)
        os.makedirs(projectBackupPath)
        for service in project.services:
            projectPluginPath = self.backupPathBuilder.getProjectPluginPath(service)
            if not os.path.exists(projectPluginPath):
                os.makedirs(projectPluginPath)
            service.plugin.getSystem().backup(service, self.backupPathBuilder)


class BackupPathBuilder(object):
    
    def __init__(self, baseDirectoryPath):
        self.baseDirPath = baseDirectoryPath
        self.miscBackupPath = os.path.join(self.baseDirPath, 'misc')
        self.projectsBackupPath = os.path.join(self.baseDirPath, 'projects')
        self.dictionary = kforge.dictionary.SystemDictionary()
    
    def getProjectPath(self, project):
        return os.path.join(self.projectsBackupPath, project.name)
    
    def getProjectPluginPath(self, service):
        return os.path.join(self.getProjectPath(service.project), service.plugin.name)
    
    def getServicePath(self, service):
        return os.path.join(self.getProjectPluginPath(service), str(service.id))

