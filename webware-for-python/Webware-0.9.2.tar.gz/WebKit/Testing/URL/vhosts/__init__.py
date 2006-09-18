from WebKit.URLParser import URLParser
import os

class VHostParser(URLParser):

    def parseHook(self, trans, requestPath, app, hook):
        host = trans.request().environ()['HTTP_HOST']
        hook.parse(trans, '/%s%s' % (host, requestPath), app)

urlParserHook = VHostParser()
