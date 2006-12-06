"""
$Id: __init__.py 3967 2006-01-26 19:06:28Z sidnei $
"""

from zope.publisher.interfaces.browser import IBrowserRequest
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class layer(IBrowserRequest):
    """The `snap` layer."""

class Snap(layer, IDefaultBrowserLayer):
    """The `snap` skin.

    It is available via `++skin++snap`.
    """
