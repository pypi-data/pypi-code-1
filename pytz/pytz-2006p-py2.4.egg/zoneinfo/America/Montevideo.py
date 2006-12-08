'''tzinfo timezone information for America/Montevideo.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Montevideo(DstTzInfo):
    '''America/Montevideo timezone definition. See datetime.tzinfo for details'''

    zone = 'America/Montevideo'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1920,5,1,3,44,44),
d(1923,10,2,3,30,0),
d(1924,4,1,3,0,0),
d(1924,10,1,3,30,0),
d(1925,4,1,3,0,0),
d(1925,10,1,3,30,0),
d(1926,4,1,3,0,0),
d(1933,10,29,3,30,0),
d(1934,4,1,3,0,0),
d(1934,10,28,3,30,0),
d(1935,3,31,3,0,0),
d(1935,10,27,3,30,0),
d(1936,3,29,3,0,0),
d(1936,11,1,3,30,0),
d(1937,3,28,3,0,0),
d(1937,10,31,3,30,0),
d(1938,3,27,3,0,0),
d(1938,10,30,3,30,0),
d(1939,3,26,3,0,0),
d(1939,10,29,3,30,0),
d(1940,3,31,3,0,0),
d(1940,10,27,3,30,0),
d(1941,3,30,3,0,0),
d(1941,8,1,3,30,0),
d(1942,1,1,3,0,0),
d(1942,12,14,3,30,0),
d(1943,3,14,2,0,0),
d(1959,5,24,3,0,0),
d(1959,11,15,2,0,0),
d(1960,1,17,3,0,0),
d(1960,3,6,2,0,0),
d(1965,4,4,3,0,0),
d(1965,9,26,2,0,0),
d(1966,4,3,3,0,0),
d(1966,10,31,2,0,0),
d(1967,4,2,3,0,0),
d(1967,10,31,2,0,0),
d(1968,5,27,3,0,0),
d(1968,12,2,2,30,0),
d(1969,5,27,3,0,0),
d(1969,12,2,2,30,0),
d(1970,5,27,3,0,0),
d(1970,12,2,2,30,0),
d(1972,4,24,3,0,0),
d(1972,8,15,2,0,0),
d(1974,3,10,3,0,0),
d(1974,12,22,2,30,0),
d(1976,10,1,2,0,0),
d(1977,12,4,3,0,0),
d(1978,4,1,2,0,0),
d(1979,10,1,3,0,0),
d(1980,5,1,2,0,0),
d(1987,12,14,3,0,0),
d(1988,3,14,2,0,0),
d(1988,12,11,3,0,0),
d(1989,3,12,2,0,0),
d(1989,10,29,3,0,0),
d(1990,3,4,2,0,0),
d(1990,10,21,3,0,0),
d(1991,3,3,2,0,0),
d(1991,10,27,3,0,0),
d(1992,3,1,2,0,0),
d(1992,10,18,3,0,0),
d(1993,2,28,2,0,0),
d(2004,9,19,3,0,0),
d(2005,3,27,4,0,0),
d(2005,10,9,5,0,0),
d(2006,3,12,4,0,0),
d(2006,10,1,5,0,0),
d(2007,3,11,4,0,0),
d(2007,10,7,5,0,0),
d(2008,3,9,4,0,0),
d(2008,10,5,5,0,0),
d(2009,3,8,4,0,0),
d(2009,10,4,5,0,0),
d(2010,3,14,4,0,0),
d(2010,10,3,5,0,0),
d(2011,3,13,4,0,0),
d(2011,10,2,5,0,0),
d(2012,3,11,4,0,0),
d(2012,10,7,5,0,0),
d(2013,3,10,4,0,0),
d(2013,10,6,5,0,0),
d(2014,3,9,4,0,0),
d(2014,10,5,5,0,0),
d(2015,3,8,4,0,0),
d(2015,10,4,5,0,0),
d(2016,3,13,4,0,0),
d(2016,10,2,5,0,0),
d(2017,3,12,4,0,0),
d(2017,10,1,5,0,0),
d(2018,3,11,4,0,0),
d(2018,10,7,5,0,0),
d(2019,3,10,4,0,0),
d(2019,10,6,5,0,0),
d(2020,3,8,4,0,0),
d(2020,10,4,5,0,0),
d(2021,3,14,4,0,0),
d(2021,10,3,5,0,0),
d(2022,3,13,4,0,0),
d(2022,10,2,5,0,0),
d(2023,3,12,4,0,0),
d(2023,10,1,5,0,0),
d(2024,3,10,4,0,0),
d(2024,10,6,5,0,0),
d(2025,3,9,4,0,0),
d(2025,10,5,5,0,0),
d(2026,3,8,4,0,0),
d(2026,10,4,5,0,0),
d(2027,3,14,4,0,0),
d(2027,10,3,5,0,0),
d(2028,3,12,4,0,0),
d(2028,10,1,5,0,0),
d(2029,3,11,4,0,0),
d(2029,10,7,5,0,0),
d(2030,3,10,4,0,0),
d(2030,10,6,5,0,0),
d(2031,3,9,4,0,0),
d(2031,10,5,5,0,0),
d(2032,3,14,4,0,0),
d(2032,10,3,5,0,0),
d(2033,3,13,4,0,0),
d(2033,10,2,5,0,0),
d(2034,3,12,4,0,0),
d(2034,10,1,5,0,0),
d(2035,3,11,4,0,0),
d(2035,10,7,5,0,0),
d(2036,3,9,4,0,0),
d(2036,10,5,5,0,0),
d(2037,3,8,4,0,0),
d(2037,10,4,5,0,0),
        ]

    _transition_info = [
i(-13500,0,'MMT'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-10800,1800,'UYHST'),
i(-12600,0,'UYT'),
i(-7200,5400,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-9000,1800,'UYHST'),
i(-10800,0,'UYT'),
i(-9000,1800,'UYHST'),
i(-10800,0,'UYT'),
i(-9000,1800,'UYHST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-9000,1800,'UYHST'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
i(-10800,0,'UYT'),
i(-7200,3600,'UYST'),
        ]

Montevideo = Montevideo()

