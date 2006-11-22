'''OpenGL extension SGIX.vertex_preclip

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.vertex_preclip to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIX.vertex_preclip import *
### END AUTOGENERATED SECTION