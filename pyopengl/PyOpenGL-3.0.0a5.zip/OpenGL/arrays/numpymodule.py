"""Numpy (new version) module implementation of the OpenGL-ctypes array interfaces

XXX Need to register handlers for all of the scalar types that numpy returns,
would like to have all return values be int/float if they are of  compatible
type as well.
"""
REGISTRY_NAME = 'numpy'
try:
	import numpy
except ImportError, err:
	raise ImportError( """No numpy module present: %s"""%(err))
import operator

# numpy's array interface has changed over time :(
testArray = numpy.array( [1,2,3,4],'i' )
if hasattr(testArray,'__array_data__'):
	def dataPointer( self, instance ):
		"""Convert given instance to a data-pointer value (integer)"""
		try:
			return long(instance.__array_data__[0],0)
		except AttributeError, err:
			instance = self.asArray( instance )
			return long(instance.__array_interface__['data'][0])
else:
	def dataPointer( self, instance ):
		"""Convert given instance to a data-pointer value (integer)"""
		try:
			return long(instance.__array_interface__['data'][0])
		except AttributeError, err:
			instance = self.asArray( instance )
			return long(instance.__array_interface__['data'][0])

from OpenGL import constants, constant
from OpenGL.arrays import formathandler

class NumpyHandler( formathandler.FormatHandler ):
	"""Numpy-specific data-type handler for OpenGL
	
	Attributes:
	
		ERROR_ON_COPY -- if True, will raise errors 
			if we have to copy an array object in order to produce
			a contiguous array of the correct type.
	"""
	HANDLED_TYPES = (numpy.ndarray, list, tuple )
	from_param = dataPointer
	dataPointer = dataPointer
	ERROR_ON_COPY = False
	def voidDataPointer( cls, value ):
		"""Given value in a known data-pointer type, return void_p for pointer"""
		return ctypes.c_void_p( self.dataPointer( value ))
	def zeros( self, dims, typeCode ):
		"""Return Numpy array of zeros in given size"""
		return numpy.zeros( dims, GL_TYPE_TO_ARRAY_MAPPING.get(typeCode) or typeCode )
	def arrayToGLType( self, value ):
		"""Given a value, guess OpenGL type of the corresponding pointer"""
		typecode = value.dtype.char
		constant = ARRAY_TO_GL_TYPE_MAPPING.get( typecode )
		if constant is None:
			raise TypeError(
				"""Don't know GL type for array of type %r, known types: %s\nvalue:%s"""%(
					typecode, ARRAY_TO_GL_TYPE_MAPPING.keys(), value,
				)
			)
		return constant
	def arraySize( self, value, typeCode = None ):
		"""Given a data-value, calculate dimensions for the array"""
		try:
			dimValue = value.shape
		except AttributeError, err:
			# XXX it's a list or a tuple, how do we determine dimensions there???
			# for now we'll just punt and convert to an array first...
			value = self.asArray( value, typeCode )
			dimValue = value.shape 
		dims = 1
		for dim in dimValue:
			dims *= dim 
		return dims 
	def arrayByteCount( self, value, typeCode = None ):
		"""Given a data-value, calculate number of bytes required to represent"""
		try:
			return self.arraySize( value, typeCode ) * value.itemsize
		except AttributeError, err:
			value = self.asArray( value, typeCode )
			return self.arraySize( value, typeCode ) * value.itemsize
	def asArray( self, value, typecode=None ):
		"""Convert given value to an array value of given typecode"""
		if value is None:
			return value
		else:
			return self.contiguous( value, typecode )

	def contiguous( self, source, typecode=None ):
		"""Get contiguous array from source
		
		source -- numpy Python array (or compatible object)
			for use as the data source.  If this is not a contiguous
			array of the given typecode, a copy will be made, 
			otherwise will just be returned unchanged.
		typecode -- optional 1-character typecode specifier for
			the numpy.array function.
			
		All gl*Pointer calls should use contiguous arrays, as non-
		contiguous arrays will be re-copied on every rendering pass.
		Although this doesn't raise an error, it does tend to slow
		down rendering.
		"""
		typecode = GL_TYPE_TO_ARRAY_MAPPING.get( typecode )
		if isinstance( source, numpy.ndarray):
			if source.flags.contiguous and (typecode is None or typecode==source.dtype.char):
				return source
			elif (source.flags.contiguous and self.ERROR_ON_COPY):
				from OpenGL import error
				raise error.CopyError(
					"""Array of type %r passed, required array of type %r""",
					source.dtype.char, typecode,
				)
			else:
				# We have to do astype to avoid errors about unsafe conversions
				# XXX Confirm that this will *always* create a new contiguous array 
				# XXX Allow a way to make this raise an error for performance reasons
				# XXX Guard against wacky conversion types like uint to float, where
				# we really don't want to have the C-level conversion occur.
				if self.ERROR_ON_COPY:
					from OpenGL import error
					raise error.CopyError(
						"""Non-contiguous array passed""",
						source,
					)
				return numpy.array( source.astype( typecode ), typecode )
		elif typecode:
			return numpy.array( source, typecode )
		else:
			return numpy.array( source )
	def unitSize( self, value, typeCode=None ):
		"""Determine unit size of an array (if possible)"""
		return value.shape[1]
	def dimensions( self, value, typeCode=None ):
		"""Determine dimensions of the passed array value (if possible)"""
		return value.shape

try:
	numpy.array( [1], 's' )
	SHORT_TYPE = 's'
except TypeError, err:
	SHORT_TYPE = 'short'

ARRAY_TO_GL_TYPE_MAPPING = {
	'd': constants.GL_DOUBLE,
	'f': constants.GL_FLOAT,
	'i': constants.GL_INT,
	SHORT_TYPE: constants.GL_SHORT,
	'c': constants.GL_UNSIGNED_BYTE,
	'b': constants.GL_BYTE,
	'I': constants.GL_UNSIGNED_INT,
}
GL_TYPE_TO_ARRAY_MAPPING = {
	constants.GL_DOUBLE: 'd',
	constants.GL_FLOAT:'f',
	constants.GL_INT: 'i',
	constants.GL_UNSIGNED_INT: 'i',
	constants.GL_UNSIGNED_BYTE: 'b',
	constants.GL_SHORT: SHORT_TYPE,
	constants.GL_UNSIGNED_SHORT: SHORT_TYPE,
	constants.GL_BYTE: 'b',
}
