#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

## Copyright 1999-2005 by LivingLogic AG, Bayreuth/Germany.
## Copyright 1999-2005 by Walter D�rwald
##
## All Rights Reserved
##
## See xist/__init__.py for the license

"""
<par>An &xist; namespace that contains definitions for all the elements
in <link href="http://www.w3.org/TR/html4/loose.dtd">&html; 4.0 transitional</link>.</par>
"""

__version__ = tuple(map(int, "$Revision: 2.69 $"[11:-2].split(".")))
# $Source: /data/cvsroot/LivingLogic/xist/_xist/ns/html.py,v $

import cgi # for parse_header

from ll.xist import xsc, utils, sims
from ll.xist.ns import xml


# common attributes types
class DirAttr(xsc.TextAttr): "direction for weak/neutral text"; values = (u"ltr", u"rtl")
class ContentTypeAttr(xsc.TextAttr): "media type, as per [RFC2045]"
class ContentTypesAttr(xsc.TextAttr): "comma-separated list of media types, as per [RFC2045]"
class CharsetAttr(xsc.TextAttr): "a character encoding, as per [RFC2045]"
class CharsetsAttr(xsc.TextAttr): "a space separated list of character encodings, as per [RFC2045]"
class LanguageCodeAttr(xsc.TextAttr): "a language code, as per [RFC3066]"
class CharacterAttr(xsc.TextAttr): "a single character, as per section 2.2 of [XML]"
class LinkTypesAttr(xsc.TextAttr): "space-separated list of link types"
class MediaDescAttr(xsc.TextAttr): "single or comma-separated list of media descriptors"
class URIListAttr(xsc.TextAttr): "a space separated list of Uniform Resource Identifiers"
class DatetimeAttr(xsc.TextAttr): "date and time information. ISO date format"
class ScriptAttr(xsc.TextAttr): "script expression"
class StyleSheetAttr(xsc.StyleAttr): "style sheet data"
class TextAttr(xsc.TextAttr): "used for titles etc."
class FrameTargetAttr(xsc.TextAttr): "render in this frame"
class LengthAttr(xsc.TextAttr): "<rep>nn</rep> for pixels or <rep>nn%</rep> for percentage length"
class MultiLengthAttr(xsc.TextAttr): "pixel, percentage, or relative"
class PixelsAttr(xsc.IntAttr): "integer representing length in pixels"
class ShapeAttr(xsc.TextAttr): "image shapes"; values = (u"rect", u"circle", u"poly", u"default")
class CoordsAttr(xsc.TextAttr): "comma separated list of lengths"
class ImgAlignAttr(xsc.TextAttr): "image alignment"; values = (u"top", u"middle", u"bottom", u"left", u"right", u"absmiddle")
class ColorAttr(xsc.ColorAttr): "a color using sRGB: #RRGGBB as Hex values"
class TextAlignAttr(xsc.TextAttr): "text alignment"; values = (u"left", u"right", u"center", u"justify")
class OLStyleAttr(xsc.TextAttr): values = "1aAiI"
class ULStyleAttr(xsc.TextAttr): values = (u"disc", u"square", u"circle")
class InputTypeAttr(xsc.TextAttr): values = (u"text", u"password", u"checkbox", u"radio", u"submit", u"reset", u"file", u"hidden", u"image", u"button")
class TRulesAttr(xsc.TextAttr): values = (u"none", u"groups", u"rows", u"cols", u"all")
class TAlignAttr(xsc.TextAttr): values = (u"left", u"right", u"center")
class CAlignAttr(xsc.TextAttr): values = (u"top", u"bottom", u"left", u"right")
class TFrameAttr(xsc.TextAttr): values = (u"void", u"above", u"below", u"hsides", u"lhs", u"rhs", u"vsides", u"box", u"border")
class ScopeAttr(xsc.TextAttr): values = (u"row", u"col", u"rowgroup", u"colgroup")


# common attributes sets
class coreattrs(xsc.Element.Attrs):
	"core attributes common to most elements"
	class id(xsc.IDAttr): "document-wide unique id"
	class class_(xsc.TextAttr): "space separated list of classes"; xmlname = "class"
	class style(StyleSheetAttr): "associated style info"
	class title(TextAttr): "advisory title/amplification"


class i18nattrs(xsc.Element.Attrs):
	"internationalization attributes"
	class lang(LanguageCodeAttr): "language code (backwards compatible)"
	class dir(DirAttr): pass


class eventattrs(xsc.Element.Attrs):
	"attributes for common UI events"
	class onclick(ScriptAttr): "a pointer button was clicked"
	class ondblclick(ScriptAttr): "a pointer button was double clicked"
	class onmousedown(ScriptAttr): "a pointer button was pressed down"
	class onmouseup(ScriptAttr): "a pointer button was released"
	class onmousemove(ScriptAttr): "a pointer was moved onto the element"
	class onmouseover(ScriptAttr): "a pointer was moved onto the element" # deprecated
	class onmouseout(ScriptAttr): "a pointer was moved away from the element"
	class onkeypress(ScriptAttr): "a key was pressed and released"
	class onkeydown(ScriptAttr): "a key was pressed down"
	class onkeyup(ScriptAttr): "a key was released"


class focusattrs(xsc.Element.Attrs):
	"attributes for elements that can get the focus"
	class accesskey(CharacterAttr): "accessibility key character"
	class tabindex(xsc.IntAttr): "position in tabbing order"
	class onfocus(ScriptAttr): "the element got the focus"
	class onblur(ScriptAttr): "the element lost the focus"


class allattrs(coreattrs, i18nattrs, eventattrs):
	pass


class cellhalignattrs(xsc.Element.Attrs):
	class align(xsc.TextAttr): values = ("left", "center", "right", "justify", "char")
	class char(CharacterAttr): pass
	class charoff(LengthAttr): pass


class cellvalignattrs(xsc.Element.Attrs):
	class valign(xsc.TextAttr): values = ("top", "middle", "bottom", "baseline")


class DocTypeHTML40transitional(xsc.DocType):
	"""
	document type for HTML 4.0 transitional
	"""
	def __init__(self):
		xsc.DocType.__init__(self, 'html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd"')


class DocTypeHTML401transitional(xsc.DocType):
	"""
	document type for HTML 4.01 transitional
	"""
	def __init__(self):
		xsc.DocType.__init__(self, 'html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"')


class DocTypeXHTML10strict(xsc.DocType):
	"""
	document type for XHTML 1.0 strict
	"""
	def __init__(self):
		xsc.DocType.__init__(self, 'html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"')


class DocTypeXHTML10transitional(xsc.DocType):
	"""
	document type for XHTML 1.0 transitional
	"""
	def __init__(self):
		xsc.DocType.__init__(self, 'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"')


class DocTypeXHTML11(xsc.DocType):
	"""
	document type for XHTML 1.1
	"""
	def __init__(self):
		xsc.DocType.__init__(self, 'html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"')


# The global structure of an HTML document
class html(xsc.Element):
	"""
	Document Structure
	"""
	class Attrs(i18nattrs):
		class id(xsc.IDAttr): pass

	def convert(self, converter):
		if converter.lang is not None and (unicode(self["lang"].convert(converter)) != converter.lang or unicode(self[(xml, "lang")].convert(converter)) != converter.lang):
			node = html(self.content, self.attrs, {"lang": converter.lang, (xml, "lang"): converter.lang})
			return node.convert(converter)
		else:
			return super(html, self).convert(converter)


class head(xsc.Element):
	"""
	Document Head
	"""
	class Attrs(i18nattrs):
		class id(xsc.IDAttr): pass
		class profile(xsc.URLAttr): pass


class title(xsc.Element):
	"""
	document title
	"""
	class Attrs(i18nattrs):
		class id(xsc.IDAttr): pass

	def unwrapHTML(self, node, converter):
		if isinstance(node, xsc.Element) and issubclass(node.__ns__, __ns__): # is this one of our own elements => filter it out
			if isinstance(node, img):
				node = node["alt"]
			else:
				node = node.content.mapped(self.unwrapHTML, converter)
		return node

	def convert(self, converter):
		content = self.content.convert(converter)
		content = content.mapped(self.unwrapHTML, converter)
		return title(content, self.attrs)


class base(xsc.Element):
	"""
	document base URI
	"""
	model = sims.Empty()
	class Attrs(xsc.Element.Attrs):
		class id(xsc.IDAttr): pass
		class href(xsc.URLAttr): pass
		class target(FrameTargetAttr): pass


class meta(xsc.Element):
	"""
	generic metainformation. If the <lit>http-equiv</lit> attribute
	has the value "content-type" the encoding in the <lit>content</lit>
	attribute will be set automatically when publishing.
	"""
	model = sims.Empty()
	class Attrs(i18nattrs):
		class id(xsc.IDAttr): pass
		class http_equiv(xsc.TextAttr): xmlname = "http-equiv"
		class name(xsc.TextAttr): pass
		class content(xsc.TextAttr): required = True
		class scheme(xsc.TextAttr): pass

	def publish(self, publisher):
		if u"http_equiv" in self.attrs:
			ctype = unicode(self[u"http_equiv"]).lower()
			if ctype == u"content-type" and u"content" in self.attrs:
				(contenttype, options) = cgi.parse_header(unicode(self[u"content"]))
				if u"charset" not in options or options[u"charset"] != publisher.encoding:
					options[u"charset"] = publisher.encoding
					node = self.__class__(
						self.attrs,
						http_equiv=u"Content-Type",
						content=(contenttype, u"; ", u"; ".join(u"%s=%s" % option for option in options.items()))
					)
					return node.publish(publisher) # return a generator-iterator
		return super(meta, self).publish(publisher) # return a generator-iterator


class link(xsc.Element):
	"""
	a media-independent link
	"""
	model = sims.Empty()
	class Attrs(allattrs):
		class charset(CharsetAttr): pass
		class href(xsc.URLAttr): pass
		class hreflang(LanguageCodeAttr): pass
		class type(ContentTypeAttr): pass
		class rel(LinkTypesAttr): pass
		class rev(LinkTypesAttr): pass
		class media(MediaDescAttr): pass
		class target(FrameTargetAttr): pass


class style(xsc.Element):
	"""
	style info, which may include CDATA sections
	"""
	model = sims.NoElements()
	class Attrs(i18nattrs):
		class id(xsc.IDAttr): pass
		class type(ContentTypeAttr): required = True
		class media(MediaDescAttr): pass
		class title(TextAttr): pass


class script(xsc.Element):
	"""
	script statements, which may include CDATA sections
	"""
	model = sims.NoElements()
	class Attrs(xsc.Element.Attrs):
		class id(xsc.IDAttr): pass
		class charset(CharsetAttr): pass
		class type(ContentTypeAttr): required = True
		class language(xsc.TextAttr): pass
		class src(xsc.URLAttr): pass
		class defer(xsc.BoolAttr): pass


class noscript(xsc.Element):
	"""
	alternate content container for non script-based rendering
	"""
	class Attrs(allattrs):
		pass


class iframe(xsc.Element):
	"""
	inline subwindow
	"""
	class Attrs(coreattrs):
		class longdesc(xsc.URLAttr): pass
		class name(xsc.TextAttr): pass
		class src(xsc.URLAttr): pass
		class frameborder(xsc.TextAttr): values = (1, 0)
		class marginwidth(PixelsAttr): pass
		class marginheight(PixelsAttr): pass
		class noresize(xsc.BoolAttr): pass # deprecated
		class scrolling(xsc.TextAttr): values = (u"yes", u"no", u"auto")
		class align(ImgAlignAttr): pass
		class height(LengthAttr): pass
		class width(LengthAttr): pass
		class hspace(xsc.IntAttr): pass # deprecated
		class vspace(xsc.IntAttr): pass # deprecated
		class bordercolor(xsc.ColorAttr): pass # deprecated


class noframes(xsc.Element):
	"""
	alternate content container for non frame-based rendering
	"""
	class Attrs(allattrs):
		pass


class body(xsc.Element):
	"""
	document body
	"""
	class Attrs(allattrs):
		class onload(ScriptAttr): pass
		class onunload(ScriptAttr): pass
		class onfocus(xsc.TextAttr): pass # deprecated
		class background(xsc.URLAttr): pass # deprecated
		class bgcolor(xsc.ColorAttr): pass # deprecated
		class text(xsc.ColorAttr): pass # deprecated
		class link(xsc.ColorAttr): pass # deprecated
		class vlink(xsc.ColorAttr): pass # deprecated
		class alink(xsc.ColorAttr): pass # deprecated
		class leftmargin(xsc.IntAttr): pass # deprecated
		class topmargin(xsc.IntAttr): pass # deprecated
		class marginwidth(xsc.IntAttr): pass # deprecated
		class marginheight(xsc.IntAttr): pass # deprecated


class div(xsc.Element):
	"""
	generic language/style container
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class p(xsc.Element):
	"""
	paragraph
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class h1(xsc.Element):
	"""
	heading
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class h2(xsc.Element):
	"""
	heading
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class h3(xsc.Element):
	"""
	heading
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class h4(xsc.Element):
	"""
	heading
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class h5(xsc.Element):
	"""
	heading
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class h6(xsc.Element):
	"""
	heading
	"""
	class Attrs(allattrs):
		class align(TextAlignAttr): pass


class ul(xsc.Element):
	"""
	unordered list
	"""
	class Attrs(allattrs):
		class type(ULStyleAttr): pass
		class compact(xsc.BoolAttr): pass


class ol(xsc.Element):
	"""
	ordered list
	"""
	class Attrs(allattrs):
		class type(OLStyleAttr): pass
		class compact(xsc.BoolAttr): pass
		class start(xsc.IntAttr): pass


class menu(xsc.Element):
	"""
	single column list (deprecated)
	"""
	class Attrs(allattrs):
		class compact(xsc.BoolAttr): pass


class dir(xsc.Element):
	"""
	multiple column list (deprecated)
	"""
	class Attrs(allattrs):
		class compact(xsc.BoolAttr): pass


class li(xsc.Element):
	"""
	list item
	"""
	class Attrs(allattrs):
		class type(xsc.TextAttr): pass
		class value(xsc.IntAttr): pass


class dl(xsc.Element):
	"""
	definition list
	"""
	class Attrs(allattrs):
		class compact(xsc.BoolAttr): pass


class dt(xsc.Element):
	"""
	definition term
	"""
	class Attrs(allattrs):
		pass


class dd(xsc.Element):
	"""
	definition description
	"""
	class Attrs(allattrs):
		pass


class address(xsc.Element):
	"""
	information on author
	"""
	class Attrs(allattrs):
		pass


class hr(xsc.Element):
	"""
	horizontal rule
	"""
	model = sims.Empty()
	class Attrs(allattrs):
		class align(xsc.TextAttr): values = (u"left", u"right", u"center")
		class noshade(xsc.BoolAttr): pass
		class size(PixelsAttr): pass
		class width(LengthAttr): pass # deprecated
		class color(xsc.ColorAttr): pass # deprecated


class pre(xsc.Element):
	"""
	preformatted text
	"""
	class Attrs(allattrs):
		class width(xsc.IntAttr): pass


class blockquote(xsc.Element):
	"""
	block-like quotes
	"""
	class Attrs(allattrs):
		class cite(xsc.URLAttr): pass


class center(xsc.Element): # deprecated
	"""
	centered block level element
	"""
	class Attrs(allattrs):
		pass


class ins(xsc.Element):
	"""
	inserted text
	"""
	class Attrs(allattrs):
		class cite(xsc.URLAttr): pass
		class datetime(DatetimeAttr): pass


class del_(xsc.Element):
	"""
	deleted text
	"""
	xmlname = "del"
	class Attrs(allattrs):
		class cite(xsc.URLAttr): pass
		class datetime(DatetimeAttr): pass


class a(xsc.Element):
	"""
	anchor
	"""
	class Attrs(allattrs, focusattrs):
		class charset(CharsetAttr): pass
		class type(ContentTypeAttr): pass
		class name(xsc.TextAttr): pass
		class href(xsc.URLAttr): pass
		class hreflang(LanguageCodeAttr): pass
		class rel(LinkTypesAttr): pass
		class rev(LinkTypesAttr): pass
		class shape(ShapeAttr): pass
		class coords(CoordsAttr): pass
		class target(FrameTargetAttr): pass
		class oncontextmenu(xsc.TextAttr): pass # deprecated


class span(xsc.Element):
	"""
	generic language/style container
	"""
	class Attrs(allattrs):
		pass


class bdo(xsc.Element):
	"""
	I18N BiDi over-ride
	"""
	class Attrs(coreattrs, eventattrs):
		class lang(LanguageCodeAttr): pass
		class dir(DirAttr): required = True


class br(xsc.Element):
	"""
	forced line break
	"""
	model = sims.Empty()
	class Attrs(coreattrs):
		class clear(xsc.TextAttr): values = (u"left", u"all", u"right", u"none")


class em(xsc.Element):
	"""
	Indicates emphasis.
	"""
	class Attrs(allattrs):
		pass


class strong(xsc.Element):
	"""
	Indicates stronger emphasis than em.
	"""
	class Attrs(allattrs):
		pass


class dfn(xsc.Element):
	"""
	Indicates that this is the defining instance of the enclosed term.
	"""
	class Attrs(allattrs):
		pass


class code(xsc.Element):
	"""
	Designates a fragment of computer code.
	"""
	class Attrs(allattrs):
		pass


class samp(xsc.Element):
	"""
	Designates sample output from programs, scripts, etc.
	"""
	class Attrs(allattrs):
		pass


class kbd(xsc.Element):
	"""
	Indicates text to be entered by the user.
	"""
	class Attrs(allattrs):
		pass


class var(xsc.Element):
	"""
	Indicates an instance of a variable or program argument.
	"""
	class Attrs(allattrs):
		pass


class cite(xsc.Element):
	"""
	Contains a citation or a reference to other sources.
	"""
	class Attrs(allattrs):
		pass


class abbr(xsc.Element):
	"""
	Indicates an abbreviated form (e.g., WWW, HTTP, URI, Mass., etc.)
	"""
	class Attrs(allattrs):
		pass


class acronym(xsc.Element):
	"""
	Indicates an acronym (e.g., WAC, radar, etc.).
	"""
	class Attrs(allattrs):
		pass


class q(xsc.Element):
	"""
	short inline quotation
	"""
	class Attrs(allattrs):
		class cite(xsc.URLAttr): pass


class sub(xsc.Element):
	"""
	subscript
	"""
	class Attrs(allattrs):
		pass


class sup(xsc.Element):
	"""
	superscript
	"""
	class Attrs(allattrs):
		pass


class tt(xsc.Element):
	"""
	teletype or monospaced text style
	"""
	class Attrs(allattrs):
		pass


class i(xsc.Element):
	"""
	italic text style
	"""
	class Attrs(allattrs):
		pass


class b(xsc.Element):
	"""
	bold text style
	"""
	class Attrs(allattrs):
		pass


class big(xsc.Element):
	"""
	large text style
	"""
	class Attrs(allattrs):
		pass


class small(xsc.Element):
	"""
	small text style
	"""
	class Attrs(allattrs):
		pass


class u(xsc.Element):
	"""
	underline text style
	"""
	class Attrs(allattrs):
		pass


class s(xsc.Element):
	"""
	strike-through text style
	"""
	class Attrs(allattrs):
		pass


class strike(xsc.Element):
	"""
	strike-through text style
	"""
	class Attrs(allattrs):
		pass


class basefont(xsc.Element): # deprecated
	"""
	base font size
	"""
	model = sims.Empty()
	class Attrs(coreattrs, i18nattrs):
		class id(xsc.IDAttr): pass
		class size(xsc.TextAttr): required = True
		class color(xsc.ColorAttr): pass
		class face(xsc.TextAttr): pass


class font(xsc.Element): # deprecated
	"""
	local change to font
	"""
	class Attrs(coreattrs, i18nattrs):
		class face(xsc.TextAttr): pass
		class size(xsc.TextAttr): pass
		class color(xsc.ColorAttr): pass


class object(xsc.Element):
	"""
	generic embedded object
	"""
	class Attrs(allattrs):
		class declare(xsc.BoolAttr): pass
		class classid(xsc.URLAttr): pass
		class codebase(xsc.URLAttr): pass
		class data(xsc.URLAttr): pass
		class type(ContentTypeAttr): pass
		class codetype(ContentTypeAttr): pass
		class archive(URIListAttr): pass
		class standby(TextAttr): pass
		class height(LengthAttr): pass
		class width(LengthAttr): pass
		class usemap(xsc.URLAttr): pass
		class name(xsc.TextAttr): pass
		class tabindex(xsc.IntAttr): pass
		class align(ImgAlignAttr): pass
		class border(PixelsAttr): pass
		class hspace(PixelsAttr): pass
		class vspace(PixelsAttr): pass


class param(xsc.Element):
	"""
	named property value
	"""
	model = sims.Empty()
	class Attrs(xsc.Element.Attrs):
		class id(xsc.IDAttr): pass
		class name(xsc.TextAttr): required = True
		class value(xsc.TextAttr): pass
		class valuetype(xsc.TextAttr): values = (u"data", u"ref", u"object")
		class type(ContentTypeAttr): pass


class applet(xsc.Element): # deprecated
	"""
	Java applet
	"""
	class Attrs(coreattrs):
		class codebase(xsc.URLAttr): pass
		class archive(xsc.TextAttr): pass
		class code(xsc.TextAttr): pass
		class object(xsc.TextAttr): pass
		class alt(TextAttr): pass
		class name(xsc.TextAttr): pass
		class width(LengthAttr): required = True
		class height(LengthAttr): required = True
		class align(ImgAlignAttr): pass
		class hspace(PixelsAttr): pass
		class vspace(PixelsAttr): pass


class img(xsc.Element):
	"""
	Embedded image
	"""
	model = sims.Empty()
	class Attrs(allattrs):
		class src(xsc.URLAttr): required = True
		class alt(TextAttr): required = True
		class name(xsc.TextAttr): pass
		class longdesc(xsc.URLAttr): pass
		class width(LengthAttr): pass
		class height(LengthAttr): pass
		class usemap(xsc.URLAttr): pass
		class ismap(xsc.BoolAttr): pass
		class align(ImgAlignAttr): pass
		class border(LengthAttr): pass
		class hspace(PixelsAttr): pass
		class vspace(PixelsAttr): pass
		class lowsrc(xsc.URLAttr): pass # deprecated

	def __unicode__(self):
		return unicode(self["alt"])


class map(xsc.Element):
	"""
	client-side image map
	"""
	class Attrs(i18nattrs, eventattrs):
		class id(xsc.IDAttr): required = True
		class class_(xsc.TextAttr): pass
		class style(StyleSheetAttr): pass
		class title(TextAttr): pass
		class name(xsc.TextAttr): pass


class area(xsc.Element):
	"""
	client-side image map area
	"""
	model = sims.Empty()
	class Attrs(allattrs, focusattrs):
		class shape(ShapeAttr): pass
		class coords(CoordsAttr): pass
		class href(xsc.URLAttr): pass
		class nohref(xsc.BoolAttr): pass
		class alt(TextAttr): required = True
		class target(FrameTargetAttr): pass


class form(xsc.Element):
	"""
	interactive form
	"""
	class Attrs(allattrs):
		class action(xsc.URLAttr): required = True
		class method(xsc.TextAttr): values = (u"get", u"post")
		class name(xsc.TextAttr): pass
		class enctype(ContentTypeAttr): pass
		class onsubmit(ScriptAttr): pass
		class onreset(ScriptAttr): pass
		class accept_charset(CharsetsAttr): xmlname = "accept-charset"
		class target(FrameTargetAttr): pass


class label(xsc.Element):
	"""
	form field label text
	"""
	class Attrs(allattrs):
		class for_(xsc.TextAttr): xmlname = "for"
		class accesskey(CharacterAttr): pass
		class onfocus(ScriptAttr): pass
		class onblur(ScriptAttr): pass


class input(xsc.Element):
	"""
	form control
	"""
	model = sims.Empty()
	class Attrs(allattrs, focusattrs):
		class type(InputTypeAttr): pass
		class name(xsc.TextAttr): pass
		class value(xsc.TextAttr): pass
		class checked(xsc.BoolAttr): pass
		class disabled(xsc.BoolAttr): pass
		class readonly(xsc.BoolAttr): pass
		class size(xsc.TextAttr): pass
		class maxlength(xsc.IntAttr): pass
		class src(xsc.URLAttr): pass
		class alt(xsc.TextAttr): pass
		class usemap(xsc.URLAttr): pass
		class onselect(ScriptAttr): pass
		class onchange(ScriptAttr): pass
		class accept(ContentTypesAttr): pass
		class align(ImgAlignAttr): pass
		class border(xsc.IntAttr): pass # deprecated


class select(xsc.Element):
	"""
	option selector
	"""
	class Attrs(allattrs):
		class name(xsc.TextAttr): pass
		class size(xsc.IntAttr): pass
		class multiple(xsc.BoolAttr): pass
		class disabled(xsc.BoolAttr): pass
		class tabindex(xsc.IntAttr): pass
		class onfocus(ScriptAttr): pass
		class onblur(ScriptAttr): pass
		class onchange(ScriptAttr): pass
		class rows(xsc.TextAttr): pass # deprecated


class optgroup(xsc.Element):
	"""
	option group
	"""
	class Attrs(allattrs):
		class disabled(xsc.BoolAttr): pass
		class label(TextAttr): required = True


class option(xsc.Element):
	"""
	selectable choice
	"""
	class Attrs(allattrs):
		class selected(xsc.BoolAttr): pass
		class disabled(xsc.BoolAttr): pass
		class label(TextAttr): pass
		class value(xsc.TextAttr): pass


class textarea(xsc.Element):
	"""
	multi-line text field
	"""
	class Attrs(allattrs, focusattrs):
		class name(xsc.TextAttr): pass
		class rows(xsc.IntAttr): required = True
		class cols(xsc.IntAttr): required = True
		class disabled(xsc.BoolAttr): pass
		class readonly(xsc.BoolAttr): pass
		class onselect(ScriptAttr): pass
		class onchange(ScriptAttr): pass
		class wrap(xsc.TextAttr): values = (u"virtual", u"physical", u"off") # deprecated


class fieldset(xsc.Element):
	"""
	form control group
	"""
	class Attrs(allattrs):
		pass


class legend(xsc.Element):
	"""
	fieldset legend
	"""
	class Attrs(allattrs):
		class accesskey(xsc.TextAttr): pass
		class align(xsc.TextAttr): values = (u"top", u"bottom", u"left", u"right")


class button(xsc.Element):
	"""
	push button
	"""
	class Attrs(allattrs, focusattrs):
		class name(xsc.TextAttr): pass
		class value(xsc.TextAttr): pass
		class type(xsc.TextAttr): values = (u"button", u"submit", u"reset")
		class disabled(xsc.BoolAttr): pass


class isindex(xsc.Element):
	model = sims.Empty()
	class Attrs(coreattrs, i18nattrs):
		class prompt(TextAttr): pass


class table(xsc.Element):
	"""
	table
	"""
	class Attrs(allattrs):
		class summary(TextAttr): pass
		class width(LengthAttr): pass
		class border(PixelsAttr): pass
		class frame(TFrameAttr): pass
		class rules(TRulesAttr): pass
		class cellspacing(LengthAttr): pass
		class cellpadding(LengthAttr): pass
		class align(TAlignAttr): pass
		class bgcolor(xsc.ColorAttr): pass # deprecated
		class height(xsc.TextAttr): pass # deprecated
		class background(xsc.URLAttr): pass # deprecated
		class bordercolor(xsc.ColorAttr): pass # deprecated
		class hspace(xsc.IntAttr): pass # deprecated
		class vspace(xsc.IntAttr): pass # deprecated


class caption(xsc.Element):
	"""
	table caption
	"""
	class Attrs(allattrs):
		class align(CAlignAttr): pass


class colgroup(xsc.Element):
	"""
	table column group
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		class span(xsc.TextAttr): pass
		class width(MultiLengthAttr): pass


class col(xsc.Element):
	"""
	table column
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		class span(xsc.TextAttr): pass
		class width(MultiLengthAttr): pass


class thead(xsc.Element):
	"""
	table header
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		pass


class tfoot(xsc.Element):
	"""
	table footer
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		pass


class tbody(xsc.Element):
	"""
	table body
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		pass


class tr(xsc.Element):
	"""
	table row
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		class bgcolor(xsc.ColorAttr): pass
		class nowrap(xsc.BoolAttr): pass # deprecated
		class width(LengthAttr): pass # deprecated
		class background(xsc.URLAttr): pass # deprecated


class th(xsc.Element):
	"""
	table header cell
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		class abbr(TextAttr): pass
		class axis(xsc.TextAttr): pass
		class headers(xsc.TextAttr): pass
		class scope(ScopeAttr): pass
		class rowspan(xsc.IntAttr): pass
		class colspan(xsc.IntAttr): pass
		class nowrap(xsc.BoolAttr): pass
		class bgcolor(xsc.ColorAttr): pass
		class width(LengthAttr): pass
		class height(LengthAttr): pass
		class background(xsc.URLAttr): pass # deprecated
		class bordercolor(xsc.ColorAttr): pass # deprecated


class td(xsc.Element):
	"""
	table data cell
	"""
	class Attrs(allattrs, cellhalignattrs, cellvalignattrs):
		class abbr(TextAttr): pass
		class axis(xsc.TextAttr): pass
		class headers(xsc.TextAttr): pass
		class scope(ScopeAttr): pass
		class rowspan(xsc.IntAttr): pass
		class colspan(xsc.IntAttr): pass
		class nowrap(xsc.BoolAttr): pass
		class bgcolor(xsc.ColorAttr): pass
		class width(LengthAttr): pass
		class height(LengthAttr): pass
		class background(xsc.URLAttr): pass # deprecated
		class bordercolor(xsc.ColorAttr): pass # deprecated


class embed(xsc.Element):
	"""
	generic embedded object (Internet Exploder)
	"""
	class Attrs(xsc.Element.Attrs):
		class width(xsc.TextAttr): pass
		class height(xsc.TextAttr): pass
		class src(xsc.URLAttr): pass
		class controller(xsc.TextAttr): pass
		class href(xsc.URLAttr): pass
		class target(xsc.TextAttr): pass
		class border(xsc.IntAttr): pass
		class pluginspage(xsc.URLAttr): pass
		class quality(xsc.TextAttr): pass
		class type(xsc.TextAttr): pass
		class bgcolor(xsc.ColorAttr): pass
		class menu(xsc.TextAttr): pass # deprecated


# The pain, the pain ...
class frameset(xsc.Element):
	"""
	window subdivision
	"""
	class Attrs(coreattrs):
		class rows(xsc.TextAttr): pass
		class cols(xsc.TextAttr): pass
		class onload(xsc.TextAttr): pass
		class onunload(xsc.TextAttr): pass
		class framespacing(xsc.TextAttr): pass # deprecated
		class border(xsc.IntAttr): pass # deprecated
		class marginwidth(xsc.IntAttr): pass # deprecated
		class marginheight(xsc.IntAttr): pass # deprecated
		class frameborder(xsc.IntAttr): pass # deprecated
		class noresize(xsc.BoolAttr): pass # deprecated
		class scrolling(xsc.TextAttr): pass # deprecated


class frame(xsc.Element):
	"""
	subwindow
	"""
	model = sims.Empty()
	class Attrs(coreattrs):
		class longdesc(xsc.TextAttr): pass
		class name(xsc.TextAttr): pass
		class src(xsc.URLAttr): pass
		class frameborder(xsc.TextAttr): pass
		class marginwidht(xsc.TextAttr): pass
		class marginheight(xsc.TextAttr): pass
		class noresize(xsc.BoolAttr): pass
		class scrolling(xsc.TextAttr): pass
		class framespacing(xsc.TextAttr): pass # deprecated
		class border(xsc.IntAttr): pass # deprecated
		class marginwidth(xsc.IntAttr): pass # deprecated
		class marginheight(xsc.IntAttr): pass # deprecated
		class frameborder(xsc.IntAttr): pass # deprecated
		class noresize(xsc.BoolAttr): pass # deprecated
		class scrolling(xsc.TextAttr): pass # deprecated


# More pain
class nobr(xsc.Element): # deprecated
	"""
	prevents line breaks
	"""


class __ns__(xsc.Namespace):
	xmlname = "html"
	xmlurl = "http://www.w3.org/1999/xhtml"
__ns__.makemod(vars())


# Parameter entities defined in the DTD
pe_special_extra = (object, embed, applet, img, map, iframe) # embed is deprecated
pe_special_basic = (br, span, bdo)
pe_special = pe_special_basic + pe_special_extra
pe_fontstyle_extra = (big, small, font, basefont)
pe_fontstyle_basic = (tt, i, b, u, s, strike)
pe_fontstyle = pe_fontstyle_basic + pe_fontstyle_extra
pe_phrase_extra = (sub, sup)
pe_phrase_basic = (em, strong, dfn, code, q, samp, kbd, var, cite, abbr, acronym)
pe_phrase = pe_phrase_basic + pe_phrase_extra
pe_inline_forms = (input, select, textarea, label, button)
pe_misc_inline = (ins, del_, script)
pe_misc = (noscript,) + pe_misc_inline
pe_inline = (a,) + pe_special + pe_fontstyle + pe_phrase + pe_inline_forms
pe_Inline = pe_inline + pe_misc_inline
pe_heading = (h1, h2, h3, h4, h5, h6)
pe_lists = (ul, ol, dl, menu, dir)
pe_blocktext = (pre, hr, blockquote, address, center, noframes)
pe_block = (p,) + pe_heading + (div,) + pe_lists + pe_blocktext + (isindex, fieldset, table)
pe_Flow = pe_block + (form,) + pe_inline + pe_misc


base.model = \
meta.model = \
link.model = \
hr.model = \
br.model = \
basefont.model = \
param.model = \
img.model = \
area.model = \
input.model = \
isindex.model = \
col.model = \
frame.model = sims.Empty()
noscript.model = \
iframe.model = \
body.model = \
div.model = \
li.model = \
dd.model = \
blockquote.model = \
center.model = \
ins.model = \
del_.model = \
th.model = \
td.model = \
nobr.model = sims.ElementsOrText(*pe_Flow)
p.model = \
h1.model = \
h2.model = \
h3.model = \
h4.model = \
h5.model = \
h6.model = \
dt.model = \
span.model = \
bdo.model = \
em.model = \
strong.model = \
dfn.model = \
code.model = \
samp.model = \
kbd.model = \
var.model = \
cite.model = \
abbr.model = \
acronym.model = \
q.model = \
sub.model = \
sup.model = \
tt.model = \
i.model = \
b.model = \
big.model = \
small.model = \
u.model = \
s.model = \
strike.model = \
font.model = \
label.model = \
legend.model = \
caption.model = sims.ElementsOrText(*pe_Inline)
ul.model = \
ol.model = \
menu.model = \
dir.model = sims.Elements(li)
title.model = \
style.model = \
script.model = \
option.model = \
textarea.model = sims.NoElements()
object.model = \
applet.model = \
embed.model = sims.ElementsOrText(*((param,) + pe_block + (form,) + pe_inline + pe_misc))
thead.model = \
tfoot.model = \
tbody.model = sims.Elements(tr)
map.model = sims.Elements(*(pe_block + (form,) + pe_misc + (area,)))
noframes.model = sims.Elements(body)
table.model = sims.Elements(caption, col, colgroup, thead, tfoot, tbody, tr)
colgroup.model = sims.Elements(col)
dl.model = sims.Elements(dt, dd)
frameset.model = sims.Elements(frameset, frame, noframes)
html.model = sims.Elements(head, body, frameset)
select.model = sims.Elements(optgroup, option)
optgroup.model = sims.Elements(option)
tr.model = sims.Elements(th, td)
head.model = sims.Elements(title, base, script, style, meta, link, object, isindex)
pre.model = sims.ElementsOrText(*((a,) + pe_special_basic + pe_fontstyle_basic + pe_phrase_basic + pe_inline_forms + pe_misc_inline))
fieldset.model = sims.ElementsOrText(*((legend,) + pe_block + (form,) + pe_inline + pe_misc))
button.model = sims.ElementsOrText(*((p,) + pe_heading + (div,) + pe_lists + pe_blocktext + (table, br, span, bdo, object, applet, img, map) + pe_fontstyle + pe_phrase + pe_misc))
form.model = sims.ElementsOrText(*(pe_block + pe_inline + pe_misc))
address.model = sims.ElementsOrText(*(pe_inline + pe_misc_inline + (p,)))
a.model = sims.ElementsOrText(*(pe_special + pe_fontstyle + pe_phrase + pe_inline_forms + pe_misc_inline))
