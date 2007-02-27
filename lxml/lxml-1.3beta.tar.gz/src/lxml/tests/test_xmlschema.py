# -*- coding: utf-8 -*-

"""
Test cases related to XML Schema parsing and validation
"""

import unittest

from common_imports import etree, doctest, HelperTestCase, fileInTestDir

class ETreeXMLSchemaTestCase(HelperTestCase):
    def test_xmlschema(self):
        tree_valid = self.parse('<a><b></b></a>')
        tree_invalid = self.parse('<a><c></c></a>')
        schema = self.parse('''
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:element name="a" type="AType"/>
  <xsd:complexType name="AType">
    <xsd:sequence>
      <xsd:element name="b" type="xsd:string" />
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
''')
        schema = etree.XMLSchema(schema)
        self.assert_(schema.validate(tree_valid))
        self.assert_(not schema.validate(tree_invalid))

    def test_xmlschema_elementtree_error(self):
        self.assertRaises(ValueError, etree.XMLSchema, etree.ElementTree())

    def test_xmlschema_invalid_schema1(self):
        schema = self.parse('''\
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <element name="a" type="AType"/>
  <xsd:complexType name="AType">
    <xsd:sequence>
      <xsd:element name="b" type="xsd:string" />
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
''')
        self.assertRaises(etree.XMLSchemaParseError,
                          etree.XMLSchema, schema)

    def test_xmlschema_invalid_schema2(self):
        schema = self.parse('<test/>')
        self.assertRaises(etree.XMLSchemaParseError,
                          etree.XMLSchema, schema)

    def test_xmlschema_file(self):
        # this will only work if we access the file through path or
        # file object..
        f = open(fileInTestDir('test.xsd'), 'r')
        schema = etree.XMLSchema(file=f)
        tree_valid = self.parse('<a><b></b></a>')
        self.assert_(schema.validate(tree_valid))

    def test_xmlschema_shortcut(self):
        tree_valid = self.parse('<a><b></b></a>')
        tree_invalid = self.parse('<a><c></c></a>')
        schema = self.parse('''\
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:element name="a" type="AType"/>
  <xsd:complexType name="AType">
    <xsd:sequence>
      <xsd:element name="b" type="xsd:string" />
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
''')
        self.assert_(tree_valid.xmlschema(schema))
        self.assert_(not tree_invalid.xmlschema(schema))

    
def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(ETreeXMLSchemaTestCase)])
    suite.addTests(
        [doctest.DocFileSuite('../../../doc/validation.txt')])
    return suite

if __name__ == '__main__':
    unittest.main()
