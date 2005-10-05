import unittest

from yaxl import *

class XpathTests(unittest.TestCase):
	def test_selectRoot(self):
		x = Element('test')
		y = x.append('test2')
		z = x.append('test3')
		
		for node in (x, y, z):
			self.assertEquals(node.select('/'), x)
	
	def test_selectSubElement(self):
		x = Element('test')
		x.append('x').text = 'something'
		
		self.assertEquals(parse('<x>something</x>'), x.select('x'))	
		
	def test_simpleAttributeSelect(self):
		x = Element('test', {'x': 5})
		
		self.assertEquals('5', x.select('@x'))

	def atest_leveledSubElementSelect(self):
		x = Element('test')
		x.append('t1').append('t2').text = 'something'
		
		self.assertEquals(x('t1/t2/.'), 'something')
		
	def test_selectWorksViaCall(self):
		x = Element('test', {'t': 'something else'})
		x.append('t1').text = 'something'
		
		self.assertEquals(x('t1'), parse('<t1>something</t1>'))		
		self.assertEquals(x('@t'), 'something else')
	
	def test_unabbrevChildAxis_singleStep(self):
		x = Element('x')
		y = x.append('y')
		y2 = x.append('y')
		z = y.append('z')
		
		self.assertEquals(x('/child::y'), (y, y2))
		self.assertEquals(y('child::z'), z)
		self.assertEquals(None, x('child::z'))		
		
	def test_unabbrevDescendantAxis_singleStep(self):
		x = Element('x')
		y = x.append('y')
		z = y.append('z')
		z2 = y.append('z')
		w = y.append('w')
		
		self.assertEquals(x('/descendant::z'), (z, z2))
		self.assertEquals(x('descendant::w'), w)
		
	def test_unabbrevParentAxis_singleStep(self):
		x = Element('x')
		y = x.append('y')
		
		self.assertEquals(x, y('parent::x'))
		self.assertEquals(x, y('parent::*'))
		self.assertEquals(None, y('parent::w'))
		self.assertEquals(None, x('parent::*'))
		
	def test_unabbrevAncestorAxis_singleStep(self):
		x = Element('x')
		y = x.append('y')
		
		self.assertEquals(x, y('ancestor::x'))
		self.assertEquals(x, y('ancestor::*'))
		self.assertEquals(None, y('ancestor::y'))
	
	# Here we are missing tests for the following axes:
	#	following-sibling
	#	preceding-sibling
	#	following
	#	preceding	
	
	def test_unabbrevAttributeAxis_singleStep(self):
		x = Element('x', {'a': 5})
		
		self.assertEquals('5', x('attribute::a'))
	
	# Missing namespace axis tests
	
	def test_unabbrevSelfAxis_singleStep(self):
		x = Element('x')
		
		self.assertEquals(None, x('self::w'))
		self.assertEquals(x, x('self::x'))
		self.assertEquals(x, x('self::*'))
		
	def test_unabbrevDescendantOrSelfAxis_singleStep(self):
		x = Element('x')
		y = x.append('y')
		z = y.append('z')
		
		self.assertEquals(z, x('descendant-or-self::z'))
		self.assertEquals(z, y('descendant-or-self::z'))
		self.assertEquals(z, z('descendant-or-self::z'))
		
	def test_unabbrevAncestorOrSelfAxis_singleStep(self):
		x = Element('x')
		y = x.append('y')
		z = y.append('z')
		
		self.assertEquals(x, x('ancestor-or-self::x'))
		self.assertEquals(x, y('ancestor-or-self::x'))
		self.assertEquals(x, z('ancestor-or-self::x'))
		
	def test_unabbrevMultiStep(self):
		x = Element('x')
		y = x.append('y', {'a': 5, 'b': 'something'})
		z1 = y.append('z', {'a': 17}, text='a test')
		z2 = y.append('z')
		z3 = y.append('z', text='another test')
		
		self.assertEquals((z1, z2, z3), x('child::y/child::z'))
		self.assertEquals('17', x('descendant-or-self::z/attribute::a'))
		self.assertEquals(('5', '17'), x('descendant-or-self::*/attribute::a'))
		self.assertEquals(None, x('descendant-or-self::z/attribute::b'))
	
class ElementTests(unittest.TestCase):
	def test_asdoc(self):
		x = Element('test')		
		
		assert '<?xml version="1.0"?><test />' == x.asdoc()
		assert x.asdoc() == x.__repr__(asdoc=True)

	def test_addingExistingNamespaceIsNoop(self):
		t = Element('test')
		t1 = t.append('t1')
		
		t.map('test', 'http://example.org')
		
		assert 'http://example.org' == t1.find_ns('test')
		assert len(t1.namespaces) == 1
		
		t.map('test', 'http://example.org')
		
		assert 'http://example.org' == t1.find_ns('test')
		assert len(t1.namespaces) == 1
	
	def test_xmlNamespaceExistsByDefault(self):
		x = Element('x')
		x['xml:lang'] = 'en'
	
	def test_defaultNamespace(self):
		x = Element('x', {'xmlns': 'http://example.org'})
		self.assertEquals('<x xmlns="http://example.org" />', str(x))
		
		y = parse('<x xmlns="http://example.org" />')
		self.assertEquals(str(y), str(x))
	
	def test_simpleEquality(self):
		assert Element('test') == Element('test')
		
	def test_equalityWithAttributesAndSubElements(self):
		t1 = Element('test')
		t2 = Element('test')
		
		t1.append('t2', {'x': 5})
		t2.append('t2', {'x': 5})
		
		assert t1 == t2
		
	def test_equalityWithNonElement(self):
		x = Element('x')
		assert x != 'x'		
	
	def test_attributeValuesAreNormalized(self):
		t1 = Element('test')
		t2 = Element('test')
				
		t1.append('t2', {'x': 5})
		t2.append('t2', {'x': 5})
		
		t1['test'] = 5
		t2['test'] = '5'
		
		assert t1 == t2
		
		t1['t2'] = u'something'
		t2['t2'] = 'something'
		
		assert t1 == t2
		
		t1[u't3'] = 'something'
		t2['t3'] = 'something'
		
		assert t1 == t2
	
	def test_namespaces(self):
		t1 = Element('test', {'xmlns:test2': 'http://www.example2.org'})
		
		t1.map('test', 'http://www.example.org')
		
		assert 'test' in t1.namespaces.keys()
		assert 'test2' in t1.namespaces.keys()

		t2 = t1.append('t2')
		
		assert t2.parent is t1
		assert isinstance(t2, Element)
		
		assert t2['xmlns:test'] == t1['xmlns:test']
		
		assert 'http://www.example.org' == t2.find_ns('test')
		assert 'http://www.example2.org' == t2.find_ns('test2')		
		
		t2['test:bob'] = 5
		
		t2['xmlns:test'] = 'http://www.example3.org'
		
		t3 = t2.append('test:t3')
		
		assert 'http://www.example3.org' == t3.find_ns('test')
	
	def test_namespacesGetOutput(self):
		t = Element('test:t', {'xmlns:test': 'http://www.example.org/'})
		assert str(t) == '<test:t xmlns:test="http://www.example.org/" />'
	
	def test_elementsOutputTextContents(self):
		test = Element('test')
		test.text = 'something'
		
		assert str(test) == '<test>something</test>'
	
	def test_addTextAsPartOfAppend(self):
		t = Element('t')
		t.append('x', text='something')
		
		assert t == parse('<t><x>something</x></t>')
	
	def test_Element2Document(self):	
		test = parse('<test />')
		
		self.assertEquals(test, parse('<test />'))
		
		assert str(test) == '<test />'
		
		test['t1'] = 'something'
		self.assertEquals(test, parse('<test t1="something" />'))
				
		test.append('t2')		
		assert test == parse('<test t1="something"><t2 /></test>')
		
		del test['t1']
		test.append('t3', {u'bob': u'test', u'jim': u'3'})
		
		try:
			test.append('test:t1')
			self.fail('Should have thrown UndeclaredNamespaceException')
		except UndeclaredNamespaceException:
			pass
		
		try:
			test['test:something'] = 'something else'
			self.fail('Should have thrown UndeclaredNamespaceException')
		except UndeclaredNamespaceException:
			pass
		
		test = Element('test', {'xmlns:test': 'http://www.example.org'})
		test.append('t2')
		test.append('t3', {'bob': 'test', 'jim': 3})
		test.append('test:t1')		
		
		d = parse("""
		<test xmlns:test="http://www.example.org">
			<t2 />
			<t3 bob="test" jim="3" />
			<test:t1 />
		</test>""")
		
		assert test == d
		
		test['test:t4'] = 'something'
		
		self.assertEquals(test, parse('<test xmlns:test="http://www.example.org" test:t4="something"><t2 /><t3 bob="test" jim="3" /><test:t1 /></test>'))
		
		test = Element('test', {'xmlns:test': 'http://example.org', 'test:t4': 'something'})
		
		try:
			del test['xmlns:test']
			self.fail('Should have raised a NamespaceNotDeletableException')
		except NamespaceNotDeletableException:
			pass
			
		del test['test:t4']
		del test['xmlns:test']
		'''
		test = Element('test')
		test.namespaces['test'] = 'http://example.org'
		t1 = test.append('t1', {'test:jim': 'something'})
		
		assert 'http://example.org' == t1.find_ns('test')
		del test['xmlns:test']
		assert 'http://example.org' == t1.find_ns('test')
		'''
		
if __name__ == '__main__':
	unittest.main()