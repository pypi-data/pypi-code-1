#############################################################################
#
#	$Id: nsc.py,v 2.16 2003/07/06 23:12:16 irmen Exp $
#	Pyro Name Server Control Tool
#
#	This is part of "Pyro" - Python Remote Objects
#	which is (c) Irmen de Jong - irmen@users.sourceforge.net
#
#############################################################################

from naming import NameServerLocator
from errors import NamingError, ConnectionDeniedError, PyroError
import Pyro.constants
import core
from protocol import getHostname

class PyroNSControl:
	def args(self, args):
		import Pyro.util
		self.Args = Pyro.util.ArgParser()
		self.Args.parse(args,'h:p:i:')
		self.Args.printIgnored()
		if self.Args.args:
			cmd = self.Args.args[0]
			del self.Args.args[0]
			return cmd
		return None	

	def connect(self, sysCmd=None):
		host = self.Args.getOpt('h',None)
		port = int(self.Args.getOpt('p', 0))
		ident = self.Args.getOpt('i',None)
		if port==0:
			port=None

		locator = NameServerLocator(identification=ident)
		if not sysCmd:
			self.NS = locator.getNS(host,port,1)
			print 'NS is at',self.NS.URI.address,'('+(getHostname(self.NS.URI.address) or '??')+') port',self.NS.URI.port
			self.NS._setIdentification(ident)
		else:
			result = locator.sendSysCommand(sysCmd,host,port,1)
			print 'NS replied to system command',sysCmd,':',result
		
	def ping(self):
		self.connect()
		self.NS.ping()
		print 'NS is up and running!'

	def listall(self):
		self.connect()
		flat=self.NS.flatlist()
		flat.sort()
		print '-------------- START DATABASE'
		for (name,val) in flat:
			print name,' --> ',str(val)
		print '-------------- END'

	def list(self):
		self.connect()
		if not self.Args.args:
			# list the current group
			print self.NS.fullName(''),'-->',
			self.printList(self.NS.list(None))
		else:
			# list all subpaths
			for n in self.Args.args:
				print self.NS.fullName(n),' -->',
				try:
					self.printList(self.NS.list(n))
				except NamingError,x:
					print '## can\'t list:',x,'##'

	def printList(self,list):
		list.sort()
		print '(',
		for (n,t) in list:
			if t==0:
				print '['+n+']',
			elif t==1:
				print n,
		print ')'

	def resolve(self):
		self.connect()
		if not self.Args.args:
			print 'No arguments, nothing to resolve'
		else:
			for n in self.Args.args:
				print n,' -->',
				try:
					print self.NS.resolve(n)
				except NamingError,x:
					print '## can\'t resolve:',x,'##'
	
	def register(self):
		self.connect()
		try:
			self.NS.register(self.Args.args[0],self.Args.args[1])
			uri=core.PyroURI(self.Args.args[1])
			print 'registered',self.Args.args[0],' --> ',uri
		except NamingError,arg:
			print 'Error from NS:',arg
		except IndexError:
			print 'Register needs 2 args: name URI'
		
	def remove(self):
		self.connect()
		for n in self.Args.args:
			try:
				self.NS.unregister(n)
				print n,'unregistered.'
			except NamingError,x:
				print '## Can\'t unregister',n,'because',x

	def creategroup(self):
		self.connect()
		for n in self.Args.args:
			try:
				self.NS.createGroup(n)
				print n,'created.'
			except NamingError,x:
				print '## Can\'t create',n,'because',x

	def deletegroup(self):
		self.connect()
		for n in self.Args.args:
			try:
				self.NS.deleteGroup(n)
				print n,'deleted.'
			except NamingError,x:
				print '## Can\'t delete',n,'because',x
				
	def showmeta(self):
		self.connect()
		if not self.Args.args:
			print 'No arguments, nothing to show meta of'
		for n in self.Args.args:
			try:
				print "META INFO OF",self.NS.fullName(n)
				print "system meta info :",self.NS._getSystemMeta(n)
				print "  user meta info :",self.NS.getMeta(n)
			except NamingError,x:
				print "## Can't get meta because",x
	
	def resync(self):
		self.connect()
		self.NS.resync()
		print 'resync done'

	def shutdown(self):
		self.connect(sysCmd='shutdown')


def usage():
	print 'PyroNS control program - usage is as follows;'
	print '>> nsc [-h host] [-p port] [-i identification] command [args...]'
	print 'where command is one of: ping, list, listall, resolve, register, remove, creategroup, deletegroup, showmeta, resync, shutdown'
	print '      host is the host where the NS should be contacted'
	print '      port is the non-standard Pyro NS broadcast port'
	print '           (if host is specified, it is the Pyro port instead)'
	print '      identification is the authentication ID to connect to the server'
	print '      args... depend on the command.'
	raise SystemExit

def main(argv):

	ctrl = PyroNSControl()
	cmd=ctrl.args(argv)

	if not cmd:
		usage()

	try:
		# nice construct to map commands to the member function to call
		call= { 'ping': ctrl.ping,
			  'list': ctrl.list,
			  'listall': ctrl.listall,
			  'resolve': ctrl.resolve,
			  'register': ctrl.register,
			  'remove': ctrl.remove,
			  'creategroup': ctrl.creategroup,
			  'deletegroup': ctrl.deletegroup,
			  'shutdown': ctrl.shutdown,
			  'showmeta': ctrl.showmeta,
			  'resync': ctrl.resync   } [cmd] 
			  
	except KeyError:
		usage()
	try:
		Pyro.core.initClient(banner=0)
		call()
	except ConnectionDeniedError,arg:
		print 'Could not connect to the server:',arg
		if str(arg)==Pyro.constants.deniedReasons[Pyro.constants.DENIED_SECURITY]:
			print "Supply correct authentication ID?"
	except PyroError,arg:
		print 'There is a problem:',arg
	except Exception,x:
		print 'CAUGHT ERROR, printing Pyro traceback >>>>>>',x
		print ''.join(Pyro.util.getPyroTraceback(x))
		print '<<<<<<< end of Pyro traceback'


