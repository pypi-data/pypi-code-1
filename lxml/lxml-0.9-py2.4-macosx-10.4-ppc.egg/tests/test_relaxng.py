# -*- coding: UTF-8 -*-

"""
Test cases related to RelaxNG parsing and validation
"""

import unittest

from common_imports import etree, HelperTestCase, fileInTestDir

class ETreeRelaxNGTestCase(HelperTestCase):
    def test_relaxng(self):
        tree_valid = self.parse('<a><b></b></a>')
        tree_invalid = self.parse('<a><c></c></a>')
        schema = self.parse('''\
<element name="a" xmlns="http://relaxng.org/ns/structure/1.0">
  <zeroOrMore>
     <element name="b">
       <text />
     </element>
  </zeroOrMore>
</element>
''')
        schema = etree.RelaxNG(schema)
        self.assert_(schema.validate(tree_valid))
        self.assert_(not schema.validate(tree_invalid))

    def test_relaxng_error(self):
        tree_invalid = self.parse('<a><c></c></a>')
        schema = self.parse('''\
<element name="a" xmlns="http://relaxng.org/ns/structure/1.0">
  <zeroOrMore>
     <element name="b">
       <text />
     </element>
  </zeroOrMore>
</element>
''')
        schema = etree.RelaxNG(schema)
        self.assert_(not schema.validate(tree_invalid))
        errors = schema.error_log
        self.assert_([ log for log in errors
                       if log.level_name == "ERROR" ])
        self.assert_([ log for log in errors
                       if "not expect" in log.message ])

    def test_relaxng_invalid_schema(self):
        schema = self.parse('''\
<element name="a" xmlns="http://relaxng.org/ns/structure/1.0">
  <zeroOrMore>
     <element name="b" />
  </zeroOrMore>
</element>
''')
        self.assertRaises(etree.RelaxNGParseError,
                          etree.RelaxNG, schema)

    def test_relaxng_invalid_schema2(self):
        schema = self.parse('''\
<grammar xmlns="http://relaxng.org/ns/structure/1.0" />
''')
        self.assertRaises(etree.RelaxNGParseError,
                          etree.RelaxNG, schema)

    def test_relaxng_invalid_schema3(self):
        schema = self.parse('''\
<grammar xmlns="http://relaxng.org/ns/structure/1.0">
  <define name="test">
    <element name="test"/>
  </define>
</grammar>
''')
        self.assertRaises(etree.RelaxNGParseError,
                          etree.RelaxNG, schema)

    def test_relaxng_invalid_schema4(self):
        # segfault
        schema = self.parse('''\
<element name="a" xmlns="mynamespace" />
''')
        self.assertRaises(etree.RelaxNGParseError,
                          etree.RelaxNG, schema)

    def test_relaxng_include(self):
        # this will only work if we access the file through path or
        # file object..
        f = open(fileInTestDir('test1.rng'), 'r')
        schema = etree.RelaxNG(file=f)

    def test_relaxng_shortcut(self):
        tree_valid = self.parse('<a><b></b></a>')
        tree_invalid = self.parse('<a><c></c></a>')
        schema = self.parse('''\
<element name="a" xmlns="http://relaxng.org/ns/structure/1.0">
  <zeroOrMore>
     <element name="b">
       <text />
     </element>
  </zeroOrMore>
</element>
''')
        self.assert_(tree_valid.relaxng(schema))
        self.assert_(not tree_invalid.relaxng(schema))

    def test_multiple_elementrees(self):
        tree = self.parse('<a><b>B</b><c>C</c></a>')
        schema = etree.RelaxNG( self.parse('''\
<element name="a" xmlns="http://relaxng.org/ns/structure/1.0">
  <element name="b">
    <text />
  </element>
  <element name="c">
    <text />
  </element>
</element>
''') )
        self.assert_(schema.validate(tree))
        self.assert_(schema.validate(tree))

        schema = etree.RelaxNG( self.parse('''\
<element name="b" xmlns="http://relaxng.org/ns/structure/1.0">
  <text />
</element>
''') )
        c_tree = etree.ElementTree(tree.getroot()[1])
        self.assertEqual(self._rootstring(c_tree), '<c>C</c>')
        self.assert_(not schema.validate(c_tree))

        b_tree = etree.ElementTree(tree.getroot()[0])
        self.assertEqual(self._rootstring(b_tree), '<b>B</b>')
        self.assert_(schema.validate(b_tree))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(ETreeRelaxNGTestCase)])
    return suite

if __name__ == '__main__':
    unittest.main()
