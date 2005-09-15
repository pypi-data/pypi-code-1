'''tzinfo timezone information for America/Godthab.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Godthab(DstTzInfo):
    '''America/Godthab timezone definition. See datetime.tzinfo for details'''

    zone = 'America/Godthab'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1916,7,28,3,26,56),
d(1980,4,6,5,0,0),
d(1980,9,28,1,0,0),
d(1981,3,29,1,0,0),
d(1981,9,27,1,0,0),
d(1982,3,28,1,0,0),
d(1982,9,26,1,0,0),
d(1983,3,27,1,0,0),
d(1983,9,25,1,0,0),
d(1984,3,25,1,0,0),
d(1984,9,30,1,0,0),
d(1985,3,31,1,0,0),
d(1985,9,29,1,0,0),
d(1986,3,30,1,0,0),
d(1986,9,28,1,0,0),
d(1987,3,29,1,0,0),
d(1987,9,27,1,0,0),
d(1988,3,27,1,0,0),
d(1988,9,25,1,0,0),
d(1989,3,26,1,0,0),
d(1989,9,24,1,0,0),
d(1990,3,25,1,0,0),
d(1990,9,30,1,0,0),
d(1991,3,31,1,0,0),
d(1991,9,29,1,0,0),
d(1992,3,29,1,0,0),
d(1992,9,27,1,0,0),
d(1993,3,28,1,0,0),
d(1993,9,26,1,0,0),
d(1994,3,27,1,0,0),
d(1994,9,25,1,0,0),
d(1995,3,26,1,0,0),
d(1995,9,24,1,0,0),
d(1996,3,31,1,0,0),
d(1996,10,27,1,0,0),
d(1997,3,30,1,0,0),
d(1997,10,26,1,0,0),
d(1998,3,29,1,0,0),
d(1998,10,25,1,0,0),
d(1999,3,28,1,0,0),
d(1999,10,31,1,0,0),
d(2000,3,26,1,0,0),
d(2000,10,29,1,0,0),
d(2001,3,25,1,0,0),
d(2001,10,28,1,0,0),
d(2002,3,31,1,0,0),
d(2002,10,27,1,0,0),
d(2003,3,30,1,0,0),
d(2003,10,26,1,0,0),
d(2004,3,28,1,0,0),
d(2004,10,31,1,0,0),
d(2005,3,27,1,0,0),
d(2005,10,30,1,0,0),
d(2006,3,26,1,0,0),
d(2006,10,29,1,0,0),
d(2007,3,25,1,0,0),
d(2007,10,28,1,0,0),
d(2008,3,30,1,0,0),
d(2008,10,26,1,0,0),
d(2009,3,29,1,0,0),
d(2009,10,25,1,0,0),
d(2010,3,28,1,0,0),
d(2010,10,31,1,0,0),
d(2011,3,27,1,0,0),
d(2011,10,30,1,0,0),
d(2012,3,25,1,0,0),
d(2012,10,28,1,0,0),
d(2013,3,31,1,0,0),
d(2013,10,27,1,0,0),
d(2014,3,30,1,0,0),
d(2014,10,26,1,0,0),
d(2015,3,29,1,0,0),
d(2015,10,25,1,0,0),
d(2016,3,27,1,0,0),
d(2016,10,30,1,0,0),
d(2017,3,26,1,0,0),
d(2017,10,29,1,0,0),
d(2018,3,25,1,0,0),
d(2018,10,28,1,0,0),
d(2019,3,31,1,0,0),
d(2019,10,27,1,0,0),
d(2020,3,29,1,0,0),
d(2020,10,25,1,0,0),
d(2021,3,28,1,0,0),
d(2021,10,31,1,0,0),
d(2022,3,27,1,0,0),
d(2022,10,30,1,0,0),
d(2023,3,26,1,0,0),
d(2023,10,29,1,0,0),
d(2024,3,31,1,0,0),
d(2024,10,27,1,0,0),
d(2025,3,30,1,0,0),
d(2025,10,26,1,0,0),
d(2026,3,29,1,0,0),
d(2026,10,25,1,0,0),
d(2027,3,28,1,0,0),
d(2027,10,31,1,0,0),
d(2028,3,26,1,0,0),
d(2028,10,29,1,0,0),
d(2029,3,25,1,0,0),
d(2029,10,28,1,0,0),
d(2030,3,31,1,0,0),
d(2030,10,27,1,0,0),
d(2031,3,30,1,0,0),
d(2031,10,26,1,0,0),
d(2032,3,28,1,0,0),
d(2032,10,31,1,0,0),
d(2033,3,27,1,0,0),
d(2033,10,30,1,0,0),
d(2034,3,26,1,0,0),
d(2034,10,29,1,0,0),
d(2035,3,25,1,0,0),
d(2035,10,28,1,0,0),
d(2036,3,30,1,0,0),
d(2036,10,26,1,0,0),
d(2037,3,29,1,0,0),
d(2037,10,25,1,0,0),
        ]

    _transition_info = [
i(-12420,0,'LMT'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
i(-7200,3600,'WGST'),
i(-10800,0,'WGT'),
        ]

Godthab = Godthab()

