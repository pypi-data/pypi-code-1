# -*- coding: utf-8 -*-
# PyTils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
#
# http://gorod-omsk.ru/blog/pythy/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Helpers for templatetags' unit tests in Django webframework
"""

__id__ = __revision__ = "$Id: helpers.py 76 2007-02-27 15:38:53Z the.pythy $"
__url__ = "$URL: https://pythy.googlecode.com/svn/trunk/pytils/pytils/test/templatetags/helpers.py $"

from django.conf import settings

settings.configure(
    TEMPLATE_DIRS=(),
    TEMPLATE_CONTEXT_PROCESSORS=(),
    TEMPLATE_LOADERS=(),
    INSTALLED_APPS=('pytils',),
)

from django import template
from django.template import loader

import unittest


class TemplateTagTestCase(unittest.TestCase):
    """
    TestCase for testing template tags and filters
    """
    def check_template_tag(self, template_name, template_string, context, result_string):
        """
        Method validates output of template tag or filter
        
        @param template_name: name of template
        @type template_name: C{str}
        
        @param template_string: contents of template
        @type template_string: C{str}

        @param context: rendering context
        @type context: C{dict}

        @param result_string: reference output
        @type result_string: C{str}
        """
        
        def test_template_loader(template_name, template_dirs=None):
            return template_string, template_name
        
        loader.template_source_loaders = [test_template_loader,]
        
        output = loader.get_template(template_name).render(template.Context(context))
        
        self.assertEquals(output, result_string)
