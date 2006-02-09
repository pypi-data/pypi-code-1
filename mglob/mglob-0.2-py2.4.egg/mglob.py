#!/usr/bin/env python

""" mglob - enhanced file list expansion module

Use as stand-alone utility (for xargs, `backticks` etc.), 
or a globbing library for own python programs. Globbing the sys.argv is something 
that almost every Windows script has to perform manually, and this module is here
to help with that task. Also Unix users will benefit from enhanced modes 
such as recursion, exclusion, directory omission...

Unlike glob.glob, directories are not included in the glob unless specified 
with 'dir:'

'expand' is the function to use in python programs. Typical use
to expand argv (esp. in windows)::

    try:
        import mglob 
        files = mglob.expand(sys.argv[1:])
    except ImportError:
        print "mglob not found; try 'easy_install mglob' for extra features"
        files = sys.argv[1:] 

Note that for unix, shell expands *normal* wildcards (*.cpp, etc.) in argv.
Therefore, you might want to use quotes with normal wildcards to prevent this 
expansion, in order for mglob to see the wildcards and get the wanted behaviour.
Not quoting the wildcards is harmless and typically has equivalent results, though.

Author: Ville Vainio <vivainio@gmail.com>
License: MIT Open Source license

"""

#Assigned in variable for "usage" printing convenience"

globsyntax = """\
This program allows specifying filenames with "mglob" mechanism.
Supported syntax in globs (wilcard matching patterns)::

 *.cpp ?ellowo*                
     - obvious. Differs from normal glob in that dirs are not included.
       Unix users might want to write this as: "*.cpp" "?ellowo*"
 rec:/usr/share=*.txt,*.doc    
     - get all *.txt and *.doc under /usr/share, 
       recursively
 rec:/usr/share
     - All files under /usr/share, recursively
 rec:*.py
     - All .py files under current working dir, recursively
 foo                           
     - File foo, or all files in dir foo
 !*.bak readme*                   
     - readme*, exclude files ending with .bak
 dir:foo                       
     - the directory foo (not files in foo)
 dir:*                         
     - all directories in current folder
 foo.py bar.* !h* rec:*.py
     - Obvious. !h* exclusion only applies for rec:*.py.
       foo.py is *not* included twice.
 @filelist.txt
     - All files listed in 'filelist.txt' file, on separate lines.
 """


__version__ = "0.2"


import os,glob,fnmatch,sys
from sets import Set as set

def recfind(p, pats = ["*"]):
    for (dp,dnames,fnames) in os.walk(p):
        for f in fnames:
            matched = False
            for p in pats:
                if fnmatch.fnmatch(f,p):
                    matched = True
                    break
            if matched:
                yield os.path.join(dp,f)            
                
def expand(flist):
    """ Expand the glob(s) in flist.
    
    flist may be either a whitespace-separated list of globs/files
    or an array of globs/files.
    
    """
    if isinstance(flist, basestring):
        flist = flist.split()
    done_set = set()
    denied_set = set()
    def once_filter(seq):
        for it in seq:
            p = os.path.abspath(it)
            if p in done_set:
                continue
            done_set.add(p)
            deny = False
            for deny_pat in denied_set:
                if fnmatch.fnmatch(os.path.basename(p), deny_pat):
                    deny = True
                    break
            if not deny:
                yield it
        return
            
    res = []

    for ent in flist:
        ent = os.path.expanduser(os.path.expandvars(ent))
        if ent.lower().startswith('rec:'):
            fields = ent[4:].split('=')            
            if len(fields) == 2:
                pth, patlist = fields
            elif len(fields) == 1:
                if os.path.isdir(fields[0]):
                    # single arg is dir
                    pth, patlist = fields[0], '*'
                else: 
                    # single arg is pattern
                    pth, patlist = '.', fields[0]
                    
            elif len(fields) == 0:
                pth, pathlist = '.','*'
                
            pats = patlist.split(',')
            res.extend(once_filter(recfind(pth, pats)))
        # filelist
        elif ent.startswith('@') and os.path.isfile(ent[1:]):
            res.extend(once_filter(open(ent[1:]).read().splitlines()))
        # exclusion
        elif ent.startswith('!'):
            denied_set.add(ent[1:])
        # glob only dirs
        elif ent.lower().startswith('dir:'):
            res.extend(once_filter(filter(os.path.isdir,glob.glob(ent[4:]))))
            
        # get all files in the specified dir
        elif os.path.isdir(ent):
            res.extend(once_filter(filter(os.path.isfile,glob.glob(ent + os.sep+"*"))))
            
        # glob only files

        elif '*' in ent or '?' in ent:
            res.extend(once_filter(filter(os.path.isfile,glob.glob(ent))))

        else:
            res.extend(once_filter([ent]))
    return res
            
            
def test():
    assert (
        expand("*.py ~/.ipython/*.py rec:/usr/share/doc-base") == 
        expand( ['*.py', '~/.ipython/*.py', 'rec:/usr/share/doc-base'] ) 
        )
    
def main():
    if len(sys.argv) < 2:
        print globsyntax
        return
    
    print "\n".join(expand(sys.argv[1:])),
    
# test()
if __name__ == "__main__":
    main()
