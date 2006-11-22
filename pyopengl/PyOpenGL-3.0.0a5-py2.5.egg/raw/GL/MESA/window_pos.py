'''OpenGL extension MESA.window_pos

Overview (from the spec)
	
	In order to set the current raster position to a specific window
	coordinate with the RasterPos command, the modelview matrix, projection
	matrix and viewport must be set very carefully.  Furthermore, if the
	desired window coordinate is outside of the window's bounds one must
	rely on a subtle side-effect of the Bitmap command in order to circumvent
	frustum clipping.
	
	This extension provides a set of functions to directly set the
	current raster position, bypassing the modelview matrix, the
	projection matrix and the viewport to window mapping.  Furthermore,
	clip testing is not performed.
	
	This greatly simplifies the process of setting the current raster
	position to a specific window coordinate prior to calling DrawPixels,
	CopyPixels or Bitmap.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/MESA/window_pos.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes

glWindowPos2dMESA = platform.createExtensionFunction( 
	'glWindowPos2dMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLdouble, constants.GLdouble,),
	doc = 'glWindowPos2dMESA( GLdouble(x), GLdouble(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2dvMESA = platform.createExtensionFunction( 
	'glWindowPos2dvMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glWindowPos2dvMESA( GLdoubleArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos2fMESA = platform.createExtensionFunction( 
	'glWindowPos2fMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLfloat, constants.GLfloat,),
	doc = 'glWindowPos2fMESA( GLfloat(x), GLfloat(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2fvMESA = platform.createExtensionFunction( 
	'glWindowPos2fvMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glWindowPos2fvMESA( GLfloatArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos2iMESA = platform.createExtensionFunction( 
	'glWindowPos2iMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint,),
	doc = 'glWindowPos2iMESA( GLint(x), GLint(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2ivMESA = platform.createExtensionFunction( 
	'glWindowPos2ivMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLintArray,),
	doc = 'glWindowPos2ivMESA( GLintArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos2sMESA = platform.createExtensionFunction( 
	'glWindowPos2sMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLshort, constants.GLshort,),
	doc = 'glWindowPos2sMESA( GLshort(x), GLshort(y) ) -> None',
	argNames = ('x', 'y',),
)

glWindowPos2svMESA = platform.createExtensionFunction( 
	'glWindowPos2svMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLshortArray,),
	doc = 'glWindowPos2svMESA( GLshortArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3dMESA = platform.createExtensionFunction( 
	'glWindowPos3dMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glWindowPos3dMESA( GLdouble(x), GLdouble(y), GLdouble(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3dvMESA = platform.createExtensionFunction( 
	'glWindowPos3dvMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glWindowPos3dvMESA( GLdoubleArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3fMESA = platform.createExtensionFunction( 
	'glWindowPos3fMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glWindowPos3fMESA( GLfloat(x), GLfloat(y), GLfloat(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3fvMESA = platform.createExtensionFunction( 
	'glWindowPos3fvMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glWindowPos3fvMESA( GLfloatArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3iMESA = platform.createExtensionFunction( 
	'glWindowPos3iMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glWindowPos3iMESA( GLint(x), GLint(y), GLint(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3ivMESA = platform.createExtensionFunction( 
	'glWindowPos3ivMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLintArray,),
	doc = 'glWindowPos3ivMESA( GLintArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos3sMESA = platform.createExtensionFunction( 
	'glWindowPos3sMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glWindowPos3sMESA( GLshort(x), GLshort(y), GLshort(z) ) -> None',
	argNames = ('x', 'y', 'z',),
)

glWindowPos3svMESA = platform.createExtensionFunction( 
	'glWindowPos3svMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLshortArray,),
	doc = 'glWindowPos3svMESA( GLshortArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos4dMESA = platform.createExtensionFunction( 
	'glWindowPos4dMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLdouble, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glWindowPos4dMESA( GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w) ) -> None',
	argNames = ('x', 'y', 'z', 'w',),
)

glWindowPos4dvMESA = platform.createExtensionFunction( 
	'glWindowPos4dvMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glWindowPos4dvMESA( GLdoubleArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos4fMESA = platform.createExtensionFunction( 
	'glWindowPos4fMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLfloat, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glWindowPos4fMESA( GLfloat(x), GLfloat(y), GLfloat(z), GLfloat(w) ) -> None',
	argNames = ('x', 'y', 'z', 'w',),
)

glWindowPos4fvMESA = platform.createExtensionFunction( 
	'glWindowPos4fvMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glWindowPos4fvMESA( GLfloatArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos4iMESA = platform.createExtensionFunction( 
	'glWindowPos4iMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glWindowPos4iMESA( GLint(x), GLint(y), GLint(z), GLint(w) ) -> None',
	argNames = ('x', 'y', 'z', 'w',),
)

glWindowPos4ivMESA = platform.createExtensionFunction( 
	'glWindowPos4ivMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLintArray,),
	doc = 'glWindowPos4ivMESA( GLintArray(v) ) -> None',
	argNames = ('v',),
)

glWindowPos4sMESA = platform.createExtensionFunction( 
	'glWindowPos4sMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLshort, constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glWindowPos4sMESA( GLshort(x), GLshort(y), GLshort(z), GLshort(w) ) -> None',
	argNames = ('x', 'y', 'z', 'w',),
)

glWindowPos4svMESA = platform.createExtensionFunction( 
	'glWindowPos4svMESA', dll=platform.GL,
	resultType=None, 
	argTypes=(arrays.GLshortArray,),
	doc = 'glWindowPos4svMESA( GLshortArray(v) ) -> None',
	argNames = ('v',),
)


def glInitWindowPosMESA():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_MESA_window_pos' )
