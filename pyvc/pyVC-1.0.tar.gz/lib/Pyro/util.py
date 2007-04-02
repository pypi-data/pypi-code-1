#############################################################################
#
#	$Id: util.py,v 2.37 2004/05/08 22:18:10 irmen Exp $
#	Pyro Utilities
#
#	This is part of "Pyro" - Python Remote Objects
#	which is (c) Irmen de Jong - irmen@users.sourceforge.net
#
#############################################################################

import os, sys, string
import time, random
import Pyro					# bring in Pyro.config
from Pyro.util2 import *	# bring in 'missing' util functions


# bogus lock class, for systems that don't have threads.
class BogusLock:
	def acquire(self): pass
	def release(self): pass

def getLockObject():	
	if supports_multithreading():
		from threading import Lock
		return Lock()
	else:
		return BogusLock()

# bogus event class, for systems that don't have threads
class BogusEvent:
	def __init__(self):
		self.flag=0
	def isSet(self): return self.flag==1
	def set(self): self.flag=1
	def clear(self): self.flag=0
	def wait(timeout=None):
		raise RuntimeError("cannot wait in non-threaded environment")

def getEventObject():
	if supports_multithreading():
		from threading import Event
		return Event()
	else:
		return BogusEvent()	
	

# Logging stuff.

# Select the logging implementation to use!
if Pyro.config.PYRO_STDLOGGING:
	# new-style logging using logging module, python 2.3+
	import logging, logging.config
	cfgfile=Pyro.config.PYRO_STDLOGGING_CFGFILE
	if not os.path.isabs(cfgfile):
		Pyro.config.PYRO_STDLOGGING_CFGFILE=os.path.join(Pyro.config.PYRO_STORAGE, cfgfile)
		cfgfile=Pyro.config.PYRO_STDLOGGING_CFGFILE
	externalConfig=0
	try:
		open(cfgfile).close()
		logging.config.fileConfig(cfgfile)
		externalConfig=1
	except IOError,x:
		# Config file couldn't be read! Use builtin config.
		# First make the logfiles absolute paths:
		if not os.path.isabs(Pyro.config.PYRO_LOGFILE):
			Pyro.config.PYRO_LOGFILE=os.path.join(Pyro.config.PYRO_STORAGE, Pyro.config.PYRO_LOGFILE)
		if not os.path.isabs(Pyro.config.PYRO_USER_LOGFILE):
			Pyro.config.PYRO_USER_LOGFILE=os.path.join(Pyro.config.PYRO_STORAGE, Pyro.config.PYRO_USER_LOGFILE)

	class LoggerBase:
		if externalConfig:
			def __init__(self):
				self.logger=logging.getLogger(self._getLoggerName())
		else:
			def __init__(self):
				self.logger=logging.getLogger("Pyro."+str(id(self)))		# each time a different logger ...
				self.setLevel(self._getPyroLevel())
				handler=logging.FileHandler(self._logfile())
				handler.setFormatter(logging.Formatter("%(asctime)s [%(process)d:%(thread)d] ** %(levelname)s ** %(message)s"))
				self.logger.addHandler(handler)
		def setLevel(self, pyroLevel):
			if pyroLevel>=3:
				self.logger.setLevel(logging.DEBUG)
			elif pyroLevel>=2:
				self.logger.setLevel(logging.WARN)
			elif pyroLevel>=1:
				self.logger.setLevel(logging.ERROR)
			else:
				self.logger.setLevel(999)
		def msg(self,source,*args):
			self.setLevel(self._getPyroLevel())
			if not args:
				(args, source) = ([source], "N/A")
			self.logger.info("%s ** %s", source, reduce(lambda x,y: str(x)+' '+str(y),args))
		def warn(self,source,*args):
			self.setLevel(self._getPyroLevel())
			if not args:
				(args, source) = ([source], "N/A")
			self.logger.warn("%s ** %s", source, reduce(lambda x,y: str(x)+' '+str(y),args))
		def error(self,source,*args):
			self.setLevel(self._getPyroLevel())
			if not args:
				(args, source) = ([source], "N/A")
			self.logger.error("%s ** %s", source, reduce(lambda x,y: str(x)+' '+str(y),args))
		def raw(self,ztr):
			self.logger.log(999,ztr.rstrip())
		def _logfile(self):
			raise NotImplementedError,'must override'
		def _getlevel(self):
			raise NotImplementedError,'must override'


	class SystemLogger(LoggerBase):
		def _getLoggerName(self):
			return "Pyro.system"
		def _getPyroLevel(self):
			return Pyro.config.PYRO_TRACELEVEL
		def _logfile(self):
			return Pyro.config.PYRO_LOGFILE
			
	class UserLogger(LoggerBase):
		def _getLoggerName(self):
			return "Pyro.user"
		def _getPyroLevel(self):
			return Pyro.config.PYRO_USER_TRACELEVEL
		def _logfile(self):
			return Pyro.config.PYRO_USER_LOGFILE
	
else:
	# classic Pyro logging. 
	
	class LoggerBase:
		# Logger base class. Subclasses must override _logfile and  _checkTraceLevel.
		def __init__(self):
			import Pyro
			self.lock=getLockObject()
		def msg(self,source,*args):
			if self._checkTraceLevel(3): self._trace('NOTE',source, args)
		def warn(self,source,*args):
			if self._checkTraceLevel(2): self._trace('WARN',source, args)
		def error(self,source,*args):
			if self._checkTraceLevel(1): self._trace('ERR!',source, args)
		def raw(self,str):
			self.lock.acquire()
			try:
				f=open(self._logfile(),'a')
				f.write(str)
				f.close()
			finally:
				self.lock.release()
		def _trace(self,typ,source, arglist):
			self.lock.acquire()
			try:
				if not arglist:
					(arglist, source) = ([source], "N/A")
				try:
					tf=open(self._logfile(),'a')
					try:
						pid=os.getpid()
						pidinfo=" ["+str(os.getpid())
					except:
						pidinfo=" ["   # XXX jython has no getpid()
					if supports_multithreading():
						pidinfo+=":"+threading.currentThread().getName()
					pidinfo+="] "	
					tf.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+
					  pidinfo+'** '+typ+' ** '+str(source)+' ** '+reduce(lambda x,y: str(x)+' '+str(y),arglist)+'\n')
					tf.close()
				except Exception,x:
					pass
			finally:
				self.lock.release()
		def _logfile(self):
			raise NotImplementedError,'must override'
		def _checkTraceLevel(self,level):
			raise NotImplementedError,'must override'
	
	class SystemLogger(LoggerBase):
		def _checkTraceLevel(self, level):
			return Pyro.config.PYRO_TRACELEVEL >= level
		def _logfile(self):
			file=Pyro.config.PYRO_LOGFILE
			if not os.path.isabs(file):
				Pyro.config.PYRO_LOGFILE=os.path.join(Pyro.config.PYRO_STORAGE, file)
			return Pyro.config.PYRO_LOGFILE
			
	class UserLogger(LoggerBase):
		def _checkTraceLevel(self, level):
			return Pyro.config.PYRO_USER_TRACELEVEL >= level
		def _logfile(self):
			file=Pyro.config.PYRO_USER_LOGFILE
			if not os.path.isabs(file):
				Pyro.config.PYRO_USER_LOGFILE=os.path.join(Pyro.config.PYRO_STORAGE, file)
			return Pyro.config.PYRO_USER_LOGFILE


# The logger object 'Log'.
Log = SystemLogger()


# Caching directory lister, outputs (filelist,dirlist) tuple
# Based upon dircache.py, but implemented in a callable object
# that has a thread-safe cache.
class DirLister:
	def __init__(self):
		self.lock=getLockObject()
		self.__listdir_cache = {}

	def __call__(self,path):
		self.lock.acquire()
		try:
			try:
				cached_mtime, files, directories = self.__listdir_cache[path]
				del self.__listdir_cache[path]
			except KeyError:
				cached_mtime, files, directories = -1, [], []
		finally:
			self.lock.release()
		mtime = os.stat(path)[8]
		if mtime <> cached_mtime:
			list = os.listdir(path)
			files=[]
			directories=[]
			for e in list:
				if os.path.isdir(os.path.join(path,e)):
					directories.append(e)
				else:
					files.append(e)
		self.lock.acquire()
		try:
			self.__listdir_cache[path] = mtime, files, directories
			return files,directories
		finally:
			self.lock.release()

listdir = DirLister()		# callable object		


# Fairly simple argument options parser. Like getopt(3).
class ArgParser:
	def __init__(self):
		pass
	def parse(self, args, optionlist):
		# optionlist is a string such as "ab:c" which means
		# we search for 3 options (-a, -b, -c) of which -b has an argument.
		self.options={}		# public, the option->value dictionary
		self.args=[]		# public, the rest of the arguments
		self.ignored=[]		# public, ignored options
		optionlist+=' '		# add sentinel
		if type(args)==type(''):
			args=string.split(args)
		while args:
			arg=args[0]
			del args[0]
			if arg[0]=='-':
				if len(arg)>=2:   # arg is an option. Check our list
					idx = string.find(optionlist,arg[1])
					if idx>=0:
						if optionlist[idx+1]==':':   # option requires argument.
							if len(arg)>=3:   # argument is appended. Use this.
								self.options[arg[1]]=arg[2:]
								continue
							# fetch argument from next string
							if len(args)>=1:
								self.options[arg[1]]=args[0]
								del args[0]
								continue
							else:   # missing arg, substitute None
								self.options[arg[1]]=None
						else:   # option requires no argument, use None
							self.options[arg[1]]=None
					else:   # didn't find this option, skip it
						self.ignored.append(arg[1])
				else:   # arg is a single '-'. Stop parsing.
					for a in args:
						self.args.append(a)
					args=None
			else:   # arg is no option, add it to the residu list and continue
				self.args.append(arg)
	def hasOpt(self, option):
		return self.options.has_key(option)
	def getOpt(self, option, default=Exception()):
		try:
			return self.options[option]
		except KeyError:
			if not isinstance(default,Exception):
				return default
			raise KeyError('no such option')
	def printIgnored(self):
		if self.ignored:
			print 'Ignored options:',
			for o in self.ignored:
				print '-'+o,
			print


_getGUID_counter=0		# extra safeguard against double numbers
_getGUID_lock=getLockObject()

if os.name=='java':
	def getGUID():
		# Jython uses java's own ID routine used by RMI
		import java.rmi.dgc
		return java.rmi.dgc.VMID().toString().replace(':','-')
else:	
	import socket, binascii
	def getGUID():
		# Generate readable GUID string.
		# The GUID is constructed as follows: hexlified string of
		# AAAAAAAA-AAAABBBB-BBBBBBBB-BBCCCCCC  (a 128-bit number in hex)
		# where A=network address, B=timestamp, C=random. 
		# The 128 bit number is returned as a string of 16 8-bits characters.
		# For A: should use the machine's MAC ethernet address, but there is no
		# portable way to get it... use the IP address + 2 bytes process id.
	
		import Pyro.protocol
		ip=Pyro.protocol.getIPAddress()
		if ip:
			networkAddrStr=binascii.hexlify(socket.inet_aton(ip))+"%04x" % os.getpid()
		else:
			# can't get IP address... use another value, like our Python id() and PID
			Log.warn('getGUID','Can\'t get IP address')
			try:
				ip=os.getpid()
			except:
				ip=0
			ip += id(getGUID)
			networkAddrStr = "%08lx%04x" % (ip, os.getpid())
	
		_getGUID_lock.acquire()  # cannot generate multiple GUIDs at once
		global _getGUID_counter
		t1=time.time()*100 +_getGUID_counter
		_getGUID_counter+=1 
		_getGUID_lock.release()
		t2=int((t1*time.clock())%sys.maxint) & 0xffffff
		t1=int(t1%sys.maxint) 
		timestamp = (long(t1) << 24) | t2 
		r2=(random.randint(0,sys.maxint/2)>>4) & 0xffff
		r3=(random.randint(0,sys.maxint/2)>>5) & 0xff
		return networkAddrStr+'%014x%06x' % (timestamp, (r2<<8)|r3 )

def genguid_scripthelper(argv):
	p=ArgParser()
	p.parse(argv,'')
	if p.args or p.ignored:
		print 'usage: genguid  (no arguments)'
		raise SystemExit
	print getGUID()



# create a weak reference proxy if available (Python 2.1+)
def weakref(obj):
	if obj is None:
		return obj
	try:
		import weakref
		return weakref.proxy(obj)
	except ImportError:	
		return obj


# Get the configured pickling module. 
# Currently supported: cPickle, pickle, gnosis.xml.pickle (@paranoia -1),
# and PyXML 0.8+'s xml.marshal.generic.
def getPickle():
	if Pyro.config.PYRO_XML_PICKLE:
		# user requires xml pickle. Fails if that is not available!
		return getXMLPickle()
	else:	
		try: 
			import cPickle
			return cPickle
		except ImportError:
			# Fall back on pickle if cPickle isn't available
			import pickle
			return pickle

_xmlpickle={}
# the following wrapper is necessary because PyXML's pickler
# cannot take a 'binary' third argument...
class PyXMLPickler:
	def __init__(self):
		import xml.marshal.generic
		self.pickle=xml.marshal.generic
	def dumps(self, obj, bin=None):
		return self.pickle.dumps(obj)
	def dump(self, obj, file, bin=None):
		return self.pickle.dumps(obj,file)
	def loads(self, str):
		return self.pickle.loads(str)
	def load(self, file):
		return self.pickle.load(file)
	
def getXMLPickle(impl=None):		
	# load & config the required xml pickle.
	# Currently supported: Gnosis Utils' gnosis.xml.pickle,
	# and PyXML 0.8+'s xml.marshal.generic
	global _xmlpickle
	if not impl:
		impl=Pyro.config.PYRO_XML_PICKLE
	impl=impl.lower()
	if impl=='any':
		# first try if PyXML is available, otherwise, choose Gnosis.
		impl='pyxml'
		Pyro.config.PYRO_XML_PICKLE=impl
		try:
			import xml.marshal.generic
		except ImportError:
			impl='gnosis'
			Pyro.config.PYRO_XML_PICKLE=impl
	if impl in _xmlpickle:
		return _xmlpickle[impl]
	try:	
		if impl=='pyxml': # PyXML init
			_xmlpickle['pyxml']=PyXMLPickler()
			return _xmlpickle['pyxml']
		elif impl=='gnosis': # Gnosis init
			import gnosis.xml.pickle
			_xmlpickle['gnosis']=gnosis.xml.pickle
			gnosis.xml.pickle.setParanoia(0)		# default paranoia level is too strict for Pyro
			gnosis.xml.pickle.setParser('SAX')		# use fastest parser (cEXPAT?)
			return gnosis.xml.pickle
		else:
			raise ImportError('unsupported xml pickle implementation requested: '+impl)
	except ImportError:
		Log.error('server was asked to use xml pickling but implementation ('+impl+') is not available')
		raise NotImplementedError('server was asked to use xml pickling but implementation ('+impl+') is not available')


# Pyro traceback printing
def getPyroTraceback(exc_obj):
	import constants
	try:
		exc_type, exc_value, exc_trb=sys.exc_info()
		remote_tb=getattr(exc_obj,constants.TRACEBACK_ATTRIBUTE,None)
		local_tb=formatTraceback(exc_type, exc_value, exc_trb)
		if remote_tb:
			return [ '---- remote Pyro traceback ----\n' ] + \
				remote_tb + [ '---- local traceback ----\n' ] +  local_tb
		else:
			# hmm. no remote tb info, return just the local tb.
			return local_tb
	finally:
		# clean up cycle to traceback
		del exc_type, exc_value, exc_trb


def formatTraceback(ex_type, ex_value, tb):
	import traceback
	if Pyro.config.PYRO_DETAILED_TRACEBACK:
		import linecache

		get_line_number = traceback.tb_lineno
	
		res = ['-'*50+ "\n",
			   " <%s> RAISED : %s\n" % (str(ex_type), str(ex_value)),
			   " Extended Stacktrace follows (most recent call last)\n",
			   '-'*50+'\n' ]
	 
		try:
			# Do some manipulation shit of stack
			if tb != None:
				frame_stack = []
				line_number_stack = []
	 
				#tb = sys.exc_info()[2]
				while 1:
					line_num = get_line_number(tb)
					line_number_stack.append(line_num)
					if not tb.tb_next:
						break
					tb = tb.tb_next
	 
				f = tb.tb_frame
				for x in line_number_stack:
					frame_stack.append(f)
					f = f.f_back
	 
				frame_stack.reverse()
	 
				lines = iter(line_number_stack)
				seen_crap = 0
				for frame in frame_stack:
					# Get items
					locals = frame.f_locals.items()[:]
	 
					line_num = lines.next()
					filename = frame.f_code.co_filename
	 
					name = None
					for key, value, in locals:
						if key == "self":
							name = "%s::%s" % (value.__class__.__name__, frame.f_code.co_name)
					if name == None:
						name = frame.f_code.co_name
	 
					res.append('File "%s", line (%s), in %s\n' % (filename, line_num, name))
					res.append("Source code:\n")
					
					code_line = linecache.getline(filename, line_num)
					if code_line:
						res.append('    %s\n' % code_line.strip())
	  
					if not seen_crap:
						seen_crap = 1
						continue
	  
					res.append("Local values:\n")
					locals.sort()
					
					for key, value, in locals:
						if key in frame.f_code.co_names:
							local_res="  %20s = " % key
							try:
								local_res += repr(value)
							except:
								try:
									local_res += str(value)
								except:
									local_res += "<ERROR>"
									
							res.append(local_res+"\n")
							
					res.append('-'*50 + '\n')
			res.append(" <%s> RAISED : %s\n" % (str(ex_type), str(ex_value)))
			res.append('-'*50+'\n')
			return res
			
		except:
			return ['-'*50+"\nError building extended traceback!!! :\n",
				  ''.join(traceback.format_exception(* sys.exc_info() ) ) + '-'*50 + '\n',
				  'Original Exception follows:\n',
				  ''.join(traceback.format_exception(ex_type, ex_value, tb)) ]

	else:
		# default traceback format.
		return traceback.format_exception(ex_type, ex_value, tb)
