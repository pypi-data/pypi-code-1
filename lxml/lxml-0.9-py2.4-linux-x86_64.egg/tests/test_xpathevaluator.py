# -*- coding: UTF-8 -*-

"""
Test cases related to XPath evaluation and the XPath class
"""

import unittest, doctest
from StringIO import StringIO

from common_imports import etree, HelperTestCase

class ETreeXPathTestCase(HelperTestCase):
    """XPath tests etree"""

    def test_xpath_boolean(self):
        tree = self.parse('<a><b></b><b></b></a>')
        self.assert_(tree.xpath('boolean(/a/b)'))
        self.assert_(not tree.xpath('boolean(/a/c)'))

    def test_xpath_number(self):
        tree = self.parse('<a>1</a>')
        self.assertEquals(1.,
                          tree.xpath('number(/a)'))
        tree = self.parse('<a>A</a>')
        actual = str(tree.xpath('number(/a)'))
        expected = ['nan', '1.#qnan']
        if not actual.lower() in expected:
            self.fail('Expected a NAN value, got %s' % actual)
        
    def test_xpath_string(self):
        tree = self.parse('<a>Foo</a>')
        self.assertEquals('Foo',
                          tree.xpath('string(/a/text())'))

    def test_xpath_list_elements(self):
        tree = self.parse('<a><b>Foo</b><b>Bar</b></a>')
        root = tree.getroot()
        self.assertEquals([root[0], root[1]],
                          tree.xpath('/a/b'))

    def test_xpath_list_nothing(self):
        tree = self.parse('<a><b/></a>')
        self.assertEquals([],
                          tree.xpath('/a/c'))
        # this seems to pass a different code path, also should return nothing
        self.assertEquals([],
                          tree.xpath('/a/c/text()'))
    
    def test_xpath_list_text(self):
        tree = self.parse('<a><b>Foo</b><b>Bar</b></a>')
        root = tree.getroot()
        self.assertEquals(['Foo', 'Bar'],
                          tree.xpath('/a/b/text()'))

    def test_xpath_list_attribute(self):
        tree = self.parse('<a b="B" c="C"/>')
        self.assertEquals(['B'],
                          tree.xpath('/a/@b'))

    def test_xpath_list_comment(self):
        tree = self.parse('<a><!-- Foo --></a>')
        self.assertEquals(['<Comment[ Foo ]>'],
                          map(repr, tree.xpath('/a/node()')))

    def test_rel_xpath_boolean(self):
        root = etree.XML('<a><b><c/></b></a>')
        el = root[0]
        self.assert_(el.xpath('boolean(c)'))
        self.assert_(not el.xpath('boolean(d)'))

    def test_rel_xpath_list_elements(self):
        tree = self.parse('<a><c><b>Foo</b><b>Bar</b></c><c><b>Hey</b></c></a>')
        root = tree.getroot()
        c = root[0]
        self.assertEquals([c[0], c[1]],
                          c.xpath('b'))
        self.assertEquals([c[0], c[1], root[1][0]],
                          c.xpath('//b'))

    def test_xpath_ns(self):
        tree = self.parse('<a xmlns="uri:a"><b></b></a>')
        root = tree.getroot()
        self.assertEquals(
            [root[0]],
            tree.xpath('//foo:b', {'foo': 'uri:a'}))
        self.assertEquals(
            [],
            tree.xpath('//foo:b', {'foo': 'uri:c'}))
        self.assertEquals(
            [root[0]],
            root.xpath('//baz:b', {'baz': 'uri:a'}))
        self.assertRaises(
            TypeError,
            root.xpath, '//b', {None: 'uri:a'})

    def test_xpath_error(self):
        tree = self.parse('<a/>')
        self.assertRaises(SyntaxError, tree.xpath, '\\fad')

    def test_xpath_evaluator(self):
        tree = self.parse('<a><b><c></c></b></a>')
        e = etree.XPathEvaluator(tree)
        root = tree.getroot()
        self.assertEquals(
            [root],
            e.evaluate('//a'))

    def test_xpath_evaluator_element(self):
        tree = self.parse('<a><b><c></c></b></a>')
        root = tree.getroot()
        e = etree.XPathEvaluator(root[0])
        self.assertEquals(
            [root[0][0]],
            e.evaluate('c'))
        
    def test_xpath_extensions(self):
        def foo(evaluator, a):
            return 'hello %s' % a
        extension = {(None, 'foo'): foo}
        tree = self.parse('<a><b></b></a>')
        e = etree.XPathEvaluator(tree, None, [extension])
        self.assertEquals(
            "hello you", e.evaluate("foo('you')"))

    def test_xpath_extensions_wrong_args(self):
        def foo(evaluator, a, b):
            return "hello %s and %s" % (a, b)
        extension = {(None, 'foo'): foo}
        tree = self.parse('<a><b></b></a>')
        e = etree.XPathEvaluator(tree, None, [extension])
        self.assertRaises(TypeError, e.evaluate, "foo('you')")

    def test_xpath_extensions_error(self):
        def foo(evaluator, a):
            return 1/0
        extension = {(None, 'foo'): foo}
        tree = self.parse('<a/>')
        e = etree.XPathEvaluator(tree, None, [extension])
        self.assertRaises(ZeroDivisionError, e.evaluate, "foo('test')")

    def test_xpath_extensions_nodes(self):
        def f(evaluator, arg):
            r = etree.Element('results')
            b = etree.SubElement(r, 'result')
            b.text = 'Hoi'
            b = etree.SubElement(r, 'result')
            b.text = 'Dag'
            return r

        x = self.parse('<a/>')
        e = etree.XPathEvaluator(x, None, [{(None, 'foo'): f}])
        r = e.evaluate("foo('World')/result")
        self.assertEquals(2, len(r))
        self.assertEquals('Hoi', r[0].text)
        self.assertEquals('Dag', r[1].text)

    def test_xpath_variables(self):
        x = self.parse('<a attr="true"/>')
        e = etree.XPathEvaluator(x)

        expr = "/a[@attr=$aval]"
        r = e.evaluate(expr, aval=1)
        self.assertEquals(0, len(r))

        r = e.evaluate(expr, aval="true")
        self.assertEquals(1, len(r))
        self.assertEquals("true", r[0].get('attr'))

        r = e.evaluate(expr, aval=True)
        self.assertEquals(1, len(r))
        self.assertEquals("true", r[0].get('attr'))


class ETreeXPathClassTestCase(HelperTestCase):
    "Tests for the XPath class"
    def test_xpath_compile_doc(self):
        x = self.parse('<a attr="true"/>')

        expr = etree.XPath("/a[@attr != 'true']")
        r = expr.evaluate(x)
        self.assertEquals(0, len(r))

        expr = etree.XPath("/a[@attr = 'true']")
        r = expr.evaluate(x)
        self.assertEquals(1, len(r))

        expr = etree.XPath( expr.path )
        r = expr.evaluate(x)
        self.assertEquals(1, len(r))

    def test_xpath_compile_element(self):
        x = self.parse('<a><b/><c/></a>')
        root = x.getroot()

        expr = etree.XPath("./b")
        r = expr.evaluate(root)
        self.assertEquals(1, len(r))
        self.assertEquals('b', r[0].tag)

        expr = etree.XPath("./*")
        r = expr.evaluate(root)
        self.assertEquals(2, len(r))

    def test_xpath_compile_vars(self):
        x = self.parse('<a attr="true"/>')

        expr = etree.XPath("/a[@attr=$aval]")
        r = expr.evaluate(x, aval=False)
        self.assertEquals(0, len(r))

        r = expr.evaluate(x, aval=True)
        self.assertEquals(1, len(r))

    def test_xpath_compile_error(self):
        self.assertRaises(SyntaxError, etree.XPath, '\\fad')

class ETreeETXPathClassTestCase(HelperTestCase):
    "Tests for the ETXPath class"
    def test_xpath_compile_ns(self):
        x = self.parse('<a><b xmlns="nsa"/><b xmlns="nsb"/></a>')

        expr = etree.ETXPath("/a/{nsa}b")
        r = expr.evaluate(x)
        self.assertEquals(1, len(r))
        self.assertEquals('{nsa}b', r[0].tag)

        expr = etree.ETXPath("/a/{nsb}b")
        r = expr.evaluate(x)
        self.assertEquals(1, len(r))
        self.assertEquals('{nsb}b', r[0].tag)

SAMPLE_XML = etree.parse(StringIO("""
<body>
  <tag>text</tag>
  <section>
    <tag>subtext</tag>
  </section>
  <tag />
  <tag />
</body>
"""))

def tag(elem):
    return elem.tag

def stringTest(ctxt, s1):
    return "Hello "+s1
    
def floatTest(ctxt, f1):
    return f1+4

def booleanTest(ctxt, b1):
    return not b1
    
def setTest(ctxt, st1):
    return st1[0]
    
def setTest2(ctxt, st1):
    return st1[0:2]

def argsTest1(ctxt, s, f, b, st):
    return ", ".join(map(str, (s, f, b, map(tag, st))))

def argsTest2(ctxt, st1, st2):
    st1.extend(st2)
    return st1

def resultTypesTest(ctxt):
    return ["x","y"]

def resultTypesTest2(ctxt):
    return resultTypesTest
    
uri = "http://www.example.com/"

extension = {(None, 'stringTest'): stringTest,
             (None, 'floatTest'): floatTest,
             (None, 'booleanTest'): booleanTest,
             (None, 'setTest'): setTest,
             (None, 'setTest2'): setTest2,
             (None, 'argsTest1'): argsTest1,
             (None, 'argsTest2'): argsTest2,
             (None, 'resultTypesTest'): resultTypesTest,
             (None, 'resultTypesTest2'): resultTypesTest2,}

def xpath():
    """
    Test xpath extension functions.
    
    >>> root = SAMPLE_XML
    >>> e = etree.XPathEvaluator(root, None, [extension])
    >>> e.evaluate("stringTest('you')")
    'Hello you'
    >>> e.evaluate(u"stringTest('\xe9lan')")
    u'Hello \\xe9lan'
    >>> e.evaluate("stringTest('you','there')")
    Traceback (most recent call last):
    ...
    TypeError: stringTest() takes exactly 2 arguments (3 given)
    >>> e.evaluate("floatTest(2)")
    6.0
    >>> e.evaluate("booleanTest(true())")
    False
    >>> map(tag, e.evaluate("setTest(/body/tag)"))
    ['tag']
    >>> map(tag, e.evaluate("setTest2(/body/*)"))
    ['tag', 'section']
    >>> e.evaluate("argsTest1('a',1.5,true(),/body/tag)")
    "a, 1.5, True, ['tag', 'tag', 'tag']"
    >>> map(tag, e.evaluate("argsTest2(/body/tag, /body/section)"))
    ['tag', 'section', 'tag', 'tag']
    >>> e.evaluate("resultTypesTest()")
    Traceback (most recent call last):
    ...
    XPathResultError: This is not a node: x
    >>> try:
    ...     e.evaluate("resultTypesTest2()")
    ... except etree.XPathResultError:
    ...     print "Got error"
    Got error
    """
   
def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(ETreeXPathTestCase)])
    suite.addTests([unittest.makeSuite(ETreeXPathClassTestCase)])
    suite.addTests([unittest.makeSuite(ETreeETXPathClassTestCase)])
    suite.addTests([doctest.DocTestSuite()])
    return suite

if __name__ == '__main__':
    unittest.main()
