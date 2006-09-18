"""COMKit

This plug-in for WebKit for Python allows COM objects such as ADO to be
used in free-threading mode in a threaded app server.  See Appendix D of
the fine book Python Programming on Win32 by Mark Hammond and Andy
Robinson for details.

To use COM, simply set EnableCOM to 1 in your AppServer.config file.
This causes the app server threads to be configured properly for
COM free-threading.  Then go ahead and use win32com inside your servlets.
"""

__all__ = []


# This function gets called by the app server during initialization
def InstallInWebKit(appServer):
	# See if enabling COM was requested
	if appServer.setting('EnableCOM', 0):

		# This must be done BEFORE pythoncom is imported -- see the book mentioned above.
		import sys
		sys.coinit_flags = 0

		# Get the win32 extensions
		import pythoncom

		# Grab references to the original initThread and delThread bound
		# methods, which we will replace
		original_initThread = appServer.initThread
		original_delThread = appServer.delThread

		# Create new versions of initThread and delThread which will call the
		# old versions
		def new_initThread(self):
			# This must be called at the beginning of any thread that uses COM
			pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)

			# Call the original initThread
			original_initThread()

		def new_delThread(self):
			# Call the original delThread
			original_delThread()

			# Uninitialize COM
			pythoncom.CoUninitialize()

		# Replace the initThread and delThread with our new versions, for
		# this instance of the appserver only
		import new
		appServer.initThread = new.instancemethod(new_initThread, appServer, appServer.__class__)
		appServer.delThread = new.instancemethod(new_delThread, appServer, appServer.__class__)

		print 'COM has been enabled.'


