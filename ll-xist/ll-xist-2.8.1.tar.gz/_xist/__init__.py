#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

## Copyright 1999-2004 by LivingLogic AG, Bayreuth, Germany.
## Copyright 1999-2004 by Walter D�rwald
##
## All Rights Reserved
##
## Permission to use, copy, modify, and distribute this software and its documentation
## for any purpose and without fee is hereby granted, provided that the above copyright
## notice appears in all copies and that both that copyright notice and this permission
## notice appear in supporting documentation, and that the name of LivingLogic AG or
## the author not be used in advertising or publicity pertaining to distribution of the
## software without specific, written prior permission.
##
## LIVINGLOGIC AG AND THE AUTHOR DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
## INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL
## LIVINGLOGIC AG OR THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL
## DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
## IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
## IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
<par>&xist; is an extensible &html;/&xml; generator written in Python.
&xist; is also a &dom; parser (built on top of &sax;2) with a very simple and
pythonesque tree &api;. Every &xml; element type corresponds to a Python class and these
Python classes provide a conversion method to transform the &xml; tree (e.g. into
&html;). &xist; can be considered <z>object oriented &xsl;</z>.</par>

<par>Some of the significant features of &xist; include:</par>
<ulist>
<item>Easily extensible with new &xml; elements,</item>
<item>Can be used for offline or online page generation,</item>
<item>Allows embedding Python code in &xml; files,</item>
<item>Supports separation of layout and logic,</item>
<item>Can be used together with <link href="http://www.modpython.org/">mod_python</link>,
<link href="http://pywx.idyll.org/">PyWX</link> or <link href="http://webware.sf.net/">Webware</link>
to generate dynamic pages,</item>
<item>Fully supports Unicode and &xml; namespaces,</item>
<item>Provides features to use &xist; together with &jsp;/Struts (when replacing
Struts tag libraries with &xist; this speeds up pages by a factor of 5&ndash;10.)</item>
</ulist>

<par>&xist; was written as a replacement for the
<link href="http://www.linguistik.uni-erlangen.de/~msbethke/software.html">&html; preprocessor &hsc;</link>,
and borrows some features and ideas from it.</par>

<par>It also borrows the basic ideas (&xml;/&html; elements as Python
objects) from
<link href="http://starship.python.net/crew/friedrich/HTMLgen/html/main.html">HTMLgen</link>
and <link href="http://dustman.net/andy/python/HyperText/">HyperText</link>.</par>
"""

__version__ = tuple(map(int, "$Revision: 2.26 $"[11:-2].split(".")))
# $Source: /data/cvsroot/LivingLogic/xist/_xist/__init__.py,v $

__all__ = ["xsc", "publishers", "presenters", "parsers", "converters", "sims", "xnd", "ns"]

