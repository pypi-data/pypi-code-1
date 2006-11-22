'''OpenGL extension EXT.paletted_texture

Overview (from the spec)
	
	EXT_paletted_texture defines new texture formats and new calls to
	support the use of paletted textures in OpenGL.  A paletted texture is
	defined by giving both a palette of colors and a set of image data which
	is composed of indices into the palette.  The paletted texture cannot
	function properly without both pieces of information so it increases the
	work required to define a texture.  This is offset by the fact that the
	overall amount of texture data can be reduced dramatically by factoring
	redundant information out of the logical view of the texture and placing
	it in the palette.
	
	Paletted textures provide several advantages over full-color textures:
	
	* As mentioned above, the amount of data required to define a
	texture can be greatly reduced over what would be needed for full-color
	specification.  For example, consider a source texture that has only 256
	distinct colors in a 256 by 256 pixel grid.  Full-color representation
	requires three bytes per pixel, taking 192K of texture data.  By putting
	the distinct colors in a palette only eight bits are required per pixel,
	reducing the 192K to 64K plus 768 bytes for the palette.  Now add an
	alpha channel to the texture.  The full-color representation increases
	by 64K while the paletted version would only increase by 256 bytes.
	This reduction in space required is particularly important for hardware
	accelerators where texture space is limited.
	
	* Paletted textures allow easy reuse of texture data for images
	which require many similar but slightly different colored objects.
	Consider a driving simulation with heavy traffic on the road.  Many of
	the cars will be similar but with different color schemes.  If
	full-color textures are used a separate texture would be needed for each
	color scheme, while paletted textures allow the same basic index data to
	be reused for each car, with a different palette to change the final
	colors.
	
	* Paletted textures also allow use of all the palette tricks
	developed for paletted displays.  Simple animation can be done, along
	with strobing, glowing and other palette-cycling effects.  All of these
	techniques can enhance the visual richness of a scene with very little
	data.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/paletted_texture.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_COLOR_INDEX1_EXT = constant.Constant( 'GL_COLOR_INDEX1_EXT', 0x80E2 )
GL_COLOR_INDEX2_EXT = constant.Constant( 'GL_COLOR_INDEX2_EXT', 0x80E3 )
GL_COLOR_INDEX4_EXT = constant.Constant( 'GL_COLOR_INDEX4_EXT', 0x80E4 )
GL_COLOR_INDEX8_EXT = constant.Constant( 'GL_COLOR_INDEX8_EXT', 0x80E5 )
GL_COLOR_INDEX12_EXT = constant.Constant( 'GL_COLOR_INDEX12_EXT', 0x80E6 )
GL_COLOR_INDEX16_EXT = constant.Constant( 'GL_COLOR_INDEX16_EXT', 0x80E7 )
GL_TEXTURE_INDEX_SIZE_EXT = constant.Constant( 'GL_TEXTURE_INDEX_SIZE_EXT', 0x80ED )
glColorTableEXT = platform.createExtensionFunction( 
	'glColorTableEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, constants.GLsizei, constants.GLenum, constants.GLenum, ctypes.c_void_p,),
	doc = 'glColorTableEXT( GLenum(target), GLenum(internalFormat), GLsizei(width), GLenum(format), GLenum(type), c_void_p(table) ) -> None',
	argNames = ('target', 'internalFormat', 'width', 'format', 'type', 'table',),
)

glGetColorTableEXT = platform.createExtensionFunction( 
	'glGetColorTableEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, constants.GLenum, ctypes.c_void_p,),
	doc = 'glGetColorTableEXT( GLenum(target), GLenum(format), GLenum(type), c_void_p(data) ) -> None',
	argNames = ('target', 'format', 'type', 'data',),
)

glGetColorTableParameterivEXT = platform.createExtensionFunction( 
	'glGetColorTableParameterivEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetColorTableParameterivEXT( GLenum(target), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('target', 'pname', 'params',),
)

glGetColorTableParameterfvEXT = platform.createExtensionFunction( 
	'glGetColorTableParameterfvEXT', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetColorTableParameterfvEXT( GLenum(target), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('target', 'pname', 'params',),
)


def glInitPalettedTextureEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_paletted_texture' )
