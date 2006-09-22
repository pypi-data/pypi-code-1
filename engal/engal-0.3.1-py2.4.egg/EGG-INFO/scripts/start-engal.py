#!/home/nbm/fs/turbogears-1.0b1/bin/python
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
        modulename="engal.config")
elif exists(join(dirname(__file__), "setup.py")):
    turbogears.update_config(configfile="dev.cfg",
        modulename="engal.config")
else:
    turbogears.update_config(configfile="prod.cfg",
        modulename="engal.config")

def setup_database():
    from engal import model
    model.Photo.createTable(ifNotExists = True)
    model.PhotoSet.createTable(ifNotExists = True)

from turbogears.startup import call_on_startup
call_on_startup.append(setup_database)

from engal.controllers import Root

turbogears.start_server(Root())
