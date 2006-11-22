'''OpenGL extension SGIX.clipmap

Overview (from the spec)
	
	Mipmaps provide a general but expensive solution when the texture image
	is very large.  This extension defines clipmaps, which occupy a small
	subset of the memory required by equivalent mipmaps, but provide much
	of the mipmap rendering capabilities.  Clipmaps are especially useful
	for rendering terrain.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/clipmap.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_LINEAR_CLIPMAP_LINEAR_SGIX = constant.Constant( 'GL_LINEAR_CLIPMAP_LINEAR_SGIX', 0x8170 )
GL_TEXTURE_CLIPMAP_CENTER_SGIX = constant.Constant( 'GL_TEXTURE_CLIPMAP_CENTER_SGIX', 0x8171 )
GL_TEXTURE_CLIPMAP_FRAME_SGIX = constant.Constant( 'GL_TEXTURE_CLIPMAP_FRAME_SGIX', 0x8172 )
GL_TEXTURE_CLIPMAP_OFFSET_SGIX = constant.Constant( 'GL_TEXTURE_CLIPMAP_OFFSET_SGIX', 0x8173 )
GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX = constant.Constant( 'GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX', 0x8174 )
GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX = constant.Constant( 'GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX', 0x8175 )
GL_TEXTURE_CLIPMAP_DEPTH_SGIX = constant.Constant( 'GL_TEXTURE_CLIPMAP_DEPTH_SGIX', 0x8176 )
GL_MAX_CLIPMAP_DEPTH_SGIX = constant.Constant( 'GL_MAX_CLIPMAP_DEPTH_SGIX', 0x8177 )
GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX = constant.Constant( 'GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX', 0x8178 )
GL_NEAREST_CLIPMAP_NEAREST_SGIX = constant.Constant( 'GL_NEAREST_CLIPMAP_NEAREST_SGIX', 0x844D )
GL_NEAREST_CLIPMAP_LINEAR_SGIX = constant.Constant( 'GL_NEAREST_CLIPMAP_LINEAR_SGIX', 0x844E )
GL_LINEAR_CLIPMAP_NEAREST_SGIX = constant.Constant( 'GL_LINEAR_CLIPMAP_NEAREST_SGIX', 0x844F )


def glInitClipmapSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGIX_clipmap' )
