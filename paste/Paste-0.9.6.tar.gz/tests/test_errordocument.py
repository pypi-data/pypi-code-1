from paste.errordocument import forward
from paste.fixture import *
from paste.recursive import RecursiveMiddleware

def simple_app(environ, start_response):
    start_response("200 OK", [('Content-type', 'text/plain')])
    return ['requested page returned']

def not_found_app(environ, start_response):
    start_response("404 Not found", [('Content-type', 'text/plain')])
    return ['requested page returned']
    
def test_ok():
    app = TestApp(simple_app)
    res = app.get('')
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '200 OK'
    assert 'requested page returned' in res
    
def error_docs_app(environ, start_response):
    if environ['PATH_INFO'] == '/not_found':
        start_response("404 Not found", [('Content-type', 'text/plain')])
        return ['Not found']
    elif environ['PATH_INFO'] == '/error':
        start_response("200 OK", [('Content-type', 'text/plain')])
        return ['Page not found']
    else:
        return simple_app(environ, start_response)
    
def test_error_docs_app():
    app = TestApp(error_docs_app)
    res = app.get('')
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '200 OK'
    assert 'requested page returned' in res
    res = app.get('/error')
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '200 OK'
    assert 'Page not found' in res
    res = app.get('/not_found', status=404)
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '404 Not found'
    assert 'Not found' in res

def test_forward():    
    app = forward(error_docs_app, codes={404:'/error'})
    app = TestApp(RecursiveMiddleware(app))
    res = app.get('')
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '200 OK'
    assert 'requested page returned' in res
    res = app.get('/error')
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '200 OK'
    assert 'Page not found' in res
    res = app.get('/not_found', status=404)
    assert res.header('content-type') == 'text/plain'
    assert res.full_status == '404 Not found'
    # Note changed response
    assert 'Page not found' in res
    
