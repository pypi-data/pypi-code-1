"""
Simple module for extracting classes and method/function codes
out of a python file
"""
import parser
import pprint
import sys
import types
import logging
log = logging.getLogger('pyparser')

PROTECTED_BEGIN = '##code-section'
PROTECTED_END = '##/code-section'


class PyModule:
    """This is the module being called directly from the rest of ArchGenXML.

    Through the __init__() you can feed it a file and it chops it up
    in neat chunks of classes and methods. This way the other parts of
    ArchGenXML can add/remove/augment those chunks.
    """

    filebuf = None
    splittedSource = None
    ast = None
    code = None
    src = None
    classes = {}
    functions = {}
    protectedSections = {}

    def __init__(self, file, mode='file'):
        """Start dividing 'file' in chunks.

        'file' is the to chunk up. By default it is the name of a file
        on the filesystem, but with 'mode' set to 'string', 'file' is
        passed as a string.
        """

        log.debug("Initialising module parser for file '%s'.",
                  file)
        # Dictionary inits
        self.classes = {}
        self.functions = {}
        self.protectedSections = {}
        self.protectionDeclarations = []
        # Read and mangle the file
        self.filebuf = self.readFile(file, mode)
        self.splitSource()
        # Note: ast = abstract syntax tree (python internal thingy),
        # generated by the imported 'parser'.
        self.ast = parser.suite(self.filebuf)
        self.code = self.ast.compile()
        # The next two filter out the classes and the top-level
        # functions in the sourcefile and the protected
        # sections. Beware that the rest is left out!
        self.findClassesAndFunctions()
        self.findProtectedSections()
        self.findProtectionDeclarations()

    def readFile(self, file, mode='file'):
        """ Read the file into a string

        File can be a filename, a file object or a big string.
        """
        if type(file) in (type(''), type(u'')):
            # filename or big string
            if mode == 'string':
                # Big string!
                result = file
            else:
                # Filename!
                result = open(file).read()
        else:
            # File object!
            result = file.read()
        return result

    def findClassesAndFunctions(self):
        """ Collect code elements in the source file

        Code elements are seperate things like functions and classes.
        The import-statements, local variables etcetera are not code
        elements and are not extracted by this method.

        The results are placed in self.classes and
        self.functions. Functions are the top-level methods, methods
        reside inside the classes.
        """
        
        # First get all the code elements as seen by the python parser
        codes = [c for c in self.code.co_consts if type(c) ==
                 types.CodeType]
        # Get the classes
        classes = [c for c in codes if self.isItAClass(c)]
        for c in classes:
            klass = PyClass(c, self)
            self.classes[c.co_name] = klass
        # Get the functions
        functions = [c for c in codes if self.isItAFunction(c)]
        for f in functions:
            func = PyFunction(f, self)
            self.functions[f.co_name] = func

    def findProtectedSections(self):
        """ Find the protected sections in the source file

        The results are placed in self.protectedSections, which is a
        dictionary. The keys are the names of the protected sections
        (like 'module-header').
        """
        
        for i in xrange(0, len(self.splittedSource)):
            line = self.splittedSource[i]
            sline = line.strip()
            if sline.startswith(PROTECTED_BEGIN):
                j = start = i
                sectionname = sline.split()[1]
                try:
                    while not self.splittedSource[j].strip().startswith(PROTECTED_END):
                        j = j+1
                except IndexError:
                    return
                end = j
                protectedSection = '\n'.join(self.splittedSource[start+1:end])
                self.protectedSections[sectionname] = protectedSection
        log.debug("In total, we found %s protected sections.",
                  len(self.protectedSections))

    def findProtectionDeclarations(self):
        """ Find the protection declarations in the source file

        The results are placed in self.protectionDeclarations, which
        is a list. You can find the protected methods by looking for
        their name in this list of strings. A bit brute-force, I
        admit.

        A restriction is that it has to be a one-line statement.
        """
        for i in xrange(0, len(self.splittedSource)):
            line = self.splittedSource[i]
            strippedLine = line.strip()
            if ('declarePublic' in strippedLine or
                'declarePrivate' in strippedLine or
                'declareProtected' in strippedLine):
                self.protectionDeclarations.append(line)
                # note: the line, so we get the good indentation

    def isItAClass(self, c):
        """ True if a code fragment is a class

        Woooh - this is a very pillar of supreme machine intelligence
        :-)
        """
        fl = c.co_firstlineno
        if self.splittedSource[fl-1].strip().startswith('class'):
            return 1
        res = len([o for o in c.co_consts if type(o) == types.CodeType])
        #print 'Class:####',c.co_name, res, c.co_consts
        return res

    def isItAFunction(self, c):
        """ True if a code fragment is a function

        Woohoo, we're advanced! Heuristics!
        """
        fl = c.co_firstlineno
        if self.splittedSource[fl-1].startswith('def'):
            return 1

    def isItAComment(self, lineNumber):
        """ True if a code fragment is a comment

        Checks if the line starts with single or double quotes
        """
        if self.splittedSource[lineNumber].strip().startswith('"""'):
            # three double quotes
            return 1
        if self.splittedSource[lineNumber].strip().startswith("'''"):
            # three single quotes
            return 1
        return 0

    def getProtectedSection(self, section):
        """ Return the named protected section

        Simple wrapper function.
        """
        return self.protectedSections.get(section)

    def printit(self):
        # Can probably be removed - early testing-by-printing
        # Perhaps something for a --verbose option? Could be very
        # handy.
        print 'PyModule:'

        print '========'
        print 'CLASSES'
        print '========'
        for c in self.classes.values():
            c.printit()

        print '========'
        print 'FUNCTIONS'
        print '========'
        for f in self.functions.values():
            f.printit()

        print '========'
        print 'PROTECTED SECTIONS'
        print '========'
        for k, v in self.protectedSections.items():
            print 'section:', k
            print '-----------'
            print v
            print '-----------'

    def splitSource(self):
        self.filebuf = self.filebuf.replace('\r', '\n')
        self.splittedSource = self.filebuf.split('\n')
        # cleanup trailing white spaces
        self.splittedSource = [s.rstrip() for s in self.splittedSource]

class PyCodeElement:
    """ Abstract superclass
    """

    module = None
    code = None
    src = None

    def __init__(self, code, module):
        """ Simple init to set the incoming code and containing module
        """
        self.code = code
        self.module = module

    def getSrc(self):
        """ Return the plain source
        """
        return self.src

    def getName(self):
        """ Return the name of the code element
        """
        return self.name


class PyFunction(PyCodeElement):
    """ Handles functions
    """
    typename = 'function'

    def __init__(self, code, module):
        """ Inits the function in 'code', contained in 'module'

        buildMethod() does some further preparation.
        """
        PyCodeElement.__init__(self, code, module)
        self.buildMethod()

    def buildMethod(self):
        """ Prepare the method for subsequent inclusion in the
        generated file
        """
        self.name = self.code.co_name
        self.start = self.code.co_firstlineno - 1
        self.src = self.extractCode()

    def printit(self):
        # Something for --verbose, not used right now
        print '%s:' % self.typename, self.code.co_name
        print '-------------------------------------------------------'
        print self.src
        print '-------------------------------------------------------'

    def getProtectedSection(self, section):
        """ Pass this request through to the containing module
        """
        # Hm. If there's a protected section inside a function, it is
        # included in the self.src. No real sense in returning
        # anything here, it is hopefully not used [reinout]
        # Not tested in the unittests!
        return self.module.getProtectedSection(section)

    def codeLength(self):
        """ Calculate the length of a method using the code.co_lnotab
        """

        log.debug("Calculating the code length for %s.",
                  self.getName())
        res=0
        log.debug("That strange self.code.co_lnotab is %r with a length of %s.",
                  self.code.co_lnotab, len(self.code.co_lnotab))
        for i in range(0, len(self.code.co_lnotab), 2):
            log.debug("Iterating, i=%s.",
                      i)
            unused_character = self.code.co_lnotab[i]
            character = self.code.co_lnotab[i+1]
            log.debug("Getting the ord() from %s, which is %s.",
                      character, ord(character))
            log.debug("The ord() from the unused other character, %s,  is %s.",
                      unused_character, ord(unused_character))
            cl = ord(character)
            log.debug("cl (code length?) is %s.",
                      cl)
            # I don't know what that next test does
            if cl != 255:
                res += cl
                log.debug("Added it to res, total length is now %s.",
                          res)
        length = res+1
        log.debug("Added 1 to the length, returning %s.",
                  length)
        return length

    def extractCode(self):
        """ Return '\n'-string containing the method code
        """
        snip = []
        length = self.codeLength()
        start = self.start
        codelist = self.module.splittedSource
        # and now take into account the trailing backslashes
        while (codelist[start+length].strip() and
               codelist[start+length].strip()[-1] == '\\'):
            length += 1
        snip = codelist[start:start+length+1]
        return '\n'.join(snip)


class PyMethod(PyFunction):
    """ Handles methods inside classes

    Basically just a copy of PyFunction.
    """
    typename = 'method'


class PyClass(PyCodeElement):
    """ Handles classes
    """
    methods = {}
    module = None
    typename = 'Class'

    def __init__(self, code, module):
        """ Simple init function

        Calls buildMethods() to extract the class's methods.
        """
        PyCodeElement.__init__(self, code, module)
        self.methods = {}
        self.name = code.co_name
        self.module = module
        self.buildMethods()

    def buildMethods(self):
        """ Extract the class's methods
        """
        methods = [o for o in self.code.co_consts if type(o) == types.CodeType]
        for m in methods:
            name = m.co_name
            self.methods[name] = PyMethod(m, self.module)

    def printit(self):
        # Unused right now
        print '======================================='
        print self.typename, ':', self.name
        print '======================================='
        for m in self.methods.values():
            m.printit()

    def getProtectedSection(self, section):
        """ Pass this request through to the containing module
        """
        return self.module.getProtectedSection(section)

    def getMethodNames(self):
        """ Return the names of the class's methods
        """
        return self.methods.keys()

    def getDocumentation(self):
        """ Return the docstring of the class

        If there's class documentation, it is the very first part of
        the class. Get it. Then test it.
        """
        try:
            candidate = self.code.co_consts[0]
        except:
            return ''
        firstLine = self.code.co_firstlineno
        # check in code...
        if self.module.isItAComment(firstLine):
            return candidate
        else:
            return ''

    def getProtectionDeclaration(self, method):
        """ Try and find a protectiondeclaration for a method

        Currently it's a brute-force string matching in module's list
        of protection declarations.
        """
        for declaration in self.module.protectionDeclarations:
            if method in declaration:
                return declaration
        return ''

if __name__=='__main__':
    mod = PyModule(sys.argv[1])
    mod.printit()

