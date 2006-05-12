name = 'wxDebug'
description = 'Xdebug viewer : displays PHP profiling output generated by Xdebug 2.x'
version = '0.1'
previous_version = '0.0'
date = 'April 25, 2006'
author = 'Harry Fuecks'
author_email = 'hfuecks@gmail.com'
url = 'http://wxdebug.python-hosting.com'
copyright = 'Copyright (C) 2006 Harry Fuecks'
license = 'GNU GENERAL PUBLIC LICENSE Version 2, June 1991'
platform = 'Any'
filename = 'wxdebug'
filename_lower = filename.lower()
pythonversion = '2.4.1'
wxpythonversion = '2.6.1.0-unicode'
languages = {'English': None,}

def __createDict(locals):
    ''' Provide the local variables as a dictionary for use in string
    formatting. See e.g. meta/help.py. '''
    metaDict = {}
    for key in locals:
        if not key.startswith('__'):
            metaDict[key] = locals[key]
    return metaDict

metaDict = __createDict(locals())
