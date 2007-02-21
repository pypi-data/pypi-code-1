#!c:\Python24\python.exe

# XXX remove after test
#import pycallgraph
#pycallgraph.start_trace()

import pkg_resources
pkg_resources.require("TurboGears")

import turbogears
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
        modulename="turboblog.config")
elif exists(join(dirname(__file__), "setup.py")):
    update_config(configfile="dev.cfg",modulename="turboblog.config")
else:
    update_config(configfile="prod.cfg",modulename="turboblog.config")

from turboblog.controllers import Root
#from turboblog.systemschedule import schedule_tasks
#turbogears.startup.call_on_startup.append(schedule_tasks)

start_server(Root())

#pycallgraph.stop_trace()
#pycallgraph.make_graph('exec_graph.png')
