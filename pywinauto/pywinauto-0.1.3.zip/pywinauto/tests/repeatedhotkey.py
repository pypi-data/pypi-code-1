# GUI Application automation and testing library
# Copyright (C) 2006 Mark Mc Mahon
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
#    Free Software Foundation, Inc.,
#    59 Temple Place,
#    Suite 330,
#    Boston, MA 02111-1307 USA

"""Repeated Hotkeys Test

**What is checked**
This test checks all the controls in a dialog to see if there are controls that
use the same hotkey character.

**How is it checked**
A list of all the hotkeys (converted to uppercase) used in the dialog is
created. Then this list is examined to see if any hotkeys are used more than
once. If any are used more than once a list of all the controls that use this
hotkey are compiled to be used in the bug report.

**When is a bug reported**
If more than one control has the same hotkey then a bug is reported.

**Bug Extra Information**
The bug contains the following extra information
Name	Description
RepeatedHotkey	This is the hotkey that is repeated between the 2 controls
converted to uppercase, String
CharsUsedInDialog	This is a list of all the hotkeys used in the dialog,
String
AllCharsInDialog	This is a list of all the characters in the dialog for
controls that have a hotkeys, String
AvailableInControlS	A list of the available characters for each control.
Any of the characters in this list could be used as the new hotkey without
conflicting with any existing hotkey.

**Is Reference dialog needed**
The reference dialog does not need to be available. If it is available then
for each bug discovered it is checked to see if it is a problem in the
reference dialog.
NOTE: Checking the reference dialog is not so exact here! Only when the
equivalent controls in the reference dialog all have the hotkeys will it be
reported as being in the reference also. I.e. if there are 3 controls with the
same hotkey in the Localised software  then those same controls in the
reference dialog must have the same hotkey for it to be reported as existing
in the reference also.

**False positive bug reports**
There should be very few false positives from this test. Sometimes a control
only has one or 2 characters eg "X:" and it is impossible to avoid a hotkey
clash. Also for Asian languages hotkeys should be the same as the US software
so probably this test should be run on those languages.

**Test Identifier**
The identifier for this test/bug is "RepeatedHotkey"
"""

testname = "RepeatedHotkey"
__revision__ = "$Revision: 189 $"

from pywinauto.win32defines import SS_NOPREFIX

#-----------------------------------------------------------------------------
def RepeatedHotkeyTest(windows):
    "Return the repeated hotkey errors"

    hotkeyControls, allChars, hotkeys = _CollectDialogInfo(windows)

    # get the available characters in the dialog
    dlgAvailable = allChars.difference(hotkeys)

    # remove some characters that aren't good choices for hotkeys
    dlgAvailable.difference_update(set("-& _"))


    bugs = []
    # for each hotkey
    for char, controls in hotkeyControls.items():

        # if there is more than one control associated then it is a bug
        if len(controls) > 1:

            ctrlsAvailableChars = ""

            # build up the available characters for each control
            for ctrl in controls:
                controlChars = ""
                controlChars = set(ctrl.Text.lower())

                controlAvailableChars = controlChars.intersection(dlgAvailable)
                controlAvailableChars = \
                    "<%s>" % _SetAsString(controlAvailableChars)

                ctrlsAvailableChars += controlAvailableChars

            refCtrls = [ctrl.ref for ctrl in controls if ctrl.ref]
            refHotkeyControls, refAllChars, refHotkeys = \
                _CollectDialogInfo(refCtrls)

            isInRef = -1
            if len(refHotkeys) > 1:
                isInRef = 1
            else:
                isInRef = 0

            bugs.append((
                controls,
                {
                    "RepeatedHotkey" : 		char,
                    "CharsUsedInDialog" :   _SetAsString(hotkeys),
                    "AllCharsInDialog" :    _SetAsString(allChars),
                    "AvailableInControls" : ctrlsAvailableChars,
                },
                testname,
                isInRef)
            )

#	# What is the algorithm to try and do all that is necessary to find
#	# if it is possible to get a fix character if none of the current
#	# characters are free
#	for bug in bugs:
#		for c, chars in bug.bugData:
#			# control has no possibilities
#			if not chars:
#				# check if there are any other hotkey controls
#				# in the dialog that could be used
#				others = set(c.Title.lower()).intersection(unUsedChars)


    return  bugs



#-----------------------------------------------------------------------------
def _CollectDialogInfo(windows):
    "Collect information on the hotkeys in the dialog"
    hotkeyControls = {}
    allChars = ''

    for win in windows:
        # skip it if it doesn't implement hotkey functionality
        if not ImplementsHotkey(win):
            continue

        # get the hotkey
        pos, char = GetHotkey(win.Text)

        # if no hotkey for this control
        # then continue
        if not char:
            continue

        # store hotkey with list of used hotkeys
        # map this hotkey to the list of controls that have it
        hotkeyControls.setdefault(char.lower(), []).append(win)


        # Add the title of this control to the list of available
        # characters for the dialog
        allChars += win.Text.lower()


    allChars = set(allChars)
    hotkeys = set(hotkeyControls.keys())

    return hotkeyControls, allChars, hotkeys


#-----------------------------------------------------------------------------
# get hokey position
def GetHotkey(text):
    "Return the position and character of the hotkey"

    # find the last & character that is not followed
    # by & or by the end of the string

    curEnd = len(text) + 1
    text = text.replace("&&", "__")
    while True:
        pos = text.rfind("&", 0, curEnd)

        # One found was at the end of the text or
        # no (more) & were found
        # so return the None value
        if pos == -1 or pos == len(text):
            return (-1, '')

        # One found but was prededed by non valid hotkey character
        # so continue, as that can't be a shortcut
        if text[pos - 1] == '&':
            curEnd = pos - 2
            continue

        # 2 ampersands in a row - so skip
        # the 1st one and continue
        return (pos, text[pos+1])



#-----------------------------------------------------------------------------
def _SetAsString(settojoin):
    "Convert the set to a ordered string"
    return "".join(sorted(settojoin))


#-----------------------------------------------------------------------------
def ImplementsHotkey(win):
    "checks whether a control interprets & character to be a hotkey"

    # buttons always implement hotkey
    if win.Class == "Button":
        return True

    # Statics do if they don't have SS_NOPREFIX style
    elif win.Class == "Static" and not win.HasStyle(SS_NOPREFIX):
        return True

    if win.Class == "MenuItem" and win.State != "2048":
        return True

    # Most controls don't - so just return false if
    # neither of the above condition hold
    return False


RepeatedHotkeyTest.TestsMenus = True

