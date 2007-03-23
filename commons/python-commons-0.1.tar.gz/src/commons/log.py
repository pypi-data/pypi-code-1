# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; py-indent-offset: 4; -*-
# vim:ft=python:et:sw=4:ts=4

"""
Convenience functions for the standard L{logging} library.

Functions are mostly self-explanatory.
"""

from strs import *
import itertools, logging, logging.handlers, sys

# TODO cleanup / reorganize this section

def log( level, flag, *args ):
    msg = ' '.join( itertools.imap( str, args ) )
    logger = logging.getLogger( flag )
    logger.log( level, msg )

def critical( flag, *args ):
    log( logging.CRITICAL, flag, *args )

def error( flag, *args ):
    log( logging.ERROR, flag, *args )

def warning( flag, *args ):
    log( logging.WARNING, flag, *args )

def debug( flag, *args ):
    log( logging.DEBUG, flag, *args )

def info( flag, *args ):
    log( logging.INFO, flag, *args )

def die( flag, *args ):
    error( flag, *args )
    sys.exit( 1 )

def config_logging( level = logging.INFO,
                    do_console = False,
                    do_file = False,
                    do_server = False,
                    flags = [],
                    path = None,
                    log_format = '%(asctime)s %(levelname)-8s %(message)s',
                    log_date_format = '%a, %d %b %Y %H:%M:%S' ):
    """
    Configures L{logging}, promoting some common configurations.

    @param level: The default log-level threshold for all
    loggers. (Note that this is not the level for all handlers.)
    @type level: int

    @param do_console: Whether to enable the console handler.
    @type do_console: bool

    @param do_file: Whether to enable the file handler.
    @type do_file: bool

    @param do_server: Whether to enable a network socket stream
    handler.
    @type do_server: bool

    @param flags: The set of flags on which to lower the threshold to
    L{logging.DEBUG}.
    @type flags: iterable

    @param path: The path of the log file (only considered if
    C{do_file} is C{True}.
    @type path: str

    @param log_format: The log message formatting template.
    @type log_format: str

    @param log_date_format: The timestamp formatting template.
    @type log_date_format: str
    """
    formatter = logging.Formatter( log_format, log_date_format )

    logging.getLogger( '' ).setLevel( level )
    logging.raiseExceptions = False

    # log to console
    if do_console:
        handler = logging.StreamHandler()
        handler.setLevel( logging.DEBUG )
        handler.setFormatter( formatter )
        logging.getLogger( '' ).addHandler( handler )

    # log to files
    if do_file and path is not None:
        handler = logging.FileHandler( path, 'w' )
        handler.setFormatter( formatter )
        handler.setLevel( logging.DEBUG )
        logging.getLogger( '' ).addHandler( handler )

    # log to the log server
    if do_server:
        handler = logging.handlers.SocketHandler( 'localhost',
                logging.handlers.DEFAULT_TCP_LOGGING_PORT )
        handler.setLevel( logging.DEBUG )
        logging.getLogger( '' ).addHandler( handler )

    for flag in flags:
        logging.getLogger( flag ).setLevel( logging.DEBUG )

####    logging.raiseExceptions = False
####    config_path = get_usr_conf( 'LOGGING_CONFIG_PATH', 'logging.ini' )
####    if config_path is not None:
####        logging.config.fileConfig( config_path )
