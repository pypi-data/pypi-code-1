import kforge.plugin.base
from kforge.ioc import *
import os
import shutil
import tarfile

class Plugin(kforge.plugin.base.ServicePlugin):
    "MoinMoin Wiki Plugin"
    
    def __init__(self, domainObject):
        super(Plugin, self).__init__(domainObject)
        self.moinUtils = MoinUtils(self.dictionary['moin.system_path'])
    
    def onServiceCreate(self, service):
        if service and service.plugin and service.plugin.name == 'moin':
            wikiPath = service.getDirPath()
            self.moinUtils.createWiki(wikiPath)
    
    def onServicePurge(self, service):
        if service and service.plugin and service.plugin.name == 'moin':
            wikiPath = service.getDirPath()
            self.moinUtils.deleteWiki(wikiPath)
    
    def getApacheConfigCommon(self):
        """
        Ensure that you have edited the moin config file to use the moinhtdocs
        values set here
        """
        htdocsPath = os.path.join(self.dictionary['moin.system_path'], 'htdocs')
        return """
        Alias /moinhtdocs %s
        """ % htdocsPath
    
    def getApacheConfig(self, service):
        return """
        ScriptAlias %(urlPath)s %(fileSystemPath)s/moin.cgi
        <Location %(urlPath)s>
            %(accessControl)s
        </Location>
        """
    
    def backup(self, service, backupPathBuilder):
        self.moinUtils.backupWiki(service.getDirPath(), backupPathBuilder.getServicePath(service))

class MoinUtils(object):
    """
    Scripts to assist with setting up moinmoin wikis:
      1. Wiki creation and deletion
      2. Automate upgrading moin wikis from version 1.2 to version 1.3
    """
    
    logger = RequiredFeature('Logger')
    
    def __init__(self, systemPath, basePath = ''):
        """
        @systemPath: path on which moin was installed (e.g. /usr/share/moin)
        @basePath: base path at which to create wikis. If not set defaults to
                   empty string in which case wikiName where supplied in
                   functions below must be full path of wiki
        """
        self.systemPath = systemPath
        self.basePath = basePath
    
    def getWikiPath(self, wikiName):
        return os.path.join(self.basePath, wikiName)

    def wikiExists(self, wikiName):
        return os.path.exists(self.getWikiPath(wikiName))

    def createWiki(self, wikiName, withData = True):
        """
        Create a new wiki instance with default files.
        Written to work for moinmoin1.3
        
        Does not copy underlay as assume this is taken from common location
        [[TODO: allow for fastcgi]]
        """
        if self.wikiExists(wikiName):
            raise('Cannot create wiki as path already exists: %s' % self.getWikiPath(wikiName))
        newWikiBasePath = self.getWikiPath(wikiName)
        self.logger.info('Creating new wiki: %s' % newWikiBasePath)
        os.makedirs(newWikiBasePath)
        if withData:
            shutil.copytree(os.path.join(self.systemPath, 'data'),
                            os.path.join(newWikiBasePath, 'data'))
        shutil.copy(os.path.join(self.systemPath, 'config/wikiconfig.py'),
                    newWikiBasePath)
        # do cgi-bin (do not install to cgi-bin but to base dir)
        # that way all paths will work out of the box
        # installCgiPath = os.path.join(newWikiBasePath, 'cgi-bin')
        # os.makedirs(installCgiPath)
        installCgiPath = newWikiBasePath
        shutil.copy(os.path.join(self.systemPath, 'server/moin.cgi'),
                    installCgiPath)
        self.setPermissions(wikiName)

    def setPermissions(self, wikiName):
        newWikiBasePath = self.getWikiPath(wikiName)
        # now set permissions
        # only webserver should have access
        if (
            os.system('chmod -R ug+rwX %s' % newWikiBasePath)
            or
            os.system('chmod -R o-rwx %s' % newWikiBasePath)):
            self.logger.error('Failed to set permissions and owner correctly on %s' % newWikiBasePath)

    def deleteWiki(self, wikiName):
        path = self.getWikiPath(wikiName)
        if os.path.exists(path):
            shutil.rmtree(path)

    def migrateWikiData(self, dataSource, dataTarget):
        import re
        # moin migration scripts path
        scriptsPath = '/usr/lib/python2.3/site-packages/MoinMoin/scripts/migration'
        dataForMigration = os.path.join(scriptsPath, 'data')
        # delete all dirs named data* in scriptsPath dir
        tfiles  = os.listdir(scriptsPath)
        regexFilter  = re.compile("data.*", re.IGNORECASE)
        tfiles = filter(regexFilter.search, tfiles)
        for ff in tfiles:
            shutil.rmtree(os.path.join(scriptsPath, ff))
        shutil.copytree(dataSource, dataForMigration)
        scriptsToRun = [
            '12_to_13_mig01.py',
            '12_to_13_mig02.py',
            '12_to_13_mig03.py',
            '12_to_13_mig04.py',
            '12_to_13_mig05.py',
            '12_to_13_mig06.py',
            '12_to_13_mig07.py',
            '12_to_13_mig08.py',
            '12_to_13_mig09.py',
            '12_to_13_mig10.py',
            '12_to_13_mig11.py']# move the data to the right place
        # have to run the scripts from the local dir for it to work
        os.chdir(scriptsPath)
        print 'Migration: START'
        for script in scriptsToRun:
            os.system('./%s > /dev/null' % script)
        print 'Migration: COMPLETED'
        if os.path.exists(dataTarget):
            shutil.rmtree(dataTarget)
        shutil.copytree(dataForMigration, dataTarget)

    def migrateWiki(self, oldWikiPath, newWikiName):
        dataSource = os.path.join(oldWikiPath, 'data')
        dataTarget = os.path.join(self.getWikiPath(newWikiName), 'data')
        # first create new wiki (without data dir)
        if self.wikiExists(newWikiName):
            self.removeWiki(newWikiName)
        self.createWiki(newWikiName, False)
        # now migrate
        self.migrateWikiData(dataSource,  dataTarget)
        # need to redo permissions because of data directory
        self.setPermissions(newWikiName)
    
    def backupWiki(self, wikiName, destPath):
        destPath = destPath + '.tgz'
        tar = tarfile.open(destPath, 'w:gz')
        tar.add(self.getWikiPath(wikiName))
        tar.close()
