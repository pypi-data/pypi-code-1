# -*- coding: utf-8 -*-

# Copyright � 2006 Steven J. Bethard <steven.bethard@gmail.com>.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted under the terms of the 3-clause BSD
# license. No warranty expressed or implied.
# For details, see the accompanying file LICENSE.txt.

import os
import StringIO
import sys
import textwrap
import tempfile
import unittest

import argparse

class Sig(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class NS(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        sorted_items = sorted(self.__dict__.items())
        kwarg_str = ', '.join('%s=%r' % tup for tup in sorted_items)
        return '%s(%s)' % (type(self).__name__, kwarg_str)

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __ne__(self, other):
        return not (self == other)

class ArgumentParserError(Exception):
    def __init__(self, message, error_code):
        Exception.__init__(self, message)
        self.message = message
        self.error_code = error_code

def stderr_to_parser_error(func, *args, **kwargs):
    # if this is being called recursively and stderr is already being
    # redirected, simply call the function and let the enclosing function
    # catch the exception
    if isinstance(sys.stderr, StringIO.StringIO):
        return func(*args, **kwargs)

    # if this is not being called recursively, redirect stderr and
    # use it as the ArgumentParserError message
    old_stderr = sys.stderr
    sys.stderr = StringIO.StringIO()
    try:
        try:
            return func(*args, **kwargs)
        except SystemExit, err:
            message = sys.stderr.getvalue()
            raise ArgumentParserError(message, err.code)
    finally:
        sys.stderr = old_stderr

class ErrorRaisingArgumentParser(argparse.ArgumentParser):
    def parse_args(self, *args, **kwargs):
        parse_args = super(ErrorRaisingArgumentParser, self).parse_args
        return stderr_to_parser_error(parse_args, *args, **kwargs)

    def exit(self, *args, **kwargs):
        exit = super(ErrorRaisingArgumentParser, self).exit
        return stderr_to_parser_error(exit, *args, **kwargs)
        
    def error(self, *args, **kwargs):
        error = super(ErrorRaisingArgumentParser, self).error
        return stderr_to_parser_error(error, *args, **kwargs)
        

class ParserTesterMetaclass(type):
    """Adds parser tests using the class attributes.

    Classes of this type should specify the following attributes:
    
    argument_signatures -- a list of Sig objects which specify
        the signatures of Argument objects to be created
    failures -- a list of args lists that should cause the parser
        to fail
    successes -- a list of (initial_args, options, remaining_args) tuples
        where initial_args specifies the string args to be parsed,
        options is a dict that should match the vars() of the options
        parsed out of initial_args, and remaining_args should be any
        remaining unparsed arguments
    """

    def __init__(cls, *args):

        # default parser signature is empty
        cls.parser_signature = Sig()

        # ---------------------------------------
        # functions for adding optional arguments
        # ---------------------------------------

        def no_groups(parser, argument_signatures):
            """Add all arguments directly to the parser"""
            for sig in argument_signatures:
                parser.add_argument(*sig.args, **sig.kwargs)
            
        def one_group(parser, argument_signatures):
            """Add all arguments under a single group in the parser"""
            group = parser.add_argument_group('foo')
            for sig in argument_signatures:
                group.add_argument(*sig.args, **sig.kwargs)

        def many_groups(parser, argument_signatures):
            """Add each argument in its own group to the parser"""
            for i, sig in enumerate(argument_signatures):
                group = parser.add_argument_group('foo:%i' % i)
                group.add_argument(*sig.args, **sig.kwargs)

        # --------------------------
        # functions for parsing args
        # --------------------------

        def listargs(parser, args):
            """Parse the args by passing in a list"""
            return parser.parse_args(args)

        def sysargs(parser, args):
            """Parse the args by defaulting to sys.argv"""
            old_sys_argv = sys.argv
            sys.argv = [old_sys_argv[0]] + args
            try:
                return parser.parse_args()
            finally:
                sys.argv = old_sys_argv

        # class that holds the combination of one optional argument
        # addition method and one arg parsing method
        class AddTests(object):
            def __init__(self, tester_cls, add_arguments, parse_args):
                self._add_arguments = add_arguments
                self._parse_args = parse_args

                add_arguments_name = self._add_arguments.__name__
                parse_args_name = self._parse_args.__name__
                for test_func in [self.test_failures, self.test_successes]:
                    func_name = test_func.__name__
                    names = func_name, add_arguments_name, parse_args_name
                    test_name = '_'.join(names)
                    def wrapper(self, test_func=test_func):
                        test_func(self)
                    wrapper.__name__ = test_name
                    setattr(tester_cls, test_name, wrapper)

            def _get_parser(self, tester):
                args = tester.parser_signature.args
                kwargs = tester.parser_signature.kwargs
                parser = ErrorRaisingArgumentParser(*args, **kwargs)
                self._add_arguments(parser, tester.argument_signatures)
                return parser

            def test_failures(self, tester):
                parser = self._get_parser(tester)
                for args_str in tester.failures:
                    args = args_str.split()
                    raises = tester.assertRaises
                    raises(ArgumentParserError, parser.parse_args, args)

            def test_successes(self, tester):
                parser = self._get_parser(tester)
                for args_str, expected_ns in tester.successes:
                    args = args_str.split()
                    result_ns = self._parse_args(parser, args)
                    tester.assertEqual(expected_ns, result_ns)

        # add tests for each combination of an optionals adding method
        # and an arg parsing method
        for add_arguments in [no_groups, one_group, many_groups]:
            for parse_args in [listargs, sysargs]:
                AddTests(cls, add_arguments, parse_args)


# ============
# Optional tests
# ============

class TestOptionalsShort(unittest.TestCase):
    """Test an Optional with a short opt string"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('-x')]
    failures = ['-x', 'a', '--foo', '-x --foo', '-x -y']
    successes = [
        ('', NS(x=None)),
        ('-x a', NS(x='a')),
        ('-xa', NS(x='a')),
        ('-x -1', NS(x='-1')),
        ('-x-1', NS(x='-1')),
    ]

class TestOptionalsNumeric(unittest.TestCase):
    """Test an Optional with a short opt string"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('-1', dest='one')]
    failures = ['-1', 'a', '--foo', '-1 --foo', '-1 -y', '-1 -1']
    successes = [
        ('', NS(one=None)),
        ('-1 a', NS(one='a')),
        ('-1a', NS(one='a')),
        ('-1 -2', NS(one='-2')),
        ('-1-2', NS(one='-2')),
    ]

class TestOptionalsLong(unittest.TestCase):
    """Test an Optional with a long opt string"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('--foo')]
    failures = ['--foo', '-f', '-f a', 'a', '--foo -x', '--foo --bar']
    successes = [
        ('', NS(foo=None)),
        ('--foo a', NS(foo='a')),
        ('--foo=a', NS(foo='a')),
        ('--foo -2.5', NS(foo='-2.5')),
        ('--foo=-2.5', NS(foo='-2.5')),
    ]

class TestOptionalsLongPartialMatch(unittest.TestCase):
    """Tests partial matching of an Optional with a long opt string"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('--badger', action='store_true'),
        Sig('--bat')
    ]
    failures = ['--bar', '--b', '--ba', '--b=2', '--ba=4', '--badge 5']
    successes = [
        ('',         NS(badger=False, bat=None)),
        ('--bat X',  NS(badger=False, bat='X' )),
        ('--bad',    NS(badger=True, bat=None)),
        ('--badg',   NS(badger=True, bat=None)),
        ('--badge',  NS(badger=True, bat=None)),
        ('--badger', NS(badger=True, bat=None)),
    ]


class TestOptionalsShortLong(unittest.TestCase):
    """Test an Optional with short and long opt strings"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('-v', '--verbose', '-n', '--noisy', action='store_true')
    ]
    failures = ['--x --verbose', '-N', 'a', '-v x']
    successes = [
        ('', NS(verbose=False)),
        ('-v', NS(verbose=True)),
        ('--verbose', NS(verbose=True)),
        ('-n', NS(verbose=True)),
        ('--noisy', NS(verbose=True)),
    ]

class TestOptionalsDest(unittest.TestCase):
    """Tests various means of setting destination"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('--foo-bar'), Sig('--baz', dest='zabbaz')]
    failures = ['a']
    successes = [
        ('--foo-bar f', NS(foo_bar='f', zabbaz=None)),
        ('--baz g', NS(foo_bar=None, zabbaz='g')),
        ('--foo-bar h --baz i', NS(foo_bar='h', zabbaz='i')),
        ('--baz j --foo-bar k', NS(foo_bar='k', zabbaz='j')),
    ]

class TestOptionalsDefault(unittest.TestCase):
    """Tests specifying a default for an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('-x'), Sig('-y', default=42)]
    failures = ['a']
    successes = [
        ('', NS(x=None, y=42)),
        ('-xx', NS(x='x', y=42)),
        ('-yy', NS(x=None, y='y')),
    ]

class TestOptionalsNargsDefault(unittest.TestCase):
    """Tests not specifying the number of args for an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('-x')]
    failures = ['a', '-x']
    successes = [
        ('', NS(x=None)),
        ('-x a', NS(x='a')),
    ]

class TestOptionalsNargs1(unittest.TestCase):
    """Tests specifying the 1 arg for an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('-x', nargs=1)]
    failures = ['a', '-x']
    successes = [
        ('', NS(x=None)),
        ('-x a', NS(x=['a'])),
    ]

class TestOptionalsNargs3(unittest.TestCase):
    """Tests specifying the 3 args for an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('-x', nargs=3)]
    failures = ['a', '-x', '-x a', '-x a b', 'a -x', 'a -x b']
    successes = [
        ('', NS(x=None)),
        ('-x a b c', NS(x=['a', 'b', 'c'])),
    ]

class TestOptionalsNargsOptional(unittest.TestCase):
    """Tests specifying an Optional arg for an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('-w', nargs='?'),
        Sig('-x', nargs='?', const=42),
        Sig('-y', nargs='?', default='spam'),
        Sig('-z', nargs='?', type=int, const='42', default='84'),
    ]
    failures = ['2']
    successes = [
        ('',     NS(w=None, x=None, y='spam', z=84)),
        ('-w',   NS(w=None, x=None, y='spam', z=84)),
        ('-w 2', NS(w='2',  x=None, y='spam', z=84)),
        ('-x',   NS(w=None, x=42,   y='spam', z=84)),
        ('-x 2', NS(w=None, x='2',  y='spam', z=84)),
        ('-y',   NS(w=None, x=None, y=None,   z=84)),
        ('-y 2', NS(w=None, x=None, y='2',    z=84)),
        ('-z',   NS(w=None, x=None, y='spam', z=42)),
        ('-z 2', NS(w=None, x=None, y='spam', z=2 )),
    ]

class TestOptionalsNargsZeroOrMore(unittest.TestCase):
    """Tests specifying an args for an Optional that accepts zero or more"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('-x', nargs='*'),
        Sig('-y', nargs='*', default='spam'),
    ]
    failures = ['a']
    successes = [
        ('',       NS(x=None,       y='spam'    )),
        ('-x',     NS(x=[],         y='spam'    )),
        ('-x a',   NS(x=['a'],      y='spam'    )),
        ('-x a b', NS(x=['a', 'b'], y='spam'    )),
        ('-y',     NS(x=None,       y=[]        )),
        ('-y a',   NS(x=None,       y=['a']     )),
        ('-y a b', NS(x=None,       y=['a', 'b'])),
    ]

class TestOptionalsNargsOneOrMore(unittest.TestCase):
    """Tests specifying an args for an Optional that accepts one or more"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('-x', nargs='+'),
        Sig('-y', nargs='+', default='spam'),
    ]
    failures = ['a', '-x', '-y', 'a -x', 'a -y b']
    successes = [
        ('',       NS(x=None,       y='spam'    )),
        ('-x a',   NS(x=['a'],      y='spam'    )),
        ('-x a b', NS(x=['a', 'b'], y='spam'    )),
        ('-y a',   NS(x=None,       y=['a']     )),
        ('-y a b', NS(x=None,       y=['a', 'b'])),
    ]

class TestOptionalsChoices(unittest.TestCase):
    """Tests specifying the choices for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('-f', choices='abc'),
        Sig('-g', type=int, choices=range(5))]
    failures = ['a', '-f d', '-fad', '-ga', '-g 6']
    successes = [
        ('', NS(f=None, g=None)),
        ('-f a', NS(f='a', g=None)),
        ('-f c', NS(f='c', g=None)),
        ('-g 0', NS(f=None, g=0)),
        ('-g 03', NS(f=None, g=3)),
        ('-fb -g4', NS(f='b', g=4)),
    ]

class TestOptionalsRequired(unittest.TestCase):    
    """Tests the an optional action that is required"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('-x', type=int, required=True),
    ]
    failures = ['a', '']
    successes = [
        ('-x 1', NS(x=1)),
        ('-x42', NS(x=42)),
    ]

class TestOptionalsActionStore(unittest.TestCase):
    """Tests the store action for an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('-x', action='store')]
    failures = ['a', 'a -x']
    successes = [
        ('', NS(x=None)),
        ('-xfoo', NS(x='foo')),
    ]

class TestOptionalsActionStoreConst(unittest.TestCase):
    """Tests the store_const action for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('-y', action='store_const', const=object)]
    failures = ['a']
    successes = [
        ('', NS(y=None)),
        ('-y', NS(y=object)),
    ]

class TestOptionalsActionStoreFalse(unittest.TestCase):
    """Tests the store_false action for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('-z', action='store_false')]
    failures = ['a', '-za', '-z a']
    successes = [
        ('', NS(z=True)),
        ('-z', NS(z=False)),
    ]

class TestOptionalsActionStoreTrue(unittest.TestCase):
    """Tests the store_true action for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('--apple', action='store_true')]
    failures = ['a', '--apple=b', '--apple b']
    successes = [
        ('', NS(apple=False)),
        ('--apple', NS(apple=True)),
    ]

class TestOptionalsActionAppend(unittest.TestCase):
    """Tests the append action for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('--baz', action='append')]
    failures = ['a', '--baz', 'a --baz', '--baz a b']
    successes = [
        ('', NS(baz=None)),
        ('--baz a', NS(baz=['a'])),
        ('--baz a --baz b', NS(baz=['a', 'b'])),
    ]

class TestOptionalsActionAppendConst(unittest.TestCase):
    """Tests the append_const action for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('-b', action='append_const', const=Exception),
        Sig('-c', action='append', dest='b')
    ]
    failures = ['a', '-c', 'a -c', '-bx', '-b x']
    successes = [
        ('', NS(b=None)),
        ('-b', NS(b=[Exception])),
        ('-b -cx -b -cyz', NS(b=[Exception, 'x', Exception, 'yz'])),
    ]

class TestOptionalsActionCount(unittest.TestCase):
    """Tests the count action for an Optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('-x', action='count')]
    failures = ['a', '-x a', '-x b', '-x a -x b']
    successes = [
        ('', NS(x=None)),
        ('-x', NS(x=1)),
    ]


# ================
# Positional tests
# ================

class TestPositionalsNargsNone(unittest.TestCase):
    """Test a Positional that doesn't specify nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo')]
    failures = ['', '-x', 'a b']
    successes = [
        ('a', NS(foo='a')),
    ]

class TestPositionalsNargs1(unittest.TestCase):
    """Test a Positional that specifies an nargs of 1"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo', nargs=1)]
    failures = ['', '-x', 'a b']
    successes = [
        ('a', NS(foo=['a'])),
    ]

class TestPositionalsNargs2(unittest.TestCase):
    """Test a Positional that specifies an nargs of 2"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo', nargs=2)]
    failures = ['', 'a', '-x', 'a b c']
    successes = [
        ('a b', NS(foo=['a', 'b'])),
    ]

class TestPositionalsNargsZeroOrMore(unittest.TestCase):
    """Test a Positional that specifies unlimited nargs"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo', nargs='*')]
    failures = ['-x']
    successes = [
        ('', NS(foo=[])),
        ('a', NS(foo=['a'])),
        ('a b', NS(foo=['a', 'b'])),
    ]

class TestPositionalsNargsZeroOrMoreDefault(unittest.TestCase):
    """Test a Positional that specifies unlimited nargs and a default"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo', nargs='*', default='bar')]
    failures = ['-x']
    successes = [
        ('', NS(foo='bar')),
        ('a', NS(foo=['a'])),
        ('a b', NS(foo=['a', 'b'])),
    ]

class TestPositionalsNargsOneOrMore(unittest.TestCase):
    """Test a Positional that specifies one or more nargs"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo', nargs='+')]
    failures = ['', '-x']
    successes = [
        ('a', NS(foo=['a'])),
        ('a b', NS(foo=['a', 'b'])),
    ]

class TestPositionalsNargsOptional(unittest.TestCase):
    """Tests an Optional Positional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='?')]
    failures = ['-x', 'a b']
    successes = [
        ('', NS(foo=None)),
        ('a', NS(foo='a')),
    ]

class TestPositionalsNargsOptionalDefault(unittest.TestCase):
    """Tests an Optional Positional with a default value"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='?', default=42)]
    failures = ['-x', 'a b']
    successes = [
        ('', NS(foo=42)),
        ('a', NS(foo='a')),
    ]

class TestPositionalsNargsOptionalConvertedDefault(unittest.TestCase):
    """Tests an Optional Positional with a default value
    __metaclass__ = ParserTesterMetaclass
    that needs to be converted to the appropriate type.
    """

    argument_signatures = [
        Sig('foo', nargs='?', type=int, default='42')
    ]
    failures = ['-x', 'a b', '1 2']
    successes = [
        ('', NS(foo=42)),
        ('1', NS(foo=1)),
    ]

class TestPositionalsNargsNoneNone(unittest.TestCase):
    """Test two Positionals that don't specify nargs"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo'), Sig('bar')]
    failures = ['', '-x', 'a', 'a b c']
    successes = [
        ('a b', NS(foo='a', bar='b')),
    ]

class TestPositionalsNargsNone1(unittest.TestCase):
    """Test a Positional with no nargs followed by one with 1"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo'), Sig('bar', nargs=1)]
    failures = ['', '--foo', 'a', 'a b c']
    successes = [
        ('a b', NS(foo='a', bar=['b'])),
    ]

class TestPositionalsNargs2None(unittest.TestCase):
    """Test a Positional with 2 nargs followed by one with none"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs=2), Sig('bar')]
    failures = ['', '--foo', 'a', 'a b', 'a b c d']
    successes = [
        ('a b c', NS(foo=['a', 'b'], bar='c')),
    ]

class TestPositionalsNargsNoneZeroOrMore(unittest.TestCase):
    """Test a Positional with no nargs followed by one with unlimited"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo'), Sig('bar', nargs='*')]
    failures = ['', '--foo']
    successes = [
        ('a', NS(foo='a', bar=[])),
        ('a b', NS(foo='a', bar=['b'])),
        ('a b c', NS(foo='a', bar=['b', 'c'])),
    ]

class TestPositionalsNargsNoneOneOrMore(unittest.TestCase):
    """Test a Positional with no nargs followed by one with one or more"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo'), Sig('bar', nargs='+')]
    failures = ['', '--foo', 'a']
    successes = [
        ('a b', NS(foo='a', bar=['b'])),
        ('a b c', NS(foo='a', bar=['b', 'c'])),
    ]

class TestPositionalsNargsNoneOptional(unittest.TestCase):
    """Test a Positional with no nargs followed by one with an Optional"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('foo'), Sig('bar', nargs='?')]
    failures = ['', '--foo', 'a b c']
    successes = [
        ('a', NS(foo='a', bar=None)),
        ('a b', NS(foo='a', bar='b')),
    ]


class TestPositionalsNargsZeroOrMoreNone(unittest.TestCase):
    """Test a Positional with unlimited nargs followed by one with none"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='*'), Sig('bar')]
    failures = ['', '--foo']
    successes = [
        ('a', NS(foo=[], bar='a')),
        ('a b', NS(foo=['a'], bar='b')),
        ('a b c', NS(foo=['a', 'b'], bar='c')),
    ]
    
class TestPositionalsNargsOneOrMoreNone(unittest.TestCase):
    """Test a Positional with one or more nargs followed by one with none"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='+'), Sig('bar')]
    failures = ['', '--foo', 'a']
    successes = [
        ('a b', NS(foo=['a'], bar='b')),
        ('a b c', NS(foo=['a', 'b'], bar='c')),
    ]
    
class TestPositionalsNargsOptionalNone(unittest.TestCase):
    """Test a Positional with an Optional nargs followed by one with none"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='?', default=42), Sig('bar')]
    failures = ['', '--foo', 'a b c']
    successes = [
        ('a', NS(foo=42, bar='a')),
        ('a b', NS(foo='a', bar='b')),
    ]
    
class TestPositionalsNargs2ZeroOrMore(unittest.TestCase):
    """Test a Positional with 2 nargs followed by one with unlimited"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs=2), Sig('bar', nargs='*')]
    failures = ['', '--foo', 'a']
    successes = [
        ('a b', NS(foo=['a', 'b'], bar=[])),
        ('a b c', NS(foo=['a', 'b'], bar=['c'])),
    ]

class TestPositionalsNargs2OneOrMore(unittest.TestCase):
    """Test a Positional with 2 nargs followed by one with one or more"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs=2), Sig('bar', nargs='+')]
    failures = ['', '--foo', 'a', 'a b']
    successes = [
        ('a b c', NS(foo=['a', 'b'], bar=['c'])),
    ]

class TestPositionalsNargs2Optional(unittest.TestCase):
    """Test a Positional with 2 nargs followed by one optional"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs=2), Sig('bar', nargs='?')]
    failures = ['', '--foo', 'a', 'a b c d']
    successes = [
        ('a b', NS(foo=['a', 'b'], bar=None)),
        ('a b c', NS(foo=['a', 'b'], bar='c')),
    ]

class TestPositionalsNargsZeroOrMore1(unittest.TestCase):
    """Test a Positional with unlimited nargs followed by one with 1"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='*'), Sig('bar', nargs=1)]
    failures = ['', '--foo', ]
    successes = [
        ('a', NS(foo=[], bar=['a'])),
        ('a b', NS(foo=['a'], bar=['b'])),
        ('a b c', NS(foo=['a', 'b'], bar=['c'])),
    ]

class TestPositionalsNargsOneOrMore1(unittest.TestCase):
    """Test a Positional with one or more nargs followed by one with 1"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='+'), Sig('bar', nargs=1)]
    failures = ['', '--foo', 'a']
    successes = [
        ('a b', NS(foo=['a'], bar=['b'])),
        ('a b c', NS(foo=['a', 'b'], bar=['c'])),
    ]

class TestPositionalsNargsOptional1(unittest.TestCase):
    """Test a Positional with an Optional nargs followed by one with 1"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='?'), Sig('bar', nargs=1)]
    failures = ['', '--foo', 'a b c']
    successes = [
        ('a', NS(foo=None, bar=['a'])),
        ('a b', NS(foo='a', bar=['b'])),
    ]

class TestPositionalsNargsNoneZeroOrMore1(unittest.TestCase):
    """Test three Positionals: no nargs, unlimited nargs and 1 nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('foo'),
        Sig('bar', nargs='*'),
        Sig('baz', nargs=1),
    ]
    failures = ['', '--foo', 'a']
    successes = [
        ('a b', NS(foo='a', bar=[], baz=['b'])),
        ('a b c', NS(foo='a', bar=['b'], baz=['c'])),
    ]
    
class TestPositionalsNargsNoneOneOrMore1(unittest.TestCase):
    """Test three Positionals: no nargs, one or more nargs and 1 nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('foo'),
        Sig('bar', nargs='+'),
        Sig('baz', nargs=1),
    ]
    failures = ['', '--foo', 'a', 'b']
    successes = [
        ('a b c', NS(foo='a', bar=['b'], baz=['c'])),
        ('a b c d', NS(foo='a', bar=['b', 'c'], baz=['d'])),
    ]
    
class TestPositionalsNargsNoneOptional1(unittest.TestCase):
    """Test three Positionals: no nargs, optional narg and 1 nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('foo'),
        Sig('bar', nargs='?', default=0.625),
        Sig('baz', nargs=1),
    ]
    failures = ['', '--foo', 'a']
    successes = [
        ('a b', NS(foo='a', bar=0.625, baz=['b'])),
        ('a b c', NS(foo='a', bar='b', baz=['c'])),
    ]

class TestPositionalsNargsOptionalOptional(unittest.TestCase):
    """Test two optional nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [
        Sig('foo', nargs='?'),
        Sig('bar', nargs='?', default=42),
    ]
    failures = ['--foo', 'a b c']
    successes = [
        ('', NS(foo=None, bar=42)),
        ('a', NS(foo='a', bar=42)),
        ('a b', NS(foo='a', bar='b')),
    ]

class TestPositionalsNargsOptionalZeroOrMore(unittest.TestCase):
    """Test an Optional narg followed by unlimited nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='?'), Sig('bar', nargs='*')]
    failures = ['--foo']
    successes = [
        ('', NS(foo=None, bar=[])),
        ('a', NS(foo='a', bar=[])),
        ('a b', NS(foo='a', bar=['b'])),
        ('a b c', NS(foo='a', bar=['b', 'c'])),
    ]

class TestPositionalsNargsOptionalOneOrMore(unittest.TestCase):
    """Test an Optional narg followed by one or more nargs"""
    __metaclass__ = ParserTesterMetaclass

    argument_signatures = [Sig('foo', nargs='?'), Sig('bar', nargs='+')]
    failures = ['', '--foo']
    successes = [
        ('a', NS(foo=None, bar=['a'])),
        ('a b', NS(foo='a', bar=['b'])),
        ('a b c', NS(foo='a', bar=['b', 'c'])),
    ]

class TestPositionalsChoicesString(unittest.TestCase):
    """Test a set of single-character choices"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('spam', choices=set('abcdefg'))]
    failures = ['', '--foo', 'h', '42', 'ef']
    successes = [
        ('a', NS(spam='a')),
        ('g', NS(spam='g')),
    ]

class TestPositionalsChoicesInt(unittest.TestCase):
    """Test a set of integer choices"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('spam', type=int, choices=range(20))]
    failures = ['', '--foo', 'h', '42', 'ef']
    successes = [
        ('4', NS(spam=4)),
        ('15', NS(spam=15)),
    ]

class TestPositionalsActionAppend(unittest.TestCase):
    """Test the 'append' action"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('spam', action='append'),
        Sig('spam', action='append', nargs=2),
    ]
    failures = ['', '--foo', 'a', 'a b', 'a b c d']
    successes = [
        ('a b c', NS(spam=['a', ['b', 'c']])),
    ]

# ========================================
# Combined optionals and positionals tests
# ========================================

class TestNargsZeroOrMore(unittest.TestCase):
    """Tests specifying an args for an Optional that accepts zero or more"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [Sig('-x', nargs='*'), Sig('y', nargs='*')]
    failures = []
    successes = [
        ('',          NS(x=None,  y=[])),
        ('-x',        NS(x=[],    y=[])),
        ('-x a',      NS(x=['a'], y=[])),
        ('-x a -- b', NS(x=['a'], y=['b'])),
        ('a',         NS(x=None,  y=['a'])),
        ('a -x',      NS(x=[],    y=['a'])),
        ('a -x b',    NS(x=['b'], y=['a'])),
    ]

class TestOptionLike(unittest.TestCase):
    """Tests options that may or may not be arguments"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('-x', type=float),
        Sig('-3', type=float, dest='y'),
        Sig('z', nargs='*'),
    ]
    failures = ['-x', '-y2.5', '-xa', '-x -a',
                '-x -3', '-x -3.5', '-3 -3.5']
    successes = [
        ('',          NS(x=None, y=None, z=[])),
        ('-x -2.5',   NS(x=-2.5, y=None, z=[])),
        ('-x -2.5 a', NS(x=-2.5, y=None, z=['a'])),
        ('-3.5',      NS(x=None, y=0.5,  z=[])),
        ('-3-.5',     NS(x=None, y=-0.5, z=[])),
        ('-3 -.5',    NS(x=None, y=-0.5, z=[])),
        ('a -3.5',    NS(x=None, y=0.5,  z=['a'])),
        ('a',         NS(x=None, y=None, z=['a'])),
        ('a -x -1',   NS(x=-1,   y=None, z=['a'])),
        ('-x -1 a',   NS(x=-1,   y=None, z=['a'])),
        ('-3 -1 a',   NS(x=None, y=-1.0, z=['a'])),
    ]

# =====================
# Type conversion tests
# =====================

class TempDirMixin(object):

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.old_dir = os.getcwd()
        os.chdir(self.temp_dir)

    def tearDown(self):
        os.chdir(self.old_dir)
        for filename in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, filename))
        os.rmdir(self.temp_dir)

class TestFileTypeR(TempDirMixin, unittest.TestCase):
    """Test the FileType option/argument type for reading files"""
    __metaclass__ = ParserTesterMetaclass

    def setUp(self):
        super(TestFileTypeR, self).setUp()
        for file_name in ['foo', 'bar']:
            file = open(os.path.join(self.temp_dir, file_name), 'w')
            file.write(file_name)
            file.close()

    class RFile(object):
        def __init__(self, name):
            self.name = name
        def __eq__(self, other):
            text = other.read()
            return self.name == text and self.name == other.name

    argument_signatures = [
        Sig('-x', type=argparse.FileType()),
        Sig('spam', type=argparse.FileType('r')),
    ]
    failures = ['-x', '-x bar']
    successes = [
        ('foo', NS(x=None, spam=RFile('foo'))),
        ('-x foo bar', NS(x=RFile('foo'), spam=RFile('bar'))),
        ('bar -x foo', NS(x=RFile('foo'), spam=RFile('bar'))),
        ('-x - -', NS(x=sys.stdin, spam=sys.stdin))
    ]

class TestFileTypeW(TempDirMixin, unittest.TestCase):
    """Test the FileType option/argument type for writing files"""
    __metaclass__ = ParserTesterMetaclass

    class WFile(object):
        def __init__(self, name):
            self.name = name
        def __eq__(self, other):
            other.write('Check that file is writable.')
            other.close()
            return self.name == other.name

    argument_signatures = [
        Sig('-x', type=argparse.FileType('w')),
        Sig('spam', type=argparse.FileType('w')),
    ]
    failures = ['-x', '-x bar']
    successes = [
        ('foo', NS(x=None, spam=WFile('foo'))),
        ('-x foo bar', NS(x=WFile('foo'), spam=WFile('bar'))),
        ('bar -x foo', NS(x=WFile('foo'), spam=WFile('bar'))),
        ('-x - -', NS(x=sys.stdout, spam=sys.stdout))
    ]

class TestTypeOutfile(TempDirMixin, unittest.TestCase):
    """Test the 'outfile' option/argument type"""
    __metaclass__ = ParserTesterMetaclass

    class Outfile(object):
        def __init__(self, name):
            self.name = name
        def __eq__(self, other):
            other.write('This file should be writable.')
            other.close()
            return self.name == other.name

    argument_signatures = [
        Sig('-x', type='outfile'),
        Sig('spam', type='outfile'),
    ]
    failures = ['-x', '-x bar']
    successes = [
        ('foo', NS(x=None, spam=Outfile('foo'))),
        ('-x foo bar', NS(x=Outfile('foo'), spam=Outfile('bar'))),
        ('bar -x foo', NS(x=Outfile('foo'), spam=Outfile('bar'))),
        ('-x - -', NS(x=sys.stdout, spam=sys.stdout))
    ]

class TestTypeCallable(unittest.TestCase):
    """Test some callables as option/argument types"""
    __metaclass__ = ParserTesterMetaclass
    
    argument_signatures = [
        Sig('--eggs', type=complex),
        Sig('spam', type=float),
    ]
    failures = ['a', '42j', '--eggs a', '--eggs 2i']
    successes = [
        ('--eggs=42 42', NS(eggs=42, spam=42.0)),
        ('--eggs 2j -- -1.5', NS(eggs=2j, spam=-1.5)),
        ('1024.675', NS(eggs=None, spam=1024.675)),
    ]

class TestTypeUserDefined(unittest.TestCase):
    """Test a user-defined option/argument type"""
    __metaclass__ = ParserTesterMetaclass
    
    class MyType(unittest.TestCase):
        def __init__(self, value):
            self.value = value
        def __eq__(self, other):
            return (type(self), self.value) == (type(other), other.value)
    
    def get_my_type(value):
        return TestTypeUserDefined.MyType(value)
    
    argument_signatures = [
        Sig('-x', type=get_my_type),
        Sig('spam', type=get_my_type),
    ]
    failures = []
    successes = [
        ('a -x b', NS(x=MyType('b'), spam=MyType('a'))),
        ('-xf g', NS(x=MyType('f'), spam=MyType('g'))),
    ]

class TestTypeRegistration(unittest.TestCase):
    """Test a user-defined type by registering it"""

    def test(self):

        def get_my_type(string):
            return 'my_type{%s}' % string

        parser = argparse.ArgumentParser()
        parser.register('type', 'my_type', get_my_type)
        parser.add_argument('-x', type='my_type')
        parser.add_argument('y', type='my_type')

        self.assertEqual(parser.parse_args('1'.split()),
                         NS(x=None, y='my_type{1}'))
        self.assertEqual(parser.parse_args('-x 1 42'.split()),
                         NS(x='my_type{1}', y='my_type{42}'))


# ============
# Action tests
# ============

class TestActionUserDefined(unittest.TestCase):
    """Test a user-defined option/argument action"""
    __metaclass__ = ParserTesterMetaclass

    class OptionalAction(argparse.Action):
        def __call__(self, parser, namespace, value, option_string=None):
            try:
                # check destination and option string
                assert self.dest == 'spam', 'dest: %s' % self.dest
                assert option_string == '-s', 'flag: %s' % option_string
                # when option is before argument, badger=2, and when
                # option is after argument, badger=<whatever was set>
                expected_ns = NS(spam=0.25)
                if value in [0.125, 0.625]:
                    expected_ns.badger = 2
                elif value in [2.0]:
                    expected_ns.badger = 84
                else:
                    raise AssertionError('value: %s' % value)
                assert expected_ns == namespace, ('expected %s, got %s' %
                                                  (expected_ns, namespace))
            except AssertionError, e:
                raise ArgumentParserError('opt_action failed: %s' % e)
            setattr(namespace, 'spam', value)

    class PositionalAction(argparse.Action):
        def __call__(self, parser, namespace, value, option_string=None):
            try:
                assert option_string is None, ('option_string: %s' %
                                               option_string)
                # check destination
                assert self.dest == 'badger', 'dest: %s' % self.dest
                # when argument is before option, spam=0.25, and when
                # option is after argument, spam=<whatever was set>
                expected_ns = NS(badger=2)
                if value in [42, 84]:
                    expected_ns.spam = 0.25
                elif value in [1]:
                    expected_ns.spam = 0.625
                elif value in [2]:
                    expected_ns.spam = 0.125
                else:
                    raise AssertionError('value: %s' % value)
                assert expected_ns == namespace, ('expected %s, got %s' %
                                                  (expected_ns, namespace))
            except AssertionError, e:
                raise ArgumentParserError('arg_action failed: %s' % e)
            setattr(namespace, 'badger', value)

    argument_signatures = [
        Sig('-s', dest='spam', action=OptionalAction,
            type=float, default=0.25),
        Sig('badger', action=PositionalAction,
            type=int, nargs='?', default=2)
    ]
    failures = []
    successes = [
        ('-s0.125', NS(spam=0.125, badger=2)),
        ('42', NS(spam=0.25, badger=42)),
        ('-s 0.625 1', NS(spam=0.625, badger=1)),
        ('84 -s2', NS(spam=2.0, badger=84)),
    ]

class TestActionRegistration(unittest.TestCase):
    """Test a user-defined action supplied by registering it"""

    class MyAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, 'foo[%s]' % values)

    def test(self):    

        parser = argparse.ArgumentParser()
        parser.register('action', 'my_action', self.MyAction)
        parser.add_argument('badger', action='my_action')

        self.assertEqual(parser.parse_args(['1']), NS(badger='foo[1]'))
        self.assertEqual(parser.parse_args(['42']), NS(badger='foo[42]'))


# ================
# Subparsers tests
# ================

class TestAddSubparsers(unittest.TestCase):
    """Test the add_subparsers method"""

    def assertArgumentParserError(self, *args, **kwargs):
        self.assertRaises(ArgumentParserError, *args, **kwargs)

    def setUp(self):
        # create a parser with a subparsers argument
        self.parser = ErrorRaisingArgumentParser(
            prog='PROG', description='main description')
        self.parser.add_argument(
            '--foo', action='store_true', help='foo help')
        self.parser.add_argument(
            'bar', type=float, help='bar help')
        subparsers = self.parser.add_subparsers(help='command help')

        # check that only one subparsers argument can be added
        self.assertArgumentParserError(self.parser.add_subparsers)

        # add parsers
        parser1 = subparsers.add_parser('1', description='1 description')
        parser1.add_argument('-w', type=int, help='w help')
        parser1.add_argument('x', choices='abc', help='x help')
        parser2 = subparsers.add_parser('2', description='2 description')
        parser2.add_argument('-y', choices='123', help='y help')
        parser2.add_argument('z', type=complex, nargs='*', help='z help')


    def test_parse_args_failures(self):
        # check some failure cases:
        for args_str in ['', 'a', 'a a', '0.5 a', '0.5 1',
                         '0.5 1 -y', '0.5 2 -w']:
            args = args_str.split()
            self.assertArgumentParserError(self.parser.parse_args, args)

    def test_parse_args(self):
        # check some non-failure cases:
        self.assertEqual(
            self.parser.parse_args('0.5 1 b -w 7'.split()),
            NS(foo=False, bar=0.5, w=7, x='b'),
        )
        self.assertEqual(
            self.parser.parse_args('0.25 --foo 2 -y 2 3j -- -1j'.split()),
            NS(foo=True, bar=0.25, y='2', z=[3j, -1j]),
        )
        self.assertEqual(
            self.parser.parse_args('--foo 0.125 1 c'.split()),
            NS(foo=True, bar=0.125, w=None, x='c'),
        )

    def test_dest(self):
        parser = ErrorRaisingArgumentParser()
        parser.add_argument('--foo', action='store_true')
        subparsers = parser.add_subparsers(dest='bar')
        parser1 = subparsers.add_parser('1')
        parser1.add_argument('baz')
        self.assertEqual(NS(foo=False, bar='1', baz='2'),
                         parser.parse_args('1 2'.split()))

    def test_help(self):
        self.assertEqual(self.parser.format_usage(),
                         'usage: PROG [-h] [--foo] bar {1,2} ...\n')
        self.assertEqual(self.parser.format_help(), textwrap.dedent('''\
            usage: PROG [-h] [--foo] bar {1,2} ...

            main description

            positional arguments:
              bar         bar help
              {1,2}       command help

            optional arguments:
              -h, --help  show this help message and exit
              --foo       foo help
            '''))

    def _test_subparser_help(self, args_str, expected_help):
        try:
            self.parser.parse_args(args_str.split())
        except ArgumentParserError, err:
            if err.message != expected_help:
                print repr(expected_help)
                print repr(err.message)
            self.assertEqual(err.message, expected_help)

    def test_subparser1_help(self):
        self._test_subparser_help('5.0 1 -h', textwrap.dedent('''\
            usage: PROG bar 1 [-h] [-w W] {a,b,c}

            1 description

            positional arguments:
              {a,b,c}     x help

            optional arguments:
              -h, --help  show this help message and exit
              -w W        w help
            '''))

    def test_subparser2_help(self):
        self._test_subparser_help('5.0 2 -h', textwrap.dedent('''\
            usage: PROG bar 2 [-h] [-y {1,2,3}] [z [z ...]]

            2 description

            positional arguments:
              z           z help

            optional arguments:
              -h, --help  show this help message and exit
              -y {1,2,3}  y help
            '''))

# ============                                  
# Groups tests
# ============

class TestPositionalsGroups(unittest.TestCase):
    """Tests that order of group positionals matches construction order"""

    def test_nongroup_first(self):
        parser = ErrorRaisingArgumentParser()
        parser.add_argument('foo')
        group = parser.add_argument_group('g')
        group.add_argument('bar')
        parser.add_argument('baz')
        expected = NS(foo='1', bar='2', baz='3')
        result = parser.parse_args('1 2 3'.split())
        self.failUnlessEqual(expected, result)

    def test_group_first(self):
        parser = ErrorRaisingArgumentParser()
        group = parser.add_argument_group('xxx')
        group.add_argument('foo')
        parser.add_argument('bar')
        parser.add_argument('baz')
        expected = NS(foo='1', bar='2', baz='3')
        result = parser.parse_args('1 2 3'.split())
        self.failUnlessEqual(expected, result)

    def test_interleaved_groups(self):
        parser = ErrorRaisingArgumentParser()
        group = parser.add_argument_group('xxx')
        parser.add_argument('foo')
        group.add_argument('bar')
        parser.add_argument('baz')
        group = parser.add_argument_group('yyy')
        group.add_argument('frell')
        expected = NS(foo='1', bar='2', baz='3', frell='4')
        result = parser.parse_args('1 2 3 4'.split())
        self.failUnlessEqual(expected, result)

# ===================
# Parent parser tests
# ===================

class TestParentParsers(unittest.TestCase):
    """Tests that parsers can be created with parent parsers"""

    def assertArgumentParserError(self, *args, **kwargs):
        self.assertRaises(ArgumentParserError, *args, **kwargs)

    def setUp(self):
        self.wxyz_parent = ErrorRaisingArgumentParser(add_help=False)
        self.wxyz_parent.add_argument('--w')
        x_group = self.wxyz_parent.add_argument_group('x')
        x_group.add_argument('-y')
        self.wxyz_parent.add_argument('z')

        self.abcd_parent = ErrorRaisingArgumentParser(add_help=False)
        self.abcd_parent.add_argument('a')
        self.abcd_parent.add_argument('-b')
        c_group = self.abcd_parent.add_argument_group('c')
        c_group.add_argument('--d')

        self.w_parent = ErrorRaisingArgumentParser(add_help=False)
        self.w_parent.add_argument('--w')

        self.z_parent = ErrorRaisingArgumentParser(add_help=False)
        self.z_parent.add_argument('z')

    def test_single_parent(self):
        parser = ErrorRaisingArgumentParser(
            parents=[self.wxyz_parent])
        self.assertEqual(parser.parse_args('-y 1 2 --w 3'.split()),
                         NS(w='3', y='1', z='2'))

    def test_multiple_parents(self):
        parser = ErrorRaisingArgumentParser(
            parents=[self.abcd_parent, self.wxyz_parent])
        self.assertEqual(parser.parse_args('--d 1 --w 2 3 4'.split()),
                         NS(a='3', b=None, d='1', w='2', y=None, z='4'))

    def test_conflicting_parents(self):
        self.assertRaises(
            argparse.ArgumentError,
            argparse.ArgumentParser,
            parents=[self.w_parent, self.wxyz_parent])

    def test_same_argument_name_parents(self):
        parser = ErrorRaisingArgumentParser(
            parents=[self.wxyz_parent, self.z_parent])
        self.assertEqual(parser.parse_args('1 2'.split()),
                         NS(w=None, y=None, z='2'))

    def test_subparser_parents(self):
        parser = ErrorRaisingArgumentParser()
        subparsers = parser.add_subparsers()
        abcde_parser = subparsers.add_parser(
            'bar', parents=[self.abcd_parent])
        abcde_parser.add_argument('e')
        self.assertEqual(parser.parse_args('bar -b 1 --d 2 3 4'.split()),
                         NS(a='3', b='1', d='2', e='4'))
        
    def test_parent_help(self):
        parser = ErrorRaisingArgumentParser(
            parents=[self.abcd_parent, self.wxyz_parent])
        parser_help = parser.format_help()
        self.assertEqual(parser_help, textwrap.dedent('''\
            usage: test_argparse.py [-h] [-b B] [--w W] [--d D] [-y Y] a z
            
            positional arguments:
              a
              z

            optional arguments:
              -h, --help  show this help message and exit
              -b B
              --w W
            
            c:
              --d D
            
            x:
              -y Y
        '''))
                         
# =================
# Set default tests
# =================

class TestSetDefaults(unittest.TestCase):
    def test_set_defaults_no_args(self):
        parser = ErrorRaisingArgumentParser()
        parser.set_defaults(x='foo')
        parser.set_defaults(y='bar', z=1)
        self.assertEqual(NS(x='foo', y='bar', z=1),
                         parser.parse_args([]))
        self.assertEqual(NS(x='foo', y='bar', z=1),
                         parser.parse_args([], NS()))
        self.assertEqual(NS(x='baz', y='bar', z=1),
                         parser.parse_args([], NS(x='baz')))
        self.assertEqual(NS(x='baz', y='bar', z=2),
                         parser.parse_args([], NS(x='baz', z=2)))

    def test_set_defaults_with_args(self):
        parser = ErrorRaisingArgumentParser()
        parser.set_defaults(x='foo', y='bar')
        parser.add_argument('-x', default='xfoox')
        self.assertEqual(NS(x='xfoox', y='bar'),
                         parser.parse_args([]))
        self.assertEqual(NS(x='xfoox', y='bar'),
                         parser.parse_args([], NS()))
        self.assertEqual(NS(x='baz', y='bar'),
                         parser.parse_args([], NS(x='baz')))
        self.assertEqual(NS(x='1', y='bar'),
                         parser.parse_args('-x 1'.split()))
        self.assertEqual(NS(x='1', y='bar'),
                         parser.parse_args('-x 1'.split(), NS()))
        self.assertEqual(NS(x='1', y='bar'),
                         parser.parse_args('-x 1'.split(), NS(x='baz')))


    def test_set_defaults_subparsers(self):
        parser = ErrorRaisingArgumentParser()
        parser.set_defaults(x='foo')
        subparsers = parser.add_subparsers()
        parser_a = subparsers.add_parser('a')
        parser_a.set_defaults(y='bar')
        self.assertEqual(NS(x='foo', y='bar'),
                         parser.parse_args('a'.split()))
        

    def test_set_defaults_parents(self):
        parent = ErrorRaisingArgumentParser(add_help=False)
        parent.set_defaults(x='foo')
        parser = ErrorRaisingArgumentParser(parents=[parent])
        self.assertEqual(NS(x='foo'), parser.parse_args([]))
        
        

# =====================
# Help formatting tests
# =====================

class TestHelpFormattingMetaclass(type):
    def __init__(cls, *args):

        class AddTests(object):
            def __init__(self, test_class, func_suffix):
                self.func_suffix = func_suffix

                for test_func in [self.test_format,
                                  self.test_print,
                                  self.test_print_file]:
                    test_name = '%s_%s' % (test_func.__name__, func_suffix)
                    def test_wrapper(self, test_func=test_func):
                        test_func(self)
                    test_wrapper.__name__ = test_name
                    setattr(test_class, test_name, test_wrapper)

            def _get_parser(self, tester):
                parser = argparse.ArgumentParser(
                    *tester.parser_signature.args,
                    **tester.parser_signature.kwargs)
                for argument_sig in tester.argument_signatures:
                    parser.add_argument(*argument_sig.args,
                                        **argument_sig.kwargs)
                group_signatures = tester.argument_group_signatures
                for group_sig, argument_sigs in group_signatures:
                    group = parser.add_argument_group(*group_sig.args,
                                                      **group_sig.kwargs)
                    for argument_sig in argument_sigs:
                        group.add_argument(*argument_sig.args,
                                           **argument_sig.kwargs)
                return parser

            def _test(self, tester, parser_text):
                expected_text = getattr(tester, self.func_suffix)
                expected_text = textwrap.dedent(expected_text)
                if expected_text != parser_text:
                    print repr(expected_text)
                    print repr(parser_text)
                    for char1, char2 in zip(expected_text, parser_text):
                        if char1 != char2:
                            print 'first diff: %r %r' % (char1, char2)
                            break
                tester.assertEqual(expected_text, parser_text)

            def test_format(self, tester):
                parser = self._get_parser(tester)
                format = getattr(parser, 'format_%s' % self.func_suffix)
                self._test(tester, format())

            def test_print(self, tester):
                parser = self._get_parser(tester)
                print_ = getattr(parser, 'print_%s' % self.func_suffix)
                oldstderr = sys.stderr
                sys.stderr = StringIO.StringIO()
                try:
                    print_()
                    parser_text = sys.stderr.getvalue()
                finally:
                    sys.stderr = oldstderr
                self._test(tester, parser_text)

            def test_print_file(self, tester):
                parser = self._get_parser(tester)
                print_ = getattr(parser, 'print_%s' % self.func_suffix)
                sfile = StringIO.StringIO()
                print_(sfile)
                parser_text = sfile.getvalue()
                self._test(tester, parser_text)

        # add tests for {format,print}_{usage,help,version}
        for func_suffix in ['usage', 'help', 'version']:
            AddTests(cls, func_suffix)


class TestHelpBiggerOptionals(unittest.TestCase):
    """Make sure that argument help aligns when options are longer"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', description='DESCRIPTION',
                           epilog='EPILOG', version='0.1')
    argument_signatures = [
        Sig('-x', action='store_true', help='X HELP'),
        Sig('--y', help='Y HELP'),
        Sig('foo', help='FOO HELP'),
        Sig('bar', help='BAR HELP'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [-v] [-x] [--y Y] foo bar
        '''
    help = usage + '''\

        DESCRIPTION

        positional arguments:
          foo            FOO HELP
          bar            BAR HELP

        optional arguments:
          -h, --help     show this help message and exit
          -v, --version  show program's version number and exit
          -x             X HELP
          --y Y          Y HELP

        EPILOG
    '''
    version = '''\
        0.1
        '''

class TestHelpBiggerOptionalGroups(unittest.TestCase):
    """Make sure that argument help aligns when options are longer"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', description='DESCRIPTION',
                           epilog='EPILOG', version='0.1')
    argument_signatures = [
        Sig('-x', action='store_true', help='X HELP'),
        Sig('--y', help='Y HELP'),
        Sig('foo', help='FOO HELP'),
        Sig('bar', help='BAR HELP'),
    ]
    argument_group_signatures = [
        (Sig('GROUP TITLE', description='GROUP DESCRIPTION'), [
            Sig('baz', help='BAZ HELP'),
            Sig('-z', nargs='+', help='Z HELP')])
    ]
    usage = '''\
        usage: PROG [-h] [-v] [-x] [--y Y] [-z Z [Z ...]] foo bar baz
        '''
    help = usage + '''\

        DESCRIPTION

        positional arguments:
          foo            FOO HELP
          bar            BAR HELP

        optional arguments:
          -h, --help     show this help message and exit
          -v, --version  show program's version number and exit
          -x             X HELP
          --y Y          Y HELP

        GROUP TITLE:
          GROUP DESCRIPTION

          baz            BAZ HELP
          -z Z [Z ...]   Z HELP
        
        EPILOG
    '''
    version = '''\
        0.1
        '''

class TestHelpBiggerPositionals(unittest.TestCase):
    """Make sure that help aligns when arguments are longer"""
    __metaclass__ = TestHelpFormattingMetaclass
    
    parser_signature = Sig(usage='USAGE', description='DESCRIPTION')
    argument_signatures = [
        Sig('-x', action='store_true', help='X HELP'),
        Sig('--y', help='Y HELP'),
        Sig('ekiekiekifekang', help='EKI HELP'),
        Sig('bar', help='BAR HELP'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: USAGE
        '''
    help = usage + '''\

        DESCRIPTION

        positional arguments:
          ekiekiekifekang  EKI HELP
          bar              BAR HELP

        optional arguments:
          -h, --help       show this help message and exit
          -x               X HELP
          --y Y            Y HELP
        '''

    version = ''

class TestHelpReformatting(unittest.TestCase):
    """Make sure that text after short names starts on the first line"""
    __metaclass__ = TestHelpFormattingMetaclass
    
    parser_signature = Sig(
        prog='PROG',
        description='   oddly    formatted\n'
                    'description\n'
                    '\n'
                    'that is so long that it should go onto multiple '
                    'lines when wrapped')
    argument_signatures = [
        Sig('-x', metavar='XX', help='oddly\n'
                                     '    formatted -x help'),
        Sig('y', metavar='yyy', help='normal y help')
    ]
    argument_group_signatures = [
        (Sig('title', description='\n'
                                  '    oddly formatted group\n'
                                  '\n'
                                  'description'),
         [Sig('-a', action='store_true',
              help=' oddly \n'
                   'formatted    -a  help  \n'
                   '    again, so long that it should be wrapped over '
                   'multiple lines')])
    ]
    usage = '''\
        usage: PROG [-h] [-x XX] [-a] yyy
        '''
    help = usage + '''\

        oddly formatted description that is so long that it should go onto multiple
        lines when wrapped

        positional arguments:
          yyy         normal y help

        optional arguments:
          -h, --help  show this help message and exit
          -x XX       oddly formatted -x help

        title:
          oddly formatted group description
            
          -a          oddly formatted -a help again, so long that it should be wrapped
                      over multiple lines
        '''
    version = ''

class TestHelpWrappingShortNames(unittest.TestCase):
    """Make sure that text after short names starts on the first line"""
    __metaclass__ = TestHelpFormattingMetaclass
    
    parser_signature = Sig(prog='PROG', description= 'D\nD' * 30)
    argument_signatures = [
        Sig('-x', metavar='XX', help='XHH HX' * 20),
        Sig('y', metavar='yyy', help='YH YH' * 20),
    ]
    argument_group_signatures = [
        (Sig('ALPHAS'), [
            Sig('-a', action='store_true', help='AHHH HHA' * 10)])
    ]
    usage = '''\
        usage: PROG [-h] [-x XX] [-a] yyy
        '''
    help = usage + '''\

        D DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD
        DD DD DD DD D

        positional arguments:
          yyy         YH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH
                      YHYH YHYH YHYH YHYH YHYH YHYH YHYH YH

        optional arguments:
          -h, --help  show this help message and exit
          -x XX       XHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH
                      HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HXXHH HX

        ALPHAS:
          -a          AHHH HHAAHHH HHAAHHH HHAAHHH HHAAHHH HHAAHHH HHAAHHH HHAAHHH
                      HHAAHHH HHAAHHH HHA
        '''
    version = ''

class TestHelpWrappingLongNames(unittest.TestCase):
    """Make sure that text after long names starts on the next line"""
    __metaclass__ = TestHelpFormattingMetaclass
    
    parser_signature = Sig(usage='USAGE', description= 'D D' * 30,
                           version='V V'*30)
    argument_signatures = [
        Sig('-x', metavar='X' * 25, help='XH XH' * 20),
        Sig('y', metavar='y' * 25, help='YH YH' * 20),
    ]
    argument_group_signatures = [
        (Sig('ALPHAS'), [
            Sig('-a', metavar='A' * 25, help='AH AH' * 20),
            Sig('z', metavar='z' * 25, help='ZH ZH' * 20)])
    ]
    usage = '''\
        usage: USAGE
        '''
    help = usage + '''\

        D DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD DD
        DD DD DD DD D

        positional arguments:
          yyyyyyyyyyyyyyyyyyyyyyyyy
                                YH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH
                                YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YHYH YH

        optional arguments:
          -h, --help            show this help message and exit
          -v, --version         show program's version number and exit
          -x XXXXXXXXXXXXXXXXXXXXXXXXX
                                XH XHXH XHXH XHXH XHXH XHXH XHXH XHXH XHXH XHXH XHXH
                                XHXH XHXH XHXH XHXH XHXH XHXH XHXH XHXH XHXH XH

        ALPHAS:
          zzzzzzzzzzzzzzzzzzzzzzzzz
                                ZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH
                                ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZHZH ZH
          -a AAAAAAAAAAAAAAAAAAAAAAAAA
                                AH AHAH AHAH AHAH AHAH AHAH AHAH AHAH AHAH AHAH AHAH
                                AHAH AHAH AHAH AHAH AHAH AHAH AHAH AHAH AHAH AH
        '''
    version = '''\
        V VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV VV
        VV VV VV VV V
        '''

class TestHelpUsage(unittest.TestCase):
    """Test basic usage messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('-w', nargs='+', help='w'),
        Sig('-x', nargs='*', help='x'),
        Sig('a', help='a'),
        Sig('b', help='b', nargs=2),
        Sig('c', help='c', nargs='?'),
    ]
    argument_group_signatures = [
        (Sig('group'), [
            Sig('-y', nargs='?', help='y'),
            Sig('-z', nargs=3, help='z'),
            Sig('d', help='d', nargs='*'),
            Sig('e', help='e', nargs='+'),
        ])
    ]
    usage = ('''\
        usage: PROG [-h] [-w W [W ...]] [-x [X [X ...]]] [-y [Y]] [-z Z Z Z]
                    a b b [c] [d [d ...]] e [e ...]
        '''
    )
    help = usage + '''\

        positional arguments:
          a               a
          b               b
          c               c

        optional arguments:
          -h, --help      show this help message and exit
          -w W [W ...]    w
          -x [X [X ...]]  x

        group:
          d               d
          e               e
          -y [Y]          y
          -z Z Z Z        z
        '''
    version = ''

class TestHelpOnlyUserGroups(unittest.TestCase):
    """Test basic usage messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', add_help=False)
    argument_signatures = []
    argument_group_signatures = [
        (Sig('xxxx'), [
            Sig('-x', help='x'),
            Sig('a', help='a'),
        ]),
        (Sig('yyyy'), [
            Sig('b', help='b'),
            Sig('-y', help='y'),
        ]),
    ]
    usage = ('''\
        usage: PROG [-x X] [-y Y] a b
        '''
    )
    help = usage + '''\

        xxxx:
          a     a
          -x X  x

        yyyy:
          b     b
          -y Y  y
        '''
    version = ''

class TestHelpUsageOptionalsWrap(unittest.TestCase):
    """Test usage messages where the optionals wrap"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('-w', metavar='W' * 25),
        Sig('-x', metavar='X' * 25),
        Sig('-y', metavar='Y' * 25),
        Sig('-z', metavar='Z' * 25),
        Sig('a'),
        Sig('b'),
        Sig('c'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [-w WWWWWWWWWWWWWWWWWWWWWWWWW] [-x XXXXXXXXXXXXXXXXXXXXXXXXX]
                    [-y YYYYYYYYYYYYYYYYYYYYYYYYY] [-z ZZZZZZZZZZZZZZZZZZZZZZZZZ]
                    a b c
        '''
    help = usage + '''\

        positional arguments:
          a
          b
          c

        optional arguments:
          -h, --help            show this help message and exit
          -w WWWWWWWWWWWWWWWWWWWWWWWWW
          -x XXXXXXXXXXXXXXXXXXXXXXXXX
          -y YYYYYYYYYYYYYYYYYYYYYYYYY
          -z ZZZZZZZZZZZZZZZZZZZZZZZZZ
        '''
    version = ''


class TestHelpUsagePositionalsWrap(unittest.TestCase):
    """Test usage messages where the positionals wrap"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('-x'),
        Sig('-y'),
        Sig('-z'),
        Sig('a' * 25),
        Sig('b' * 25),
        Sig('c' * 25),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [-x X] [-y Y] [-z Z]
                    aaaaaaaaaaaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbbbbbb
                    ccccccccccccccccccccccccc
        '''
    help = usage + '''\

        positional arguments:
          aaaaaaaaaaaaaaaaaaaaaaaaa
          bbbbbbbbbbbbbbbbbbbbbbbbb
          ccccccccccccccccccccccccc

        optional arguments:
          -h, --help            show this help message and exit
          -x X
          -y Y
          -z Z
        '''
    version = ''

class TestHelpUsageOptionalsPositionalsWrap(unittest.TestCase):
    """Test usage messages where the optionals and positionals wrap"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('-x', metavar='X' * 25),
        Sig('-y', metavar='Y' * 25),
        Sig('-z', metavar='Z' * 25),
        Sig('a' * 25),
        Sig('b' * 25),
        Sig('c' * 25),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [-x XXXXXXXXXXXXXXXXXXXXXXXXX] [-y YYYYYYYYYYYYYYYYYYYYYYYYY]
                    [-z ZZZZZZZZZZZZZZZZZZZZZZZZZ]
                    aaaaaaaaaaaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbbbbbb
                    ccccccccccccccccccccccccc
        '''
    help = usage + '''\

        positional arguments:
          aaaaaaaaaaaaaaaaaaaaaaaaa
          bbbbbbbbbbbbbbbbbbbbbbbbb
          ccccccccccccccccccccccccc

        optional arguments:
          -h, --help            show this help message and exit
          -x XXXXXXXXXXXXXXXXXXXXXXXXX
          -y YYYYYYYYYYYYYYYYYYYYYYYYY
          -z ZZZZZZZZZZZZZZZZZZZZZZZZZ
        '''
    version = ''

class TestHelpUsageOptionalsOnlyWrap(unittest.TestCase):
    """Test usage messages where there are only optionals and they wrap"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('-x', metavar='X' * 25),
        Sig('-y', metavar='Y' * 25),
        Sig('-z', metavar='Z' * 25),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [-x XXXXXXXXXXXXXXXXXXXXXXXXX] [-y YYYYYYYYYYYYYYYYYYYYYYYYY]
                    [-z ZZZZZZZZZZZZZZZZZZZZZZZZZ]
        '''
    help = usage + '''\

        optional arguments:
          -h, --help            show this help message and exit
          -x XXXXXXXXXXXXXXXXXXXXXXXXX
          -y YYYYYYYYYYYYYYYYYYYYYYYYY
          -z ZZZZZZZZZZZZZZZZZZZZZZZZZ
        '''
    version = ''

class TestHelpUsagePositionalsOnlyWrap(unittest.TestCase):
    """Test usage messages where there are only positionals and they wrap"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', add_help=False)
    argument_signatures = [
        Sig('a' * 25),
        Sig('b' * 25),
        Sig('c' * 25),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG aaaaaaaaaaaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbbbbbbbbb
                    ccccccccccccccccccccccccc
        '''
    help = usage + '''\

        positional arguments:
          aaaaaaaaaaaaaaaaaaaaaaaaa
          bbbbbbbbbbbbbbbbbbbbbbbbb
          ccccccccccccccccccccccccc
        '''
    version = ''


class TestHelpVariableExpansion(unittest.TestCase):
    """Test that variables are expanded properly in help messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('-x', type='int',
            help='x %(prog)s %(default)s %(type)s'),
        Sig('-y', action='store_const', default=42, const='XXX',
            help='y %(prog)s %(default)s %(const)s'),
        Sig('--foo', choices='abc',
            help='foo %(prog)s %(default)s %(choices)s'),
        Sig('--bar', default='baz', choices=[1, 2], metavar='BBB',
            help='bar %(prog)s %(default)s %(dest)s'),
        Sig('spam', help='spam %(prog)s %(default)s'),
        Sig('badger', default=0.5, help='badger %(prog)s %(default)s'),
    ]
    argument_group_signatures = [
        (Sig('group'), [
            Sig('-a', help='a %(prog)s %(default)s'),
            Sig('-b', default=-1, help='b %(prog)s %(default)s'),
        ])
    ]
    usage = ('''\
        usage: PROG [-h] [-x X] [-y] [--foo {a,b,c}] [--bar BBB] [-a A] [-b B]
                    spam badger
        ''')
    help = usage + '''\

        positional arguments:
          spam           spam PROG None
          badger         badger PROG 0.5

        optional arguments:
          -h, --help     show this help message and exit
          -x X           x PROG None int
          -y             y PROG 42 XXX
          --foo {a,b,c}  foo PROG None a, b, c
          --bar BBB      bar PROG baz bar

        group:
          -a A           a PROG None
          -b B           b PROG -1
        '''
    version = ''

class TestHelpSuppressUsage(unittest.TestCase):
    """Test that items can be suppressed in usage messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', usage=argparse.SUPPRESS)
    argument_signatures = [
        Sig('--foo', help='foo help'),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = []
    help = '''\
        positional arguments:
          spam        spam help

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO   foo help
        '''
    usage = ''
    version = ''

class TestHelpSuppressOptional(unittest.TestCase):
    """Test that optional arguments can be suppressed in help messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', add_help=False)
    argument_signatures = [
        Sig('--foo', help=argparse.SUPPRESS),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG spam
        '''
    help = usage + '''\

        positional arguments:
          spam  spam help
        '''
    version = ''

class TestHelpSuppressOptionalGroup(unittest.TestCase):
    """Test that optional groups can be suppressed in help messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('--foo', help='foo help'),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = [
        (Sig('group'), [Sig('--bar', help=argparse.SUPPRESS)])
    ]
    usage = '''\
        usage: PROG [-h] [--foo FOO] spam
        '''
    help = usage + '''\

        positional arguments:
          spam        spam help

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO   foo help
        '''
    version = ''

class TestHelpSuppressPositional(unittest.TestCase):
    """Test that positional arguments can be suppressed in help messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('--foo', help='foo help'),
        Sig('spam', help=argparse.SUPPRESS),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [--foo FOO]
        '''
    help = usage + '''\

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO   foo help
        '''
    version = ''

class TestHelpRequiredOptional(unittest.TestCase):
    """Test that required options don't look optional"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('--foo', required=True, help='foo help'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] --foo FOO
        '''
    help = usage + '''\

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO   foo help
        '''
    version = ''

class TestHelpNoHelpOptional(unittest.TestCase):
    """Test that the --help argument can be suppressed help messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', add_help=False)
    argument_signatures = [
        Sig('--foo', help='foo help'),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [--foo FOO] spam
        '''
    help = usage + '''\

        positional arguments:
          spam       spam help

        optional arguments:
          --foo FOO  foo help
        '''
    version = ''

class TestHelpVersionOptional(unittest.TestCase):
    """Test that the --version argument can be suppressed help messages"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG', version='1.0')
    argument_signatures = [
        Sig('--foo', help='foo help'),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [-v] [--foo FOO] spam
        '''
    help = usage + '''\

        positional arguments:
          spam           spam help

        optional arguments:
          -h, --help     show this help message and exit
          -v, --version  show program's version number and exit
          --foo FOO      foo help
        '''
    version = '''\
        1.0
        '''

class TestHelpNone(unittest.TestCase):
    """Test that no errors occur if no help is specified"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(prog='PROG')
    argument_signatures = [
        Sig('--foo'),
        Sig('spam'),
    ]
    argument_group_signatures = []
    usage = '''\
        usage: PROG [-h] [--foo FOO] spam
        '''
    help = usage + '''\

        positional arguments:
          spam

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO
        '''
    version = ''

class TestHelpRawText(unittest.TestCase):
    """Test the RawTextHelpFormatter"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(
        prog='PROG', formatter_class=argparse.RawTextHelpFormatter,
        description='Keep the formatting\n'
                    '    exactly as it is written\n'
                    '\n'
                    'here\n')

    argument_signatures = [
        Sig('--foo', help='    foo help should also\n'
                          'appear as given here'),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = [
        (Sig('title', description='    This text\n'
                                  '  should be indented\n'
                                  '    exactly like it is here\n'),
         [Sig('--bar', help='bar help')])
    ]
    usage = '''\
        usage: PROG [-h] [--foo FOO] [--bar BAR] spam
        '''
    help = usage + '''\

        Keep the formatting
            exactly as it is written

        here

        positional arguments:
          spam        spam help

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO       foo help should also
                      appear as given here

        title:
              This text
            should be indented
              exactly like it is here

          --bar BAR   bar help
        '''
    version = ''

class TestHelpRawDescription(unittest.TestCase):
    """Test the RawTextHelpFormatter"""
    __metaclass__ = TestHelpFormattingMetaclass

    parser_signature = Sig(
        prog='PROG', formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Keep the formatting\n'
                    '    exactly as it is written\n'
                    '\n'
                    'here\n')

    argument_signatures = [
        Sig('--foo', help='  foo help should not\n'
                          '    retain this odd formatting'),
        Sig('spam', help='spam help'),
    ]
    argument_group_signatures = [
        (Sig('title', description='    This text\n'
                                  '  should be indented\n'
                                  '    exactly like it is here\n'),
         [Sig('--bar', help='bar help')])
    ]
    usage = '''\
        usage: PROG [-h] [--foo FOO] [--bar BAR] spam
        '''
    help = usage + '''\

        Keep the formatting
            exactly as it is written

        here

        positional arguments:
          spam        spam help

        optional arguments:
          -h, --help  show this help message and exit
          --foo FOO   foo help should not retain this odd formatting

        title:
              This text
            should be indented
              exactly like it is here

          --bar BAR   bar help
        '''
    version = ''

# =====================================
# Optional/Positional constructor tests
# =====================================


class TestInvalidArgumentConstructors(unittest.TestCase):
    """Test a bunch of invalid Argument constructors"""
    
    def assertTypeError(self, *args, **kwargs):
        parser = argparse.ArgumentParser()
        self.assertRaises(TypeError, parser.add_argument,
                          *args, **kwargs)

    def assertValueError(self, *args, **kwargs):
        parser = argparse.ArgumentParser()
        self.assertRaises(ValueError, parser.add_argument,
                          *args, **kwargs)

    def test_invalid_keyword_arguments(self):
        self.assertTypeError('-x', bar=None)
        self.assertTypeError('-y', callback='foo')
        self.assertTypeError('-y', callback_args=())
        self.assertTypeError('-y', callback_kwargs={})

    def test_missing_destination(self):
        self.assertTypeError()
        for action in ['append', 'store']:
            self.assertTypeError(action=action)

    def test_invalid_option_strings(self):
        self.assertValueError('--')
        self.assertValueError('---')

    def test_invalid_action(self):
        self.assertTypeError('-x', action='foo')
        self.assertTypeError('foo', action='baz')

    def test_no_argument_actions(self):
        for action in ['store_const', 'store_true', 'store_false',
                       'append_const', 'count']:
            for attrs in [dict(type=int), dict(nargs='+'),
                          dict(choices='ab')]:
                self.assertTypeError('-x', action=action, **attrs)

    def test_no_argument_no_const_actions(self):
        # options with zero arguments
        for action in ['store_true', 'store_false', 'count']:
            
            # const is always disallowed
            self.assertTypeError('-x', const='foo',action=action)
            
            # nargs is always disallowed
            self.assertTypeError('-x', nargs='*', action=action)

    def test_more_than_one_argument_actions(self):
        for action in ['store', 'append']:
            
            # nargs=0 is disallowed
            self.assertValueError('-x', nargs=0, action=action)
            self.assertValueError('spam', nargs=0, action=action)
            
            # const is disallowed with non-optional arguments
            for nargs in [1, '*', '+']:
                 self.assertValueError('-x', const='foo',
                                       nargs=nargs, action=action)
                 self.assertValueError('spam', const='foo',
                                       nargs=nargs, action=action)

    def test_required_const_actions(self):
        for action in ['store_const', 'append_const']:

            # nargs is always disallowed
            self.assertTypeError('-x', nargs='+', action=action)

    def test_parsers_action_missing_params(self):
        self.assertTypeError('command', action='parsers')
        self.assertTypeError('command', action='parsers', prog='PROG')
        self.assertTypeError('command', action='parsers',
                             parser_class=argparse.ArgumentParser)

    def test_required_positional(self):
        self.assertTypeError('foo', required=True)
        
    def test_user_defined_action(self):

        class Success(Exception):
            pass

        class Action(object):
            def __init__(self, option_strings, dest, const, default):
                if dest == 'spam':
                    if const is Success:
                        if default is Success:
                            raise Success()
            def __call__(self, *args, **kwargs):
                pass

        parser = argparse.ArgumentParser()
        self.assertRaises(Success, parser.add_argument, '--spam',
                          action=Action, default=Success, const=Success)
        self.assertRaises(Success, parser.add_argument, 'spam',
                          action=Action, default=Success, const=Success)

# ================================
# Actions returned by add_argument
# ================================

class TestActionsReturned(unittest.TestCase):

    def test_dest(self):
        parser = argparse.ArgumentParser()
        action = parser.add_argument('--foo')
        self.assertEqual(action.dest, 'foo')
        action = parser.add_argument('-b', '--bar')
        self.assertEqual(action.dest, 'bar')
        action = parser.add_argument('-x', '-y')
        self.assertEqual(action.dest, 'x')

    def test_misc(self):
        parser = argparse.ArgumentParser()
        action = parser.add_argument('--foo', nargs='?', const=42,
                                     default=84, type=int, choices=[1, 2],
                                     help='FOO', metavar='BAR', dest='baz')
        self.assertEqual(action.nargs, '?')
        self.assertEqual(action.const, 42)
        self.assertEqual(action.default, 84)
        self.assertEqual(action.type, int)
        self.assertEqual(action.choices, [1, 2])
        self.assertEqual(action.help, 'FOO')
        self.assertEqual(action.metavar, 'BAR')
        self.assertEqual(action.dest, 'baz')
                

# ================================
# Argument conflict handling tests
# ================================

class TestConflictHandling(unittest.TestCase):

    def test_bad_type(self):
        self.assertRaises(ValueError, argparse.ArgumentParser,
                          conflict_handler='foo')

    def test_conflict_error(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-x')
        self.assertRaises(argparse.ArgumentError,
                          parser.add_argument, '-x')
        parser.add_argument('--spam')
        self.assertRaises(argparse.ArgumentError,
                          parser.add_argument, '--spam')

    def test_resolve_error(self):
        get_parser = argparse.ArgumentParser
        parser = get_parser(prog='PROG', conflict_handler='resolve')
        
        parser.add_argument('-x', help='OLD X')
        parser.add_argument('-x', help='NEW X')
        self.assertEqual(parser.format_help(), textwrap.dedent('''\
            usage: PROG [-h] [-x X]

            optional arguments:
              -h, --help  show this help message and exit
              -x X        NEW X
            '''))

        parser.add_argument('--spam', metavar='OLD_SPAM')
        parser.add_argument('--spam', metavar='NEW_SPAM')
        self.assertEqual(parser.format_help(), textwrap.dedent('''\
            usage: PROG [-h] [-x X] [--spam NEW_SPAM]

            optional arguments:
              -h, --help       show this help message and exit
              -x X             NEW X
              --spam NEW_SPAM
            '''))


# =============================
# Help and Version option tests
# =============================

class TestOptionalsHelpVersionActions(unittest.TestCase):
    """Test the help and version actions"""

    def _get_error_message(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except ArgumentParserError, err:
            return err.message
        else:
            self.assertRaises(ArgumentParserError, func, *args, **kwargs)

    def assertPrintHelpExit(self, parser, args_str):
        self.assertEqual(
            parser.format_help(),
            self._get_error_message(parser.parse_args, args_str.split()))

    def assertPrintVersionExit(self, parser, args_str):
        self.assertEqual(
            parser.format_version(),
            self._get_error_message(parser.parse_args, args_str.split()))

    def assertArgumentParserError(self, parser, *args):
        self.assertRaises(ArgumentParserError, parser.parse_args, args)

    def test_version(self):
        parser = ErrorRaisingArgumentParser(version='1.0')
        self.assertPrintHelpExit(parser, '-h')
        self.assertPrintHelpExit(parser, '--help')
        self.assertPrintVersionExit(parser, '-v')
        self.assertPrintVersionExit(parser, '--version')

    def test_version_no_help(self):        
        parser = ErrorRaisingArgumentParser(add_help=False, version='1.0')
        self.assertArgumentParserError(parser, '-h')
        self.assertArgumentParserError(parser, '--help')
        self.assertPrintVersionExit(parser, '-v')
        self.assertPrintVersionExit(parser, '--version')

    def test_no_help(self):
        parser = ErrorRaisingArgumentParser(add_help=False)
        self.assertArgumentParserError(parser, '-h')
        self.assertArgumentParserError(parser, '--help')
        self.assertArgumentParserError(parser, '-v')
        self.assertArgumentParserError(parser, '--version')

    def test_alternate_help_version(self):
        parser = ErrorRaisingArgumentParser()
        parser.add_argument('-x', action='help')
        parser.add_argument('-y', action='version')
        self.assertPrintHelpExit(parser, '-x')
        self.assertPrintVersionExit(parser, '-y')
        self.assertArgumentParserError(parser, '-v')
        self.assertArgumentParserError(parser, '--version')

    def test_help_version_extra_arguments(self):
        parser = ErrorRaisingArgumentParser(version='1.0')
        parser.add_argument('-x', action='store_true')
        parser.add_argument('y')

        # try all combinations of valid prefixes and suffixes
        valid_prefixes = ['', '-x', 'foo', '-x bar', 'baz -x']
        valid_suffixes = valid_prefixes + ['--bad-option', 'foo bar baz']
        for prefix in valid_prefixes:
            for suffix in valid_suffixes:
                format = '%s %%s %s' % (prefix, suffix)
            self.assertPrintHelpExit(parser, format % '-h')
            self.assertPrintHelpExit(parser, format % '--help')
            self.assertPrintVersionExit(parser, format % '-v')
            self.assertPrintVersionExit(parser, format % '--version')
        

# ======================
# str() and repr() tests
# ======================

class TestStrings(unittest.TestCase):
    """Test str()  and repr() on Optionals and Positionals"""

    def assertStringEqual(self, obj, result_string):
        for func in [str, repr]:
            self.assertEqual(func(obj), result_string)

    def test_optional(self):
        option = argparse.Action(
            option_strings=['--foo', '-a', '-b'],
            dest='b',
            type='int',
            nargs='+',
            default=42,
            choices=[1, 2, 3],
            help='HELP',
            metavar='METAVAR')
        string = (
            "Action(option_strings=['--foo', '-a', '-b'], dest='b', "
            "nargs='+', const=None, default=42, type='int', "
            "choices=[1, 2, 3], help='HELP', metavar='METAVAR')"
        )
        self.assertStringEqual(option, string)

    def test_argument(self):
        argument = argparse.Action(
            option_strings=[],
            dest='x',
            type=float,
            nargs='?',
            default=2.5,
            choices=[0.5, 1.5, 2.5],
            help='H HH H',
            metavar='MV MV MV')
        string = (
            "Action(option_strings=[], dest='x', nargs='?', "
            "const=None, default=2.5, type=%r, choices=[0.5, 1.5, 2.5], "
            "help='H HH H', metavar='MV MV MV')" % float
        )
        self.assertStringEqual(argument, string)

    def test_namespace(self):
        ns = argparse.Namespace(foo=42, bar='spam')
        string = "Namespace(bar='spam', foo=42)"
        self.assertStringEqual(ns, string)

    def test_parser(self):
        parser = argparse.ArgumentParser(prog='PROG')
        string = (
            "ArgumentParser(prog='PROG', usage=None, description=None, "
            "version=None, formatter_class=%r, conflict_handler='error', "
            "add_help=True)" % argparse.HelpFormatter
        )
        self.assertStringEqual(parser, string)

# ===============
# Namespace tests
# ===============

class TestNamespace(unittest.TestCase):

    def test_constructor(self):
        ns = argparse.Namespace()
        self.assertRaises(AttributeError, getattr, ns, 'x')

        ns = argparse.Namespace(a=42, b='spam')
        self.assertEqual(ns.a, 42)
        self.assertEqual(ns.b, 'spam')

    def test_equality(self):
        ns1 = argparse.Namespace(a=1, b=2)
        ns2 = argparse.Namespace(b=2, a=1)
        ns3 = argparse.Namespace(a=1)
        ns4 = argparse.Namespace(b=2)

        self.assertEqual(ns1, ns2)
        self.assertNotEqual(ns1, ns3)
        self.assertNotEqual(ns1, ns4)
        self.assertNotEqual(ns2, ns3)
        self.assertNotEqual(ns2, ns4)
        self.failUnless(ns1 != ns3)
        self.failUnless(ns1 != ns4)
        self.failUnless(ns2 != ns3)
        self.failUnless(ns2 != ns4)



if __name__ == '__main__':
    unittest.main()
