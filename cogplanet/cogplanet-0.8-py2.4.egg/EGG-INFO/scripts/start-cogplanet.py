#!/usr/local/bin/python
import pkg_resources
pkg_resources.require("TurboGears")

from turbogears import update_config, start_server
import cherrypy
cherrypy.lowercase_api = True
from os.path import *
import sys

# first look on the command line for a desired config file,
# if it's not on the command line, then
# look for setup.py in this directory. If it's not there, this script is
# probably installed
if len(sys.argv) > 1:
    update_config(configfile=sys.argv[1], 
        modulename="cogplanet.config")
elif exists(join(dirname(__file__), "setup.py")):
    update_config(configfile="dev.cfg",modulename="cogplanet.config")
else:
    update_config(configfile="prod.cfg",modulename="cogplanet.config")

import cogplanet.easy_config

from cogplanet.controllers import PlanetController


start_server(PlanetController())
