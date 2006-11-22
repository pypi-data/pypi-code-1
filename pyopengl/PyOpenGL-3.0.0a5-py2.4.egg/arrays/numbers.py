"""Numbers passed as array handling code for PyOpenGL
"""
REGISTRY_NAME = 'numbers'
from OpenGL import constants
from OpenGL.arrays import formathandler
import ctypes

class NumberHandler( formathandler.FormatHandler ):
	"""Allows the user to pass a bald Python float,int, etceteras as an array-of-1"""
	HANDLED_TYPES = (
		int,long,float,
		constants.GLdouble,
		constants.GLfloat,
		constants.GLint,
		constants.GLshort,
		constants.GLuint,
		constants.GLushort, 
		constants.GLclampf,
		constants.GLclampd,
	)
	def from_param( self, value ):
		"""If it's a ctypes value, pass on, otherwise do asArray"""
		if not isinstance( value, TARGET_TYPE_TUPLE ):
			return self.asArray( value )
		return ctypes.byref(value)
	dataPointer = from_param
	def zeros( self, dims, typeCode=None ):
		"""Currently don't allow Number as output types!"""
		raise NotImplemented( """Number data-type not allowed as an output array format""" )
	def ones( self, dims, typeCode=None ):
		"""Currently don't allow Number as output types!"""
		raise NotImplemented( """Number data-type not allowed as an output array format""" )
	def arrayToGLType( self, value ):
		"""Given a value, guess OpenGL type of the corresponding pointer"""
		if isinstance( value, TARGET_TYPE_TUPLE ):
			return TARGET_TYPES[ type(value) ]
		else:
			guess = DEFAULT_TYPES.get( type(value))
			if guess is not None:
				return guess[1]
			raise TypeError( """Can't guess array data-type for %r types"""%(type(value)))
	def arraySize( self, value, typeCode = None ):
		"""Given a data-value, calculate ravelled size for the array"""
		return 1
	def asArray( self, value, typecode=None ):
		"""Convert given value to an array value of given typecode"""
		if isinstance( value, TARGET_TYPE_TUPLE ):
			return value
		targetType = CONSTANT_TO_TYPE.get( typecode )
		if targetType is not None:
			return targetType( value )
		raise TypeError( """Don't know how to convert %r to an array type"""%(
			typeCode,
		))
	def unitSize( self, value, typeCode=None ):
		"""Determine unit size of an array (if possible)"""
		return 1 # there's only 1 possible value in the set...
	def registerEquivalent( self, typ, base ):
		"""Register a sub-class for handling as the base-type"""
		global TARGET_TYPE_TUPLE
		for source in (DEFAULT_TYPES, TARGET_TYPES, BYTE_SIZES):
			if source.has_key( base ):
				source[typ] = source[base]
		if TARGET_TYPES.has_key( base ):
			TARGET_TYPE_TUPLE = TARGET_TYPE_TUPLE + (base,)

DEFAULT_TYPES = {
	float: (constants.GLdouble,constants.GL_DOUBLE),
	int: (constants.GLint,constants.GL_INT),
	long: (constants.GLint,constants.GL_INT),
}
TARGET_TYPES = dict([
	(getattr( constants,n),c)
	for (n,c) in constants.ARRAY_TYPE_TO_CONSTANT
])
TARGET_TYPE_TUPLE = tuple([
	getattr(constants,n) 
	for (n,c) in constants.ARRAY_TYPE_TO_CONSTANT
])
CONSTANT_TO_TYPE = dict([
	(c,getattr( constants, n))
	for (n,c) in constants.ARRAY_TYPE_TO_CONSTANT
])

BYTE_SIZES = dict([
	( c, ctypes.sizeof( getattr( constants, n) ) )
	for (n,c) in constants.ARRAY_TYPE_TO_CONSTANT
])
del n,c
