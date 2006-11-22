'''OpenGL extension EXT.multi_draw_arrays

Overview (from the spec)
	
	These functions behave identically to the standard OpenGL 1.1 functions
	glDrawArrays() and glDrawElements() except they handle multiple lists of
	vertices in one call. Their main purpose is to allow one function call
	to render more than one primitive such as triangle strip, triangle fan,
	etc.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/multi_draw_arrays.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes

glMultiDrawArraysEXT = platform.createExtensionFunction( 
	'glMultiDrawArraysEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLintArray, arrays.GLsizeiArray, constants.GLsizei,),
	doc = 'glMultiDrawArraysEXT( GLenum(mode), GLintArray(first), GLsizeiArray(count), GLsizei(primcount) ) -> None',
	argNames = ('mode', 'first', 'count', 'primcount',),
)

glMultiDrawElementsEXT = platform.createExtensionFunction( 
	'glMultiDrawElementsEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLsizeiArray, constants.GLenum, ctypes.POINTER(ctypes.c_void_p), constants.GLsizei,),
	doc = 'glMultiDrawElementsEXT( GLenum(mode), GLsizeiArray(count), GLenum(type), POINTER(ctypes.c_void_p)(indices), GLsizei(primcount) ) -> None',
	argNames = ('mode', 'count', 'type', 'indices', 'primcount',),
)


def glInitMultiDrawArraysEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_multi_draw_arrays' )
