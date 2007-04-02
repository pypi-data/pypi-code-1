#############################################################################
#
#	$Id: __init__.py,v 2.7 2003/03/05 20:46:05 irmen Exp $
#	Pyro file to make Pyro a package, and to set up configuration.
#
#	This is part of "Pyro" - Python Remote Objects
#	Which is (c) Irmen de Jong - irmen@users.sourceforge.net
#
#############################################################################


# Initialize Pyro Configuration.
#
# This is put here because it could actually initialize config stuff needed
# even before the code calls core.initClient or core.initServer.
#
# Pyro.config is a class, which has a __getattr__ member, so all
# pyro code can use Pyro.config.<itemname> to look up a value.
# This allows for tweaking the configuration lookups by writing
# a custom __getattr__ and/or __init__ for the class.
# However, currently the class initializer adds configuration items
# as regular class data members.


import configuration, os

config = configuration.Config()
try:
	confFile = os.environ['PYRO_CONFIG_FILE']
except KeyError:
	confFile = ''
if not confFile and os.path.isfile('Pyro.conf'):
	confFile='Pyro.conf'
config.setup(confFile)



