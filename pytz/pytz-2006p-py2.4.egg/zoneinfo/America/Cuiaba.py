'''tzinfo timezone information for America/Cuiaba.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Cuiaba(DstTzInfo):
    '''America/Cuiaba timezone definition. See datetime.tzinfo for details'''

    zone = 'America/Cuiaba'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1914,1,1,3,44,20),
d(1931,10,3,15,0,0),
d(1932,4,1,3,0,0),
d(1932,10,3,4,0,0),
d(1933,4,1,3,0,0),
d(1949,12,1,4,0,0),
d(1950,4,16,4,0,0),
d(1950,12,1,4,0,0),
d(1951,4,1,3,0,0),
d(1951,12,1,4,0,0),
d(1952,4,1,3,0,0),
d(1952,12,1,4,0,0),
d(1953,3,1,3,0,0),
d(1963,12,9,4,0,0),
d(1964,3,1,3,0,0),
d(1965,1,31,4,0,0),
d(1965,3,31,3,0,0),
d(1965,12,1,4,0,0),
d(1966,3,1,3,0,0),
d(1966,11,1,4,0,0),
d(1967,3,1,3,0,0),
d(1967,11,1,4,0,0),
d(1968,3,1,3,0,0),
d(1985,11,2,4,0,0),
d(1986,3,15,3,0,0),
d(1986,10,25,4,0,0),
d(1987,2,14,3,0,0),
d(1987,10,25,4,0,0),
d(1988,2,7,3,0,0),
d(1988,10,16,4,0,0),
d(1989,1,29,3,0,0),
d(1989,10,15,4,0,0),
d(1990,2,11,3,0,0),
d(1990,10,21,4,0,0),
d(1991,2,17,3,0,0),
d(1991,10,20,4,0,0),
d(1992,2,9,3,0,0),
d(1992,10,25,4,0,0),
d(1993,1,31,3,0,0),
d(1993,10,17,4,0,0),
d(1994,2,20,3,0,0),
d(1994,10,16,4,0,0),
d(1995,2,19,3,0,0),
d(1995,10,15,4,0,0),
d(1996,2,11,3,0,0),
d(1996,10,6,4,0,0),
d(1997,2,16,3,0,0),
d(1997,10,6,4,0,0),
d(1998,3,1,3,0,0),
d(1998,10,11,4,0,0),
d(1999,2,21,3,0,0),
d(1999,10,3,4,0,0),
d(2000,2,27,3,0,0),
d(2000,10,8,4,0,0),
d(2001,2,18,3,0,0),
d(2001,10,14,4,0,0),
d(2002,2,17,3,0,0),
d(2002,11,3,4,0,0),
d(2003,2,16,3,0,0),
d(2004,11,2,4,0,0),
d(2005,2,20,3,0,0),
d(2005,10,16,4,0,0),
d(2006,2,19,3,0,0),
d(2006,11,5,4,0,0),
d(2007,2,25,3,0,0),
d(2007,11,4,4,0,0),
d(2008,2,24,3,0,0),
d(2008,11,2,4,0,0),
d(2009,2,22,3,0,0),
d(2009,11,1,4,0,0),
d(2010,2,28,3,0,0),
d(2010,11,7,4,0,0),
d(2011,2,27,3,0,0),
d(2011,11,6,4,0,0),
d(2012,2,26,3,0,0),
d(2012,11,4,4,0,0),
d(2013,2,24,3,0,0),
d(2013,11,3,4,0,0),
d(2014,2,23,3,0,0),
d(2014,11,2,4,0,0),
d(2015,2,22,3,0,0),
d(2015,11,1,4,0,0),
d(2016,2,28,3,0,0),
d(2016,11,6,4,0,0),
d(2017,2,26,3,0,0),
d(2017,11,5,4,0,0),
d(2018,2,25,3,0,0),
d(2018,11,4,4,0,0),
d(2019,2,24,3,0,0),
d(2019,11,3,4,0,0),
d(2020,2,23,3,0,0),
d(2020,11,1,4,0,0),
d(2021,2,28,3,0,0),
d(2021,11,7,4,0,0),
d(2022,2,27,3,0,0),
d(2022,11,6,4,0,0),
d(2023,2,26,3,0,0),
d(2023,11,5,4,0,0),
d(2024,2,25,3,0,0),
d(2024,11,3,4,0,0),
d(2025,2,23,3,0,0),
d(2025,11,2,4,0,0),
d(2026,2,22,3,0,0),
d(2026,11,1,4,0,0),
d(2027,2,28,3,0,0),
d(2027,11,7,4,0,0),
d(2028,2,27,3,0,0),
d(2028,11,5,4,0,0),
d(2029,2,25,3,0,0),
d(2029,11,4,4,0,0),
d(2030,2,24,3,0,0),
d(2030,11,3,4,0,0),
d(2031,2,23,3,0,0),
d(2031,11,2,4,0,0),
d(2032,2,29,3,0,0),
d(2032,11,7,4,0,0),
d(2033,2,27,3,0,0),
d(2033,11,6,4,0,0),
d(2034,2,26,3,0,0),
d(2034,11,5,4,0,0),
d(2035,2,25,3,0,0),
d(2035,11,4,4,0,0),
d(2036,2,24,3,0,0),
d(2036,11,2,4,0,0),
d(2037,2,22,3,0,0),
d(2037,11,1,4,0,0),
        ]

    _transition_info = [
i(-13440,0,'LMT'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
i(-14400,0,'AMT'),
i(-10800,3600,'AMST'),
        ]

Cuiaba = Cuiaba()

