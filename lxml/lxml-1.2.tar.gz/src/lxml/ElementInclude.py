#
# ElementTree
# $Id: ElementInclude.py 1862 2004-06-18 07:31:02Z Fredrik $
#
# limited xinclude support for element trees
#
# history:
# 2003-08-15 fl   created
# 2003-11-14 fl   fixed default loader
#
# Copyright (c) 2003-2004 by Fredrik Lundh.  All rights reserved.
#
# fredrik@pythonware.com
# http://www.pythonware.com
#
# --------------------------------------------------------------------
# The ElementTree toolkit is
#
# Copyright (c) 1999-2004 by Fredrik Lundh
#
# By obtaining, using, and/or copying this software and/or its
# associated documentation, you agree that you have read, understood,
# and will comply with the following terms and conditions:
#
# Permission to use, copy, modify, and distribute this software and
# its associated documentation for any purpose and without fee is
# hereby granted, provided that the above copyright notice appears in
# all copies, and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of
# Secret Labs AB or the author not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
#
# SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
# TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-
# ABILITY AND FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR
# BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY
# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
# OF THIS SOFTWARE.
# --------------------------------------------------------------------

##
# Limited XInclude support for the ElementTree package.
##

import copy
from lxml import etree

try:
    set
except NameError:
    from sets import Set as set

XINCLUDE = "{http://www.w3.org/2001/XInclude}"

XINCLUDE_INCLUDE = XINCLUDE + "include"
XINCLUDE_FALLBACK = XINCLUDE + "fallback"

##
# Fatal include error.

class FatalIncludeError(etree.LxmlSyntaxError):
    pass

##
# ET compatible default loader.
# This loader reads an included resource from disk.
#
# @param href Resource reference.
# @param parse Parse mode.  Either "xml" or "text".
# @param encoding Optional text encoding.
# @return The expanded resource.  If the parse mode is "xml", this
#    is an ElementTree instance.  If the parse mode is "text", this
#    is a Unicode string.  If the loader fails, it can return None
#    or raise an IOError exception.
# @throws IOError If the loader fails to load the resource.

def default_loader(href, parse, encoding=None):
    file = open(href)
    if parse == "xml":
        data = etree.parse(file).getroot()
    else:
        data = file.read()
        if encoding:
            data = data.decode(encoding)
    file.close()
    return data

##
# Default loader used by lxml.etree - handles custom resolvers properly
# 

def _lxml_default_loader(href, parse, encoding=None, parser=None):
    if parse == "xml":
        data = etree.parse(href, parser).getroot()
    else:
        data = open(href).read()
        if encoding:
            data = data.decode(encoding)
    return data

##
# Wrapper for ET compatibility - drops the parser

def _wrap_et_loader(loader):
    def load(href, parse, encoding=None, parser=None):
        return loader(href, parse, encoding)
    return load


##
# Expand XInclude directives.
#
# @param elem Root element.
# @param loader Optional resource loader.  If omitted, it defaults
#     to {@link default_loader}.  If given, it should be a callable
#     that implements the same interface as <b>default_loader</b>.
# @throws FatalIncludeError If the function fails to include a given
#     resource, or if the tree contains malformed XInclude elements.
# @throws IOError If the function fails to load a given resource.
# @returns the node or its replacement if it was an XInclude node

def include(elem, loader=None):
    if hasattr(elem, 'getroot'):
        #if hasattr(elem, 'docinfo'):
        #    base_url = elem.docinfo.URL
        _include(elem.getroot(), loader)
    else:
        _include(elem, loader)

def _include(elem, loader=None, _parent_hrefs=None):
    if loader is not None:
        load_include = _wrap_et_loader(loader)
    else:
        load_include = _lxml_default_loader

    if _parent_hrefs is None:
        _parent_hrefs = set()

    parser = elem.getroottree().parser

    include_elements = list(
        elem.getiterator('{http://www.w3.org/2001/XInclude}*'))

    for e in include_elements:
        if e.tag == XINCLUDE_INCLUDE:
            # process xinclude directive
            href = e.get("href")
            parse = e.get("parse", "xml")
            parent = e.getparent()
            if parse == "xml":
                if href in _parent_hrefs:
                    raise FatalIncludeError(
                        "recursive include of %r detected" % href
                        )
                _parent_hrefs.add(href)
                node = load_include(href, parse, parser=parser)
                if node is None:
                    raise FatalIncludeError(
                        "cannot load %r as %r" % (href, parse)
                        )
                node = _include(node, loader, _parent_hrefs)
                if e.tail:
                    node.tail = (node.tail or "") + e.tail
                if parent is None:
                    return node # replaced the root node!
                parent.replace(e, node)
            elif parse == "text":
                text = load_include(href, parse, encoding=e.get("encoding"))
                if text is None:
                    raise FatalIncludeError(
                        "cannot load %r as %r" % (href, parse)
                        )
                predecessor = e.getprevious()
                if predecessor is not None:
                    predecessor.tail = (predecessor.tail or "") + text
                elif parent is None:
                    return text # replaced the root node!
                else:
                    parent.text = (parent.text or "") + text + (e.tail or "")
                parent.remove(e)
            else:
                raise FatalIncludeError(
                    "unknown parse type in xi:include tag (%r)" % parse
                )
        elif e.tag == XINCLUDE_FALLBACK:
            parent = e.getparent()
            if parent is not None and parent.tag != XINCLUDE_INCLUDE:
                raise FatalIncludeError(
                    "xi:fallback tag must be child of xi:include (%r)" % e.tag
                    )
        else:
            raise FatalIncludeError(
                "Invalid element found in XInclude namespace (%r)" % e.tag
                )
    return elem
