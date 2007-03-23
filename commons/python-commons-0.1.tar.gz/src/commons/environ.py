# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; py-indent-offset: 4; -*-
# vim:ft=python:et:sw=4:ts=4

"""
Environment variables.
"""

import os

def is_environ_set( name ):
    """
    Tests if an environment variable is set and non-empty.

    @param name: The environment variable's name.
    @type name: str

    @return: True if the environment variable is set and non-empty;
    false otherwise.
    @rtype: bool
    """
    try:
        return os.environ[ name ] != ''
    except KeyError:
        return False

def get_environs( *names ):
    """
    Get the value from a prioritized ordering of environment
    variables.
    
    @param names: The names of the environment variables to scan.
    @type names: str

    @return: The value of the first variable that is set, or None if
    none are set.
    @rtype: str
    """
    for name in names:
        try:
            return os.environ[ name ]
        except KeyError:
            pass
    else:
        return None

