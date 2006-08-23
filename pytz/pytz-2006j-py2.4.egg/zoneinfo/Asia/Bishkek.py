'''tzinfo timezone information for Asia/Bishkek.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Bishkek(DstTzInfo):
    '''Asia/Bishkek timezone definition. See datetime.tzinfo for details'''

    zone = 'Asia/Bishkek'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1924,5,1,19,1,36),
d(1930,6,20,19,0,0),
d(1981,3,31,18,0,0),
d(1981,9,30,17,0,0),
d(1982,3,31,18,0,0),
d(1982,9,30,17,0,0),
d(1983,3,31,18,0,0),
d(1983,9,30,17,0,0),
d(1984,3,31,18,0,0),
d(1984,9,29,20,0,0),
d(1985,3,30,20,0,0),
d(1985,9,28,20,0,0),
d(1986,3,29,20,0,0),
d(1986,9,27,20,0,0),
d(1987,3,28,20,0,0),
d(1987,9,26,20,0,0),
d(1988,3,26,20,0,0),
d(1988,9,24,20,0,0),
d(1989,3,25,20,0,0),
d(1989,9,23,20,0,0),
d(1990,3,24,20,0,0),
d(1990,9,29,20,0,0),
d(1991,3,30,20,0,0),
d(1991,8,30,20,0,0),
d(1992,4,11,19,0,0),
d(1992,9,26,18,0,0),
d(1993,4,10,19,0,0),
d(1993,9,25,18,0,0),
d(1994,4,9,19,0,0),
d(1994,9,24,18,0,0),
d(1995,4,8,19,0,0),
d(1995,9,23,18,0,0),
d(1996,4,6,19,0,0),
d(1996,9,28,18,0,0),
d(1997,3,29,21,30,0),
d(1997,10,25,20,30,0),
d(1998,3,28,21,30,0),
d(1998,10,24,20,30,0),
d(1999,3,27,21,30,0),
d(1999,10,30,20,30,0),
d(2000,3,25,21,30,0),
d(2000,10,28,20,30,0),
d(2001,3,24,21,30,0),
d(2001,10,27,20,30,0),
d(2002,3,30,21,30,0),
d(2002,10,26,20,30,0),
d(2003,3,29,21,30,0),
d(2003,10,25,20,30,0),
d(2004,3,27,21,30,0),
d(2004,10,30,20,30,0),
d(2005,3,26,21,30,0),
d(2005,8,11,18,0,0),
        ]

    _transition_info = [
i(17880,0,'LMT'),
i(18000,0,'FRUT'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(25200,3600,'FRUST'),
i(21600,0,'FRUT'),
i(21600,0,'FRUST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(18000,0,'KGT'),
i(21600,3600,'KGST'),
i(21600,0,'KGT'),
        ]

Bishkek = Bishkek()

