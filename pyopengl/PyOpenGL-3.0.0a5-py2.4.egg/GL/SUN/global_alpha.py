'''OpenGL extension SUN.global_alpha

This module customises the behaviour of the 
OpenGL.raw.GL.SUN.global_alpha to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SUN.global_alpha import *
### END AUTOGENERATED SECTION