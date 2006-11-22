'''OpenGL extension ARB.transpose_matrix

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.transpose_matrix to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.transpose_matrix import *
### END AUTOGENERATED SECTION
for typ,arrayType in (
	('d',arrays.GLdoubleArray),
	('f',arrays.GLfloatArray),
):
	for function in ('glLoadTransposeMatrix','glMultTransposeMatrix'):
		name = '%s%sARB'%(function,typ)
		globals()[name] = arrays.setInputArraySizeType(
			globals()[name],
			16,
			arrayType, 
			'm',
		)
		del function,name
	del typ,arrayType
