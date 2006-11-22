'''OpenGL extension EXT.texture

Overview (from the spec)
	
	The original intention of this extension was simply to support various
	numeric resolutions of color components in texture images.  While it
	accomplishes this, it also accomplishes a larger task, that of
	formalizing the notion of an internal format for images, corresponding
	to the external format that already existed for image data in host
	memory.  This notion of an internal image format will be used
	extensively in later extensions, especially those concerned with pixel
	manipulation.
	
	The idea of an internal format is simple: rather than treating a
	retained image as having 1, 2, 3, or 4 components, treat it as though
	it has a specific format, such as LUMINANCE_ALPHA, or just ALPHA.  Then
	define the semantics of the use of internal images with these formats in
	a consistent way.  Because texture mapping is already defined in GL, the
	semantics for internal-format images were chosen to match those of the 1,
	2, 3, and 4 component internal images that already existed.  The new
	semantics are a superset of the old ones, however, so this extension
	adds capabilities to GL, as well as allowing internal resolutions to be
	specified.
	
	This extension also defines a robust method for applications to
	determine what combinations of texture dimensions and resolutions are
	supported by an implementation.  It also introduces a new texture
	environment: REPLACE_EXT.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_ALPHA4_EXT = constant.Constant( 'GL_ALPHA4_EXT', 0x803B )
GL_ALPHA8_EXT = constant.Constant( 'GL_ALPHA8_EXT', 0x803C )
GL_ALPHA12_EXT = constant.Constant( 'GL_ALPHA12_EXT', 0x803D )
GL_ALPHA16_EXT = constant.Constant( 'GL_ALPHA16_EXT', 0x803E )
GL_LUMINANCE4_EXT = constant.Constant( 'GL_LUMINANCE4_EXT', 0x803F )
GL_LUMINANCE8_EXT = constant.Constant( 'GL_LUMINANCE8_EXT', 0x8040 )
GL_LUMINANCE12_EXT = constant.Constant( 'GL_LUMINANCE12_EXT', 0x8041 )
GL_LUMINANCE16_EXT = constant.Constant( 'GL_LUMINANCE16_EXT', 0x8042 )
GL_LUMINANCE4_ALPHA4_EXT = constant.Constant( 'GL_LUMINANCE4_ALPHA4_EXT', 0x8043 )
GL_LUMINANCE6_ALPHA2_EXT = constant.Constant( 'GL_LUMINANCE6_ALPHA2_EXT', 0x8044 )
GL_LUMINANCE8_ALPHA8_EXT = constant.Constant( 'GL_LUMINANCE8_ALPHA8_EXT', 0x8045 )
GL_LUMINANCE12_ALPHA4_EXT = constant.Constant( 'GL_LUMINANCE12_ALPHA4_EXT', 0x8046 )
GL_LUMINANCE12_ALPHA12_EXT = constant.Constant( 'GL_LUMINANCE12_ALPHA12_EXT', 0x8047 )
GL_LUMINANCE16_ALPHA16_EXT = constant.Constant( 'GL_LUMINANCE16_ALPHA16_EXT', 0x8048 )
GL_INTENSITY_EXT = constant.Constant( 'GL_INTENSITY_EXT', 0x8049 )
GL_INTENSITY4_EXT = constant.Constant( 'GL_INTENSITY4_EXT', 0x804A )
GL_INTENSITY8_EXT = constant.Constant( 'GL_INTENSITY8_EXT', 0x804B )
GL_INTENSITY12_EXT = constant.Constant( 'GL_INTENSITY12_EXT', 0x804C )
GL_INTENSITY16_EXT = constant.Constant( 'GL_INTENSITY16_EXT', 0x804D )
GL_RGB2_EXT = constant.Constant( 'GL_RGB2_EXT', 0x804E )
GL_RGB4_EXT = constant.Constant( 'GL_RGB4_EXT', 0x804F )
GL_RGB5_EXT = constant.Constant( 'GL_RGB5_EXT', 0x8050 )
GL_RGB8_EXT = constant.Constant( 'GL_RGB8_EXT', 0x8051 )
GL_RGB10_EXT = constant.Constant( 'GL_RGB10_EXT', 0x8052 )
GL_RGB12_EXT = constant.Constant( 'GL_RGB12_EXT', 0x8053 )
GL_RGB16_EXT = constant.Constant( 'GL_RGB16_EXT', 0x8054 )
GL_RGBA2_EXT = constant.Constant( 'GL_RGBA2_EXT', 0x8055 )
GL_RGBA4_EXT = constant.Constant( 'GL_RGBA4_EXT', 0x8056 )
GL_RGB5_A1_EXT = constant.Constant( 'GL_RGB5_A1_EXT', 0x8057 )
GL_RGBA8_EXT = constant.Constant( 'GL_RGBA8_EXT', 0x8058 )
GL_RGB10_A2_EXT = constant.Constant( 'GL_RGB10_A2_EXT', 0x8059 )
GL_RGBA12_EXT = constant.Constant( 'GL_RGBA12_EXT', 0x805A )
GL_RGBA16_EXT = constant.Constant( 'GL_RGBA16_EXT', 0x805B )
GL_TEXTURE_RED_SIZE_EXT = constant.Constant( 'GL_TEXTURE_RED_SIZE_EXT', 0x805C )
GL_TEXTURE_GREEN_SIZE_EXT = constant.Constant( 'GL_TEXTURE_GREEN_SIZE_EXT', 0x805D )
GL_TEXTURE_BLUE_SIZE_EXT = constant.Constant( 'GL_TEXTURE_BLUE_SIZE_EXT', 0x805E )
GL_TEXTURE_ALPHA_SIZE_EXT = constant.Constant( 'GL_TEXTURE_ALPHA_SIZE_EXT', 0x805F )
GL_TEXTURE_LUMINANCE_SIZE_EXT = constant.Constant( 'GL_TEXTURE_LUMINANCE_SIZE_EXT', 0x8060 )
GL_TEXTURE_INTENSITY_SIZE_EXT = constant.Constant( 'GL_TEXTURE_INTENSITY_SIZE_EXT', 0x8061 )
GL_REPLACE_EXT = constant.Constant( 'GL_REPLACE_EXT', 0x8062 )
GL_PROXY_TEXTURE_1D_EXT = constant.Constant( 'GL_PROXY_TEXTURE_1D_EXT', 0x8063 )
GL_PROXY_TEXTURE_2D_EXT = constant.Constant( 'GL_PROXY_TEXTURE_2D_EXT', 0x8064 )
GL_TEXTURE_TOO_LARGE_EXT = constant.Constant( 'GL_TEXTURE_TOO_LARGE_EXT', 0x8065 )


def glInitTextureEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_EXT_texture' )
