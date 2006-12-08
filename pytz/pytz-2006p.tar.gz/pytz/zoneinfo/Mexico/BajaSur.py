'''tzinfo timezone information for Mexico/BajaSur.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class BajaSur(DstTzInfo):
    '''Mexico/BajaSur timezone definition. See datetime.tzinfo for details'''

    zone = 'Mexico/BajaSur'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1922,1,1,7,0,0),
d(1927,6,11,6,0,0),
d(1930,11,15,6,0,0),
d(1931,5,2,6,0,0),
d(1931,10,1,6,0,0),
d(1932,4,1,7,0,0),
d(1942,4,24,6,0,0),
d(1949,1,14,7,0,0),
d(1970,1,1,8,0,0),
d(1996,4,7,9,0,0),
d(1996,10,27,8,0,0),
d(1997,4,6,9,0,0),
d(1997,10,26,8,0,0),
d(1998,4,5,9,0,0),
d(1998,10,25,8,0,0),
d(1999,4,4,9,0,0),
d(1999,10,31,8,0,0),
d(2000,4,2,9,0,0),
d(2000,10,29,8,0,0),
d(2001,5,6,9,0,0),
d(2001,9,30,8,0,0),
d(2002,4,7,9,0,0),
d(2002,10,27,8,0,0),
d(2003,4,6,9,0,0),
d(2003,10,26,8,0,0),
d(2004,4,4,9,0,0),
d(2004,10,31,8,0,0),
d(2005,4,3,9,0,0),
d(2005,10,30,8,0,0),
d(2006,4,2,9,0,0),
d(2006,10,29,8,0,0),
d(2007,4,1,9,0,0),
d(2007,10,28,8,0,0),
d(2008,4,6,9,0,0),
d(2008,10,26,8,0,0),
d(2009,4,5,9,0,0),
d(2009,10,25,8,0,0),
d(2010,4,4,9,0,0),
d(2010,10,31,8,0,0),
d(2011,4,3,9,0,0),
d(2011,10,30,8,0,0),
d(2012,4,1,9,0,0),
d(2012,10,28,8,0,0),
d(2013,4,7,9,0,0),
d(2013,10,27,8,0,0),
d(2014,4,6,9,0,0),
d(2014,10,26,8,0,0),
d(2015,4,5,9,0,0),
d(2015,10,25,8,0,0),
d(2016,4,3,9,0,0),
d(2016,10,30,8,0,0),
d(2017,4,2,9,0,0),
d(2017,10,29,8,0,0),
d(2018,4,1,9,0,0),
d(2018,10,28,8,0,0),
d(2019,4,7,9,0,0),
d(2019,10,27,8,0,0),
d(2020,4,5,9,0,0),
d(2020,10,25,8,0,0),
d(2021,4,4,9,0,0),
d(2021,10,31,8,0,0),
d(2022,4,3,9,0,0),
d(2022,10,30,8,0,0),
d(2023,4,2,9,0,0),
d(2023,10,29,8,0,0),
d(2024,4,7,9,0,0),
d(2024,10,27,8,0,0),
d(2025,4,6,9,0,0),
d(2025,10,26,8,0,0),
d(2026,4,5,9,0,0),
d(2026,10,25,8,0,0),
d(2027,4,4,9,0,0),
d(2027,10,31,8,0,0),
d(2028,4,2,9,0,0),
d(2028,10,29,8,0,0),
d(2029,4,1,9,0,0),
d(2029,10,28,8,0,0),
d(2030,4,7,9,0,0),
d(2030,10,27,8,0,0),
d(2031,4,6,9,0,0),
d(2031,10,26,8,0,0),
d(2032,4,4,9,0,0),
d(2032,10,31,8,0,0),
d(2033,4,3,9,0,0),
d(2033,10,30,8,0,0),
d(2034,4,2,9,0,0),
d(2034,10,29,8,0,0),
d(2035,4,1,9,0,0),
d(2035,10,28,8,0,0),
d(2036,4,6,9,0,0),
d(2036,10,26,8,0,0),
d(2037,4,5,9,0,0),
d(2037,10,25,8,0,0),
        ]

    _transition_info = [
i(-25560,0,'LMT'),
i(-25200,0,'MST'),
i(-21600,0,'CST'),
i(-25200,0,'MST'),
i(-21600,0,'CST'),
i(-25200,0,'MST'),
i(-21600,0,'CST'),
i(-25200,0,'MST'),
i(-28800,0,'PST'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
        ]

BajaSur = BajaSur()

