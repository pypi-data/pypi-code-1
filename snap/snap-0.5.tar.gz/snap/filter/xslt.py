"""
WSGI middleware to filter app output through XSLT.

This employs libxslt/libxml2 by way of lxml (http://codespeak.net/lxml/) to
optionally filter the output of a wrapped application through an XSLT
stylesheet.

The stylesheet is parsed at filter creation time from a configuration
variable provided when creating the filter.

Originally inspired by xslfilter.py from l.m.orchard <l.m.orchard@pobox.com>

$Id: xslt.py 3965 2006-01-26 13:50:03Z sidnei $
"""

import os
import os.path
from lxml import etree
from StringIO import StringIO

class XSLTFilter:
    """WSGI application class wrapper which provides XSLT filtering
    """

    def __init__(self, app, style):
        """Wrap a given WSGI app, with optional path to local XSL files.
        """
        self.app = app
        self.status = '200 OK'
        self.headers_out = []
        self.style = style

    def start_response(self, status, headers_out):
        """Intercept the response start from the filtered app.
        """
        self.status = status
        self.headers_out = headers_out

    def __call__(self, env, start_response):
        """Facilitate WSGI API by providing a callable hook.
        """
        self.env = env
        self.real_start = start_response
        return self.__iter__()

    def __iter__(self):
        """"""
        result = self.app(self.env, self.start_response)
        result_iter = result.__iter__()
        transform_ok = False
        headers_out = []

        # Search for XML content header and XSL query parameter.
        for n, v in self.headers_out:
            if (n.lower() == 'content-type' and
                'text/xml' in v or 'text/html' in v):
                transform_ok = True

        if not transform_ok:
            # Don't transform, just pass headers & content through.
            headers_out += self.headers_out
            iter_out = result_iter

        else:
            # Get the XSL param, set some headers for troubleshooting.
            headers_out.append(('X-Filter', 'XSL'))

            # Parse the output, transform the output.
            doc_file = StringIO("".join(result_iter))
            doc = etree.parse(doc_file)

            # Apply the XSL and get the results as a string.
            result = self.style.apply(doc)

            # Delete 'xml:base' attribute which has a path to the theme.
            xmlbase = '{http://www.w3.org/XML/1998/namespace}base'
            root = result.getroot()
            if root.attrib.has_key(xmlbase):
                del root.attrib[xmlbase]
            del root

            # And finally stringify the transformed tree.
            result_str = self.style.tostring(result)

            # Munge content-type and -length headers.
            for n, v in self.headers_out:
                if n.lower() == 'content-length':
                    v = len(result_str)
                headers_out.append((n, v))

            # Produce the string list iterator out of the filtered output.
            iter_out = [result_str].__iter__()

        # Finish up with the output headers and iterator
        self.real_start(self.status, headers_out)
        return iter_out

# "Compile" the site theme into an XSLT transform.  Open the site
# theme compiler and the theme "input doc".  The theme input doc is
# used to pull in the HTML file for the site theme and the rule file.
# These are pulled in using XInclude.
xins = "http://www.w3.org/2001/XInclude"

def theme_filter_factory(global_conf, theme_base):
    input_path = os.path.join(theme_base, 'input.xsl')
    input_doc = etree.ElementTree(file=input_path)
    for node in input_doc.xpath('//xi:include', {'xi': xins}):
        # Fix href so it's absolute.
        href = os.path.join(theme_base, node.get('href'))
        node.set('href', href)
    input_doc.xinclude()

    compiler_path = os.path.join(theme_base, 'compiler.xsl')
    compiler_doc = etree.ElementTree(file=compiler_path)
    compiler = etree.XSLT(compiler_doc)
    style = etree.XSLT(compiler.apply(input_doc))

    def filter(app):
        return XSLTFilter(app, style)
    return filter
