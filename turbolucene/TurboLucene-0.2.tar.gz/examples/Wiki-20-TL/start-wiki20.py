#!/usr/bin/env python2.4
import pkg_resources
pkg_resources.require("TurboGears")

import turbogears
import cherrypy
cherrypy.lowercase_api = True

from os.path import *
import sys

# first look on the command line for a desired config file,
# if it's not on the command line, then
# look for setup.py in this directory. If it's not there, this script is
# probably installed
if len(sys.argv) > 1:
    turbogears.update_config(configfile=sys.argv[1], 
        modulename="wiki20.config")
elif exists(join(dirname(__file__), "setup.py")):
    turbogears.update_config(configfile="dev.cfg",
        modulename="wiki20.config")
else:
    turbogears.update_config(configfile="prod.cfg",
        modulename="wiki20.config")

from wiki20.controllers import Root

turbogears.start_server(Root())
