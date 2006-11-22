'''OpenGL extension EXT.shared_texture_palette

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.shared_texture_palette to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.shared_texture_palette import *
### END AUTOGENERATED SECTION