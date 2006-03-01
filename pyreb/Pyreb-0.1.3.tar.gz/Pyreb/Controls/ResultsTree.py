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

import wx
import wx.gizmos as gizmos
import wx.xrc as xrc

class PyrebResultsTree (gizmos.TreeListCtrl):
    def __init__(self, parent, id, pos, size, style, name):
        #Set default styles
        style |= wx.TR_HAS_BUTTONS
        style |= wx.TR_NO_LINES
        style |= wx.TR_LINES_AT_ROOT
        style |= wx.TR_DEFAULT_STYLE
        style |= wx.SUNKEN_BORDER
        gizmos.TreeListCtrl.__init__(self, parent, id, pos, size, style, wx.DefaultValidator, name)
        self.AddColumn("Match")
        self.AddColumn("Group")
        self.AddColumn("Position")
        self.AddColumn("Text")
        self.SetMainColumn(0) # the one with the tree in it...
        self.AddRoot("No matches")
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
    
    def OnSize(self, event):
        TotalWidth = self.GetClientSize().GetWidth()
        for i in range(0, 4):
            self.SetColumnWidth(i, TotalWidth / 4)
        event.Skip(True)
        
    def ShowMatches(self, Mo=None):
        root = self.GetRootItem()
        self.DeleteChildren(root)
        if (not Mo):
            self.SetItemText(root, "No Matches")
            return
        Reobj = Mo.re
        Text = Mo.string
        
        start = Mo.start()
        end = Mo.end()
        length = end - start
        groupdict = Reobj.groupindex
        self.SetItemText(root, "Match 0", 0)
        self.SetItemText(root, "0", 1)
        self.SetItemText(root, "%d - %d" % (start, end), 2)
        self.SetItemText(root, Text[start:end].replace("\n", "\\n"), 3)
        i = 1
        for data in Mo.groups():
            start = Mo.start(i)
            end = Mo.end(i)
            groupname = i
            for x in groupdict:
                if (groupdict[x] == i):
                    groupname = x
            itm = self.AppendItem(root, "Match %d" % i)
            self.SetItemText(itm, str(groupname), 1)
            self.SetItemText(itm, "%d - %d" % (start, end), 2)
            self.SetItemText(itm, Text[start:end].replace("\n", "\\n"), 3)
            i+=1
        
        end = Mo.end()
        length = len(Text)
        if (length != end):
            itm = self.AppendItem(root, "Unmatched data")
            self.SetItemText(itm, "", 1)
            self.SetItemText(itm, "%d - %d" % (start, end), 2)
            self.SetItemText(itm, Text[end:].replace("\n", "\\n"), 3)
        self.Expand(root)
    
    def OnCloseWindow(self, event):
        self.Destroy()

class PrePyrebResultsTree(gizmos.TreeListCtrl):
    def __init__(self):
        p = gizmos.PreTreeListCtrl()
        self.PostCreate(p)
    
    def Create(self, parent, id, pos, size, style, name):
        gizmos.TreeListCtrl.Create(self, parent, id, pos, size, style, wx.DefaultValidator, name)
        self.AddColumn("Match")
        self.AddColumn("Group")
        self.AddColumn("Position")
        self.AddColumn("Text")
        self.SetMainColumn(0) # the one with the tree in it...
        self.AddRoot("No matches")

class PyrebResultsTreeXmlHandler(xrc.XmlResourceHandler):
    def __init__(self):
        xrc.XmlResourceHandler.__init__(self)
        # Specify the styles recognized by objects of this type
        self.AddStyle("wxTR_HAS_BUTTONS", wx.TR_HAS_BUTTONS)
        self.AddStyle("wxTR_NO_LINES", wx.TR_NO_LINES)
        self.AddStyle("wxTR_LINES_AT_ROOT", wx.TR_LINES_AT_ROOT)
        self.AddStyle("wxTR_DEFAULT_STYLE", wx.TR_DEFAULT_STYLE)
        self.AddStyle("wxSUNKEN_BORDER", wx.SUNKEN_BORDER)
        self.AddWindowStyles()

    # This method and the next one are required for XmlResourceHandlers
    def CanHandle(self, node):
        return self.IsOfClass(node, "PyrebResultsTree")
    
    def DoCreateResource(self):
        widget = self.GetInstance()
        style = 0
        style |= self.GetStyle("style", wx.TR_HAS_BUTTONS)
        style |= self.GetStyle("style", wx.TR_NO_LINES)
        style |= self.GetStyle("style", wx.TR_LINES_AT_ROOT)
        style |= self.GetStyle("style", wx.TR_DEFAULT_STYLE)
        style |= self.GetStyle("style", wx.SUNKEN_BORDER)
        size = self.GetSize()
        if 1:
            assert widget is None
            widget = PyrebResultsTree(self.GetParentAsWindow(), self.GetID(), 
                        self.GetPosition(), size, style, self.GetName() )
        else:
            if widget is None:
                widget = PrePyrebResultsTree()
            widget.Create (self.GetParentAsWindow(), self.GetID(), self.GetPosition(),
                            size, style, self.GetName() )
        
        # These two things should be done in either case:
        # Set standard window attributes
        self.SetupWindow(widget)
        # Create any child windows of this node
        self.CreateChildren(widget)

        return widget
