'''OpenGL extension SGIX.texture_add_env

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_add_env.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
GL_TEXTURE_ENV_BIAS_SGIX = constant.Constant( 'GL_TEXTURE_ENV_BIAS_SGIX', 0x80BE )


def glInitTextureAddEnvSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( 'GL_SGIX_texture_add_env' )
