'''OpenGL extension EXT.rescale_normal

Overview (from the spec)
	
	When normal rescaling is enabled a new operation is added to the
	transformation of the normal vector into eye coordinates.  The normal vector 
	is rescaled after it is multiplied by the inverse modelview matrix and 
	before it is normalized.  
	
	The rescale factor is chosen so that in many cases normal vectors with unit
	length in object coordinates will not need to be normalized as they
	are transformed into eye coordinates.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/rescale_normal.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_RESCALE_NORMAL_EXT = constant.Constant( 'GL_RESCALE_NORMAL_EXT', 0x803A )


def glInitRescaleNormalEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_rescale_normal' )
