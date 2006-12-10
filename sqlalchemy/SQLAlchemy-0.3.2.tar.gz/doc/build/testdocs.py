import sys
sys.path = ['../../lib', './lib/'] + sys.path

import os
import re
import doctest
import sqlalchemy.util as util
import sqlalchemy.logging as salog
import logging

salog.default_enabled=True
rootlogger = logging.getLogger('sqlalchemy')
rootlogger.setLevel(logging.NOTSET)
class MyStream(object):
    def write(self, string):
        sys.stdout.write(string)
        sys.stdout.flush()
    def flush(self):
        pass
handler = logging.StreamHandler(MyStream())
handler.setFormatter(logging.Formatter('%(message)s'))
rootlogger.addHandler(handler)


def teststring(s, name, globs=None, verbose=None, report=True, 
               optionflags=0, extraglobs=None, raise_on_error=False, 
               parser=doctest.DocTestParser()):

    from doctest import DebugRunner, DocTestRunner, master

    # Assemble the globals.
    if globs is None:
        globs = {}
    else:
        globs = globs.copy()
    if extraglobs is not None:
        globs.update(extraglobs)

    if raise_on_error:
        runner = DebugRunner(verbose=verbose, optionflags=optionflags)
    else:
        runner = DocTestRunner(verbose=verbose, optionflags=optionflags)

    test = parser.get_doctest(s, globs, name, name, 0)
    runner.run(test)

    if report:
        runner.summarize()

    if master is None:
        master = runner
    else:
        master.merge(runner)

    return runner.failures, runner.tries

def replace_file(s, newfile):
    engine = r"'(sqlite|postgres|mysql):///.*'"
    engine = re.compile(engine, re.MULTILINE)
    s, n = re.subn(engine, "'sqlite:///" + newfile + "'", s)
    if not n:
        raise ValueError("Couldn't find suitable create_engine call to replace '%s' in it" % oldfile)
    return s

filename = 'content/tutorial.txt'
s = open(filename).read()
s = replace_file(s, ':memory:')
teststring(s, filename)

