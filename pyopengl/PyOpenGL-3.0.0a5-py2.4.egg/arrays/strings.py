"""String-array-handling code for PyOpenGL
"""
from OpenGL.arrays._strings import dataPointer
from OpenGL import constants
from OpenGL.arrays import formathandler
import ctypes

class StringHandler( formathandler.FormatHandler ):
	"""String-specific data-type handler for OpenGL"""
	HANDLED_TYPES = (str, )
	from_param = staticmethod( dataPointer )
	dataPointer = staticmethod( dataPointer )
	def zeros( self, dims, typeCode=None ):
		"""Currently don't allow strings as output types!"""
		raise NotImplemented( """String data-type not allowed as an output array format""" )
	def ones( self, dims, typeCode=None ):
		"""Currently don't allow strings as output types!"""
		raise NotImplemented( """String data-type not allowed as an output array format""" )
	def arrayToGLType( self, value ):
		"""Given a value, guess OpenGL type of the corresponding pointer"""
		raise NotImplemented( """Can't guess data-type from a string-type argument""" )
	def arraySize( self, value, typeCode = None ):
		"""Given a data-value, calculate ravelled size for the array"""
		# need to get bits-per-element...
		byteCount = BYTE_SIZES[ typeCode ]
		return len(value)//byteCount
	def arrayByteCount( self, value, typeCode = None ):
		"""Given a data-value, calculate number of bytes required to represent"""
		return len(value)
	def asArray( self, value, typecode=None ):
		"""Convert given value to an array value of given typecode"""
		if isinstance( value, str ):
			return value
		# could convert types to string here, but we're not registered for 
		# anything save string types...
		raise TypeError( """String handler got non-string object: %r"""%(type(value)))
	def dimensions( self, value, typeCode=None ):
		"""Determine dimensions of the passed array value (if possible)"""
		raise TypeError(
			"""Cannot calculate dimensions for a String data-type"""
		)

BYTE_SIZES = {
	constants.GL_DOUBLE: ctypes.sizeof( constants.GLdouble ),
	constants.GL_FLOAT: ctypes.sizeof( constants.GLfloat ),
	constants.GL_INT: ctypes.sizeof( constants.GLint ),
	constants.GL_SHORT: ctypes.sizeof( constants.GLshort ),
	constants.GL_UNSIGNED_BYTE: ctypes.sizeof( constants.GLubyte ),
	constants.GL_UNSIGNED_SHORT: ctypes.sizeof( constants.GLshort ),
	constants.GL_BYTE: ctypes.sizeof( constants.GLbyte ),
	constants.GL_UNSIGNED_INT: ctypes.sizeof( constants.GLuint ),
}
