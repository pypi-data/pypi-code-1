'''OpenGL extension EXT.texture_perturb_normal

Overview (from the spec)
	
	This extension defines a mechanism for using texture values to perturb
	the fragment normal vector prior to fragment lighting.  It enables a
	direct implementation of the original formulation of bump mapping by
	Blinn.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_perturb_normal.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_PERTURB_EXT = constant.Constant( 'GL_PERTURB_EXT', 0x85AE )
GL_TEXTURE_NORMAL_EXT = constant.Constant( 'GL_TEXTURE_NORMAL_EXT', 0x85AF )
glTextureNormalEXT = platform.createExtensionFunction( 
	'glTextureNormalEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum,),
	doc = 'glTextureNormalEXT( GLenum(mode) ) -> None',
	argNames = ('mode',),
)


def glInitTexturePerturbNormalEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_texture_perturb_normal' )
