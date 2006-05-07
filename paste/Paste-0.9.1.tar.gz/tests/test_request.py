# (c) 2005 Ben Bangert
# This module is part of the Python Paste Project and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
from paste.request import *
from paste.fixture import *
from py.test import raises

def simpleapp(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    request = WSGIRequest(environ)
    return ['Hello world!\n', 'The get is %s' % str(request.GET),
        'Val is %s' % request.GET.get('name')]

def test_gets():
    app = TestApp(simpleapp)
    res = app.get('/')
    assert 'Hello' in res
    assert "get is {}" in res
    
    res = app.get('/?name=george')
    assert "get is {'name': ['george']}" in res
    assert "Val is george" in res
