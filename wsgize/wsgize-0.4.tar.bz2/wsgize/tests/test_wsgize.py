# Copyright (c) 2005, the Lawrence Journal-World
# Copyright (c) 2006 L. C. Rees
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#    
#    2. Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of Django nor the names of its contributors may be used
#       to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
from wsgize import *


class TestWsize(unittest.TestCase):

    def test_wsgize_default(self):
        def sr(start, hdr, exc=None): pass
        @wsgize()
        def app(environ, start_response):
            return 'Test'
        self.assertEqual(app({}, sr), ['Test'])

    def test_wsgize_custom(self):
        def sr(start, hdr, exc=None): pass
        @wsgize(response=404, mime='text/plain')
        def app(environ, start_response):
            return 'Test'
        self.assertEqual(app({}, sr), ['Test'])

    def test_wsgiwrap_default(self):
        def sr(start, hdr, exc=None): pass
        @wsgiwrap()
        def app(*arg, **kw):
            return '%s %s%s' % (arg[0], kw['kw'], arg[1])
        env = {'wsgiorg.routing_args':(('Hello', '!'), {'kw':'world'})}
        self.assertEqual(app(env, sr), ['Hello world!'])

    def test_wsgiwrap_both(self):
        def sr(start, hdr, exc=None): pass
        @wsgiwrap(response=404, mime='text/plain')
        def app(*arg, **kw):
            return '%s %s%s' % (arg[0], kw['kw'], arg[1])
        env = {'wsgiorg.routing_args':(('Hello', '!'), {'kw':'world'})}
        self.assertEqual(app(env, sr), ['Hello world!'])

    def test_wsgiwrap_args(self):
        def sr(start, hdr, exc=None): pass
        @wsgiwrap(response=404, mime='text/plain')
        def app(*arg):
            return '%s world%s' % (arg[0], arg[1])
        env = {'wsgiorg.routing_args':(('Hello', '!'), {})}
        self.assertEqual(app(env, sr), ['Hello world!'])        
            
    def test_wsgiwrap_kwargs(self):
        def sr(start, hdr, exc=None): pass
        @wsgiwrap(response=404, mime='text/plain')
        def app(**kw):
            return 'Hello %s!' % kw['kw']
        env = {'wsgiorg.routing_args':((), {'kw':'world'})}
        self.assertEqual(app(env, sr), ['Hello world!'])

    def test_route(self):
        def sr(start, hdr, exc=None): pass
        @route('next')        
        @wsgiwrap()
        def app2(**kw):
            return 'Hello %s!' % kw['kw']
        @wsgize()
        def app1(env, start):
            env['wsgiorg.routing_args'] = ((), {'kw':'world'})
            env['wsgize.callable'] = 'next'
            return WsgiRoute()(env, start)            
        self.assertEqual(app1({}, sr), ['Hello world!']) 


if __name__ == '__main__': unittest.main()    