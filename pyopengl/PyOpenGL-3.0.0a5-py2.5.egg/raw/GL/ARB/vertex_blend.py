'''OpenGL extension ARB.vertex_blend

Overview (from the spec)
	
	This extension provides the ability to replace the single
	modelview transformation with a set of n vertex units. (Where
	n is constrained to an implementation defined maximum.) Each
	unit has its own modelview transform matrix. For each unit,
	there is a current weight associated with the vertex. When
	this extension is enabled the vertices are transformed by
	the modelview matrices of all of the enabled units. Afterward,
	these results are scaled by the weights for the respective
	units and then summed to create the eye-space vertex. A
	similar procedure is followed for the normals, except they
	are transformed by the inverse transpose of the modelview
	matrices.
	
	This extension is an orthoganalized version of functionality
	already provided by other 3D graphics API's.
	

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/vertex_blend.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_MAX_VERTEX_UNITS_ARB = constant.Constant( 'GL_MAX_VERTEX_UNITS_ARB', 0x86A4 )
glget.addGLGetConstant( GL_MAX_VERTEX_UNITS_ARB, (1,) )
GL_ACTIVE_VERTEX_UNITS_ARB = constant.Constant( 'GL_ACTIVE_VERTEX_UNITS_ARB', 0x86A5 )
glget.addGLGetConstant( GL_ACTIVE_VERTEX_UNITS_ARB, (1,) )
GL_WEIGHT_SUM_UNITY_ARB = constant.Constant( 'GL_WEIGHT_SUM_UNITY_ARB', 0x86A6 )
glget.addGLGetConstant( GL_WEIGHT_SUM_UNITY_ARB, (1,) )
GL_VERTEX_BLEND_ARB = constant.Constant( 'GL_VERTEX_BLEND_ARB', 0x86A7 )
glget.addGLGetConstant( GL_VERTEX_BLEND_ARB, (1,) )
GL_CURRENT_WEIGHT_ARB = constant.Constant( 'GL_CURRENT_WEIGHT_ARB', 0x86A8 )
glget.addGLGetConstant( GL_CURRENT_WEIGHT_ARB, (1,) )
GL_WEIGHT_ARRAY_TYPE_ARB = constant.Constant( 'GL_WEIGHT_ARRAY_TYPE_ARB', 0x86A9 )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_TYPE_ARB, (1,) )
GL_WEIGHT_ARRAY_STRIDE_ARB = constant.Constant( 'GL_WEIGHT_ARRAY_STRIDE_ARB', 0x86AA )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_STRIDE_ARB, (1,) )
GL_WEIGHT_ARRAY_SIZE_ARB = constant.Constant( 'GL_WEIGHT_ARRAY_SIZE_ARB', 0x86AB )
glget.addGLGetConstant( GL_WEIGHT_ARRAY_SIZE_ARB, (1,) )
GL_WEIGHT_ARRAY_POINTER_ARB = constant.Constant( 'GL_WEIGHT_ARRAY_POINTER_ARB', 0x86AC )
GL_WEIGHT_ARRAY_ARB = constant.Constant( 'GL_WEIGHT_ARRAY_ARB', 0x86AD )
GL_MODELVIEW0_ARB = constant.Constant( 'GL_MODELVIEW0_ARB', 0x1700 )
GL_MODELVIEW1_ARB = constant.Constant( 'GL_MODELVIEW1_ARB', 0x850A )
GL_MODELVIEW2_ARB = constant.Constant( 'GL_MODELVIEW2_ARB', 0x8722 )
GL_MODELVIEW3_ARB = constant.Constant( 'GL_MODELVIEW3_ARB', 0x8723 )
GL_MODELVIEW4_ARB = constant.Constant( 'GL_MODELVIEW4_ARB', 0x8724 )
GL_MODELVIEW5_ARB = constant.Constant( 'GL_MODELVIEW5_ARB', 0x8725 )
GL_MODELVIEW6_ARB = constant.Constant( 'GL_MODELVIEW6_ARB', 0x8726 )
GL_MODELVIEW7_ARB = constant.Constant( 'GL_MODELVIEW7_ARB', 0x8727 )
GL_MODELVIEW8_ARB = constant.Constant( 'GL_MODELVIEW8_ARB', 0x8728 )
GL_MODELVIEW9_ARB = constant.Constant( 'GL_MODELVIEW9_ARB', 0x8729 )
GL_MODELVIEW10_ARB = constant.Constant( 'GL_MODELVIEW10_ARB', 0x872A )
GL_MODELVIEW11_ARB = constant.Constant( 'GL_MODELVIEW11_ARB', 0x872B )
GL_MODELVIEW12_ARB = constant.Constant( 'GL_MODELVIEW12_ARB', 0x872C )
GL_MODELVIEW13_ARB = constant.Constant( 'GL_MODELVIEW13_ARB', 0x872D )
GL_MODELVIEW14_ARB = constant.Constant( 'GL_MODELVIEW14_ARB', 0x872E )
GL_MODELVIEW15_ARB = constant.Constant( 'GL_MODELVIEW15_ARB', 0x872F )
GL_MODELVIEW16_ARB = constant.Constant( 'GL_MODELVIEW16_ARB', 0x8730 )
GL_MODELVIEW17_ARB = constant.Constant( 'GL_MODELVIEW17_ARB', 0x8731 )
GL_MODELVIEW18_ARB = constant.Constant( 'GL_MODELVIEW18_ARB', 0x8732 )
GL_MODELVIEW19_ARB = constant.Constant( 'GL_MODELVIEW19_ARB', 0x8733 )
GL_MODELVIEW20_ARB = constant.Constant( 'GL_MODELVIEW20_ARB', 0x8734 )
GL_MODELVIEW21_ARB = constant.Constant( 'GL_MODELVIEW21_ARB', 0x8735 )
GL_MODELVIEW22_ARB = constant.Constant( 'GL_MODELVIEW22_ARB', 0x8736 )
GL_MODELVIEW23_ARB = constant.Constant( 'GL_MODELVIEW23_ARB', 0x8737 )
GL_MODELVIEW24_ARB = constant.Constant( 'GL_MODELVIEW24_ARB', 0x8738 )
GL_MODELVIEW25_ARB = constant.Constant( 'GL_MODELVIEW25_ARB', 0x8739 )
GL_MODELVIEW26_ARB = constant.Constant( 'GL_MODELVIEW26_ARB', 0x873A )
GL_MODELVIEW27_ARB = constant.Constant( 'GL_MODELVIEW27_ARB', 0x873B )
GL_MODELVIEW28_ARB = constant.Constant( 'GL_MODELVIEW28_ARB', 0x873C )
GL_MODELVIEW29_ARB = constant.Constant( 'GL_MODELVIEW29_ARB', 0x873D )
GL_MODELVIEW30_ARB = constant.Constant( 'GL_MODELVIEW30_ARB', 0x873E )
GL_MODELVIEW31_ARB = constant.Constant( 'GL_MODELVIEW31_ARB', 0x873F )
glWeightbvARB = platform.createExtensionFunction( 
	'glWeightbvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLbyteArray,),
	doc = 'glWeightbvARB( GLint(size), GLbyteArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightsvARB = platform.createExtensionFunction( 
	'glWeightsvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLshortArray,),
	doc = 'glWeightsvARB( GLint(size), GLshortArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightivARB = platform.createExtensionFunction( 
	'glWeightivARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLintArray,),
	doc = 'glWeightivARB( GLint(size), GLintArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightfvARB = platform.createExtensionFunction( 
	'glWeightfvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLfloatArray,),
	doc = 'glWeightfvARB( GLint(size), GLfloatArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightdvARB = platform.createExtensionFunction( 
	'glWeightdvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLdoubleArray,),
	doc = 'glWeightdvARB( GLint(size), GLdoubleArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightubvARB = platform.createExtensionFunction( 
	'glWeightubvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLubyteArray,),
	doc = 'glWeightubvARB( GLint(size), GLubyteArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightusvARB = platform.createExtensionFunction( 
	'glWeightusvARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLushortArray,),
	doc = 'glWeightusvARB( GLint(size), GLushortArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightuivARB = platform.createExtensionFunction( 
	'glWeightuivARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, arrays.GLuintArray,),
	doc = 'glWeightuivARB( GLint(size), GLuintArray(weights) ) -> None',
	argNames = ('size', 'weights',),
)

glWeightPointerARB = platform.createExtensionFunction( 
	'glWeightPointerARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLenum, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glWeightPointerARB( GLint(size), GLenum(type), GLsizei(stride), c_void_p(pointer) ) -> None',
	argNames = ('size', 'type', 'stride', 'pointer',),
)

glVertexBlendARB = platform.createExtensionFunction( 
	'glVertexBlendARB', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLint,),
	doc = 'glVertexBlendARB( GLint(count) ) -> None',
	argNames = ('count',),
)


def glInitVertexBlendARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_ARB_vertex_blend' )
