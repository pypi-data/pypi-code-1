"""
$Id: exceptions.py 4380 2006-03-16 14:21:05Z sidnei $
"""

import sys
import traceback
from types import StringTypes

from zope.exceptions.exceptionformatter import format_exception
from zope.interface.common.interfaces import IException

__metaclass__ = type


class NotFoundView:

    def __init__(self, context, request):
        self.context = context
        self.request = request
        if hasattr(context, 'args'):
            self.target_object, self.target_name = context.args
        else:
            # zope.publisher.interfaces.NotFound
            self.target_name = context.getName()
            self.target_object = context.getObject()

    def __call__(self, *args, **kw):
        self.request.response.setStatus(404)
        return self.index(*args, **kw)

class ExceptionDebugView:
    """ Render exceptions for debugging."""

    def __init__(self, context, request):

        self.context = context
        self.request = request

        self.error_type, self.error_object, tb = info = sys.exc_info()

        try:
            strtype = str(getattr(info[0], '__name__', info[0]))

            if not isinstance(info[2], StringTypes):
                self.tb_text = ''.join(
                        format_exception(*info, **{'as_html': 0}))
                self.tb_html = ''.join(
                    format_exception(*info, **{'as_html': 1}))
            else:
                self.tb_text = info[2]
        except:
            try:
                self.tb_lines = traceback.format_tb(tb)
            finally:
                del tb

        info = None

    def __call__(self, *args, **kw):
        self.request.response.setStatus(500)
        return self.index(*args, **kw)
