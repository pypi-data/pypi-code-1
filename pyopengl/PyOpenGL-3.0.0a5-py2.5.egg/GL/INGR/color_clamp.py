'''OpenGL extension INGR.color_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.INGR.color_clamp to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.INGR.color_clamp import *
### END AUTOGENERATED SECTION