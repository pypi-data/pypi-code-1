'''OpenGL extension EXT.subtexture

Overview (from the spec)
	
	This extension allows a contiguous portion of an already-existing
	texture image to be redefined, without affecting the remaining portion
	of the image, or any of the other state that describe the texture.  No
	provision is made to query a subregion of a texture.
	
	Semantics for null image pointers are defined for TexImage1D,
	TexImage2D, and TexImage3DEXT.  Null image pointers can be used by
	applications to effectively support texture arrays whose dimensions
	are not a power of 2.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/subtexture.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes

glTexSubImage1DEXT = platform.createExtensionFunction( 
	'glTexSubImage1DEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLint, constants.GLsizei, constants.GLenum, constants.GLenum, ctypes.c_void_p,),
	doc = 'glTexSubImage1DEXT( GLenum(target), GLint(level), GLint(xoffset), GLsizei(width), GLenum(format), GLenum(type), c_void_p(pixels) ) -> None',
	argNames = ('target', 'level', 'xoffset', 'width', 'format', 'type', 'pixels',),
)

glTexSubImage2DEXT = platform.createExtensionFunction( 
	'glTexSubImage2DEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLint, constants.GLint, constants.GLsizei, constants.GLsizei, constants.GLenum, constants.GLenum, ctypes.c_void_p,),
	doc = 'glTexSubImage2DEXT( GLenum(target), GLint(level), GLint(xoffset), GLint(yoffset), GLsizei(width), GLsizei(height), GLenum(format), GLenum(type), c_void_p(pixels) ) -> None',
	argNames = ('target', 'level', 'xoffset', 'yoffset', 'width', 'height', 'format', 'type', 'pixels',),
)


def glInitSubtextureEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_subtexture' )
