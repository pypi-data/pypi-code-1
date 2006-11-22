'''OpenGL extension EXT.texture_cube_map

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture_cube_map to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.texture_cube_map import *
### END AUTOGENERATED SECTION