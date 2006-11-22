"""The wrapping code for providing natural ctypes-based OpenGL interface"""
import ctypes
from OpenGL import platform, error
glGetError = platform.OpenGL.glGetError
from OpenGL import converters
from OpenGL.converters import DefaultCConverter
from OpenGL.converters import returnCArgument,returnPyArgument
NULL = object()

def asList( o ):
	"""Convert to a list if not already one"""
	if not isinstance( o, list ):
		return list(o)
	return o

class Wrapper( object ):
	"""Wrapper around a ctypes cFunction object providing SWIG-like hooks
	
	Attributes:
	
		wrappedOperation -- base operation, normally a ctypes function 
			with data-types and error-checking specified
		pyConverters -- converters for incoming Python arguments,
			provide 1:1 mapping to incoming Python arguments, can
			suppress an argument from the argument-set as well
				see setPyConverter
		pyConverterNames -- caching/storage of the argument names 
			for the Python converters 
		cConverters -- converters for incoming C-level arguments
			produce Python-level objects in 1:1 mapping to ctypes
			arguments from pyConverters results
				see setCConverter
		cResolvers -- converters turning Python-level objects into 
			ctypes-compatible data-types 
				see setCResolver
	
	Generic Attributes:
	
		{ARG1}_LOOKUP_{ARG2} -- lookup dictionaries to provide sizes for 
			ARG1 output value from the value of ARG2, provided for 
			documentation/reference
		{ARG1}_FROM_{ARG2} -- lookup functions to provide sizes for ARG1
			output value from the value of ARG2, provided for 
			documentation/reference
	"""
	localProperties = (
		'wrappedOperation', 
		'__file__',
		'pyConverters',
		'pyConverterNames',
		'cConverters',
		'cResolvers',
		'storeValues',
		'returnValues',
	)
	def __init__( self, wrappedOperation ):
		"""Initialise the wrapper, storing wrappedOperation"""
		if isinstance( wrappedOperation, Wrapper ):
			wrappedOperation = wrappedOperation.wrappedOperation
		self.wrappedOperation = wrappedOperation
	def __getattr__( self, key ):
		"""Delegate attribute lookup to our wrappedOperation"""
		if key != 'wrappedOperation':
			return getattr( self.wrappedOperation, key )
		raise AttributeError( key )
	def __nonzero__( self ):
		"""Is this function/wrapper available?"""
		return bool( self.wrappedOperation )
	def __setattr__( self, key, value ):
		"""Forward attribute setting to our wrappedOperation"""
		if key in self.localProperties:
			super( Wrapper, self ).__setattr__( key, value )
		else:
			return setattr( self.wrappedOperation, key, value )
	def pyArgIndex( self, argName ):
		"""Return the Python-argument index for the given argument name"""
		argNames = getattr( self, 'pyConverterNames', None )
		if argNames is None:
			argNames = self.wrappedOperation.argNames
		try:
			return asList( argNames ).index( argName )
		except (ValueError,IndexError), err:
			raise KeyError( """No argument %r in argument list %r"""%(
				argName, argNames
			))
	def cArgIndex( self, argName ):
		"""Return the C-argument index for the given argument name"""
		argNames = self.wrappedOperation.argNames
		try:
			return asList( argNames ).index( argName )
		except (ValueError,IndexError), err:
			raise KeyError( """No argument %r in argument list %r"""%(
				argName, argNames
			))
	def setOutput( 
		self, outArg, size=(1,), pnameArg=None, 
		arrayType=None, oldStyleReturn=True,
	):
		"""Set the given argName to be an output array
		
		size -- either a tuple compatible with arrayType.zeros or 
			a function taking pname to produce such a value.
		arrayType -- array data-type used to generate the output 
			array using the zeros class method...
		pname -- optional argument passed into size function
		"""
		if arrayType is None:
			# figure out from self.wrappedOperation's argtypes
			index = self.cArgIndex( outArg )
			arrayType = self.wrappedOperation.argtypes[ index ]
		if pnameArg is None:
			assert not callable( size )
			conv = converters.Output(
				name=outArg,
				size=size,
				arrayType=arrayType,
			)
		else:
			if isinstance( size, dict ):
				setattr( self, '%s_LOOKUP_%s'%(outArg,pnameArg), size )
				size = size.__getitem__
			else:
				setattr( self, '%s_FROM_%s'%(outArg,pnameArg), size )
			assert callable( size )
			conv = converters.SizedOutput(
				name=outArg,
				specifier=pnameArg,
				lookup=size,
				arrayType=arrayType,
			)
		if oldStyleReturn:
			returnObject = conv.oldStyleReturn
		else:
			returnObject = converters.returnCArgument( outArg )
		return self.setPyConverter(
			outArg
		).setCConverter(
			outArg, conv,
		).setReturnValues(
			returnObject
		)
	def setPyConverter( self, argName, function = NULL ):
		"""Set Python-argument converter for given argument
		
		argName -- the argument name which will be coerced to a usable internal
			format using the function provided.
		function -- None (indicating a simple copy), NULL (default) to eliminate
			the argument from the Python argument-list, or a callable object with 
			the signature:
			
				converter(arg, wrappedOperation, args)
			
			where arg is the particular argument on which the convert is working,
			wrappedOperation is the underlying wrapper, and args is the set of 
			original Python arguments to the function.
		
		Note that you need exactly the same number of pyConverters as Python 
		arguments.
		"""
		if not hasattr( self, 'pyConverters' ):
			self.pyConverters = [None]*len( self.wrappedOperation.argNames )
			self.pyConverterNames = list(self.wrappedOperation.argNames)
		try:
			i = asList( self.pyConverterNames ).index( argName )
		except ValueError:
			raise AttributeError( """No argument named %r left in pyConverters for %r: %s"""%(
				argName, self.wrappedOperation.__name__, self.pyConverterNames,
			))
		if function is NULL:
			del self.pyConverters[i]
			del self.pyConverterNames[i]
		else:
			self.pyConverters[i] = function 
		return self
	def setCConverter( self, argName, function ):
		"""Set C-argument converter for a given argument
		
		argName -- the argument name whose C-compatible representation will 
			be calculated with the passed function.
		function -- None (indicating a simple copy), a non-callable object to
			be copied into the result-list itself, or a callable object with 
			the signature:
			
				converter( pyArgs, index, wrappedOperation )
			
			where pyArgs is the set of passed Python arguments, with the 
			pyConverters already applied, index is the index of the C argument 
			and wrappedOperation is the underlying function.
		
		C-argument converters are your chance to expand/contract a Python 
		argument list (pyArgs) to match the number of arguments expected by
		the ctypes baseOperation.  You can't have a "null" C-argument converter,
		as *something* has to be passed to the C-level function in the 
		parameter.
		"""
		if not hasattr( self, 'cConverters' ):
			self.cConverters = [None]*len( self.wrappedOperation.argNames )
		try:
			if not isinstance(self.wrappedOperation.argNames, list):
				self.wrappedOperation.argNames = list( self.wrappedOperation.argNames )
			i = asList( self.wrappedOperation.argNames ).index( argName )
		except ValueError:
			raise AttributeError( """No argument named %r left in cConverters: %s"""%(
				argName, self.wrappedOperation.argNames,
			))
		self.cConverters[i] = function 
		return self
	def setCResolver( self, argName, function=NULL ):
		"""Set C-argument converter for a given argument"""
		if not hasattr( self, 'cResolvers' ):
			self.cResolvers = [None]*len( self.wrappedOperation.argNames )
		try:
			if not isinstance(self.wrappedOperation.argNames, list):
				self.wrappedOperation.argNames = list( self.wrappedOperation.argNames )
			i = asList( self.wrappedOperation.argNames).index( argName )
		except ValueError:
			raise AttributeError( """No argument named %r left in cConverters: %s"""%(
				argName, self.wrappedOperation.argNames,
			))
		if function is NULL:
			del self.cResolvers[i]
		else:
			self.cResolvers[i] = function 
		return self
	def setStoreValues( self, function=NULL ):
		"""Set the storage-of-arguments function for the whole wrapper"""
		if function is NULL:
			try:
				del self.storeValues
			except Exception, err:
				pass
		else:
			self.storeValues = function
		return self
	def setReturnValues( self, function=NULL ):
		"""Set the return-of-results function for the whole wrapper"""
		if function is NULL:
			try:
				del self.returnValues
			except Exception, err:
				pass
		else:
			self.returnValues = function
		return self
	def finalise( self ):
		"""Finalise our various elements into simple index-based operations"""
		for attribute in ('pyConverters','cConverters','cResolvers' ):
			value = getattr( self, attribute, None )
			if value is not None:
				for i,item in enumerate(value):
					if hasattr( item, 'finalise' ):
						try:
							item.finalise( self )
						except Exception, err:
							raise error.Error(
								"""Error finalising item %s in %s for %s (%r): %s"""%(
									i,attribute,self,item,err,
								)
							)
		if hasattr( self, 'cConverters' ):
			for i,converter in enumerate( self.cConverters ):
				if isinstance( converter, (type(None),DefaultCConverter )):
					self.cConverters[i] = DefaultCConverter( self.pyArgIndex( self.argNames[i]) )
		for attribute in ('storeValues','returnValues',):
			item = getattr( self, attribute, None )
			if hasattr( item, 'finalise' ):
				item.finalise( self )
		callFunction = self.finaliseCall()
		if not callFunction:
			raise RuntimeError( """Missing finalised call type for %s"""%( self, ))
		else:
			self.__class__.__call__ = callFunction
		return self
	def finaliseCall( self ):
		"""Produce specialised versions of call for finalised wrapper object
		
		This returns a version of __call__ that only does that work which is
		required by the particular wrapper object
		
		This is essentially a huge set of expanded nested functions, very 
		inelegant...
		"""
		pyConverters = getattr( self, 'pyConverters', None )
		cConverters = getattr( self, 'cConverters', None )
		cResolvers = getattr( self, 'cResolvers', None )
		wrappedOperation = self.wrappedOperation
		storeValues = getattr( self, 'storeValues', None )
		returnValues = getattr( self, 'returnValues', None )
		if pyConverters:
			if cConverters:
				if cResolvers:
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return result 
							return wrapperCall
				else:
					# null cResolvers
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return result 
							return wrapperCall
			else:
				# null cConverters
				if cResolvers:
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = pyArgs
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = pyArgs
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = pyArgs
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArgs = pyArgs
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return result 
							return wrapperCall
				else:
					# null cResolvers
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArguments = pyArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArguments = pyArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArguments = pyArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								if len(pyConverters) != len(args):
									raise ValueError(
										"""%s requires %r arguments (%s), received %s: %r"""%(
											wrappedOperation.__name__,
											len(pyConverters),
											", ".join( self.pyConverterNames ),
											len(args),
											args
										)
									)
								pyArgs = []
								for (converter,arg) in zip(pyConverters,args):
									if converter is None:
										pyArgs.append( arg )
									else:
										pyArgs.append( converter(arg, self, args) )
								cArguments = pyArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return result 
							return wrapperCall
		else:
			# null pyConverters
			if cConverters:
				if cResolvers:
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return result 
							return wrapperCall
				else:
					# null cResolvers
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return returnValues(
									result,
									self,
									pyArgs,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								pyArgs = args 
								cArgs = []
								for (index,converter) in enumerate( cConverters ):
									# move enumerate out...
									if not callable(converter):
										cArgs.append( converter )
									else:
										try:
											cArgs.append(
												converter( pyArgs, index, self )
											)
										except Exception, err:
											if hasattr( err, 'args' ):
												err.args += (
													"""Failure in cConverter %r"""%(converter),
													pyArgs, index, self,
												)
											raise
								cArguments = cArgs
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = pyArgs
									raise err
								return result 
							return wrapperCall
			else:
				# null cConverters
				if cResolvers:
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								cArgs = args
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									args,
									cArgs,
								)
								return returnValues(
									result,
									self,
									args,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								cArgs = args
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									args,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								cArgs = args
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								return returnValues(
									result,
									self,
									args,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								cArgs = args
								cArguments = []
								for (converter, value) in zip( cResolvers, cArgs ):
									if converter is None:
										cArguments.append( value )
									else:
										cArguments.append( converter( value ) )
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								return result 
							return wrapperCall
				else:
					# null cResolvers
					if storeValues:
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all possible operations"""
								cArguments = args
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									args,
									cArgs,
								)
								return returnValues(
									result,
									self,
									args,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues"""
								cArguments = args
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								# handle storage of persistent argument values...
								storeValues(
									result,
									self,
									args,
									cArgs,
								)
								return result 
							return wrapperCall
					else: # null storeValues
						if returnValues:
							def wrapperCall( self, *args ):
								"""Wrapper with all save storeValues"""
								cArguments = args
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								return returnValues(
									result,
									self,
									args,
									cArgs,
								)
							return wrapperCall
						else:
							def wrapperCall( self, *args ):
								"""Wrapper with all save returnValues and storeValues"""
								cArguments = args
								try:
									result = self.wrappedOperation( *cArguments )
								except ctypes.ArgumentError, err:
									err.args = err.args + (cArguments,)
									raise err
								except error.GLError, err:
									err.cArgs = cArgs 
									err.pyArgs = args
									raise err
								return result 
							return wrapperCall
	def __call__( self, *args, **named ):
		"""Finalise the wrapper before calling it"""
		return self.finalise()( *args, **named )

	def _unspecialised__call__( self, *args ):
		"""Expand arguments, call the function, store values and check errors"""
		pyConverters = getattr( self, 'pyConverters', None )
		if pyConverters:
			if len(pyConverters) != len(args):
				raise ValueError(
					"""%s requires %r arguments (%s), received %s: %r"""%(
						self.wrappedOperation.__name__,
						len(pyConverters),
						", ".join( self.pyConverterNames ),
						len(args),
						args
					)
				)
			pyArgs = []
			for (converter,arg) in zip(pyConverters,args):
				if converter is None:
					pyArgs.append( arg )
				else:
					pyArgs.append( converter(arg, self, args) )
		else:
			pyArgs = args 
		cConverters = getattr( self, 'cConverters', None )
		if cConverters:
			cArgs = []
			for (index,converter) in enumerate( cConverters ):
				if not callable(converter):
					cArgs.append( converter )
				else:
					try:
						cArgs.append(
							converter( pyArgs, index, self )
						)
					except Exception, err:
						if hasattr( err, 'args' ):
							err.args += (
								"""Failure in cConverter %r"""%(converter),
								pyArgs, index, self,
							)
						raise
		else:
			cArgs = pyArgs
		cResolvers = getattr( self, 'cResolvers', None )
		if cResolvers:
			cArguments = []
			for (converter, value) in zip( cResolvers, cArgs ):
				if converter is None:
					cArguments.append( value )
				else:
					cArguments.append( converter( value ) )
		else:
			cArguments = cArgs
		try:
			result = self.wrappedOperation( *cArguments )
		except ctypes.ArgumentError, err:
			err.args = err.args + (cArguments,)
			raise err
		except error.GLError, err:
			err.cArgs = cArgs 
			err.pyArgs = pyArgs
			raise err
		storeValues = getattr( self, 'storeValues', None )
		if storeValues is not None:
			# handle storage of persistent argument values...
			storeValues(
				result,
				self,
				pyArgs,
				cArgs,
			)
		returnValues = getattr( self, 'returnValues', None )
		if returnValues is not None:
			return returnValues(
				result,
				self,
				pyArgs,
				cArgs,
			)
		else:
			return result

def wrapper( wrappedOperation ):
	"""Create a Wrapper sub-class instance for the given wrappedOperation
	
	The purpose of this function is to create a subclass of Wrapper which
	has the __doc__ and __name__ of the wrappedOperation so that the instance of
	the wrapper will show up as <functionname instance @ address> by default,
	and will have the docstring available naturally in pydoc and the like.
	"""
	if isinstance( wrappedOperation, Wrapper ):
		return wrappedOperation
	dict = {
		'__doc__': wrappedOperation.__doc__,
		'__slots__': ('wrappedOperation', ),
	}
	cls = type( wrappedOperation.__name__, (Wrapper,), dict )
	instance = cls(wrappedOperation)
	return instance
