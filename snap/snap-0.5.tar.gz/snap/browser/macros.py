"""
$Id: macros.py 3966 2006-01-26 14:56:39Z sidnei $
"""

from zope.app.basicskin.standardmacros import StandardMacros as BaseMacros

class StandardMacros(BaseMacros):

    macro_pages = (('snap_macros',) +
                   BaseMacros.macro_pages)
