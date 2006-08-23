'''tzinfo timezone information for Navajo.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Navajo(DstTzInfo):
    '''Navajo timezone definition. See datetime.tzinfo for details'''

    zone = 'Navajo'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1918,3,31,9,0,0),
d(1918,10,27,8,0,0),
d(1919,3,30,9,0,0),
d(1919,10,26,8,0,0),
d(1920,3,28,9,0,0),
d(1920,10,31,8,0,0),
d(1921,3,27,9,0,0),
d(1921,5,22,8,0,0),
d(1942,2,9,9,0,0),
d(1945,8,14,23,0,0),
d(1945,9,30,8,0,0),
d(1965,4,25,9,0,0),
d(1965,10,31,8,0,0),
d(1966,4,24,9,0,0),
d(1966,10,30,8,0,0),
d(1967,4,30,9,0,0),
d(1967,10,29,8,0,0),
d(1968,4,28,9,0,0),
d(1968,10,27,8,0,0),
d(1969,4,27,9,0,0),
d(1969,10,26,8,0,0),
d(1970,4,26,9,0,0),
d(1970,10,25,8,0,0),
d(1971,4,25,9,0,0),
d(1971,10,31,8,0,0),
d(1972,4,30,9,0,0),
d(1972,10,29,8,0,0),
d(1973,4,29,9,0,0),
d(1973,10,28,8,0,0),
d(1974,1,6,9,0,0),
d(1974,10,27,8,0,0),
d(1975,2,23,9,0,0),
d(1975,10,26,8,0,0),
d(1976,4,25,9,0,0),
d(1976,10,31,8,0,0),
d(1977,4,24,9,0,0),
d(1977,10,30,8,0,0),
d(1978,4,30,9,0,0),
d(1978,10,29,8,0,0),
d(1979,4,29,9,0,0),
d(1979,10,28,8,0,0),
d(1980,4,27,9,0,0),
d(1980,10,26,8,0,0),
d(1981,4,26,9,0,0),
d(1981,10,25,8,0,0),
d(1982,4,25,9,0,0),
d(1982,10,31,8,0,0),
d(1983,4,24,9,0,0),
d(1983,10,30,8,0,0),
d(1984,4,29,9,0,0),
d(1984,10,28,8,0,0),
d(1985,4,28,9,0,0),
d(1985,10,27,8,0,0),
d(1986,4,27,9,0,0),
d(1986,10,26,8,0,0),
d(1987,4,5,9,0,0),
d(1987,10,25,8,0,0),
d(1988,4,3,9,0,0),
d(1988,10,30,8,0,0),
d(1989,4,2,9,0,0),
d(1989,10,29,8,0,0),
d(1990,4,1,9,0,0),
d(1990,10,28,8,0,0),
d(1991,4,7,9,0,0),
d(1991,10,27,8,0,0),
d(1992,4,5,9,0,0),
d(1992,10,25,8,0,0),
d(1993,4,4,9,0,0),
d(1993,10,31,8,0,0),
d(1994,4,3,9,0,0),
d(1994,10,30,8,0,0),
d(1995,4,2,9,0,0),
d(1995,10,29,8,0,0),
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
d(2001,4,1,9,0,0),
d(2001,10,28,8,0,0),
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
d(2007,3,11,9,0,0),
d(2007,11,4,8,0,0),
d(2008,3,9,9,0,0),
d(2008,11,2,8,0,0),
d(2009,3,8,9,0,0),
d(2009,11,1,8,0,0),
d(2010,3,14,9,0,0),
d(2010,11,7,8,0,0),
d(2011,3,13,9,0,0),
d(2011,11,6,8,0,0),
d(2012,3,11,9,0,0),
d(2012,11,4,8,0,0),
d(2013,3,10,9,0,0),
d(2013,11,3,8,0,0),
d(2014,3,9,9,0,0),
d(2014,11,2,8,0,0),
d(2015,3,8,9,0,0),
d(2015,11,1,8,0,0),
d(2016,3,13,9,0,0),
d(2016,11,6,8,0,0),
d(2017,3,12,9,0,0),
d(2017,11,5,8,0,0),
d(2018,3,11,9,0,0),
d(2018,11,4,8,0,0),
d(2019,3,10,9,0,0),
d(2019,11,3,8,0,0),
d(2020,3,8,9,0,0),
d(2020,11,1,8,0,0),
d(2021,3,14,9,0,0),
d(2021,11,7,8,0,0),
d(2022,3,13,9,0,0),
d(2022,11,6,8,0,0),
d(2023,3,12,9,0,0),
d(2023,11,5,8,0,0),
d(2024,3,10,9,0,0),
d(2024,11,3,8,0,0),
d(2025,3,9,9,0,0),
d(2025,11,2,8,0,0),
d(2026,3,8,9,0,0),
d(2026,11,1,8,0,0),
d(2027,3,14,9,0,0),
d(2027,11,7,8,0,0),
d(2028,3,12,9,0,0),
d(2028,11,5,8,0,0),
d(2029,3,11,9,0,0),
d(2029,11,4,8,0,0),
d(2030,3,10,9,0,0),
d(2030,11,3,8,0,0),
d(2031,3,9,9,0,0),
d(2031,11,2,8,0,0),
d(2032,3,14,9,0,0),
d(2032,11,7,8,0,0),
d(2033,3,13,9,0,0),
d(2033,11,6,8,0,0),
d(2034,3,12,9,0,0),
d(2034,11,5,8,0,0),
d(2035,3,11,9,0,0),
d(2035,11,4,8,0,0),
d(2036,3,9,9,0,0),
d(2036,11,2,8,0,0),
d(2037,3,8,9,0,0),
d(2037,11,1,8,0,0),
        ]

    _transition_info = [
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MDT'),
i(-25200,0,'MST'),
i(-21600,3600,'MWT'),
i(-21600,3600,'MPT'),
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

Navajo = Navajo()

