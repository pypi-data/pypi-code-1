#!/usr/bin/env python
# -*- coding: ANSI_X3.4-1968 -*-
# generated by wxGlade 0.4 on Wed Nov 15 11:56:11 2006

import StringIO
import os.path
import pprint
import sys
import traceback

import wx
import wx.lib.mixins.listctrl

import FFSessionEditor as FFSE

VERSION = "1.0"

ABOUT_TITLE = "Firefox Session Editor "+VERSION

NO_CONTENT_MSG = "Open a Firefox session to continue."
SO_SELECTION_MSG = "No entries have been selected."
NOTHING_TO_SAVE_MSG = "There is nothing to save."

WILDCARD="JSON files (*.js)|*.js|All files (*)|*"


# ColumnSorter chokes on unicode, which this will hopefully filter out.
def filter_alnum(s):
    """Lowercase and filter non-alphanumeric characters out of a string."""
    if s == None:
        return ''
    chars = [str(c).lower() for c in s if c.isalnum()]
    return ''.join(chars)


def error(parent):
    """Show an error traceback."""
    sio = StringIO.StringIO()
    traceback.print_exc(file=sio)
    message = sio.getvalue()
    d = wx.MessageDialog(parent, message, "Error", wx.OK | wx.ICON_ERROR)
    d.ShowModal()
    d.Destroy()

def warning(parent, message):
    """Show a warning message."""
    d = wx.MessageDialog(parent, message, "Warning", wx.OK | wx.ICON_WARNING)
    d.ShowModal()
    d.Destroy()


class PropertiesDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PropertiesDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, -1)
        self.props_text = wx.TextCtrl(self.panel_2, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
        self.dismiss_button = wx.Button(self.panel_2, -1, "Dismiss", style=wx.BU_EXACTFIT)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_dismiss, self.dismiss_button)
        # end wxGlade

        # Make it monospaced.
        oldfont = self.props_text.GetFont()
        newfont = wx.Font(oldfont.GetPointSize(), wx.TELETYPE,
                          oldfont.GetStyle(), oldfont.GetWeight())
        self.props_text.SetFont(newfont)

    def __set_properties(self):
        # begin wxGlade: PropertiesDialog.__set_properties
        self.SetTitle("Properties")
        self.SetSize((400, 300))
        self.dismiss_button.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PropertiesDialog.__do_layout
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(self.props_text, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_6.Add(self.dismiss_button, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ADJUST_MINSIZE, 3)
        self.panel_2.SetAutoLayout(True)
        self.panel_2.SetSizer(sizer_6)
        sizer_6.Fit(self.panel_2)
        sizer_6.SetSizeHints(self.panel_2)
        sizer_5.Add(self.panel_2, 1, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_5)
        self.Layout()
        # end wxGlade

    def on_dismiss(self, event): # wxGlade: PropertiesDialog.<event_handler>
        self.Close()

# end of class PropertiesDialog


class AboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.about_title = wx.StaticText(self, -1, "Firefox Session Editor X.XX")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "Copyright (C) 2006 Kevin Vance <kvance@kvance.com>.\n\nThis is free software, and you are welcome to redistribute it under the terms of the GNU GPL version 2 or higher.\n\nThis program includes a modified version of demjson, Copyright (C) 2006 Deron E. Meranda <http://deron.meranda.us/>", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
        self.dismiss_button = wx.Button(self, -1, "Dismiss", style=wx.BU_LEFT|wx.BU_RIGHT|wx.BU_EXACTFIT)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_dismiss, self.dismiss_button)
        # end wxGlade

        self.about_title.SetLabel(ABOUT_TITLE)

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle("About")
        self.about_title.SetFont(wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.text_ctrl_1.SetMinSize((393, 150))
        self.dismiss_button.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.about_title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.text_ctrl_1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ADJUST_MINSIZE, 5)
        sizer_1_copy.Add(self.dismiss_button, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(sizer_1_copy, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        sizer_3.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def on_dismiss(self, event): # wxGlade: AboutDialog.<event_handler>
        self.Destroy()

# end of class AboutDialog


class AppFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AppFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.content_panel = wx.ScrolledWindow(self, -1, style=wx.TAB_TRAVERSAL)
        self.util_panel = wx.Panel(self, -1)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        self.SetMenuBar(self.menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_OPEN, "&Open Firefox Session...\tCtrl+O", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(10000, "Open &File...\tCtrl+F", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVE, "&Save\tCtrl+S", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVEAS, "Save &As...\tShift+Ctrl+S", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_CLOSE, "&Close\tCtrl+W", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_EXIT, "E&xit\tCtrl+Q", "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_DELETE, "&Delete\tDel", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_PROPERTIES, "Entry &Properties...\tCtrl+P", "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&Edit")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, "&About...", "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&Help")
        # Menu Bar end
        self.label_2 = wx.StaticText(self.util_panel, -1, "Search:")
        self.search_field = wx.TextCtrl(self.util_panel, -1, "")
        self.search_choice = wx.Choice(self.util_panel, -1, choices=["Title", "URL", "ID"])
        self.delete_button = wx.Button(self.util_panel, wx.ID_DELETE, "&Delete", style=wx.BU_EXACTFIT)
        self.static_line_1 = wx.StaticLine(self, -1)
        self.no_content_label = wx.StaticText(self.content_panel, -1, "No content message", style=wx.ALIGN_CENTRE)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.on_open, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.on_open_file, id=10000)
        self.Bind(wx.EVT_MENU, self.on_save, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.on_save_as, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.on_close, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_MENU, self.on_exit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.on_delete, id=wx.ID_DELETE)
        self.Bind(wx.EVT_MENU, self.on_properties, id=wx.ID_PROPERTIES)
        self.Bind(wx.EVT_MENU, self.on_about, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_TEXT, self.on_search_update, self.search_field)
        self.Bind(wx.EVT_CHOICE, self.on_search_update, self.search_choice)
        self.Bind(wx.EVT_BUTTON, self.on_delete, id=wx.ID_DELETE)
        # end wxGlade

        self.Bind(wx.EVT_CLOSE , self.on_close_window)

        self.enable_menu_items(False)

        self.no_content_label.SetLabel(NO_CONTENT_MSG)
        self.session = None
        self.session_list = None
        self.file_path = None
        self.modified = False

    def __set_properties(self):
        # begin wxGlade: AppFrame.__set_properties
        self.SetTitle("Firefox Session Editor")
        self.SetSize((605, 400))
        self.search_choice.SetSelection(0)
        self.delete_button.Enable(False)
        self.content_panel.SetScrollRate(10, 10)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AppFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.FlexGridSizer(1, 4, 0, 0)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.label_2, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(self.search_field, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(sizer_1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.search_choice, 0, wx.RIGHT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 13)
        sizer_4.Add(self.delete_button, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 3)
        self.util_panel.SetAutoLayout(True)
        self.util_panel.SetSizer(sizer_4)
        sizer_4.Fit(self.util_panel)
        sizer_4.SetSizeHints(self.util_panel)
        sizer_4.AddGrowableCol(1)
        sizer_2.Add(self.util_panel, 0, wx.EXPAND, 0)
        sizer_2.Add(self.static_line_1, 0, wx.EXPAND, 0)
        content_sizer.Add(self.no_content_label, 0, wx.ALL|wx.ADJUST_MINSIZE, 3)
        self.content_panel.SetAutoLayout(True)
        self.content_panel.SetSizer(content_sizer)
        content_sizer.Fit(self.content_panel)
        content_sizer.SetSizeHints(self.content_panel)
        sizer_2.Add(self.content_panel, 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    
    def enable_menu_items(self, enable):
        """Enable or disable menu items that need a session to be open."""
        for menu_id, ids in ((0, (wx.ID_SAVE, wx.ID_SAVEAS, wx.ID_CLOSE)),
                             (1, (wx.ID_DELETE, wx.ID_PROPERTIES))):
            menu = self.menubar.GetMenu(menu_id)
            for id in ids:
                menu.FindItemById(id).Enable(enable)


    def open_confirm(self):
        retval = True
        if self.modified:
            d = wx.MessageDialog(self, "You have unsaved changes.  Are you "\
                                 "sure you want to open a new file?",
                                 style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
            if d.ShowModal() == wx.ID_NO:
                retval = False
            d.Destroy()
        return retval

    def close_confirm(self):
        retval = True
        if self.modified:
            d = wx.MessageDialog(self, "You have made unsaved changes.  Do "\
                                 "you still want to close the file?",
                                 style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
            if d.ShowModal() == wx.ID_NO:
                retval = False
            d.Destroy()
        return retval


    def on_open(self, event): # wxGlade: AppFrame.<event_handler>
        if not self.open_confirm():
            return

        try:
            profiles = FFSE.firefox.get_profiles()
        except:
            error(self)
            return
        if len(profiles) == 0:
            warning(self, "No Firefox profiles could be found.")
            return
        elif len(profiles) == 1:
            profile = profiles[0]
        else:
            choices = [ x['name'] for x in profiles ]
            d = wx.SingleChoiceDialog(self, 'Select a profile:',
                                      'Profile Selection', choices)
            cancelled = (d.ShowModal() == wx.ID_CANCEL)
            d.Destroy()
            if cancelled:
                return
            profile = profiles[d.GetSelection()]

        path = os.path.join(profile['path'], 'sessionstore.js')
        if not os.path.exists(path):
            warning(self, "No session file was found in Firefox profile %s." %
                    profile['name'])
            return
        self.open_file(path)


    def on_open_file(self, event): # wxGlade: AppFrame.<event_handler>
        if not self.open_confirm():
            return
        fd = wx.FileDialog(self, "Open a session file.", wildcard=WILDCARD,
                           style=wx.OPEN)
        if fd.ShowModal() == wx.ID_OK:
            self.open_file(fd.GetPath())
        fd.Destroy()

    def on_save(self, event): # wxGlade: AppFrame.<event_handler>
        if self.session == None:
            warning(self, NOTHING_TO_SAVE_MSG)
            return

        filename = os.path.split(self.file_path)[1]
        d = wx.MessageDialog(self, "This operation is not reversible.  Do "\
                             "you want to overwrite %s?" % filename,
                             style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
        if d.ShowModal() == wx.ID_YES:
            self.save_file(self.file_path)
        d.Destroy()

    def on_save_as(self, event): # wxGlade: AppFrame.<event_handler>
        if self.session == None:
            warning(self, NOTHING_TO_SAVE_MSG)
            return

        fd = wx.FileDialog(self, "Save a session file.", wildcard=WILDCARD,
                           style=wx.SAVE|wx.OVERWRITE_PROMPT)
        if fd.ShowModal() == wx.ID_OK:
            self.file_path = fd.GetPath()
            self.save_file(self.file_path)
        fd.Destroy()

    def on_close(self, event): # wxGlade: AppFrame.<event_handler>
        if self.session == None:
            return
        if self.close_confirm():
            self.clear_list()
            self.file_path = None
            self.modified = False
            self.enable_menu_items(False)
            self.session = None

    def on_exit(self, event): # wxGlade: AppFrame.<event_handler>
        self.Close(False)

    def on_delete(self, event): # wxGlade: AppFrame.<event_handler>
        lst = self.session_list
        if lst == None:
            return
        selection = lst.get_selection()
        if len(lst.get_selection()) == 0:
            warning(self, NO_SELECTION_MSG)
            return

        if len(selection) == 1:
            items = 'this item'
        else:
            items = 'these items'
        d = wx.MessageDialog(self, "This operation is not reversible.  Do "\
                             "you still want to delete %s?" % items,
                             style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)

        cancelled = (d.ShowModal() == wx.ID_NO)
        d.Destroy()
        if cancelled:
            return

        try:
            for entry in selection:
                FFSE.firefox.session_remove_entry(self.session, entry)
            lst.delete_selection()
        except:
            error(self)
            return
        self.modified = True

    def on_about(self, event): # wxGlade: AppFrame.<event_handler>
        d = AboutDialog(self)
        d.ShowModal()
        d.Destroy()

    def on_search_update(self, event): # wxGlade: AppFrame.<event_handler>
        self.run_filter()

    def on_close_window(self, event):
        if self.modified and not self.close_confirm():
            event.Veto()
        else:
            self.Destroy()

    def on_properties(self, event): # wxGlade: AppFrame.<event_handler>
        if self.session_list == None:
            return
        d = PropertiesDialog(self)
        selection = self.session_list.get_selection()
        if len(selection) == 0:
            warning(self, NO_SELECTION_MESSAGE)
            return
        if len(selection) == 1:
            selection = selection[0]
        text = StringIO.StringIO()
        pprint.pprint(selection, stream=text, width=40)
        d.props_text.SetValue(text.getvalue())
        d.ShowModal()
        d.Destroy()

    def on_context_menu(self, event):
        if self.session_list == None:
            return
        selection = self.session_list.get_selection()
        if selection == None:
            return
        
        position = event.GetPosition()
        menu = SessionListContextMenu()
        self.session_list.PopupMenu(menu, position)


    def open_file(self, path):
        """Open the session file into this window."""
        try:
            f = file(path, 'rt')
        except:
            error(self)
            return

        try:
            self.session = FFSE.firefox.session_load(f)
        except:
            error(self)
            f.close()
            return
        f.close()
        self.create_list()
        self.file_path = path
        self.modified = False
        self.enable_menu_items(True)
        self.run_filter()

    def save_file(self, path):
        """Save the current session to a file."""
        try:
            f = file(path, 'wt')
        except:
            error(self)
            return

        try:
            firefox.session_save(self.session, f)
        except:
            error(self)
        f.close()

    def create_list(self):
        """Create a new session list out of self.session."""
        self.session_list = SessionListCtrl(self.content_panel)
        self.session_list.fill(self.session)

        sizer = self.content_panel.GetSizer()
        sizer.Clear(False)
        sizer.Add(self.session_list, 1, wx.EXPAND | wx.ADJUST_MINSIZE)
        sizer.Layout()
        self.no_content_label.Hide()

        self.delete_button.Enable()
        self.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.on_context_menu,
                  self.session_list)

    def clear_list(self):
        """Clear out the list, blowing away the current session data."""
        self.delete_button.Disable()
        self.Unbind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.session_list)

        sizer = self.content_panel.GetSizer()
        sizer.Clear(True)
        sizer.Add(self.no_content_label, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        self.no_content_label.Show()
        sizer.Layout()
        self.session_list = None

    def run_filter(self):
        """Filter the list based on the search field."""
        if self.session_list != None:
            string = self.search_field.GetValue()
            col = self.search_choice.GetSelection()
            self.session_list.filter(string, col)

# end of class AppFrame


class FFSEApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        app_frame = AppFrame(None, -1, "")
        self.SetTopWindow(app_frame)
        app_frame.Show()
        return 1

# end of class FFSEApp

class SessionListContextMenu(wx.Menu):
    def __init__(self):
        wx.Menu.__init__(self)
        self.Append(wx.ID_PROPERTIES, "&Properties", "", wx.ITEM_NORMAL)
        self.AppendSeparator()
        self.Append(wx.ID_DELETE, "&Delete", "", wx.ITEM_NORMAL)


class SessionListCtrl(wx.ListCtrl,
                      wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin,
                      wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1,
                             style=wx.LC_REPORT|wx.LC_VIRTUAL)
        wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, numColumns=3)

        self.InsertColumn(0, 'Title')
        self.SetColumnWidth(0, 230)
        self.InsertColumn(1, 'URL')
        self.SetColumnWidth(1, 250)
        self.InsertColumn(2, 'ID')
        self.SetItemCount(0)

        # Original entries, with the same index as realDataMap.
        self.entries      = {}

        # Store list data here. { index: (col1, col2, col3), ... }
        self.realDataMap  = {}
        # A copy of realDataMap with only alphanumerics for sorting.
        self.itemDataMap  = {}
        # Map a list index to a realDataMap index.
        self.itemIndexMap = []

        # Backup copies of realDataMap and itemDataMap, which get erased by
        # filtering:
        self.original_cols       = {}
        self.original_alpha_cols = {}

    def GetListCtrl(self):
        return self

    def OnGetItemText(self, item, col):
        index = self.itemIndexMap[item]
        text = self.realDataMap[index][col]
        if text == None:
            if col == 0:
                return u'(No title)'
            elif col == 1:
                return u'(No URL)'
        else:
            return unicode(text)

    def SortItems(self, sorter=cmp):
        items = list(self.itemDataMap.keys())
        items.sort(sorter)
        self.itemIndexMap = items
        self.SetItemCount(len(self.itemDataMap))
        self.Refresh()
        # TODO: Update the selection, and ensure its visibility

    def fill(self, data):
        """Fill the list with session data."""
        try:
            entries = FFSE.firefox.session_extract_entries(data)
            for e in entries:
                index = len(self.itemDataMap)
                title = e.get('title')
                url   = e.get('url')
                id    = e.get('ID')
                self.entries[index]     = e
                self.realDataMap[index] = (title, url, id)
                self.itemDataMap[index] = (filter_alnum(title),
                                           filter_alnum(url),
                                           id)
                self.original_cols[index]       = self.realDataMap[index]
                self.original_alpha_cols[index] = self.itemDataMap[index]
        except:
            error(self)
        self.itemIndexMap = self.itemDataMap.keys()
        self.SetItemCount(len(self.itemDataMap))
        self.SortListItems(0, 1)    # column 0, ascending order (1)
        self.Refresh()

    def delete_selection(self):
        did_anything = False

        selection = self.GetFirstSelected()
        while selection != -1:
            self.Select(selection, False)

            index = self.itemIndexMap[selection]
            entry = self.entries[index]

            del self.entries[index]
            del self.realDataMap[index]
            del self.itemDataMap[index]
            del self.original_cols[index]
            del self.original_alpha_cols[index]
            self.itemIndexMap.remove(index)

            did_anything = True
            selection = self.GetFirstSelected()
        # end while

        if did_anything:
            self.SetItemCount(len(self.itemDataMap))
            self.Refresh()

    def get_selection_indices(self):
        """Return the wx.ListCtrl indices of the selection."""
        result = []
        selection = self.GetFirstSelected()
        while selection != -1:
            result.append(selection)
            selection = self.GetNextSelected(selection)
        return result

    def get_selection(self):
        """Return the entry values currently selected."""
        result = []
        selection = self.get_selection_indices()
        for list_index in selection:
            entry_index = self.itemIndexMap[list_index]
            result.append(self.entries[entry_index])
        return result

    def filter(self, string, col):
        """Filter the list to match a string on a given column."""
        # Map selected entry-indices to list-indices.
        old_selection = {}
        for i in self.get_selection_indices():
            old_selection[self.itemIndexMap[i]] = i

        self.realDataMap.clear()
        self.itemDataMap.clear()
        pattern = string.lower()
        for index, row in self.original_cols.items():
            if pattern in unicode(row[col]).lower():
                self.realDataMap[index] = self.original_cols[index]
                self.itemDataMap[index] = self.original_alpha_cols[index]
                visible = True
            else: # Remove a filtered entry from the selection.
                if index in old_selection:
                    self.Select(old_selection[index], False)


        self.SortListItems()
        

if __name__ == "__main__":
    ffse = FFSEApp(0)
    ffse.MainLoop()
