#! /usr/bin/python
#
# Copyright (C) 2006 Giuseppe Corbelli
#
# This file is part of Pyreb.
#
# Pyreb is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# Pyreb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Pyreb; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import threading, SimpleXMLRPCServer, wx

myEVT_EXT_SETTEXT = wx.NewEventType()
EVT_EXT_SETTEXT = wx.PyEventBinder(myEVT_EXT_SETTEXT)

myEVT_EXT_GETTEXT = wx.NewEventType()
EVT_EXT_GETTEXT = wx.PyEventBinder(myEVT_EXT_GETTEXT)

myEVT_EXT_SETREGEX = wx.NewEventType()
EVT_EXT_SETREGEX = wx.PyEventBinder(myEVT_EXT_SETREGEX)

myEVT_EXT_GETREGEX = wx.NewEventType()
EVT_EXT_GETREGEX = wx.PyEventBinder(myEVT_EXT_GETREGEX)

class SetTextEvent(wx.PyEvent):
    """
    Custom wxPython event, needed to communicate a "Set" action
    to pyreb.
    """
    def __init__(self, evtType, txt):
        wx.PyEvent.__init__(self, eventType=evtType)
        self.text = txt

class GetTextEvent(wx.PyEvent):
    """
    Custom wxPython event, needed to communicate a "Get" action
    to pyreb.
    """
    def __init__(self, evtType):
        wx.PyEvent.__init__(self, eventType=evtType)
        self.text = ''

class PyrebAPI:
    """
    Methods exported by the XMLRPC server.
    """
    def __init__(self, Wnd):
        """
        Initializes the API container
        @param Wnd: Pyreb main window, needed to pass events along
        """
        self.Wnd = Wnd
    
    def setText(self, Text):
        """
        Set the text in the 'Text to analyze' control. The actual regex will
        be appliead against the new text.
        @param Text: Text to be displayed
        """
        evt = SetTextEvent(myEVT_EXT_SETTEXT, Text)
        wx.PostEvent(self.Wnd, evt)
        return "setText"

    def getText(self):
        """
        Get the text in the 'Text to analyze' control
        @return: Text in the control
        """
        evt = GetTextEvent(myEVT_EXT_GETTEXT)
        wx.PostEvent(self.Wnd, evt)
        return evt.text
        
    def setRegex(self, Text):
        """
        Set the Regular expression. After being set, the regex will be applied
        @param Text: Regex to be set and applied
        """
        evt = SetTextEvent(myEVT_EXT_SETREGEX, Text)
        wx.PostEvent(self.Wnd, evt)
        return "setRegex"

    def getRegex(self):
        """
        Get the Regular expression.
        @return: Current regex.
        """
        evt = GetTextEvent(myEVT_EXT_GETREGEX)
        wx.PostEvent(self.Wnd, evt)
        return evt.text

def handlerSetup(handler, API):
    handler.register_introspection_functions()
    handler.register_function(API.setText, "Pyreb.setText")
    handler.register_function(API.getText, "Pyreb.getText")
    handler.register_function(API.setRegex, "Pyreb.setRegex")
    handler.register_function(API.getRegex, "Pyreb.getRegex")
    
class PyrebXMLRPCServer(threading.Thread):
    """
    Simple XMLRPC server to control Pyreb instance.
    The server is run in a separate thread. The pyreb instance
    is controlled using custom wxWidgets events: for this reason
    the server needs pyreb main window instance.
    """
    def __init__(self, Wnd, Port=17787):
        """
        Initialize the server.
        @param Wnd: Pyreb main window
        @param Port: Port to bind the server
        """
        threading.Thread.__init__(self)
        self.Port = Port
        self.Wnd = Wnd
        self.Mutex = threading.Lock()
        
    def run(self):
        handler = SimpleXMLRPCServer.SimpleXMLRPCServer( ('localhost', self.Port), logRequests=False)
        api = PyrebAPI(self.Wnd)
        handlerSetup(handler, api)
        while (True):
            #Should really find a better way to stop the server...
            if (True == self.Mutex.acquire(0)):
                return
            handler.handle_request()
