"""This script installs a Zope instance with Silva in it.
"""

import os
import sys
import copy
import tempfile

import ploneenv.main

parser = copy.deepcopy(ploneenv.main.parser)
parser.usage = '%%prog [OPTIONS] NEW_DIRECTORY\n\n%s' % __doc__

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    options, args = parser.parse_args(args)
    if not args or len(args) > 1:
        raise ploneenv.main.BadCommand("You must provide a single output directory")
    options.output_dir = args[0]
    
    if options.mkzopeinstance is None:
        parser.error("You must provide the path to the "
                     "mkzopeinstance.py script using the --mkzo option.")
    
    ploneenv.main.verbose = options.verbose

    if not options.requirements and not options.no_requirements:
        f = tempfile.NamedTemporaryFile()
        f.write('Silva')
        f.flush()
        options.requirements = [f.name]

    ploneenv.main.make_zope_instance(options)
    ploneenv.main.make_working_env(options)

    print
    print "silvainstall: Success!  You can now start your Zope using "
    print "    %s/bin/zopectl start" % options.output_dir

if __name__ == '__main__':
    main()

