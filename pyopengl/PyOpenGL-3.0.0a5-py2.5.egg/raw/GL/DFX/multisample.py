'''OpenGL extension DFX.multisample

Overview (from the spec)
	
	    This extension provides a mechanism to antialias all GL primitives:
	    points, lines, polygons, bitmaps, and images. The technique is to
	    sample all primitives multiple times at each pixel. The color sample
	    values are resolved to a single, displayable color each time a pixel
	    is updated, so the antialiasing appears to be automatic at the
	    application level. Because each sample includes depth and stencil
	    information, the depth and stencil functions perform equivalently to
	    the single-sample mode.
	
	    An additional buffer, called the multisample buffer, is added to the
	    framebuffer. Pixel sample values, including color, depth, and
	    stencil values, are stored in this buffer. When the framebuffer
	    includes a multisample buffer, it does not also include separate
	    depth or stencil buffers, even if the multisample buffer does not
	    store depth or stencil values. Color buffers (left/right,
	    front/back, and aux) do coexist with the multisample buffer,
	    however.
	
	    Multisample antialiasing is most valuable for rendering polygons,
	    because it requires no sorting for hidden surface elimination, and
	    it correctly handles adjacent polygons, object silhouettes, and even
	    intersecting polygons. If only points or lines are being rendered,
	    the "smooth" antialiasing mechanism provided by the base GL may
	    result in a higher quality image.
	
	    This extension is a subset of SGIS_multisample. It differs in these
	    key ways:
	
	       * Fragment alpha values are not affected by the fragment sample mask
	       * The sample locations may or may not be fixed. Thus, there is no
		 support for rendering the scene multiple times with different
		 sample points.
	       * Fragment masks are not computed for images or for bitmasks.
	
	    Because of these differences a new extension was created. However,
	    it is not expected that this extension will co-exist with
	    SGIS_multisample. Because of this and the fact that there are only
	    32 push/pop bits the MULTISAMPLE_BIT_SGIS state value is the same as
	    MUTLISAMPLE_BIT_3DFX.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/DFX/multisample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_MULTISAMPLE_3DFX = constant.Constant( 'GL_MULTISAMPLE_3DFX', 0x86B2 )
glget.addGLGetConstant( GL_MULTISAMPLE_3DFX, (1,) )
GL_SAMPLE_BUFFERS_3DFX = constant.Constant( 'GL_SAMPLE_BUFFERS_3DFX', 0x86B3 )
glget.addGLGetConstant( GL_SAMPLE_BUFFERS_3DFX, (1,) )
GL_SAMPLES_3DFX = constant.Constant( 'GL_SAMPLES_3DFX', 0x86B4 )
glget.addGLGetConstant( GL_SAMPLES_3DFX, (1,) )
GL_MULTISAMPLE_BIT_3DFX = constant.Constant( 'GL_MULTISAMPLE_BIT_3DFX', 0x20000000 )


def glInitMultisampleDFX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_DFX_multisample' )
