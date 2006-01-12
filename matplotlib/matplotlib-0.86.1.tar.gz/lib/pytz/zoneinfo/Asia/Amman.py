'''tzinfo timezone information for Asia/Amman.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Amman(DstTzInfo):
    '''Asia/Amman timezone definition. See datetime.tzinfo for details'''

    _zone = 'Asia/Amman'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1930,12,31,21,36,16),
d(1973,6,5,22,0,0),
d(1973,9,30,21,0,0),
d(1974,4,30,22,0,0),
d(1974,9,30,21,0,0),
d(1975,4,30,22,0,0),
d(1975,9,30,21,0,0),
d(1976,4,30,22,0,0),
d(1976,10,31,21,0,0),
d(1977,4,30,22,0,0),
d(1977,9,30,21,0,0),
d(1978,4,29,22,0,0),
d(1978,9,29,21,0,0),
d(1985,3,31,22,0,0),
d(1985,9,30,21,0,0),
d(1986,4,3,22,0,0),
d(1986,10,2,21,0,0),
d(1987,4,2,22,0,0),
d(1987,10,1,21,0,0),
d(1988,3,31,22,0,0),
d(1988,10,6,21,0,0),
d(1989,5,7,22,0,0),
d(1989,10,5,21,0,0),
d(1990,4,26,22,0,0),
d(1990,10,4,21,0,0),
d(1991,4,16,22,0,0),
d(1991,9,26,21,0,0),
d(1992,4,9,22,0,0),
d(1992,10,1,21,0,0),
d(1993,4,1,22,0,0),
d(1993,9,30,21,0,0),
d(1994,3,31,22,0,0),
d(1994,9,15,21,0,0),
d(1995,4,6,22,0,0),
d(1995,9,14,22,0,0),
d(1996,4,4,22,0,0),
d(1996,9,19,22,0,0),
d(1997,4,3,22,0,0),
d(1997,9,18,22,0,0),
d(1998,4,2,22,0,0),
d(1998,9,17,22,0,0),
d(1999,6,30,22,0,0),
d(1999,9,29,22,0,0),
d(2000,3,29,22,0,0),
d(2000,9,27,22,0,0),
d(2001,3,28,22,0,0),
d(2001,9,26,22,0,0),
d(2002,3,27,22,0,0),
d(2002,9,25,22,0,0),
d(2003,3,26,22,0,0),
d(2003,9,24,22,0,0),
d(2004,3,24,22,0,0),
d(2004,9,29,22,0,0),
d(2005,3,30,22,0,0),
d(2005,9,28,22,0,0),
d(2006,3,29,22,0,0),
d(2006,9,27,22,0,0),
d(2007,3,28,22,0,0),
d(2007,9,26,22,0,0),
d(2008,3,26,22,0,0),
d(2008,9,24,22,0,0),
d(2009,3,25,22,0,0),
d(2009,9,23,22,0,0),
d(2010,3,24,22,0,0),
d(2010,9,29,22,0,0),
d(2011,3,30,22,0,0),
d(2011,9,28,22,0,0),
d(2012,3,28,22,0,0),
d(2012,9,26,22,0,0),
d(2013,3,27,22,0,0),
d(2013,9,25,22,0,0),
d(2014,3,26,22,0,0),
d(2014,9,24,22,0,0),
d(2015,3,25,22,0,0),
d(2015,9,23,22,0,0),
d(2016,3,30,22,0,0),
d(2016,9,28,22,0,0),
d(2017,3,29,22,0,0),
d(2017,9,27,22,0,0),
d(2018,3,28,22,0,0),
d(2018,9,26,22,0,0),
d(2019,3,27,22,0,0),
d(2019,9,25,22,0,0),
d(2020,3,25,22,0,0),
d(2020,9,23,22,0,0),
d(2021,3,24,22,0,0),
d(2021,9,29,22,0,0),
d(2022,3,30,22,0,0),
d(2022,9,28,22,0,0),
d(2023,3,29,22,0,0),
d(2023,9,27,22,0,0),
d(2024,3,27,22,0,0),
d(2024,9,25,22,0,0),
d(2025,3,26,22,0,0),
d(2025,9,24,22,0,0),
d(2026,3,25,22,0,0),
d(2026,9,23,22,0,0),
d(2027,3,24,22,0,0),
d(2027,9,29,22,0,0),
d(2028,3,29,22,0,0),
d(2028,9,27,22,0,0),
d(2029,3,28,22,0,0),
d(2029,9,26,22,0,0),
d(2030,3,27,22,0,0),
d(2030,9,25,22,0,0),
d(2031,3,26,22,0,0),
d(2031,9,24,22,0,0),
d(2032,3,24,22,0,0),
d(2032,9,29,22,0,0),
d(2033,3,30,22,0,0),
d(2033,9,28,22,0,0),
d(2034,3,29,22,0,0),
d(2034,9,27,22,0,0),
d(2035,3,28,22,0,0),
d(2035,9,26,22,0,0),
d(2036,3,26,22,0,0),
d(2036,9,24,22,0,0),
d(2037,3,25,22,0,0),
d(2037,9,23,22,0,0),
        ]

    _transition_info = [
i(8640,0,'LMT'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
i(10800,3600,'EEST'),
i(7200,0,'EET'),
        ]

Amman = Amman()

