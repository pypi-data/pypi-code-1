'''OpenGL extension HP.occlusion_test

This module customises the behaviour of the 
OpenGL.raw.GL.HP.occlusion_test to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.HP.occlusion_test import *
### END AUTOGENERATED SECTION