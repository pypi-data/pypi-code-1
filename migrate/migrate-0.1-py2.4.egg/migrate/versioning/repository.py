from pkg_resources import resource_string,resource_filename
import os,shutil
import string
from migrate.versioning.base import *
from migrate.versioning.template import template
from migrate.versioning.cfgparse import *
from migrate.versioning.pathed import *
from migrate.versioning import script
from migrate.versioning.version import VerNum
import version

class RepositoryError(Exception):
    pass
class InvalidRepositoryError(RepositoryError):
    pass

class Changeset(dict):
    """A collection of changes to be applied to a database
    Changesets are bound to a repository and manage a set of logsql scripts from
    that repository.
    Behaves like a dict, for the most part. Keys are ordered based on start/end.
    """
    def __init__(self,start,*changes,**k):
        """Give a start version; step must be explicitly stated"""
        self.step = k.pop('step',1)
        self.start = VerNum(start)
        self.end = self.start
        for change in changes:
            self.add(change)

    class _iter:
        def __init__(self,object):
            self.object = object
            self.keys = object.keys()
            self.keys.reverse()
        def next(self):
            try:
                key = self.keys.pop()
            except:
                raise StopIteration
            change = self.object[key]
            ret = key,change
            return ret
    def __iter__(self):
        return self._iter(self)
    
    def keys(self):
        """In a series of upgrades x -> y, keys are version x. Sorted."""
        ret = super(Changeset,self).keys()
        # Reverse order if downgrading
        ret.sort(reverse=(self.step < 1))
        return ret

    def add(self,change):
        key = self.end
        self.end += self.step
        self[key] = change
        
    def run(self,*p,**k):
        for version,change in self:
            change.run(*p,**k)

class Repository(Pathed):
    """A project's change script repository"""
    # Configuration file, inside repository
    _config='migrate.cfg'
    # Version information, inside repository
    _versions='versions'

    def __init__(self,path):
        log.info('Loading repository %s...'%path)
        self.verify(path)
        super(Repository,self).__init__(path)
        self.config=Config(os.path.join(self.path,self._config))
        self.versions=version.Collection(os.path.join(self.path,self._versions))
        log.info('Repository %s loaded successfully')
        log.debug('Config: %r'%self.config.to_dict())
    
    @classmethod
    def verify(cls,path):
        """Ensure the target path is a valid repository
        Throws InvalidRepositoryError if not
        """
        # Ensure the existance of required files
        try:
            cls.require_found(path)
            cls.require_found(os.path.join(path,cls._config))
            cls.require_found(os.path.join(path,cls._versions))
        except PathNotFoundError,e:
            raise InvalidRepositoryError(path)
    
    @classmethod
    def prepare_config(cls,pkg,rsrc,name,**opts):
        """Prepare a project configuration file for a new project"""
        # Prepare opts
        defaults=dict(
            version_table='_version',
            repository_id=name,
            required_dbs=[],
        )
        for key,val in defaults.iteritems():
            if (key not in opts) or (opts[key] is None):
                opts[key]=val

        # Prepare text
        #src = os.path.join(pkg,rsrc)
        #fd=open(src,'r')
        #tmpl = fd.read()
        #fd.close()
        tmpl = resource_string(pkg,rsrc)
        ret = string.Template(tmpl).substitute(opts)
        return ret

    @classmethod
    def create(cls,path,name,**opts):
        """Create a repository at a specified path"""
        cls.require_notfound(path)

        pkg,rsrc = template.default_repository(as_pkg=True)
        tmplpkg = '.'.join((pkg,rsrc))
        tmplfile = resource_filename(pkg,rsrc)
        config_text = cls.prepare_config(tmplpkg,cls._config,name,**opts)
        # Create repository
        try:
            shutil.copytree(tmplfile,path)
            # Edit config defaults
            fd = open(os.path.join(path,cls._config),'w')
            fd.write(config_text)
            fd.close()
        except:
            #raise
            log.error("There was an error creating your repository")
        return cls(path)
    
    def commit(self,*p,**k):
        reqd = self.config.get('db_settings','required_dbs')
        return self.versions.commit(required=reqd,*p,**k)
    
    latest=property(lambda self: self.versions.latest)
    version_table=property(lambda self: self.config.get('db_settings','version_table'))
    id=property(lambda self: self.config.get('db_settings','repository_id'))

    def version(self,*p,**k):
        return self.versions.version(*p,**k)
    
    @classmethod
    def clear(cls):
        Pathed.clear(cls)
        version.Collection.clear()
    
    def changeset(self,database,start,end=None):
        """Create a changeset to migrate this dbms from ver. start to end/latest
        """
        start = VerNum(start)
        if end is None:
            end = self.latest
        else:
            end = VerNum(end)
        if start <= end:
            step = 1
            range_mod = 1
            op = 'upgrade'
        else: 
            step = -1
            range_mod = 0
            op = 'downgrade'
        versions = range(start+range_mod,end+range_mod,step)
        changes = []
        for v in versions:
            change = self.version(v).script(database,op).log
            changes.append(change)
        ret = Changeset(start,step=step,*changes)
        return ret

