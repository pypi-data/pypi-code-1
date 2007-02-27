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
Unit tests for pytils' dt templatetags for Django web framework
"""

__id__ = __revision__ = "$Id: test_dt.py 76 2007-02-27 15:38:53Z the.pythy $"
__url__ = "$URL: https://pythy.googlecode.com/svn/trunk/pytils/pytils/test/templatetags/test_dt.py $"

import datetime
from pytils.test.templatetags import helpers

class DtDefaultTestCase(helpers.TemplateTagTestCase):
    
    def setUp(self):
        self.date = datetime.datetime(2007, 1, 26, 15, 50)
        self.date_before = datetime.datetime.now() - datetime.timedelta(1, 2000)
    
    def test_load(self):
        self.check_template_tag('load_tag', '{% load pytils_dt %}', {}, '')
    
    def test_ru_strftime_filter(self):
        self.check_template_tag('ru_strftime_filter', 
            '{% load pytils_dt %}{{ val|ru_strftime:"%d %B %Y, %A" }}', 
            {'val': self.date},
            '26 января 2007, пятница')
    
    def test_ru_strftime_inflected_filter(self):
        self.check_template_tag('ru_strftime_inflected_filter', 
            '{% load pytils_dt %}{{ val|ru_strftime_inflected:"в %A, %d %B %Y" }}', 
            {'val': self.date},
            'в пятницу, 26 января 2007')
    
    def test_distance_filter(self):
        self.check_template_tag('distance_filter', 
            '{% load pytils_dt %}{{ val|distance_of_time }}', 
            {'val': self.date_before},
            'вчера')
        
        self.check_template_tag('distance_filter', 
            '{% load pytils_dt %}{{ val|distance_of_time:3 }}', 
            {'val': self.date_before},
            '1 день 0 часов 33 минуты назад')
    
    # без отладки, если ошибка -- по умолчанию пустая строка
    def test_ru_strftime_error(self):
        self.check_template_tag('ru_strftime_error', 
            '{% load pytils_dt %}{{ val|ru_strftime:"%d %B %Y" }}', 
            {'val': 1}, 
            '')


if __name__ == '__main__':
    import unittest
    unittest.main()
