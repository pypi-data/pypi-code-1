#!/usr/bin/env python

from unittest import TestCase
import StringIO, re, UserDict

from mechanoid.misc.Request import Request
import mechanoid, mechanoid.misc.Errors

class MockMethod:
	def __init__(self, meth_name, action, handle):
		self.meth_name = meth_name
		self.handle = handle
		self.action = action
	def __call__(self, *args):
		return apply(self.handle, (self.meth_name, self.action)+args)

class MockHeaders(UserDict.UserDict):
	def getallmatchingheaders(self, name):
		return ["%s: %s" % (k, v) for k, v in self.data.iteritems()]
	def getheaders(self, name):
		return self.data.values()

class MockResponse:
	def __init__(self, url="http://example.com/", data=None, info=None):
		self.url = url
		self._f = StringIO.StringIO(data)
		if info is None: info = {}
		self._info = MockHeaders(info)
	def info(self): return self._info
	def geturl(self): return self.url
	def read(self, size=-1): return self._f.read(size)
	def seek(self, whence):
		assert whence == 0
		self._f.seek(0)

class MockHandler:
	processor_order = 500
	handler_order = -1
	def __init__(self, methods):
		self._define_methods(methods)
	def _define_methods(self, methods):
		for name, action in methods:
			if name.endswith("_open"):
				meth = MockMethod(name, action, self.handle)
			else:
				meth = MockMethod(name, action, self.process)
			setattr(self.__class__, name, meth)
	def handle(self, fn_name, response, *args, **kwds):
		self.parent.calls.append((self, fn_name, args, kwds))
		if response:
			r = response
			r.seek(0)
		else:
			r = MockResponse()
		req = args[0]
		r.url = req.get_full_url()
		return r
	def process(self, fn_name, action, *args, **kwds):
		self.parent.calls.append((self, fn_name, args, kwds))
		if fn_name.endswith("_request"):
			return args[0]
		else:
			return args[1]
	def close(self): pass
	def add_parent(self, parent):
		self.parent = parent
		self.parent.calls = []
	def __cmp__(self, other):
		if hasattr(other, "handler_order"):
			return cmp(self.handler_order, other.handler_order)
		# No handler_order, leave in original order.  Yuck.
		return -1

class TestBrowser(mechanoid.Browser):
	default_features = ["_seek"]
	default_others = []
	default_schemes = []


class BrowserTests(TestCase):
	def test_referer(self):
		b = TestBrowser()
		url = "http://www.example.com/"
		r = MockResponse(url,
"""<html>
<head><title>Title</title></head>
<body>
<form name="form1">
 <input type="hidden" name="foo" value="bar"></input>
 <input type="submit"></input>
 </form>
<a href="http://example.com/foo/bar.html" name="apples"></a>
<a href="https://example.com/spam/eggs.html" name="secure"></a>
<a href="blah://example.com/" name="pears"></a>
</body>
</html>
""", {"content-type": "text/html"})
		b.add_handler(MockHandler([("http_open", r)]))

		# Referer not added by .open()...
		req = Request(url)
		b.open(req)
		self.assert_(req.get_header("Referer") is None)
		# ...even if we're visiting a document
		b.open(req)
		self.assert_(req.get_header("Referer") is None)
		# Referer added by .click_link() and .click()
		b.select_form("form1")
		req2 = b.click()
		self.assert_(req2.get_header("Referer") == url)
		r2 = b.open(req2)
		req3 = b.click_link(name="apples")
		self.assert_(req3.get_header("Referer") == url+"?foo=bar")
		# Referer not added when going from https to http URL
		b.add_handler(MockHandler([("https_open", r)]))
		r3 = b.open(req3)
		req4 = b.click_link(name="secure")
		self.assert_(req4.get_header("Referer") ==
					 "http://example.com/foo/bar.html")
		r4 = b.open(req4)
		req5 = b.click_link(name="apples")
		self.assert_(not req5.has_header("Referer"))
		# Referer not added for non-http, non-https requests
		b.add_handler(MockHandler([("blah_open", r)]))
		req6 = b.click_link(name="pears")
		self.assert_(not req6.has_header("Referer"))
		# Referer not added when going from non-http, non-https URL
		r4 = b.open(req6)
		req7 = b.click_link(name="apples")
		self.assert_(not req7.has_header("Referer"))

		# XXX Referer added for redirect

	def test_encoding(self):
		import mechanoid
		from StringIO import StringIO
		import urllib, mimetools
		# always take first encoding, since that's the one
		b = mechanoid.Browser()
		for s, ct in [("", b.default_encoding),

					  ("Foo: Bar\r\n\r\n", b.default_encoding),

					  ("Content-Type: text/html; charset=UTF-8\r\n\r\n",
					   "UTF-8"),

					  ("Content-Type: text/html; charset=UTF-8\r\n"
					   "Content-Type: text/html: charset=KOI8-R\r\n\r\n",
					   "UTF-8"),
					  ]:
			msg = mimetools.Message(StringIO(s))
			r = urllib.addinfourl(StringIO(""), msg, "http://www.example.com/")
			self.assert_(b._Browser__encoding(r) == ct)

	def test_history(self):
		import mechanoid
		b = TestBrowser()
		b.add_handler(MockHandler([("http_open", None)]))
		r1 = b.open("http://example.com/")
		r2 = b.open("http://example.com/foo")
		self.assert_(b.back() is r1)
		r3 = b.open("http://example.com/bar")
		r4 = b.open("http://example.com/spam")
		self.assert_(b.back() is r3)
		self.assert_(b.back() is r1)
		 # reloading does a real HTTP fetch rather than using history cache
		r5 = b.reload()
		self.assert_(r5 is not r1)
		# .geturl() gets fed through to b.response
		self.assertEquals(b.geturl(), "http://example.com/")
		# can go back n times
		r6 = b.open("http://example.com/spam")
		r7 = b.open("http://example.com/spam")
		self.assert_(b.back(2) is r5)

	def test_empty(self):
		import mechanoid
		url = "http://example.com/"

		b = TestBrowser()
		b.add_handler(MockHandler([("http_open", MockResponse(url, "", {}))]))
		r = b.open(url)
		self.assert_(not b._Browser__is_html())
		self.assertRaises(mechanoid.misc.Errors.BrowserStateError, b.links)
		self.assertRaises(mechanoid.misc.Errors.BrowserStateError, b.forms)
		self.assertRaises(mechanoid.misc.Errors.BrowserStateError, b.title)
		self.assertRaises(mechanoid.misc.Errors.BrowserStateError, b.select_form)
		self.assertRaises(mechanoid.misc.Errors.BrowserStateError, b.select_form,
						  name="blah")
		self.assertRaises(mechanoid.misc.Errors.BrowserStateError, b.find_link,
						  name="blah")

		b = TestBrowser()
		r = MockResponse(url,
"""<html>
<head><title>Title</title></head>
<body>
</body>
</html>
""", {"content-type": "text/html"})
		b.add_handler(MockHandler([("http_open", r)]))
		r = b.open(url)
		self.assert_(b.title() == "Title")
		self.assert_(len(list(b.links())) == 0)
		self.assert_(len(list(b.forms())) == 0)
		self.assertRaises(ValueError, b.select_form)
		self.assertRaises(mechanoid.misc.Errors.FormNotFoundError, b.select_form,
						  name="blah")
		self.assertRaises(mechanoid.misc.Errors.FormNotFoundError, b.select_form,
						  predicate=lambda x: True)
		self.assertRaises(mechanoid.misc.Errors.LinkNotFoundError, b.find_link,
						  name="blah")
		self.assertRaises(mechanoid.misc.Errors.LinkNotFoundError, b.find_link,
						  predicate=lambda x: True)

	def test_forms(self):
		import mechanoid
		url = "http://example.com"

		b = TestBrowser()
		r = MockResponse(url,
"""<html>
<head><title>Title</title></head>
<body>
<form name="form1">
 <input type="text"></input>
 <input type="checkbox" name="cheeses" value="cheddar"></input>
 <input type="checkbox" name="cheeses" value="edam"></input>
 <input type="submit" name="one"></input>
</form>
<a href="http://example.com/foo/bar.html" name="apples">
<form name="form2">
 <input type="submit" name="two">
</form>
</body>
</html>
""", {"content-type": "text/html"})
		b.add_handler(MockHandler([("http_open", r)]))
		r = b.open(url)

		forms = b.forms()
		self.assert_(len(forms) == 2)
		for got, expect in zip([f.name for f in forms], [
			"form1", "form2"]):
			self.assert_(got == expect)

		self.assertRaises(mechanoid.misc.Errors.FormNotFoundError, b.select_form, "foo")

		# no form is set yet
		self.assertRaises(AttributeError, getattr, b, "possible_items")
		b.select_form("form1")
		# now unknown methods are fed through to selected ClientForm.HTMLForm
		self.assert_(b.possible_items("cheeses") == ["cheddar", "edam"])
		b["cheeses"] = ["cheddar", "edam"]

		b.select_form(nr=1)
		self.assert_(b.name == "form2")

	def test_links(self):
		import mechanoid
		url = "http://example.com/"

		b = TestBrowser()
		r = MockResponse(url,
"""<html>
<head><title>Title</title></head>
<body>
<a href="http://example.com/foo/bar.html" name="apples"></a>
<a name="pears"></a>
<a href="spam" name="pears"></a>
<area href="blah" name="foo"></area>
<form name="form2">
 <input type="submit" name="two">
</form>
<frame name="name" href="href" src="src"></frame>
<iframe name="name2" href="href" src="src"></iframe>
<a name="name3" href="one">yada yada</a>
<a name="pears" href="two" weird="stuff">rhubarb</a>
<a></a>
<a/>
<iframe src="foo"/>
</body>
</html>
""", {"content-type": "text/html"})
		b.add_handler(MockHandler([("http_open", r)]))
		r = b.open(url)

		from mechanoid.misc.Link import Link
		exp_links = [
			# base_url, url, text, tag, attrs
			Link(url, "http://example.com/foo/bar.html", "", "a",
				 [("href", "http://example.com/foo/bar.html"),
				  ("name", "apples")]),
			Link(url, "spam", "", "a", [("href", "spam"), ("name", "pears")]),
			Link(url, "blah", None, "area",
				 [("href", "blah"), ("name", "foo")]),
			Link(url, "src", None, "frame",
				 [("name", "name"), ("href", "href"), ("src", "src")]),
			Link(url, "src", None, "iframe",
				 [("name", "name2"), ("href", "href"), ("src", "src")]),
			Link(url, "one", "yada yada", "a",
				 [("name", "name3"), ("href", "one")]),
			Link(url, "two", "rhubarb", "a",
				 [("name", "pears"), ("href", "two"), ("weird", "stuff")]),
			Link(url, "foo", None, "iframe",
				 [("src", "foo")]),
			]
		links = b.links()
		self.assert_(len(links) == len(exp_links))
		for got, expect in zip(links, exp_links):
			self.assert_(got == expect)
		# nr
		l = b.find_link()
		self.assert_(l.url == "http://example.com/foo/bar.html")
		l = b.find_link(nr=1)
		self.assert_(l.url == "spam")
		# text
		l = b.find_link(text="yada yada")
		self.assert_(l.url == "one")
		self.assertRaises(mechanoid.misc.Errors.LinkNotFoundError,
						  b.find_link, text="da ya")
		l = b.find_link(text_regex=re.compile("da ya"))
		self.assert_(l.url == "one")
		# name
		l = b.find_link(name="name3")
		self.assert_(l.url == "one")
		l = b.find_link(name_regex=re.compile("oo"))
		self.assert_(l.url == "blah")
		# url
		l = b.find_link(url="spam")
		self.assert_(l.url == "spam")
		l = b.find_link(url_regex=re.compile("pam"))
		self.assert_(l.url == "spam")
		# tag
		l = b.find_link(tag="area")
		self.assert_(l.url == "blah")
		# predicate
		l = b.find_link(predicate=
						lambda l: dict(l.attrs).get("weird") == "stuff")
		self.assert_(l.url == "two")
		# combinations
		l = b.find_link(name="pears", nr=1)
		self.assert_(l.text == "rhubarb")
		l = b.find_link(url="src", nr=0, name="name2")
		self.assert_(l.tag == "iframe")
		self.assert_(l.url == "src")
		self.assertRaises(mechanoid.misc.Errors.LinkNotFoundError, b.find_link,
						  url="src", nr=1, name="name2")
		l = b.find_link(tag="a", predicate=
						lambda l: dict(l.attrs).get("weird") == "stuff")
		self.assert_(l.url == "two")

		# .links()
		self.assert_(list(b.links(url="src")) == [
			Link(url, url='src', text=None, tag='frame',
				 attrs=[('name', 'name'), ('href', 'href'), ('src', 'src')]),
			Link(url, url='src', text=None, tag='iframe',
				 attrs=[('name', 'name2'), ('href', 'href'), ('src', 'src')]),
			])

	def test_base_uri(self):
		import mechanoid
		url = "http://example.com/"

		for html, urls in [
			(
"""<base href="http://www.python.org/foo/">
<a href="bar/baz.html"></a>
<a href="/bar/baz.html"></a>
<a href="http://example.com/bar/baz.html"></a>
""",
			[
			"http://www.python.org/foo/bar/baz.html",
			"http://www.python.org/bar/baz.html",
			"http://example.com/bar/baz.html",
			]),
			(
"""<a href="bar/baz.html"></a>
<a href="/bar/baz.html"></a>
<a href="http://example.com/bar/baz.html"></a>
""",
			[
			"http://example.com/bar/baz.html",
			"http://example.com/bar/baz.html",
			"http://example.com/bar/baz.html",
			]
			),
			]:
			b = TestBrowser()
			r = MockResponse(url, html, {"content-type": "text/html"})
			b.add_handler(MockHandler([("http_open", r)]))
			r = b.open(url)
			self.assert_([link.absolute_url for link in b.links()] == urls)


class UserAgentTests(TestCase):
	def test_set_handled_schemes(self):
		import mechanoid
		from mechanoid.useragent.UserAgent import UserAgent
		class MockHandlerClass(MockHandler):
			def __call__(self): return self
		class BlahHandlerClass(MockHandlerClass): pass
		class BlahProcessorClass(MockHandlerClass): pass
		BlahHandler = BlahHandlerClass([("blah_open", None)])
		BlahProcessor = BlahProcessorClass([("blah_request", None)])
		class TestUserAgent(UserAgent):
			default_others = []
			default_features = []
			handler_classes = UserAgent.handler_classes.copy()
			handler_classes.update(
				{"blah": BlahHandler, "_blah": BlahProcessor})
		ua = TestUserAgent()

		self.assert_(len(ua.handlers) == 5)
		ua.set_handled_schemes(["http", "https"])
		self.assert_(len(ua.handlers) == 2)
		self.assertRaises(ValueError,
			ua.set_handled_schemes, ["blah", "non-existent"])
		self.assertRaises(ValueError,
			ua.set_handled_schemes, ["blah", "_blah"])
		ua.set_handled_schemes(["blah"])

		req = Request("blah://example.com/")
		r = ua.open(req)
		exp_calls = [("blah_open", (req,), {})]
		assert len(ua.calls) == len(exp_calls)
		for got, expect in zip(ua.calls, exp_calls):
			self.assert_(expect == got[1:])

		ua.calls = []
		req = Request("blah://example.com/")
		ua._UserAgent__set_handler("_blah", True)
		r = ua.open(req)
		exp_calls = [
			("blah_request", (req,), {}),
			("blah_open", (req,), {})]
		#XXX fails on 2.4
#		assert len(ua.calls) == len(exp_calls)
#		for got, expect in zip(ua.calls, exp_calls):
#			self.assert_(expect == got[1:])
		ua._UserAgent__set_handler("_blah", True)

if __name__ == "__main__":
	import unittest
	unittest.main()
