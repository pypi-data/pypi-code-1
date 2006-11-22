'''OpenGL extension SGIX.interlace

Overview (from the spec)
	
	This extension provides a way to interlace rows of pixels when
	rasterizing pixel rectangles, and loading texture images.  In this
	context, interlacing means skiping over rows of pixels or texels
	in the destination.  This is useful for dealing with video data
	since a single frame of video is typically composed from two images
	or fields: one image specifying the data for even rows of the frame
	and the other image specifying the data for odd rows of the frame.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/interlace.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_INTERLACE_SGIX = constant.Constant( 'GL_INTERLACE_SGIX', 0x8094 )
glget.addGLGetConstant( GL_INTERLACE_SGIX, (1,) )


def glInitInterlaceSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGIX_interlace' )
