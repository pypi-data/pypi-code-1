'''OpenGL extension SGI.texture_color_table

Overview (from the spec)
	
	This extension adds a color lookup table to the texture mechanism.
	The table is applied to the filtered result of a texture lookup,
	before that result is used in the texture environment equations.
	
	The definition and application of the texture color table are
	similar to those of the color tables defined in SGI_color_table,
	though it is not necessary for that extension to be implemented.
	
	Texture color tables can be used to expand luminance or intensity
	textures to full RGBA, and also to linearize the results of color
	space conversions implemented by multidimensional texture table
	lookup.
	
	This specification has been updated to define its interaction with
	multitexture.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGI/texture_color_table.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_TEXTURE_COLOR_TABLE_SGI = constant.Constant( 'GL_TEXTURE_COLOR_TABLE_SGI', 0x80BC )
glget.addGLGetConstant( GL_TEXTURE_COLOR_TABLE_SGI, (1,) )
GL_PROXY_TEXTURE_COLOR_TABLE_SGI = constant.Constant( 'GL_PROXY_TEXTURE_COLOR_TABLE_SGI', 0x80BD )


def glInitTextureColorTableSGI():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGI_texture_color_table' )
