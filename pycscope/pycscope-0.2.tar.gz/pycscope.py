#!/usr/bin/env python
"""
PyCscope

PyCscope creates a Cscope-like index file for a tree of Python source.
"""

__author__ = "Dean Hall (dwhall256\x40yahoo\x2Ecom)"
__copyright__ = "Copyright 2006 Dean Hall.  See LICENSE for details."
__date__ = "2006/08/12"
__version__ = "0.2"
__usage__ = """Usage: pycscope.py [-R] [-f reffile] [source files]

-R              Recurse directories for files.
-f reffile      Use reffile as cross-ref file name instead of cscope.out."""


import getopt, sys, os, os.path, types
import keyword, parser, symbol, token

# Marks as defined by Cscope
MARK_FILE = "\t@"
MARK_FUNC_DEF = "\t$"
MARK_FUNC_CALL = "\t`"
MARK_FUNC_END = "\t}"
MARK_INCLUDE = "\t~<"   # TODO: assume all includes are global for now
MARK_ASGN = "\t="
MARK_CLASS = "\tc"
MARK_GLOBAL = "\tg"
MARK_FUNC_PARM = "\tp"

# Reverse the key,value pairs in the token dict
tok_name_lookup = dict((v,k) for k,v in token.tok_name.iteritems())
TOK_NEWLINE = tok_name_lookup["NEWLINE"]
TOK_NAME = tok_name_lookup["NAME"]
TOK_LPAR = tok_name_lookup["LPAR"]
TOK_ENDMARKER = tok_name_lookup["ENDMARKER"]
TOK_INDENT = tok_name_lookup["INDENT"]
TOK_DEDENT = tok_name_lookup["DEDENT"]

# Reverse the key,value pairs in the symbol dict
sym_name_lookup = dict((v,k) for k,v in symbol.sym_name.iteritems())
SYM_TRAILER = sym_name_lookup["trailer"]
SYM_VARARGSLIST = sym_name_lookup["varargslist"]

# Get the list of Python keywords and add a few common builtins
kwlist = keyword.kwlist
kwlist.extend(("True", "False", "None", "object"))

# Globals for the recursive walkAst function
latestnewline = 1
latestsymbol = ""
latesttoken = ""
prevtoken = ""
mark = ""
infuncdef = False
indentcount = 0


def main():
    """Parse command line args and act accordingly.
    """
    # Parse the command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "Rf:")
    except getopt.GetoptError:
        print __usage__
        sys.exit(2)
    recurse = False
    indexfn = "cscope.out"
    for o, a in opts:
        if o == "-R":
            recurse = True
        if o == "-f":
            indexfn = a

    # Create the buffer to store the output (list of strings)
    indexbuff = []

    # Search current dir by default
    if len(args) == 0:
        args = "."

    # Parse the given list of files/dirs
    basepath = os.getcwd()
    for name in args:
        if os.path.isdir(os.path.join(basepath, name)):
            parseDir(basepath, name, indexbuff, recurse)
        else:
            parseFile(basepath, name, indexbuff)

    # Symbol data for the last file ends with a file mark
    indexbuff.append("\n" + MARK_FILE)
    # Write trailer info
    indexbuff.append("\n\n1\n.\n")
    writeIndex(basepath, indexfn, indexbuff)


def parseDir(basepath, relpath, indexbuff, recurse):
    """Parses all files in the directory and
    recurses into subdirectories if requested.
    """
    dirpath = os.path.join(basepath, relpath)
    for name in os.listdir(dirpath):
        fullpath = os.path.join(dirpath, name)
        if os.path.isdir(fullpath) and recurse:
            parseDir(basepath, os.path.join(relpath, name), indexbuff, recurse)
        else:
            parseFile(basepath, os.path.join(relpath, name), indexbuff)


def parseFile(basepath, relpath, indexbuff):
    """Parses a source file and puts the resulting index into the buffer.
    """
    # Don't parse if it's not python source
    if relpath[-3:] != ".py":
        return

    # Open the file and get the contents
    fullpath = os.path.join(basepath, relpath)
    f = open(fullpath, 'r')
    filecontents = f.read()
    f.close()

    # Add the file mark to the index
    indexbuff.append("\n%s%s" % (MARK_FILE, relpath))
    global latestnewline
    latestnewline = len(indexbuff)

    # Add path info to any syntax errors in the source files
    try:
        parseSource(filecontents, indexbuff)
    except SyntaxError, se:
        se.filename = fullpath
        raise se


def parseSource(sourcecode, indexbuff):
    """Parses python source code and puts the resulting index into the buffer.
    """
    # Parse the source to an Abstract Syntax Tree
    ast = parser.suite(sourcecode)
    astlist = parser.ast2list(ast, True)

    # Set these globals before each file's AST is walked
    global sourcelinehassymbol
    sourcelinehassymbol = False
    global currentlinenum
    currentlinenum = 0

    # Walk the AST to index the rest of the file
    walkAst(astlist, indexbuff)


def walkAst(astlist, indexbuff):
    """Scan the AST for tokens, write out index lines.
    """
    global latestnewline
    global latestsymbol
    global latesttoken
    global prevtoken
    global mark
    global sourcelinehassymbol
    global infuncdef
    global indentcount
    global currentlinenum

    # Remember the latest symbol
    if astlist[0] > 256:
        latestsymbol = astlist[0]

    # Handle the tokens
    else:
        # Save the previous token and get the latest one
        prevtoken = latesttoken
        latesttoken = astlist[0]

        # If this code is on a new line number
        if astlist[2] != currentlinenum:
            currentlinenum = astlist[2]

            # If there was a symbol of interest,
            # remember this location in the index
            if sourcelinehassymbol:
                latestnewline = len(indexbuff)
                sourcelinehassymbol = False

            # If there was no symbol of interest between this and the previous
            # newline, remove all entries added since the previous newline
            else:
                del indexbuff[latestnewline:]

            # Write the new line number
            indexbuff.append("\n\n%d " % astlist[2])

            # Clear an include mark when a newline token is reached
            # This is what ends a comma-separated list of modules after import
            if mark == MARK_INCLUDE:
                mark = ""

        if latesttoken == TOK_NAME:
            # If a name is not a python keyword, it is a symbol of interest
            if astlist[1] not in kwlist:

                # Remember that there is a symbol of interest
                sourcelinehassymbol = True

                # Write the mark and the symbol
                indexbuff.append("\n%s%s\n" % (mark, astlist[1]))

                # Clear the mark unless it's an include mark
                # This is what allows a comma-separated list of modules after import
                if mark != MARK_INCLUDE:
                    mark = ""

            # If the name is a python keyword
            else:
                # Some keywords determine what mark should prefix the next name
                kw = astlist[1]
                if kw == "def":
                    mark = MARK_FUNC_DEF

                    # Remember that we're in a function definition
                    infuncdef = True
                    indentcount = 0
                elif kw == "import":
                    mark = MARK_INCLUDE
                elif kw == "class":
                    mark = MARK_CLASS

                # Write out the keyword
                indexbuff.append("%s " % kw)

        # This set of tokens and symbols indicates a function call (not perfect)
        elif (latesttoken == TOK_LPAR) and (prevtoken == TOK_NAME) and (
            (latestsymbol == SYM_TRAILER) or (latestsymbol == SYM_VARARGSLIST)):

            # Insert a function-call mark before the previous name
            indexbuff[-1] = "\n%s%s( " % (MARK_FUNC_CALL, indexbuff[-1][1:])

        # Count the number of indents; to be used by dedent
        elif latesttoken == TOK_INDENT:
            if infuncdef:
                indentcount += 1

        # When dedent reaches the level of the function def,
        # write the function-end mark
        elif latesttoken == TOK_DEDENT:
            if infuncdef:
                indentcount -= 1
                if indentcount == 0:
                    indexbuff.insert(-1, "\n\n%d \n%s\n" % (astlist[2], MARK_FUNC_END))
                    latestnewline += 1
                    infuncdef = False

        # Replace the last line number placeholder with a newline
        # when at the end of a file
        elif latesttoken == TOK_ENDMARKER:
            if len(indexbuff) > 0:
                indexbuff[-1] = "\n"

        # For uninteresting tokens, just write the accompanying string
        else:
            if len(astlist[1]) > 0:
                nonsymboltext = astlist[1].replace("\n","\\n") + ' '
            else:
                nonsymboltext = ''
            indexbuff.append(nonsymboltext)

    # Recurse into all nodes
    for i in range(1, len(astlist)):
        if type(astlist[i]) == types.ListType:
            walkAst(astlist[i], indexbuff)


def writeIndex(basepath, indexfn, indexbuff):
    """Write the index buffer to the output file.
    """
    fout = open(os.path.join(basepath, indexfn), 'w')
    # Write the header, index and footer
    # TODO: fout.write("pscope %s %s 42\n" % (__version__, cwd))
    fout.write("pscope %s %s 42" % ("15", basepath))
    fout.write(''.join(indexbuff))
    fout.close()


if __name__ == "__main__":
    main()
