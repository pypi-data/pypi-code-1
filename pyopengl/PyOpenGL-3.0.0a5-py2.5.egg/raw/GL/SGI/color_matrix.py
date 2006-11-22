'''OpenGL extension SGI.color_matrix

Overview (from the spec)
	
	    This extension adds a 4x4 matrix stack to the pixel transfer path.  The
	    matrix operates on RGBA pixel groups, using the equation
	
		C' = MC,
	
	    where
	
		    |R|
		C = |G|
		    |B|
		    |A|
	
	    and M is the 4x4 matrix on the top of the color matrix stack.  After
	    the matrix multiplication, each resulting color component is scaled
	    and biased by a programmed amount.  Color matrix multiplication follows
	    convolution (and the scale, and bias that are associated with
	    convolution.)
	
	    The color matrix can be used to reassign and duplicate color components.
	    It can also be used to implement simple color space conversions.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGI/color_matrix.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_COLOR_MATRIX_SGI = constant.Constant( 'GL_COLOR_MATRIX_SGI', 0x80B1 )
glget.addGLGetConstant( GL_COLOR_MATRIX_SGI, (4,4) )
GL_COLOR_MATRIX_STACK_DEPTH_SGI = constant.Constant( 'GL_COLOR_MATRIX_STACK_DEPTH_SGI', 0x80B2 )
glget.addGLGetConstant( GL_COLOR_MATRIX_STACK_DEPTH_SGI, (1,) )
GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI = constant.Constant( 'GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI', 0x80B3 )
glget.addGLGetConstant( GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI, (1,) )
GL_POST_COLOR_MATRIX_RED_SCALE_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_RED_SCALE_SGI', 0x80B4 )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_RED_SCALE_SGI, (1,) )
GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI', 0x80B5 )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI, (1,) )
GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI', 0x80B6 )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI, (1,) )
GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI', 0x80B7 )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI, (1,) )
GL_POST_COLOR_MATRIX_RED_BIAS_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_RED_BIAS_SGI', 0x80B8 )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_RED_BIAS_SGI, (1,) )
GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI', 0x80B9 )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI, (1,) )
GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI', 0x80BA )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI, (1,) )
GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI = constant.Constant( 'GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI', 0x80BB )
glget.addGLGetConstant( GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI, (1,) )


def glInitColorMatrixSGI():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGI_color_matrix' )
