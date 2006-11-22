'''OpenGL extension ATI.vertex_streams

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.vertex_streams to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ATI.vertex_streams import *
### END AUTOGENERATED SECTION