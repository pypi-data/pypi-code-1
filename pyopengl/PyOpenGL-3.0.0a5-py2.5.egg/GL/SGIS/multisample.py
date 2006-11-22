'''OpenGL extension SGIS.multisample

This module customises the behaviour of the 
OpenGL.raw.GL.SGIS.multisample to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIS.multisample import *
### END AUTOGENERATED SECTION