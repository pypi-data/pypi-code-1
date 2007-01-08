"""
A Plugin to provide wordpress subsystem applications.

## Notes ##

We follow an approach where we install a copy of the wordpress code for every
install.

There might be nicer approaches involving symlinking (see e.g. [1]) or the use
of wordpress mu but these all seem to have problems if the blogs aren't laid
out in some consistent manner.

[1]: <http://coderseye.com/2005/wordpress-2-multi-blogging-made-easy.html>

## Installation ##

1. Install Wordpress 2.0 on your system in a master directory.

2. Setup a mysql database for use by the wordpress services (they will all
share the same db)

3. Edit wp-config-sample.php to have to correspond to the database you have
just set up. This file will be use as the template for the config file for each
of the KForge wordpress installations created in the future.

4. Add the following configuration section to your kforge config

[wordpress]
# path to your master wordpress installation that will be used as a template
master_path = /path/to/your/wordpress/installation
# shell command to run in order to backup the wordpress db
backup_command = mysqldump --user=<insert-name> --password=<insert-password> <db-name>

5. That's it!
"""
import os
import shutil
import commands

import kforge.plugin.base

class Plugin(kforge.plugin.base.ServicePlugin):
    """Wordpress Plugin to provide wordpress services to projects
    """

    def __init__(self, domainObject):
        super(Plugin, self).__init__(domainObject)
        master_path = self.dictionary['wordpress.master_path']
        self.utils = kforge.plugin.wordpress.WordpressUtil(master_path)

    def onServiceCreate(self, service):
        if service and service.plugin and service.plugin.name == 'wordpress':
            path = service.getDirPath()
            dbTablePrefix = '%s_%s_' % (service.project.name, service.name)
            self.utils.create(path, dbTablePrefix)
            msg = 'WordpressPlugin: Created service %s on path: %s)' % (
                service, path
            )
            self.log(msg)

    def onServicePurge(self, service):
        if service and service.plugin and service.plugin.name == 'wordpress':
            path = service.getDirPath()
            if os.path.exists(path):
                shutil.rmtree(path)
            # TODO: delete tables from the db
            msg = 'WordpressPlugin: Deleted service %s on path: %s' % (
                service, path
            )
            self.log(msg)
            
    def getApacheConfig(self, service):
        return ''

    def backup(self, service, backupPathBuilder):
        # this is not great at present since we do a backup of the **whole**
        # database for every service even though there is only one database for
        # all wordpress services
        backupPath = backupPathBuilder.getServicePath(service)
        backupPath += '.gz'
        basecmd = self.dictionary['wordpress.backup_command']
        cmd = basecmd + ' | gzip > %s' % backupPath
        status, output = commands.getstatusoutput(cmd)
        if status:
            # do not use KForge exceptions here as would like to be standalone
            raise Exception('Failed to backup. Output was: %s' % output)


class WordpressUtil(object):

    def __init__(self, master_path):
        self.master_path = master_path

    def _get_parent_directory(self, new_path):
        if new_path.endswith('/'): # assumes unix style path!
            new_path = new_path[:-1]
        # this should work once we have stripped the trailing /
        parentDir = os.path.dirname(new_path)
        return parentDir

    def create(self, new_path, db_prefix):
        """Create wordpress installation
        """
        parentDir = self._get_parent_directory(new_path)
        if not os.path.exists(parentDir):
            os.makedirs(parentDir)
        shutil.copytree(self.master_path, new_path)
        # TODO symlink plugins and themes?

        # maximum allowed table names are 64 in mysql >= 4.0
        # assuming a max of 15 for project name need to make sure service name
        # is less than, say, 20-30 characters
        src_path = os.path.join(self.master_path, 'wp-config-sample.php')
        dest_path = os.path.join(new_path, 'wp-config.php')
        config = file(src_path).read()

        config = config.replace("$table_prefix  = 'wp_';",
                "$table_prefix = '%s';" % db_prefix)

        outfile = file(dest_path, 'w')
        outfile.write(config)
        outfile.close()

