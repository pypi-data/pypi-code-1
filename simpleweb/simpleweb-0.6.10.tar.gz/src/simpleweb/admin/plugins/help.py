import sys
import simpleweb

def help(name, args):
	if len(args) < 1:
		print "Usage: simpleweb-admin [command]"
		print
		print "Available Commands:"
		plugins = __import__('simpleweb.admin.plugins', {}, {}, 'plugins')
		for i in plugins.__all__:
			print "  %s" % (i)
		print "  help"
		print "  help [command]"

	if len(args) == 1:
		command = args[0]
		try:
			module = __import__('simpleweb.admin.plugins.%s' % (command), {}, {}, command)
		except ImportError:
			sys.stderr.write("Command '%s' is not implemented\n" % (command))
		else:
			sys.stdout.write("%s\n" % (getattr(module, command).__doc__))
