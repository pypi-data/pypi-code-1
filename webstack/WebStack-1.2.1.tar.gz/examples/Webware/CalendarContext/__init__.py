#!/usr/bin/env python

"""
Webware context for the Calendar application (post Webware 0.8.1).
"""

from WebStack.Adapters.Webware import deploy
from Calendar import CalendarResource

# NOTE: Initialising a shared resource.
# Choose or customise one of the following if the example fails.

resource = CalendarResource()
#resource = CalendarResource("iso-8859-1")

urlParser = deploy(resource, handle_errors=1)

# vim: tabstop=4 expandtab shiftwidth=4
