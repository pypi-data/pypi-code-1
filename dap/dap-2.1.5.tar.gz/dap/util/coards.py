"""Convert COARDS time specification to a datetime object.

This function converts between a given COARDS time specification and a
Python datetime object, which is much more useful. Suppose you have an
Array of values [1,2,3] and units "days since 1998-03-01 12:00:00":

    >>> a = [1, 2, 3]
    >>> units = 'days since 1998-03-01 12:00:00'
    >>> b = [parseUdunits(value, units) for value in a]
    >>> print b[0].year
    1998
    >>> b[1] > b[0]
    True
    >>> print b[1] - b[0]
    1 day, 0:00:00

The list 'b' now contains objects which can be compared and manipulated in
a consistent way.
"""

__author__ = "Roberto De Almeida <rob@pydap.org>"

import re
import datetime

# Constants in seconds.
SECOND = 1.0
MINUTE = 60.0
HOUR = 3.6e3
DAY = 8.64e4
SHAKE = 1e-8
SIDEREAL_DAY = 8.616409e4
SIDEREAL_HOUR = 3.590170e3
SIDEREAL_MINUTE = 5.983617e1
SIDEREAL_SECOND = 0.9972696
SIDEREAL_YEAR = 3.155815e7
TROPICAL_YEAR = 3.15569259747e7
LUNAR_MONTH = 29.530589 * DAY
COMMON_YEAR = 365 * DAY
LEAP_YEAR = 366 * DAY
JULIAN_YEAR = 365.25 * DAY
GREGORIAN_YEAR = 365.2425 * DAY
SIDEREAL_MONTH = 27.321661 * DAY
TROPICAL_MONTH = 27.321582 * DAY
FORTNIGHT = 14 * DAY
WEEK = 7 * DAY
JIFFY = 1e-2 
EON = 1e9 * TROPICAL_YEAR
MONTH = TROPICAL_YEAR/12

class FixedOffset(datetime.tzinfo):
    """Fixed offset in minutes east from UTC.
    
    This is just a stub Timezone with fixed offset.
    """

    def __init__(self, offset, name):
        self.__offset = datetime.timedelta(minutes=offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return datetime.timedelta(0)


def parseDateString(origin):
    """Parses a date string and returns a datetime object.

    This function parses the 'origin' part of the time unit. It should be
    something like:

        2004-11-03 14:42:27.0 +2:00

    Lots of things are optional; just the date is mandatory.
    """
    # yyyy-mm-dd [hh:mm:ss[.s][ [+-]hh[:][mm]]]
    p = re.compile( r'''(?P<year>\d{1,4})           # yyyy
                        -                           #
                        (?P<month>\d{1,2})          # mm or m
                        -                           #
                        (?P<day>\d{1,2})            # dd or d
                                                    #
                        (?:                         # [optional time and timezone]
                            \s                      #
                            (?P<hour>\d{1,2})       #   hh or h
                            :                       #
                            (?P<min>\d{1,2})        #   mm or m
                            :                       #
                            (?P<sec>\d{1,2})        #   ss or s
                                                    #
                            (?:                     #   [optional decisecond]
                                \.                  #       .
                                (?P<dsec>\d)        #       s
                            )?                      #
                            (?:                     #   [optional timezone]
                                \s                  #
                                (?P<ho>[+-]?        #       [+ or -]
                                \d{1,2})            #       hh or h
                                :?                  #       [:]
                                (?P<mo>\d{2})?      #       [mm]
                            )?                      #
                        )?                          #
                        $                           # EOL
                    ''', re.VERBOSE)

    m = p.match(origin.strip())
    if m:
        c = m.groupdict(0)
        
        # Instantiate timezone object.
        offset = int(c['ho'])*60 + int(c['mo'])
        tz = FixedOffset(offset, 'Unknown')

        return datetime.datetime(int(c['year']),
                                 int(c['month']),
                                 int(c['day']),
                                 int(c['hour']),
                                 int(c['min']),
                                 int(c['sec']),
                                 int(c['dsec']) * 100000,
                                 tz)
    
    raise Exception, 'Invalid date origin: %s' % origin


def parseUnits(unit):
    """Parse units.

    This function transforms all Udunits defined time units, returning it
    converted to seconds.
    """
    udunits = [(SECOND,             ['second', 'seconds', 'sec', 's']),
               (MINUTE,             ['minute', 'minutes', 'min']),
               (HOUR,               ['hour', 'hours', 'hr', 'h']),
               (DAY,                ['day', 'days', 'd']),
               (SHAKE,              ['shake', 'shakes']),
               (SIDEREAL_DAY,       ['sidereal_day', 'sidereal_days']),
               (SIDEREAL_HOUR,      ['sidereal_hour', 'sidereal_hours']),
               (SIDEREAL_MINUTE,    ['sidereal_minute', 'sidereal_minutes']),
               (SIDEREAL_SECOND,    ['sidereal_second', 'sidereal_seconds']),
               (SIDEREAL_YEAR,      ['sidereal_year', 'sidereal_years']),
               (TROPICAL_YEAR,      ['tropical_year', 'tropical_years', 'year', 'years', 'yr', 'a']),
               (LUNAR_MONTH,        ['lunar_month', 'lunar_months']),
               (COMMON_YEAR,        ['common_year', 'common_years']),
               (LEAP_YEAR,          ['leap_year', 'leap_years']),
               (JULIAN_YEAR,        ['julian_year', 'julian_years']),
               (GREGORIAN_YEAR,     ['gregorian_year', 'gregorian_years']),
               (SIDEREAL_MONTH,     ['sidereal_month', 'sidereal_months']),
               (TROPICAL_MONTH,     ['tropical_month', 'tropical_months']),
               (FORTNIGHT,          ['fortnight', 'fortnights']),
               (WEEK,               ['week', 'weeks']),
               (JIFFY,              ['jiffy', 'jiffies']),
               (EON,                ['eon', 'eons']),
               (MONTH,              ['month', 'months']),
              ]
    
    for seconds, units in udunits:
        if unit in units: return seconds

    raise Exception, 'Invalid date unit: %s' % unit


def parseUdunits(value, s):
    """Convert time specification to datetime object.

    This function converts a time specification defined by a value and a 
    unit, returning a datetime object from the Python native module of the
    same name.
    """
    s = s.lower()
    try:
        parts = s.split(' since ')
        unit = parts[0]
        origin = parts[1]
    except:
        raise Exception, 'Invalid date string: %s' % s

    # Convert origin to datetime object.
    origin = parseDateString(origin)

    # Convert unit to seconds.
    unit = parseUnits(unit)
    offset = value * unit

    return origin + datetime.timedelta(seconds=offset)


def datetimeToUdunits(dt, s):
    """Convert from datetime to Udunits.

    This function is useful when saving data to a NetCDF file, eg.

        >>> today = datetime.datetime(2005, 02, 15, 0, 0, 0, 0, FixedOffset(0, 'Unknown'))
        >>> print datetimeToUdunits(today, 'days since 2005-01-01 12:00:00 -3:00')
        44.375
        >>> today = datetime.datetime(2005, 02, 15, 0, 0, 0, 0)
        >>> print datetimeToUdunits(today, 'days since 2005-01-01 12:00:00 -3:00')
        44.5
    """
    s = s.lower()
    try:
        parts = s.split(' since ')
        unit = parts[0]
        origin = parts[1]
    except:
        raise Exception, 'Invalid date string: %s' % s

    # Convert origin to datetime object.
    origin = parseDateString(origin)

    # If dt has no time zone info, we assume the same as the origin?
    if not dt.tzinfo: dt = datetime.datetime(dt.year,
                                             dt.month,
                                             dt.day,
                                             dt.hour,
                                             dt.minute,
                                             dt.second,
                                             dt.microsecond,
                                             origin.tzinfo)

    # Calculate delta in seconds.
    delta = dt - origin
    
    return timedeltaToUdunits(delta, unit)


# Backward compatibility.
toUdunits = datetimeToUdunits


def timedeltaToUdunits(delta, unit):
    """Convert from timedelta to Udunits.

        >>> dt = datetime.timedelta(1, 10, 100)  # 1 day, 10 secs, 100 msecs
        >>> print timedeltaToUdunits(dt, 'days')
        1.0001157419
    """
    # Calculate delta in seconds.
    unit = unit.lower()
    delta = delta.seconds + delta.days * 3600 * 24 + delta.microseconds * 1e-6

    # Return delta in desired unit.
    return delta / parseUnits(unit)
    

def convertUnits(L, current_unit, new_unit):
    for v in L:
        # Convert to datetime.
        dt = parseUdunits(v, current_unit)
        yield datetimeToUdunits(dt, new_unit)


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
