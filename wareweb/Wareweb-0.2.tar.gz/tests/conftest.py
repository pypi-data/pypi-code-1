import sys, os
import pkg_resources

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
pkg_resources.require('Paste')
