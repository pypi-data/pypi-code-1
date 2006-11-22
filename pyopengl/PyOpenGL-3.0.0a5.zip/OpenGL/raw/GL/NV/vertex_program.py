'''OpenGL extension NV.vertex_program

Overview (from the spec)
	
	Unextended OpenGL mandates a certain set of configurable per-vertex
	computations defining vertex transformation, texture coordinate
	generation and transformation, and lighting.  Several extensions
	have added further per-vertex computations to OpenGL.  For example,
	extensions have defined new texture coordinate generation modes
	(ARB_texture_cube_map, NV_texgen_reflection, NV_texgen_emboss), new
	vertex transformation modes (EXT_vertex_weighting), new lighting modes
	(OpenGL 1.2's separate specular and rescale normal functionality),
	several modes for fog distance generation (NV_fog_distance), and
	eye-distance point size attenuation (EXT_point_parameters).
	
	Each such extension adds a small set of relatively inflexible
	per-vertex computations.
	
	This inflexibility is in contrast to the typical flexibility provided
	by the underlying programmable floating point engines (whether
	micro-coded vertex engines, DSPs, or CPUs) that are traditionally used
	to implement OpenGL's per-vertex computations.  The purpose of this
	extension is to expose to the OpenGL application writer a significant
	degree of per-vertex programmability for computing vertex parameters.
	
	For the purposes of discussing this extension, a vertex program is
	a sequence of floating-point 4-component vector operations that
	determines how a set of program parameters (defined outside of
	OpenGL's begin/end pair) and an input set of per-vertex parameters
	are transformed to a set of per-vertex output parameters.
	
	The per-vertex computations for standard OpenGL given a particular
	set of lighting and texture coordinate generation modes (along with
	any state for extensions defining per-vertex computations) is, in
	essence, a vertex program.  However, the sequence of operations is
	defined implicitly by the current OpenGL state settings rather than
	defined explicitly as a sequence of instructions.
	
	This extension provides an explicit mechanism for defining vertex
	program instruction sequences for application-defined vertex programs.
	In order to define such vertex programs, this extension defines
	a vertex programming model including a floating-point 4-component
	vector instruction set and a relatively large set of floating-point
	4-component registers.
	
	The extension's vertex programming model is designed for efficient
	hardware implementation and to support a wide variety of vertex
	programs.  By design, the entire set of existing vertex programs
	defined by existing OpenGL per-vertex computation extensions can be
	implemented using the extension's vertex programming model.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/vertex_program.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_VERTEX_PROGRAM_NV = constant.Constant( 'GL_VERTEX_PROGRAM_NV', 0x8620 )
glget.addGLGetConstant( GL_VERTEX_PROGRAM_NV, (1,) )
GL_VERTEX_STATE_PROGRAM_NV = constant.Constant( 'GL_VERTEX_STATE_PROGRAM_NV', 0x8621 )
GL_ATTRIB_ARRAY_SIZE_NV = constant.Constant( 'GL_ATTRIB_ARRAY_SIZE_NV', 0x8623 )
GL_ATTRIB_ARRAY_STRIDE_NV = constant.Constant( 'GL_ATTRIB_ARRAY_STRIDE_NV', 0x8624 )
GL_ATTRIB_ARRAY_TYPE_NV = constant.Constant( 'GL_ATTRIB_ARRAY_TYPE_NV', 0x8625 )
GL_CURRENT_ATTRIB_NV = constant.Constant( 'GL_CURRENT_ATTRIB_NV', 0x8626 )
GL_PROGRAM_LENGTH_NV = constant.Constant( 'GL_PROGRAM_LENGTH_NV', 0x8627 )
GL_PROGRAM_STRING_NV = constant.Constant( 'GL_PROGRAM_STRING_NV', 0x8628 )
GL_MODELVIEW_PROJECTION_NV = constant.Constant( 'GL_MODELVIEW_PROJECTION_NV', 0x8629 )
GL_IDENTITY_NV = constant.Constant( 'GL_IDENTITY_NV', 0x862A )
GL_INVERSE_NV = constant.Constant( 'GL_INVERSE_NV', 0x862B )
GL_TRANSPOSE_NV = constant.Constant( 'GL_TRANSPOSE_NV', 0x862C )
GL_INVERSE_TRANSPOSE_NV = constant.Constant( 'GL_INVERSE_TRANSPOSE_NV', 0x862D )
GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV = constant.Constant( 'GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV', 0x862E )
glget.addGLGetConstant( GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV, (1,) )
GL_MAX_TRACK_MATRICES_NV = constant.Constant( 'GL_MAX_TRACK_MATRICES_NV', 0x862F )
glget.addGLGetConstant( GL_MAX_TRACK_MATRICES_NV, (1,) )
GL_MATRIX0_NV = constant.Constant( 'GL_MATRIX0_NV', 0x8630 )
GL_MATRIX1_NV = constant.Constant( 'GL_MATRIX1_NV', 0x8631 )
GL_MATRIX2_NV = constant.Constant( 'GL_MATRIX2_NV', 0x8632 )
GL_MATRIX3_NV = constant.Constant( 'GL_MATRIX3_NV', 0x8633 )
GL_MATRIX4_NV = constant.Constant( 'GL_MATRIX4_NV', 0x8634 )
GL_MATRIX5_NV = constant.Constant( 'GL_MATRIX5_NV', 0x8635 )
GL_MATRIX6_NV = constant.Constant( 'GL_MATRIX6_NV', 0x8636 )
GL_MATRIX7_NV = constant.Constant( 'GL_MATRIX7_NV', 0x8637 )
GL_CURRENT_MATRIX_STACK_DEPTH_NV = constant.Constant( 'GL_CURRENT_MATRIX_STACK_DEPTH_NV', 0x8640 )
glget.addGLGetConstant( GL_CURRENT_MATRIX_STACK_DEPTH_NV, (1,) )
GL_CURRENT_MATRIX_NV = constant.Constant( 'GL_CURRENT_MATRIX_NV', 0x8641 )
glget.addGLGetConstant( GL_CURRENT_MATRIX_NV, (4,4) )
GL_VERTEX_PROGRAM_POINT_SIZE_NV = constant.Constant( 'GL_VERTEX_PROGRAM_POINT_SIZE_NV', 0x8642 )
glget.addGLGetConstant( GL_VERTEX_PROGRAM_POINT_SIZE_NV, (1,) )
GL_VERTEX_PROGRAM_TWO_SIDE_NV = constant.Constant( 'GL_VERTEX_PROGRAM_TWO_SIDE_NV', 0x8643 )
glget.addGLGetConstant( GL_VERTEX_PROGRAM_TWO_SIDE_NV, (1,) )
GL_PROGRAM_PARAMETER_NV = constant.Constant( 'GL_PROGRAM_PARAMETER_NV', 0x8644 )
GL_ATTRIB_ARRAY_POINTER_NV = constant.Constant( 'GL_ATTRIB_ARRAY_POINTER_NV', 0x8645 )
GL_PROGRAM_TARGET_NV = constant.Constant( 'GL_PROGRAM_TARGET_NV', 0x8646 )
GL_PROGRAM_RESIDENT_NV = constant.Constant( 'GL_PROGRAM_RESIDENT_NV', 0x8647 )
GL_TRACK_MATRIX_NV = constant.Constant( 'GL_TRACK_MATRIX_NV', 0x8648 )
GL_TRACK_MATRIX_TRANSFORM_NV = constant.Constant( 'GL_TRACK_MATRIX_TRANSFORM_NV', 0x8649 )
GL_VERTEX_PROGRAM_BINDING_NV = constant.Constant( 'GL_VERTEX_PROGRAM_BINDING_NV', 0x864A )
glget.addGLGetConstant( GL_VERTEX_PROGRAM_BINDING_NV, (1,) )
GL_PROGRAM_ERROR_POSITION_NV = constant.Constant( 'GL_PROGRAM_ERROR_POSITION_NV', 0x864B )
glget.addGLGetConstant( GL_PROGRAM_ERROR_POSITION_NV, (1,) )
GL_VERTEX_ATTRIB_ARRAY0_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY0_NV', 0x8650 )
GL_VERTEX_ATTRIB_ARRAY1_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY1_NV', 0x8651 )
GL_VERTEX_ATTRIB_ARRAY2_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY2_NV', 0x8652 )
GL_VERTEX_ATTRIB_ARRAY3_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY3_NV', 0x8653 )
GL_VERTEX_ATTRIB_ARRAY4_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY4_NV', 0x8654 )
GL_VERTEX_ATTRIB_ARRAY5_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY5_NV', 0x8655 )
GL_VERTEX_ATTRIB_ARRAY6_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY6_NV', 0x8656 )
GL_VERTEX_ATTRIB_ARRAY7_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY7_NV', 0x8657 )
GL_VERTEX_ATTRIB_ARRAY8_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY8_NV', 0x8658 )
GL_VERTEX_ATTRIB_ARRAY9_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY9_NV', 0x8659 )
GL_VERTEX_ATTRIB_ARRAY10_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY10_NV', 0x865A )
GL_VERTEX_ATTRIB_ARRAY11_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY11_NV', 0x865B )
GL_VERTEX_ATTRIB_ARRAY12_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY12_NV', 0x865C )
GL_VERTEX_ATTRIB_ARRAY13_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY13_NV', 0x865D )
GL_VERTEX_ATTRIB_ARRAY14_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY14_NV', 0x865E )
GL_VERTEX_ATTRIB_ARRAY15_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY15_NV', 0x865F )
GL_MAP1_VERTEX_ATTRIB0_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB0_4_NV', 0x8660 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB0_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB1_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB1_4_NV', 0x8661 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB1_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB2_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB2_4_NV', 0x8662 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB2_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB3_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB3_4_NV', 0x8663 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB3_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB4_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB4_4_NV', 0x8664 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB4_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB5_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB5_4_NV', 0x8665 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB5_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB6_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB6_4_NV', 0x8666 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB6_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB7_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB7_4_NV', 0x8667 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB7_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB8_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB8_4_NV', 0x8668 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB8_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB9_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB9_4_NV', 0x8669 )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB9_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB10_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB10_4_NV', 0x866A )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB10_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB11_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB11_4_NV', 0x866B )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB11_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB12_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB12_4_NV', 0x866C )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB12_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB13_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB13_4_NV', 0x866D )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB13_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB14_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB14_4_NV', 0x866E )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB14_4_NV, (4,) )
GL_MAP1_VERTEX_ATTRIB15_4_NV = constant.Constant( 'GL_MAP1_VERTEX_ATTRIB15_4_NV', 0x866F )
glget.addGLGetConstant( GL_MAP1_VERTEX_ATTRIB15_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB0_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB0_4_NV', 0x8670 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB0_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB1_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB1_4_NV', 0x8671 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB1_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB2_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB2_4_NV', 0x8672 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB2_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB3_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB3_4_NV', 0x8673 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB3_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB4_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB4_4_NV', 0x8674 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB4_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB5_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB5_4_NV', 0x8675 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB5_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB6_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB6_4_NV', 0x8676 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB6_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB7_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB7_4_NV', 0x8677 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB7_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB8_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB8_4_NV', 0x8678 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB8_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB9_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB9_4_NV', 0x8679 )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB9_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB10_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB10_4_NV', 0x867A )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB10_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB11_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB11_4_NV', 0x867B )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB11_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB12_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB12_4_NV', 0x867C )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB12_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB13_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB13_4_NV', 0x867D )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB13_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB14_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB14_4_NV', 0x867E )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB14_4_NV, (4,) )
GL_MAP2_VERTEX_ATTRIB15_4_NV = constant.Constant( 'GL_MAP2_VERTEX_ATTRIB15_4_NV', 0x867F )
glget.addGLGetConstant( GL_MAP2_VERTEX_ATTRIB15_4_NV, (4,) )
glAreProgramsResidentNV = platform.createExtensionFunction( 
	'glAreProgramsResidentNV', dll=platform.GL,
	resultType=constants.GLboolean, 
	argTypes=(constants.GLsizei, arrays.GLuintArray, ctypes.POINTER(constants.GLboolean),),
	doc = 'glAreProgramsResidentNV( GLsizei(n), GLuintArray(programs), POINTER(constants.GLboolean)(residences) ) -> constants.GLboolean',
	argNames = ('n', 'programs', 'residences',),
)

glBindProgramNV = platform.createExtensionFunction( 
	'glBindProgramNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint,),
	doc = 'glBindProgramNV( GLenum(target), GLuint(id) ) -> None',
	argNames = ('target', 'id',),
)

glDeleteProgramsNV = platform.createExtensionFunction( 
	'glDeleteProgramsNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glDeleteProgramsNV( GLsizei(n), GLuintArray(programs) ) -> None',
	argNames = ('n', 'programs',),
)

glExecuteProgramNV = platform.createExtensionFunction( 
	'glExecuteProgramNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, arrays.GLfloatArray,),
	doc = 'glExecuteProgramNV( GLenum(target), GLuint(id), GLfloatArray(params) ) -> None',
	argNames = ('target', 'id', 'params',),
)

glGenProgramsNV = platform.createExtensionFunction( 
	'glGenProgramsNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glGenProgramsNV( GLsizei(n), GLuintArray(programs) ) -> None',
	argNames = ('n', 'programs',),
)

glGetProgramParameterdvNV = platform.createExtensionFunction( 
	'glGetProgramParameterdvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glGetProgramParameterdvNV( GLenum(target), GLuint(index), GLenum(pname), GLdoubleArray(params) ) -> None',
	argNames = ('target', 'index', 'pname', 'params',),
)

glGetProgramParameterfvNV = platform.createExtensionFunction( 
	'glGetProgramParameterfvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetProgramParameterfvNV( GLenum(target), GLuint(index), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('target', 'index', 'pname', 'params',),
)

glGetProgramivNV = platform.createExtensionFunction( 
	'glGetProgramivNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetProgramivNV( GLuint(id), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('id', 'pname', 'params',),
)

glGetProgramStringNV = platform.createExtensionFunction( 
	'glGetProgramStringNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLubyteArray,),
	doc = 'glGetProgramStringNV( GLuint(id), GLenum(pname), GLubyteArray(program) ) -> None',
	argNames = ('id', 'pname', 'program',),
)

glGetTrackMatrixivNV = platform.createExtensionFunction( 
	'glGetTrackMatrixivNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetTrackMatrixivNV( GLenum(target), GLuint(address), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('target', 'address', 'pname', 'params',),
)

glGetVertexAttribdvNV = platform.createExtensionFunction( 
	'glGetVertexAttribdvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLdoubleArray,),
	doc = 'glGetVertexAttribdvNV( GLuint(index), GLenum(pname), GLdoubleArray(params) ) -> None',
	argNames = ('index', 'pname', 'params',),
)

glGetVertexAttribfvNV = platform.createExtensionFunction( 
	'glGetVertexAttribfvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetVertexAttribfvNV( GLuint(index), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('index', 'pname', 'params',),
)

glGetVertexAttribivNV = platform.createExtensionFunction( 
	'glGetVertexAttribivNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetVertexAttribivNV( GLuint(index), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('index', 'pname', 'params',),
)

glGetVertexAttribPointervNV = platform.createExtensionFunction( 
	'glGetVertexAttribPointervNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, ctypes.POINTER(ctypes.c_void_p),),
	doc = 'glGetVertexAttribPointervNV( GLuint(index), GLenum(pname), POINTER(ctypes.c_void_p)(pointer) ) -> None',
	argNames = ('index', 'pname', 'pointer',),
)

glIsProgramNV = platform.createExtensionFunction( 
	'glIsProgramNV', dll=platform.GL,
	resultType=constants.GLboolean, 
	argTypes=(constants.GLuint,),
	doc = 'glIsProgramNV( GLuint(id) ) -> constants.GLboolean',
	argNames = ('id',),
)

glLoadProgramNV = platform.createExtensionFunction( 
	'glLoadProgramNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLsizei, arrays.GLubyteArray,),
	doc = 'glLoadProgramNV( GLenum(target), GLuint(id), GLsizei(len), GLubyteArray(program) ) -> None',
	argNames = ('target', 'id', 'len', 'program',),
)

glProgramParameter4dNV = platform.createExtensionFunction( 
	'glProgramParameter4dNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLdouble, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glProgramParameter4dNV( GLenum(target), GLuint(index), GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w) ) -> None',
	argNames = ('target', 'index', 'x', 'y', 'z', 'w',),
)

glProgramParameter4dvNV = platform.createExtensionFunction( 
	'glProgramParameter4dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, arrays.GLdoubleArray,),
	doc = 'glProgramParameter4dvNV( GLenum(target), GLuint(index), GLdoubleArray(v) ) -> None',
	argNames = ('target', 'index', 'v',),
)

glProgramParameter4fNV = platform.createExtensionFunction( 
	'glProgramParameter4fNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLfloat, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glProgramParameter4fNV( GLenum(target), GLuint(index), GLfloat(x), GLfloat(y), GLfloat(z), GLfloat(w) ) -> None',
	argNames = ('target', 'index', 'x', 'y', 'z', 'w',),
)

glProgramParameter4fvNV = platform.createExtensionFunction( 
	'glProgramParameter4fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, arrays.GLfloatArray,),
	doc = 'glProgramParameter4fvNV( GLenum(target), GLuint(index), GLfloatArray(v) ) -> None',
	argNames = ('target', 'index', 'v',),
)

glProgramParameters4dvNV = platform.createExtensionFunction( 
	'glProgramParameters4dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLuint, arrays.GLdoubleArray,),
	doc = 'glProgramParameters4dvNV( GLenum(target), GLuint(index), GLuint(count), GLdoubleArray(v) ) -> None',
	argNames = ('target', 'index', 'count', 'v',),
)

glProgramParameters4fvNV = platform.createExtensionFunction( 
	'glProgramParameters4fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLuint, arrays.GLfloatArray,),
	doc = 'glProgramParameters4fvNV( GLenum(target), GLuint(index), GLuint(count), GLfloatArray(v) ) -> None',
	argNames = ('target', 'index', 'count', 'v',),
)

glRequestResidentProgramsNV = platform.createExtensionFunction( 
	'glRequestResidentProgramsNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glRequestResidentProgramsNV( GLsizei(n), GLuintArray(programs) ) -> None',
	argNames = ('n', 'programs',),
)

glTrackMatrixNV = platform.createExtensionFunction( 
	'glTrackMatrixNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint, constants.GLenum, constants.GLenum,),
	doc = 'glTrackMatrixNV( GLenum(target), GLuint(address), GLenum(matrix), GLenum(transform) ) -> None',
	argNames = ('target', 'address', 'matrix', 'transform',),
)

glVertexAttribPointerNV = platform.createExtensionFunction( 
	'glVertexAttribPointerNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLint, constants.GLenum, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glVertexAttribPointerNV( GLuint(index), GLint(fsize), GLenum(type), GLsizei(stride), c_void_p(pointer) ) -> None',
	argNames = ('index', 'fsize', 'type', 'stride', 'pointer',),
)

glVertexAttrib1dNV = platform.createExtensionFunction( 
	'glVertexAttrib1dNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLdouble,),
	doc = 'glVertexAttrib1dNV( GLuint(index), GLdouble(x) ) -> None',
	argNames = ('index', 'x',),
)

glVertexAttrib1dvNV = platform.createExtensionFunction( 
	'glVertexAttrib1dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLdoubleArray,),
	doc = 'glVertexAttrib1dvNV( GLuint(index), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib1fNV = platform.createExtensionFunction( 
	'glVertexAttrib1fNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLfloat,),
	doc = 'glVertexAttrib1fNV( GLuint(index), GLfloat(x) ) -> None',
	argNames = ('index', 'x',),
)

glVertexAttrib1fvNV = platform.createExtensionFunction( 
	'glVertexAttrib1fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLfloatArray,),
	doc = 'glVertexAttrib1fvNV( GLuint(index), GLfloatArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib1sNV = platform.createExtensionFunction( 
	'glVertexAttrib1sNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLshort,),
	doc = 'glVertexAttrib1sNV( GLuint(index), GLshort(x) ) -> None',
	argNames = ('index', 'x',),
)

glVertexAttrib1svNV = platform.createExtensionFunction( 
	'glVertexAttrib1svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLshortArray,),
	doc = 'glVertexAttrib1svNV( GLuint(index), GLshortArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib2dNV = platform.createExtensionFunction( 
	'glVertexAttrib2dNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLdouble, constants.GLdouble,),
	doc = 'glVertexAttrib2dNV( GLuint(index), GLdouble(x), GLdouble(y) ) -> None',
	argNames = ('index', 'x', 'y',),
)

glVertexAttrib2dvNV = platform.createExtensionFunction( 
	'glVertexAttrib2dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLdoubleArray,),
	doc = 'glVertexAttrib2dvNV( GLuint(index), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib2fNV = platform.createExtensionFunction( 
	'glVertexAttrib2fNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLfloat, constants.GLfloat,),
	doc = 'glVertexAttrib2fNV( GLuint(index), GLfloat(x), GLfloat(y) ) -> None',
	argNames = ('index', 'x', 'y',),
)

glVertexAttrib2fvNV = platform.createExtensionFunction( 
	'glVertexAttrib2fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLfloatArray,),
	doc = 'glVertexAttrib2fvNV( GLuint(index), GLfloatArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib2sNV = platform.createExtensionFunction( 
	'glVertexAttrib2sNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLshort, constants.GLshort,),
	doc = 'glVertexAttrib2sNV( GLuint(index), GLshort(x), GLshort(y) ) -> None',
	argNames = ('index', 'x', 'y',),
)

glVertexAttrib2svNV = platform.createExtensionFunction( 
	'glVertexAttrib2svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLshortArray,),
	doc = 'glVertexAttrib2svNV( GLuint(index), GLshortArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib3dNV = platform.createExtensionFunction( 
	'glVertexAttrib3dNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glVertexAttrib3dNV( GLuint(index), GLdouble(x), GLdouble(y), GLdouble(z) ) -> None',
	argNames = ('index', 'x', 'y', 'z',),
)

glVertexAttrib3dvNV = platform.createExtensionFunction( 
	'glVertexAttrib3dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLdoubleArray,),
	doc = 'glVertexAttrib3dvNV( GLuint(index), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib3fNV = platform.createExtensionFunction( 
	'glVertexAttrib3fNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glVertexAttrib3fNV( GLuint(index), GLfloat(x), GLfloat(y), GLfloat(z) ) -> None',
	argNames = ('index', 'x', 'y', 'z',),
)

glVertexAttrib3fvNV = platform.createExtensionFunction( 
	'glVertexAttrib3fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLfloatArray,),
	doc = 'glVertexAttrib3fvNV( GLuint(index), GLfloatArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib3sNV = platform.createExtensionFunction( 
	'glVertexAttrib3sNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glVertexAttrib3sNV( GLuint(index), GLshort(x), GLshort(y), GLshort(z) ) -> None',
	argNames = ('index', 'x', 'y', 'z',),
)

glVertexAttrib3svNV = platform.createExtensionFunction( 
	'glVertexAttrib3svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLshortArray,),
	doc = 'glVertexAttrib3svNV( GLuint(index), GLshortArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib4dNV = platform.createExtensionFunction( 
	'glVertexAttrib4dNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLdouble, constants.GLdouble, constants.GLdouble, constants.GLdouble,),
	doc = 'glVertexAttrib4dNV( GLuint(index), GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w) ) -> None',
	argNames = ('index', 'x', 'y', 'z', 'w',),
)

glVertexAttrib4dvNV = platform.createExtensionFunction( 
	'glVertexAttrib4dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLdoubleArray,),
	doc = 'glVertexAttrib4dvNV( GLuint(index), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib4fNV = platform.createExtensionFunction( 
	'glVertexAttrib4fNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLfloat, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glVertexAttrib4fNV( GLuint(index), GLfloat(x), GLfloat(y), GLfloat(z), GLfloat(w) ) -> None',
	argNames = ('index', 'x', 'y', 'z', 'w',),
)

glVertexAttrib4fvNV = platform.createExtensionFunction( 
	'glVertexAttrib4fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLfloatArray,),
	doc = 'glVertexAttrib4fvNV( GLuint(index), GLfloatArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib4sNV = platform.createExtensionFunction( 
	'glVertexAttrib4sNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLshort, constants.GLshort, constants.GLshort, constants.GLshort,),
	doc = 'glVertexAttrib4sNV( GLuint(index), GLshort(x), GLshort(y), GLshort(z), GLshort(w) ) -> None',
	argNames = ('index', 'x', 'y', 'z', 'w',),
)

glVertexAttrib4svNV = platform.createExtensionFunction( 
	'glVertexAttrib4svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLshortArray,),
	doc = 'glVertexAttrib4svNV( GLuint(index), GLshortArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttrib4ubNV = platform.createExtensionFunction( 
	'glVertexAttrib4ubNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLubyte, constants.GLubyte, constants.GLubyte, constants.GLubyte,),
	doc = 'glVertexAttrib4ubNV( GLuint(index), GLubyte(x), GLubyte(y), GLubyte(z), GLubyte(w) ) -> None',
	argNames = ('index', 'x', 'y', 'z', 'w',),
)

glVertexAttrib4ubvNV = platform.createExtensionFunction( 
	'glVertexAttrib4ubvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, arrays.GLubyteArray,),
	doc = 'glVertexAttrib4ubvNV( GLuint(index), GLubyteArray(v) ) -> None',
	argNames = ('index', 'v',),
)

glVertexAttribs1dvNV = platform.createExtensionFunction( 
	'glVertexAttribs1dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLdoubleArray,),
	doc = 'glVertexAttribs1dvNV( GLuint(index), GLsizei(count), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs1fvNV = platform.createExtensionFunction( 
	'glVertexAttribs1fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glVertexAttribs1fvNV( GLuint(index), GLsizei(count), GLfloatArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs1svNV = platform.createExtensionFunction( 
	'glVertexAttribs1svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLshortArray,),
	doc = 'glVertexAttribs1svNV( GLuint(index), GLsizei(count), GLshortArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs2dvNV = platform.createExtensionFunction( 
	'glVertexAttribs2dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLdoubleArray,),
	doc = 'glVertexAttribs2dvNV( GLuint(index), GLsizei(count), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs2fvNV = platform.createExtensionFunction( 
	'glVertexAttribs2fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glVertexAttribs2fvNV( GLuint(index), GLsizei(count), GLfloatArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs2svNV = platform.createExtensionFunction( 
	'glVertexAttribs2svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLshortArray,),
	doc = 'glVertexAttribs2svNV( GLuint(index), GLsizei(count), GLshortArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs3dvNV = platform.createExtensionFunction( 
	'glVertexAttribs3dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLdoubleArray,),
	doc = 'glVertexAttribs3dvNV( GLuint(index), GLsizei(count), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs3fvNV = platform.createExtensionFunction( 
	'glVertexAttribs3fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glVertexAttribs3fvNV( GLuint(index), GLsizei(count), GLfloatArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs3svNV = platform.createExtensionFunction( 
	'glVertexAttribs3svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLshortArray,),
	doc = 'glVertexAttribs3svNV( GLuint(index), GLsizei(count), GLshortArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs4dvNV = platform.createExtensionFunction( 
	'glVertexAttribs4dvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLdoubleArray,),
	doc = 'glVertexAttribs4dvNV( GLuint(index), GLsizei(count), GLdoubleArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs4fvNV = platform.createExtensionFunction( 
	'glVertexAttribs4fvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glVertexAttribs4fvNV( GLuint(index), GLsizei(count), GLfloatArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs4svNV = platform.createExtensionFunction( 
	'glVertexAttribs4svNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLshortArray,),
	doc = 'glVertexAttribs4svNV( GLuint(index), GLsizei(count), GLshortArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)

glVertexAttribs4ubvNV = platform.createExtensionFunction( 
	'glVertexAttribs4ubvNV', dll=platform.GL,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLsizei, arrays.GLubyteArray,),
	doc = 'glVertexAttribs4ubvNV( GLuint(index), GLsizei(count), GLubyteArray(v) ) -> None',
	argNames = ('index', 'count', 'v',),
)


def glInitVertexProgramNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_NV_vertex_program' )
