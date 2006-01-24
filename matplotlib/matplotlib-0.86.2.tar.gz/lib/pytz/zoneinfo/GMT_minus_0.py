'''tzinfo timezone information for GMT_minus_0.'''
from pytz.tzinfo import StaticTzInfo
from pytz.tzinfo import memorized_timedelta as timedelta

class GMT_minus_0(StaticTzInfo):
    '''GMT_minus_0 timezone definition. See datetime.tzinfo for details'''
    _zone = 'GMT_minus_0'
    _utcoffset = timedelta(seconds=0)
    _tzname = 'GMT'

GMT_minus_0 = GMT_minus_0()

