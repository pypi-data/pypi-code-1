import logging
import os
import setuptools.archive_util
import shutil
import subprocess
import sys
import tempfile
import urllib2
import virtualenv
import zc.buildout

class Venv(object):
    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options
        self.logger = logging.getLogger(self.name)
        buildout['buildout'].setdefault('downloads-cache', 
                os.path.join(buildout['buildout']['directory'], 'downloads'))
        self.downloads = buildout['buildout']['downloads-cache']
        self.offline = buildout['buildout']['offline'].lower() == 'true'

    def update(self):
        pass

    def install(self):
        """Turn the buildout directory into a virtualenv, if it isn't
        already.  If the buildout venv is already activated, continue
        with the buildout.  If not, recursively launch buildout with
        the venv activated, then exit."""
        buildout_dir = self.buildout['buildout']['directory']
        bin_dir = self.buildout['buildout']['bin-directory']
        self.venv_python_path = venv_python_path = '%s/python' % bin_dir

        # make the venv? (XXX: is this test too weak)
        is_venv = os.path.exists(venv_python_path)
        if not is_venv:
            venv_file = virtualenv.__file__
            if venv_file[-4:] in ('.pyc', '.pyo') :
                venv_file = venv_file[:-1]
            subprocess.call([sys.executable, venv_file, buildout_dir])

        # re-run bootstrap.py?
        buildout_exec = open('%s/buildout' % bin_dir)
        is_venv_bootstrapped = venv_python_path in buildout_exec.readline()
        if not is_venv_bootstrapped:
            # re-initialize and -launch the buildout
            subprocess.call([venv_python_path,
                             '%s/bootstrap.py' % buildout_dir])

        # re-launch the buildout?
        if sys.executable != venv_python_path:
            subprocess.call('%s/buildout' % bin_dir)
            sys.exit()

        # we only get to this point if buildout was run in venv; do a
        # last bit of env tweaking
        if bin_dir not in os.environ['PATH']:
            os.environ['PATH'] = "%s:%s" % (bin_dir, os.environ['PATH'])

        # install any distutils packages?
        if self.options.get('distutils_urls'):
            self._distutils()

        return ()

    def _distutils(self):
        """Download and install any specified distutils packages into
        the created venv."""
        urls = self.options.get('distutils_urls').split()
        for url in urls:
            self.logger.info('Processing %s' % url)
            path = self._get_archive(url)
            tmp = tempfile.mkdtemp(prefix="buildout-")
            try:
                args = ['install']
                self.logger.debug('Extracting into %s' % tmp)
                setuptools.archive_util.unpack_archive(path, tmp)
                # Let's find our setup.py
                search_paths = [os.path.join(tmp, 'setup.py'),]
                for d in os.listdir(tmp):
                    search_paths.append(os.path.join(tmp, d, 'setup.py'))
                setup_path = None
                for p in search_paths:
                    self.logger.debug("Checking %s" % p)
                    if os.path.exists(p):
                        setup_path = p
                if setup_path is None:
                    raise zc.buildout.UserError, \
                        "Could not find a setup.py in this package"
                self.logger.info("Installing")
                self._install_pkg(setup_path)
            finally:
                shutil.rmtree(tmp)

    def _install_pkg(self, setup_path):
        old_dir = os.getcwd()
        os.chdir(os.path.dirname(setup_path))
        try:
            cmd = [self.venv_python_path, 'setup.py', 'install']
            subprocess.call(' '.join(cmd), shell=True)
        finally:
            os.chdir(old_dir)
            
    def _get_archive(self, url):
        fname = os.path.basename(url)
        path = os.path.join(self.downloads, fname)
        if os.path.exists(path):
            self.logger.debug(" -> already cached")
        else:
            if self.offline:
                raise zc.buildout.UserError, \
                    "Can not download archive because of offline-mode"
            self.logger.debug(" -> downloading")
            out = open(path, 'wb+')
            try:
                fp = urllib2.urlopen(url)
                for line in fp:
                    out.write(line)
            finally:
                out.close()
        return path
