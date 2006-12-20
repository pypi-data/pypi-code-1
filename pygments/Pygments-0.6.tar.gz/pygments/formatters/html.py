# -*- coding: utf-8 -*-
"""
    pygments.formatters.html
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter for HTML output.

    :copyright: 2006 by Georg Brandl, Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import sys, os
import cStringIO

from pygments.formatter import Formatter
from pygments.token import Token, Text, STANDARD_TYPES
from pygments.util import get_bool_opt, get_int_opt


__all__ = ['HtmlFormatter']


def escape_html(text):
    """Escape &, <, > as well as single and double quotes for HTML."""
    return text.replace('&', '&amp;').  \
                replace('<', '&lt;').   \
                replace('>', '&gt;').   \
                replace('"', '&quot;'). \
                replace("'", '&#39;')


def get_random_id():
    """Return a random id for javascript fields."""
    from random import random
    from time import time
    try:
        from hashlib import sha1 as sha
    except ImportError:
        import sha
        sha = sha.new
    return sha('%s|%s' % (random(), time())).hexdigest()


def _get_ttype_class(ttype):
    fname = STANDARD_TYPES.get(ttype)
    if fname:
        return fname
    aname = ''
    while fname is None:
        aname = '-' + ttype[-1] + aname
        ttype = ttype.parent
        fname = STANDARD_TYPES.get(ttype, '')
    return fname + aname


DOC_TEMPLATE = '''\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>
  <title>%(title)s</title>
  <meta http-equiv="content-type" content="text/html; charset=%(encoding)s">
  <style type="text/css">
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
%(styledefs)s
  </style>
</head>
<body>
<h2>%(title)s</h2>

%(code)s

</body>
</html>
'''


DOC_TEMPLATE_EXTERNALCSS = '''\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>
  <title>%(title)s</title>
  <meta http-equiv="content-type" content="text/html; charset=%(encoding)s">
  <link rel="stylesheet" href="%(cssfile)s">
</head>
<body>
<h2>%(title)s</h2>

%(code)s

</body>
</html>
'''


CSSFILE_TEMPLATE = '''\
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
%(styledefs)s
'''


class HtmlFormatter(Formatter):
    """
    Output HTML <span> tags with appropriate classes.

    Additional options accepted:

    ``nowrap``
        If set to true, don't wrap the tokens at all. This disables
        all other options (default: False).
    ``noclasses``
        If set to true, token <span>s will not use CSS classes, but
        inline styles.
    ``classprefix``
        Prefix for token CSS classes, is prepended to all token style
        classes (e.g. class="o" -> class="_o" if classprefix == '_')
        (default: '').
    ``cssclass``
        CSS class for the wrapping <div> (default: 'highlight').
    ``cssstyles``
        Inline CSS styles for the wrapping <div>. (default: '').
    ``cssfile``
        If the ``full`` option is ``True`` and this is not ``''``,
        put the CSS in a separate file whose name is given by this option
        (default: ''). New in 0.6.
    ``linenos``
        If set to ``True``, output line numbers (default: False).
    ``linenostart``
        The line number for the first line (default: 1).
    ``linenostep``
        If set to a number n > 1, only every nth line number is printed
        (default: 1).
    ``linenospecial``
        If set to a number n > 0, every nth line number is given a special
        CSS class ``special`` (default: 0).
    ``nobackground``
        If set to ``True`` the formatter won't output the background color
        for the overall element (this automatically defaults to ``False``
        when there is no overall element [eg: no argument for the
        `get_syntax_defs` method given]) (default: ``False``). New in 0.6.
    """

    def __init__(self, **options):
        Formatter.__init__(self, **options)
        self.nowrap = get_bool_opt(options, 'nowrap', False)
        self.noclasses = get_bool_opt(options, 'noclasses', False)
        self.classprefix = options.get('classprefix', '')
        self.cssclass = options.get('cssclass', 'highlight')
        self.cssstyles = options.get('cssstyles', '')
        self.cssfile = options.get('cssfile', '')
        self.linenos = get_bool_opt(options, 'linenos', False)
        self.linenostart = abs(get_int_opt(options, 'linenostart', 1))
        self.linenostep = abs(get_int_opt(options, 'linenostep', 1))
        self.linenospecial = abs(get_int_opt(options, 'linenospecial', 0))
        self.nobackground = get_bool_opt(options, 'nobackground', False)

        self._class_cache = {}
        self._create_stylesheet()

    def _get_css_class(self, ttype):
        """Return the css class of this token type prefixed with
        the classprefix option."""
        if ttype in self._class_cache:
            return self._class_cache[ttype]
        return self.classprefix + _get_ttype_class(ttype)

    def _create_stylesheet(self):
        t2c = self.ttype2class = {Token: ''}
        c2s = self.class2style = {}
        cp = self.classprefix
        for ttype, ndef in self.style:
            name = cp + _get_ttype_class(ttype)
            style = ''
            if ndef['color']:
                style += 'color: #%s; ' % ndef['color']
            if ndef['bold']:
                style += 'font-weight: bold; '
            if ndef['italic']:
                style += 'font-style: italic; '
            if ndef['underline']:
                style += 'text-decoration: underline; '
            if ndef['bgcolor']:
                style += 'background-color: #%s; ' % ndef['bgcolor']
            if ndef['border']:
                style += 'border: 1px solid #%s; ' % ndef['border']
            if style:
                t2c[ttype] = name
                # save len(ttype) to enable ordering the styles by
                # hierarchy (necessary for CSS cascading rules!)
                c2s[name] = (style[:-2], ttype, len(ttype))

    def get_style_defs(self, arg=''):
        """
        Return CSS style definitions for the classes produced by the
        current highlighting style. ``arg`` can be a string of selectors
        to insert before the token type classes.
        """
        if isinstance(arg, basestring):
            args = [arg]
        else:
            args = list(arg)

        def prefix(cls):
            tmp = []
            for arg in args:
                tmp.append((arg and arg + ' ' or '') + '.' + cls)
            return ', '.join(tmp)

        styles = [(level, ttype, cls, style)
                  for cls, (style, ttype, level) in self.class2style.iteritems()
                  if cls and style]
        styles.sort()
        lines = ['%s { %s } /* %s */' % (prefix(cls), style, repr(ttype)[6:])
                 for level, ttype, cls, style in styles]
        if arg and not self.nobackground and \
           self.style.background_color is not None:
            text_style = ''
            if Text in self.ttype2class:
                text_style = ' ' + self.class2style[self.ttype2class[Text]][0]
            lines.insert(0, '%s{ background: %s;%s }' %
                         (arg, self.style.background_color, text_style))
        return '\n'.join(lines)

    def _format_nowrap(self, tokensource, outfile, lnos=False):
        lncount = 0
        nocls = self.noclasses
        enc = self.encoding
        # for <span style=""> lookup only
        getcls = self.ttype2class.get
        c2s = self.class2style

        write = outfile.write
        lspan = ''
        for ttype, value in tokensource:
            if enc:
                value = value.encode(enc)
            htmlvalue = escape_html(value)
            if lnos:
                lncount += value.count("\n")

            if nocls:
                cclass = getcls(ttype)
                while cclass is None:
                    ttype = ttype.parent
                    cclass = getcls(ttype)
                cspan = cclass and '<span style="%s">' % c2s[cclass][0]
            else:
                cls = self._get_css_class(ttype)
                cspan = cls and '<span class="%s">' % cls

            if cspan == lspan:
                if not cspan:
                    write(htmlvalue)
                else:
                    write(htmlvalue.replace('\n', '</span>\n' + cspan))
            elif htmlvalue: # if no value, leave old span open
                if lspan:
                    write('</span>')
                lspan = cspan
                if cspan:
                    htmlvalue = htmlvalue.replace('\n', '</span>\n' + cspan)
                    write(cspan + htmlvalue)
                else:
                    write(htmlvalue)
        if lspan:
            write('</span>')
        return lncount

    def format(self, tokensource, outfile):
        if self.nowrap:
            self._format_nowrap(tokensource, outfile)
            return

        realoutfile = outfile
        lnos = self.linenos
        full = self.full

        div = ('<div' + (self.cssclass and ' class="%s" ' % self.cssclass)
               + (self.cssstyles and ' style="%s"' % self.cssstyles) + '>')
        if full or lnos:
            outfile = cStringIO.StringIO()
        else:
            outfile.write(div)

        outfile.write('<pre>')
        lncount = self._format_nowrap(tokensource, outfile, lnos)
        outfile.write('</pre>')

        ret = ''
        if lnos:
            fl = self.linenostart
            mw = len(str(lncount + fl - 1))
            sp = self.linenospecial
            st = self.linenostep
            if sp:
                ls = '\n'.join([(i%st == 0 and
                                 (i%sp == 0 and '<span class="special">%*d</span>'
                                  or '%*d') % (mw, i)
                                 or '')
                                for i in range(fl, fl + lncount)])
            else:
                ls = '\n'.join([(i%st == 0 and ('%*d' % (mw, i)) or '')
                                for i in range(fl, fl + lncount)])

            ret = div + ('<table><tr>'
                         '<td class="linenos"><pre>' +
                         ls + '</pre></td><td class="code">')
            ret += outfile.getvalue()
            ret += '</td></tr></table>'

        if full:
            if not ret:
                ret = div + outfile.getvalue() + '</div>\n'
            if self.cssfile:
                try:
                    filename = realoutfile.name
                    cssfilename = os.path.join(os.path.dirname(filename), self.cssfile)
                except AttributeError:
                    print >>sys.stderr, 'Note: Cannot determine output file name, ' \
                          'using current directory as base for the CSS file name'
                    cssfilename = self.cssfile
                realoutfile.write(DOC_TEMPLATE_EXTERNALCSS %
                                  dict(title     = self.title,
                                       cssfile   = self.cssfile,
                                       encoding  = self.encoding,
                                       code      = ret))
                try:
                    cf = open(cssfilename, "w")
                    cf.write(CSSFILE_TEMPLATE % {'styledefs':
                                                 self.get_style_defs('body')})
                    cf.close()
                except IOError, err:
                    err.strerror = 'Error writing CSS file: ' + err.strerror
                    raise
            else:
                realoutfile.write(DOC_TEMPLATE %
                                  dict(title     = self.title,
                                       styledefs = self.get_style_defs('body'),
                                       encoding  = self.encoding,
                                       code      = ret))
        elif lnos:
            realoutfile.write(ret + '</div>\n')
        else:
            realoutfile.write('</div>\n')
