# -*- coding: utf-8 -*-
"""
    pocoo.utils.profiler
    ~~~~~~~~~~~~~~~~~~~~

    Provides a WSGI Profiler middleware for finding bottlenecks.

    :license: GNU GPL, see LICENSE for more details.
    :copyright: 2006 by Armin Ronacher.
"""
import sys
try:
    from cProfile import Profile
except ImportError:
    from profile import Profile
from pstats import Stats


class MergeStream(object):
    """
    A object that redirects `write` calls to multiple streams.
    Use this to log to both `sys.stdout` and a file::

        f = file('profiler.log')
        stream = MergeStream(sys.stdout, f)
        profiler = ProfilerMiddleware(app, stream)
    """

    def __init__(self, *streams):
        if not streams:
            raise TypeError('at least one stream must be given')
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)


class ProfilerMiddleware(object):
    """
    Simple profiler middleware
    """

    def __init__(self, app, stream=sys.stdout):
        self._app = app
        self._stream = stream

    def __call__(self, environ, start_response):
        response_body = []
        
        def catching_start_response(status, headers, exc_info=None):
            start_response(status, headers, exc_info)
            return response_body.append
        
        def runapp():
            response_body.extend(self._app(environ, catching_start_response))

        p = Profile()
        p.runcall(runapp)
        body = ''.join(response_body)
        stats = Stats(p)
        stats.sort_stats('time', 'calls')
        
        self._stream.write('-' * 80)
        self._stream.write('\nPATH: %r\n' % environ.get('PATH_INFO'))
        stats.print_stats()
        self._stream.write('-' * 80 + '\n\n')

        return [body]
