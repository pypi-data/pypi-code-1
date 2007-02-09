"""Configuration for instance manager
"""

# Directory in the user's homedir where we store our config.
CONFIGDIR = '.instancemanager'
SITECONFIG = '/etc/instancemanager/sitedefaults.py'
SECRET_PREFIX='local-'
STUB_PREFIX='stub.'

CONFIGCHANGES = {
    '#    security-policy-implementation python':
    'security-policy-implementation python\n',
    'verbose-security on': 'verbose-security on\n',
    'debug-mode on': 'debug-mode on\n',
    'devmode on': 'devmode on\n',
    }

PORTSNIPPET = """<http-server>
  address %(port)s
</http-server>
"""
Z3PORTSNIPPET= """<server>
  type HTTP
  address %(port)s
</server>
"""

FTPPORTSNIPPET = """<ftp-server>
  address %(ftp_port)s
</ftp-server>
"""

Z3FTPPORTSNIPPET= """<server ftp>
  type FTP
  address %(ftp_port)s
</server>
"""

ZEOCONFIGCHANGES = {
    'monitor-address': '  monitor-address %(monitor_port)s\n',
    }

LOGFILE = 'instancemanager.log'

QISCRIPT = 'quickreinstaller.py'
UISCRIPT = 'uninstaller.py'

PACKSCRIPT = 'pack.py'
 
CHANGEOWNSCRIPT = 'changeownership.py'

ZEOSNIPPET = """<zodb_db main>
  mount-point /
  # ZODB cache, in number of objects
  cache-size 500
  <zeoclient>
    server localhost:%(zeoport)s
    storage 1
    name zeostorage
    var $INSTANCE/var
    # ZEO client cache, in bytes
    cache-size 20MB
    # Uncomment to have a persistent disk cache
    %(zeo_client_line)s
  </zeoclient>
</zodb_db>
"""

Z3ZEOSNIPPET = """<zodb>
  <zeoclient>
    server localhost:%(zeoport)s
    storage 1
    # ZEO client cache, in bytes
    cache-size 20MB
    # Uncomment to have a persistent disk cache
    #client zeo1
  </zeoclient>
</zodb>
"""

DATABASE_TEMPFILES = [
    'Data.fs.tmp',
    'Data.fs.index',
    'Data.fs.lock',
    ]

APACHE_TEMPLATE = """
For the apache config:

  # Use the simple example at 
  # http://plone.org/documentation/tutorial/plone-apache/virtualhost
  # as your starting point.

  # Configuration for use with a squid that is configured using CacheFu.
  # Normalize URLs by removing trailing /'s
  RewriteRule ^/(.*)/$ http://127.0.0.1:3128/http/%(sn)s/80/$1 [L,P]
  # Pass all other urls straight through
  RewriteRule ^/(.*)$  http://127.0.0.1:3128/http/%(sn)s/80/$1 [L,P]

  # If you have zope directly behind apache, use the following;
  #RewriteRule ^(.*) http://localhost:%(zopeport)s/VirtualHostBase/http/%(sn)s:80/%(plonesite)s/VirtualHostRoot$1 [L,P]


For at the end of the cachefu squid.cfg (in CacheFuDocumentation/squid):

  yoursitenamehere.com: 127.0.0.1:%(zopeport)s/%(plonesite)s

"""
