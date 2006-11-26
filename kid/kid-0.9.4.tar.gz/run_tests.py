#!/usr/bin/env python

"""Runs the suite of Kid tests.

For best results, run with py.test as follows:

    py.test -xl

Or run with nose using the following command:

    nosetests -xd

py.test and nose provide nicer tracebacks and inspect variables
when assertions fail. You can also run this test suite directly by:

   python run_tests.py -x

You can omit the -x option in all of the above commands if you do
not want the testing to stop after the first failed test.

"""

import sys
from os.path import dirname, abspath, join as joinpath

if __name__ == '__main__':
    __file__ = sys.argv[0]
base_dir = abspath(dirname(__file__))
if not base_dir in sys.path:
    sys.path.insert(1, base_dir)
test_dir = joinpath(base_dir, 'test')

import kid.test
kid.test.template_package = 'test.'
kid.test.template_dir = test_dir
kid.test.output_dir = test_dir

def run_suite(args):
    kid.test.run_suite(args)

if __name__ == '__main__':
    run_suite(sys.argv[1:])
