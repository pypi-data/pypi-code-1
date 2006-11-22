'''OpenGL extension ARB.point_parameters

Overview (from the spec)
	
	    This extension supports additional geometric characteristics of
	    points. It can be used to render particles or tiny light sources,
	    commonly referred to as "Light points".
	
	    The raster brightness of a point is a function of the point area,
	    point color, point transparency, and the response of the display's
	    electron gun and phosphor. The point area and the point transparency
	    are derived from the point size, currently provided with the <size>
	    parameter of glPointSize.
	
	    The primary motivation is to allow the size of a point to be
	    affected by distance attenuation. When distance attenuation has an
	    effect, the final point size decreases as the distance of the point
	    from the eye increases.
	
	    The secondary motivation is a mean to control the mapping from the
	    point size to the raster point area and point transparency. This is
	    done in order to increase the dynamic range of the raster brightness
	    of points. In other words, the alpha component of a point may be
	    decreased (and its transparency increased) as its area shrinks below
	    a defined threshold.
	
	    This extension defines a derived point size to be closely related to
	    point brightness. The brightness of a point is given by:
	
				1
		dist_atten(d) = -------------------
				a + b * d + c * d^2
	
		brightness(Pe) = Brightness * dist_atten(|Pe|)
	
	    where 'Pe' is the point in eye coordinates, and 'Brightness' is some
	    initial value proportional to the square of the size provided with
	    PointSize. Here we simplify the raster brightness to be a function
	    of the rasterized point area and point transparency.
	
			    brightness(Pe)	 brightness(Pe) >= Threshold_Area
		area(Pe) =
			    Threshold_Area	 Otherwise
	
		factor(Pe) = brightness(Pe)/Threshold_Area
	
		alpha(Pe) = Alpha * factor(Pe)
	
	    where 'Alpha' comes with the point color (possibly modified by
	    lighting).
	
	    'Threshold_Area' above is in area units. Thus, it is proportional to
	    the square of the threshold provided by the programmer through this
	    extension.
	
	    The new point size derivation method applies to all points, while
	    the threshold applies to multisample points only.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/point_parameters.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_POINT_SIZE_MIN_ARB = constant.Constant( 'GL_POINT_SIZE_MIN_ARB', 0x8126 )
GL_POINT_SIZE_MAX_ARB = constant.Constant( 'GL_POINT_SIZE_MAX_ARB', 0x8127 )
GL_POINT_FADE_THRESHOLD_SIZE_ARB = constant.Constant( 'GL_POINT_FADE_THRESHOLD_SIZE_ARB', 0x8128 )
GL_POINT_DISTANCE_ATTENUATION_ARB = constant.Constant( 'GL_POINT_DISTANCE_ATTENUATION_ARB', 0x8129 )
glPointParameterfARB = platform.createExtensionFunction( 
	'glPointParameterfARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat,),
	doc = 'glPointParameterfARB( GLenum(pname), GLfloat(param) ) -> None',
	argNames = ('pname', 'param',),
)

glPointParameterfvARB = platform.createExtensionFunction( 
	'glPointParameterfvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glPointParameterfvARB( GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('pname', 'params',),
)


def glInitPointParametersARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_ARB_point_parameters' )
