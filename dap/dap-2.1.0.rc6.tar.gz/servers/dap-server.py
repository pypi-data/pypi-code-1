#!/usr/bin/env python
import sys
import os 
import optparse

from paste.httpserver import serve

from dap.wsgi.application import DapServerApplication as application
from dap.util.logger import LoggerMiddleware as middleware

def main(root, port, logfile, level):
    # Build WSGI DAP application.
    app = application(root)

    # Apply logger middleware.
    app = middleware(app, filename=logfile, level=level)

    # Run server.
    serve(app, port=port)


if __name__ == "__main__":
    # Parse options.
    parser = optparse.OptionParser()
    parser.add_option('-d', '--pid', dest='pidfile',
                      default=None,
                      help="pid file")
    parser.add_option('-p', '--port', dest='port',
                      default=8888, type='int',
                      help="port to serve on (default 8888)")
    parser.add_option('-l', '--log', dest='logfile',
                      default=None,
                      help="log file")
    parser.add_option('-v', '--level', dest='level',
                      default='ERROR',
                      help="logging level: DEBUG, INFO, WARN[ING], ERROR or CRITICAL/FATAL")
    options, args = parser.parse_args()
    
    # Get the app root. Defaults to current directory.
    pwd = os.environ['PWD']
    if not len(args) == 1: root = pwd
    else: root = os.path.join(pwd, args[0])  # absolute path

    # Get absolute path for PID file and log.
    pidfile = options.pidfile
    logfile = options.logfile
    if pidfile: pidfile = os.path.join(pwd, pidfile)
    if logfile: logfile = os.path.join(pwd, logfile)
    
    # do the UNIX double-fork magic, see Stevens' "Advanced 
    # Programming in the UNIX Environment" for details (ISBN 0201563177)
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit first parent
            sys.exit(0) 
    except OSError, e: 
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1)

    # decouple from parent environment
    os.chdir("/") 
    os.setsid() 
    os.umask(0) 

    # do second fork
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit from second parent, print eventual PID before
            print "Daemon PID %d" % pid 
            # Try to store pid.
            if pidfile:
                try:
                    f = open(pidfile, 'w')
                    f.write('%d\n' % pid)
                    f.close()
                except IOError, e:
                    print >>sys.stderr, "unable to open PID file: %d (%s)" % (e.errno, e.strerror) 
                    sys.exit(1) 
            sys.exit(0) 
    except OSError, e: 
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1) 

    # start the daemon main loop
    main(root, options.port, logfile, options.level) 

