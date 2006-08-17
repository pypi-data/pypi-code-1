#!/usr/bin/env python


"""
Autogenerated by CHEETAH: The Python-Powered Template Engine
 CHEETAH VERSION: 1.0
 Generation time: Thu Aug 17 07:48:38 2006
   Source file: xhtml.tmpl
   Source file last modified: Thu Aug 17 07:48:32 2006
"""

__CHEETAH_genTime__ = 'Thu Aug 17 07:48:38 2006'
__CHEETAH_src__ = 'xhtml.tmpl'
__CHEETAH_version__ = '1.0'

##################################################
## DEPENDENCIES

import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from webskine.util import time_ago

##################################################
## MODULE CONSTANTS

try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time

##################################################
## CLASSES

class xhtml(Template):
    """
    
    Autogenerated by CHEETAH: The Python-Powered Template Engine
    """

    ##################################################
    ## GENERATED METHODS


    def __init__(self, *args, **KWs):
        """
        
        """

        Template.__init__(self, *args, **KWs)

    def respond(self,
            trans=None,
            VFFSL=valueFromFrameOrSearchList,
            VFN=valueForName):


        """
        This is the main method generated by Cheetah
        """

        if not trans: trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            dummyTrans = True
        else: dummyTrans = False
        write = trans.response().write
        SL = self._searchList
        globalSetVars = self._globalSetVars
        filter = self._currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''<!-- vim: set encoding=utf-8: -->

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>''')
        __v = VFFSL(SL,"title",True)
        if __v is not None: write(filter(__v, rawExpr='$title')) # from line 9, col 12.
        write('''</title>

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="Content-Language" content="en-us">

    <link rel="alternate" title="Tao etc." href="''')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 14, col 50.
        write('atom" type="application/atom+xml" />\n    <link rel="stylesheet" type="text/css" href="')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 15, col 50.
        write('''css/style.css" />

    <script type="text/javascript">
        var jsonStore = "''')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='$home')) # from line 18, col 26.
        write('";\n    </script>\n    <script type="text/javascript" src="')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 20, col 41.
        write('js/jquery.js"></script>\n    <script type="text/javascript" src="')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 21, col 41.
        write('js/tinymce/jscripts/tiny_mce/tiny_mce.js"></script>\n    <script type="text/javascript" src="')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 22, col 41.
        write('js/json.js"></script>\n    <script type="text/javascript" src="')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 23, col 41.
        write('js/cookies.js"></script>\n    <script type="text/javascript" src="')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='${home}')) # from line 24, col 41.
        write('''js/webskine.js"></script>
</head>

<body>
    <div id="header">
        <h1><a href="''')
        __v = VFFSL(SL,"home",True)
        if __v is not None: write(filter(__v, rawExpr='$home')) # from line 29, col 22.
        write('" title="Home">')
        __v = VFFSL(SL,"title",True)
        if __v is not None: write(filter(__v, rawExpr='$title')) # from line 29, col 42.
        write('''</a></h1>
    </div>

    <div id="main">
''')
        for entry in VFFSL(SL,"entries",True):
            write('        <div class="entry" id="')
            __v = VFFSL(SL,"entry.id",True)
            if __v is not None: write(filter(__v, rawExpr='$entry.id')) # from line 34, col 32.
            write('">\n            <h2><a href="')
            __v = VFFSL(SL,"entry.id",True)
            if __v is not None: write(filter(__v, rawExpr='$entry.id')) # from line 35, col 26.
            write('" title="Permalink for this post" class="title">')
            __v = VFFSL(SL,"entry.title",True)
            if __v is not None: write(filter(__v, rawExpr='$entry.title')) # from line 35, col 83.
            write('''</a></h2>

            <div class="content">
                ''')
            __v = VFFSL(SL,"entry.content.content",True)
            if __v is not None: write(filter(__v, rawExpr='$entry.content.content')) # from line 38, col 17.
            write('''
            </div>

            <p class="footnote">Updated ''')
            __v = VFFSL(SL,"time_ago",False)(VFFSL(SL,"entry.updated",True))
            if __v is not None: write(filter(__v, rawExpr='$time_ago($entry.updated)')) # from line 41, col 41.
            write('''</p>

            <p class="break">❁</p>
        </div>
''')
        write('''    </div>

    <div id="footer">
        <p>This weblog by <a href="http://dealmeida.net/projects/webskine">webskine</a> &mdash; &copy; Roberto De Almeida 2006</p>
    </div>
</body>

</html>
''')
        
        ########################################
        ## END - generated method body
        
        return dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## GENERATED ATTRIBUTES


    __str__ = respond

    _mainCheetahMethod_for_xhtml= 'respond'


# CHEETAH was developed by Tavis Rudd, Mike Orr, Ian Bicking and Chuck Esterbrook;
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org

##################################################
## if run from command line:
if __name__ == '__main__':
    xhtml().runAsMainProgram()

