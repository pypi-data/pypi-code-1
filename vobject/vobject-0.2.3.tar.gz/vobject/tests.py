"""Long or boring tests for vobjects."""

import vobject, behavior

#------------------- Testing and running functions -----------------------------
def _test():
    import doctest, vobject, tests, icalendar, __init__, re
    doctest.testmod(vobject, verbose=0)
    doctest.testmod(tests, verbose=0)
    doctest.testmod(icalendar, verbose=0)
    doctest.testmod(__init__, verbose=0)
    
if __name__ == '__main__':
    _test()
    
#------------------------------ Tests ------------------------------------------
# See http://cvs.sourceforge.net/viewcvs.py/freeassociation/libical/test-data/
# for good sampledata.


testSilly="""
sillyname:name
profile:sillyprofile
stuff:folded
 line
""" + "morestuff;asinine:this line is not folded, \
but in practice probably ought to be, as it is exceptionally long, \
and moreover demonstratively stupid"

icaltest=r"""BEGIN:VCALENDAR
CALSCALE:GREGORIAN
X-WR-TIMEZONE;VALUE=TEXT:US/Pacific
METHOD:PUBLISH
PRODID:-//Apple Computer\, Inc//iCal 1.0//EN
X-WR-CALNAME;VALUE=TEXT:Example
VERSION:2.0
BEGIN:VEVENT
SEQUENCE:5
DTSTART;TZID=US/Pacific:20021028T140000
RRULE:FREQ=Weekly;COUNT=10
DTSTAMP:20021028T011706Z
SUMMARY:Coffee with Jason
UID:EC9439B1-FF65-11D6-9973-003065F99D04
DTEND;TZID=US/Pacific:20021028T150000
BEGIN:VALARM
TRIGGER;VALUE=DURATION:-P1D
ACTION:DISPLAY
DESCRIPTION:Event reminder\, with comma\nand line feed
END:VALARM
END:VEVENT
BEGIN:VTIMEZONE
TZID:US/Pacific
LAST-MODIFIED:19870101T000000Z
BEGIN:STANDARD
DTSTART:19671029T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19870405T020000
RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
END:DAYLIGHT
END:VTIMEZONE
END:VCALENDAR"""

vcardtest = """BEGIN:VCARD
VERSION:3.0
FN:Daffy Duck Knudson (with Bugs Bunny and Mr. Pluto)
N:Knudson;Daffy Duck (with Bugs Bunny and Mr. Pluto)
NICKNAME:gnat and gnu and pluto
BDAY;value=date:02-10;11-05;01-01
TEL;type=HOME:+01-(0)2-765.43.21
TEL;type=CELL:+01-(0)5-555.55.55
ACCOUNT;type=HOME:010-1234567-05
ADR;type=HOME:;;Haight Street 512;Novosibirsk;;80214;Gnuland
TEL;type=HOME:+01-(0)2-876.54.32
ORG:University of Novosibirsk, Department of Octopus
  Parthenogenesis
END:VCARD"""

badstream = r"""BEGIN:VCALENDAR
CALSCALE:GREGORIAN
X-WR-TIMEZONE;VALUE=TEXT:US/Pacific
METHOD:PUBLISH
PRODID:-//Apple Computer\, Inc//iCal 1.0//EN
X-WR-CALNAME;VALUE=TEXT:Example
VERSION:2.0
BEGIN:VEVENT
DTSTART:20021028T140000Z
BEGIN:VALARM
TRIGGER:20021028T120000Z
ACTION:DISPLAY
DESCRIPTION:This trigger is a date-time without a VALUE=DATE-TIME parameter
END:VALARM
END:VEVENT
END:VCALENDAR"""

timezones = r"""

BEGIN:VTIMEZONE
TZID:US/Pacific
BEGIN:STANDARD
DTSTART:19671029T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19870405T020000
RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VTIMEZONE
TZID:US/Eastern
BEGIN:STANDARD
DTSTART:19671029T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZOFFSETFROM:-0400
TZOFFSETTO:-0500
TZNAME:EST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19870405T020000
RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4
TZOFFSETFROM:-0500
TZOFFSETTO:-0400
TZNAME:EDT
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VTIMEZONE
TZID:Santiago
BEGIN:STANDARD
DTSTART:19700314T000000
TZOFFSETFROM:-0300
TZOFFSETTO:-0400
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SA
TZNAME:Pacific SA Standard Time
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19701010T000000
TZOFFSETFROM:-0400
TZOFFSETTO:-0300
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=2SA
TZNAME:Pacific SA Daylight Time
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VTIMEZONE
TZID:W. Europe
BEGIN:STANDARD
DTSTART:19701025T030000
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
TZNAME:W. Europe Standard Time
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19700329T020000
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
TZNAME:W. Europe Daylight Time
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VTIMEZONE
TZID:US/Fictitious-Eastern
LAST-MODIFIED:19870101T000000Z
BEGIN:STANDARD
DTSTART:19671029T020000
RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
TZOFFSETFROM:-0400
TZOFFSETTO:-0500
TZNAME:EST
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:19870405T020000
RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4;UNTIL=20050403T070000Z
TZOFFSETFROM:-0500
TZOFFSETTO:-0400
TZNAME:EDT
END:DAYLIGHT
END:VTIMEZONE

BEGIN:VTIMEZONE
TZID:America/Montreal
LAST-MODIFIED:20051013T233643Z
BEGIN:DAYLIGHT
DTSTART:20050403T070000
TZOFFSETTO:-0400
TZOFFSETFROM:+0000
TZNAME:EDT
END:DAYLIGHT
BEGIN:STANDARD
DTSTART:20051030T020000
TZOFFSETTO:-0500
TZOFFSETFROM:-0400
TZNAME:EST
END:STANDARD
END:VTIMEZONE

"""

__test__ = { "Test readOne" :
    """
    >>> import StringIO
    >>> from vobject import readOne
    >>> f2 = StringIO.StringIO(testSilly) 
    >>> silly = readOne(f2)
    >>> silly
    <sillyprofile| [<MORESTUFF{}this line is not folded, but in practice probably ought to be, as it is exceptionally long, and moreover demonstratively stupid>, <SILLYNAME{}name>, <STUFF{}foldedline>]>
    >>> silly.stuff[0]
    <STUFF{}foldedline>
    >>> original = silly.serialize()
    >>> f3 = StringIO.StringIO(original)
    >>> silly2 = readOne(f3)
    >>> silly2.serialize()==original
    True
    >>> s3 = StringIO.StringIO('cn:Babs Jensen\\r\\ncn:Barbara J Jensen\\r\\nsn:Jensen\\r\\nemail:babs@umich.edu\\r\\nphone:+1 313 747-4454\\r\\nx-id:1234567890\\r\\n')
    >>> ex1 = readOne(s3)
    >>> ex1
    <*unnamed*| [<CN{}Babs Jensen>, <CN{}Barbara J Jensen>, <EMAIL{}babs@umich.edu>, <PHONE{}+1 313 747-4454>, <SN{}Jensen>, <X-ID{}1234567890>]>
    >>> ex1.serialize()
    u'CN:Babs Jensen\\r\\nCN:Barbara J Jensen\\r\\nEMAIL:babs@umich.edu\\r\\nPHONE:+1 313 747-4454\\r\\nSN:Jensen\\r\\nX-ID:1234567890\\r\\n'
    """,
    
    "Validate sampledata.txt" :
    """
    >>> import vobject, icalendar
    >>> f=open("sampledata.txt")
    >>> c=list(vobject.readComponents(f, validate=True))
    >>> c[1].vevent[0].dtend[0].value
    datetime.datetime(1998, 3, 12, 9, 30, tzinfo=<tzicalvtz 'US-Eastern'>)
    >>> c[1].vevent[0].dtend[0].value.astimezone(icalendar.getTzid("UTC"))
    datetime.datetime(1998, 3, 12, 14, 30, tzinfo=tzutc())
    """,
    
    "Import icaltest" :
    """
    >>> import vobject, StringIO
    >>> f = StringIO.StringIO(icaltest)
    >>> c = vobject.readOne(f, validate=True)
    >>> c.vevent[0].valarm[0].trigger[0]
    <TRIGGER{}-1 day, 0:00:00>
    >>> c.vevent[0].dtstart[0].value
    datetime.datetime(2002, 10, 28, 14, 0, tzinfo=<tzicalvtz 'US/Pacific'>)
    >>> c.vevent[0].dtend[0].value
    datetime.datetime(2002, 10, 28, 15, 0, tzinfo=<tzicalvtz 'US/Pacific'>)
    >>> c.vevent[0].dtstamp[0].value
    datetime.datetime(2002, 10, 28, 1, 17, 6, tzinfo=tzutc())
    >>> c.vevent[0].valarm[0].description[0].value
    u'Event reminder, with comma\\nand line feed'
    >>> c.vevent[0].valarm[0].description[0].serialize()
    u'DESCRIPTION:Event reminder\\\\, with comma\\\\nand line feed\\r\\n'
    >>> vevent = c.vevent[0].transformFromNative()
    >>> vevent.rrule[0]
    <RRULE{}FREQ=Weekly;COUNT=10>
    """,
    
    "Parsing tests" :
    """
    >>> import icalendar
    >>> parseRDate = icalendar.MultiDateBehavior.transformToNative
    >>> icalendar.stringToTextValues('')
    ['']
    >>> icalendar.stringToTextValues('abcd,efgh')
    ['abcd', 'efgh']
    >>> icalendar.stringToPeriod("19970101T180000Z/19970102T070000Z")
    (datetime.datetime(1997, 1, 1, 18, 0, tzinfo=tzutc()), datetime.timedelta(0, 46800))
    >>> parseRDate(vobject.textLineToContentLine("RDATE;VALUE=DATE:19970304,19970504,19970704,19970904"))
    <RDATE{'VALUE': ['DATE']}[datetime.date(1997, 3, 4), datetime.date(1997, 5, 4), datetime.date(1997, 7, 4), datetime.date(1997, 9, 4)]>
    >>> parseRDate(vobject.textLineToContentLine("RDATE;VALUE=PERIOD:19960403T020000Z/19960403T040000Z,19960404T010000Z/PT3H"))
    <RDATE{'VALUE': ['PERIOD']}[(datetime.datetime(1996, 4, 3, 2, 0, tzinfo=tzutc()), datetime.timedelta(0, 7200)), (datetime.datetime(1996, 4, 4, 1, 0, tzinfo=tzutc()), datetime.timedelta(0, 10800))]>
    """,
    
    "read failure" :
    """
    >>> import StringIO, vobject
    >>> f = StringIO.StringIO(badstream)
    >>> vevent = vobject.readOne(f)
    Traceback (most recent call last):
    ...
    ParseError: In component starting at line 11: got unexpected character reading in duration: 20021028T120000Z
    """,
    
    "unicode test" :
    """
    >>> import StringIO, vobject
    >>> f = file('utf8_test.ics', 'rb')
    >>> vevent = vobject.readOne(f).vevent[0]
    >>> vevent.summary[0].value
    u'The title \\u3053\\u3093\\u306b\\u3061\\u306f\\u30ad\\u30c6\\u30a3'
    >>> summary = vevent.summary[0].value
    """,
    
    "regular expression test" :
    """
    >>> import re, vobject
    >>> re.findall(vobject.patterns['name'], '12foo-bar:yay')
    ['12foo-bar', 'yay']
    >>> re.findall(vobject.patterns['safe_char'], 'a;b"*,cd')
    ['a', 'b', '*', 'c', 'd']
    >>> re.findall(vobject.patterns['qsafe_char'], 'a;b"*,cd')
    ['a', ';', 'b', '*', ',', 'c', 'd']
    >>> re.findall(vobject.patterns['param_value'], '"quoted";not-quoted;start"after-illegal-quote', re.VERBOSE)
    ['"quoted"', '', 'not-quoted', '', 'start', '', 'after-illegal-quote', '']
    >>> match = vobject.line_re.match('TEST;ALTREP="http://www.wiz.org":value:;"')
    >>> match.group('value')
    'value:;"'
    >>> match.group('name')
    'TEST'
    >>> match.group('params')
    ';ALTREP="http://www.wiz.org"'
    """,
    
    "VTIMEZONE creation test:" :
        
    """
    >>> import vobject, icalendar, dateutil.tz, StringIO, dateutil.zoneinfo
    >>> brazil = dateutil.zoneinfo.gettz("Brazil/East")
    >>> icalendar.TimezoneComponent.pickTzid(brazil)
    'BRT'
    >>> f = StringIO.StringIO(timezones)
    >>> tzs = dateutil.tz.tzical(f)
    >>> tzs.get("US/Pacific")
    <tzicalvtz 'US/Pacific'>
    >>> icalendar.TimezoneComponent(_)
    <VTIMEZONE | <TZID{}US/Pacific>>
    >>> pacific = _
    >>> print pacific.serialize().replace(vobject.CRLF, vobject.LF).strip()
    BEGIN:VTIMEZONE
    TZID:US/Pacific
    BEGIN:STANDARD
    DTSTART:20001029T020000
    RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
    TZNAME:PST
    TZOFFSETFROM:-0700
    TZOFFSETTO:-0800
    END:STANDARD
    BEGIN:DAYLIGHT
    DTSTART:20000402T020000
    RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4
    TZNAME:PDT
    TZOFFSETFROM:-0800
    TZOFFSETTO:-0700
    END:DAYLIGHT
    END:VTIMEZONE
    >>> (_)
    <VTIMEZONE | <TZID{}US/Pacific>>
    >>> santiago = icalendar.TimezoneComponent(tzs.get('Santiago'))
    >>> ser = santiago.serialize()
    >>> print ser.replace(vobject.CRLF, vobject.LF).strip()
    BEGIN:VTIMEZONE
    TZID:Santiago
    BEGIN:STANDARD
    DTSTART:20000311T000000
    RRULE:FREQ=YEARLY;BYDAY=2SA;BYMONTH=3
    TZNAME:Pacific SA Standard Time
    TZOFFSETFROM:-0300
    TZOFFSETTO:-0400
    END:STANDARD
    BEGIN:DAYLIGHT
    DTSTART:20001014T000000
    RRULE:FREQ=YEARLY;BYDAY=2SA;BYMONTH=10
    TZNAME:Pacific SA Daylight Time
    TZOFFSETFROM:-0400
    TZOFFSETTO:-0300
    END:DAYLIGHT
    END:VTIMEZONE
    >>> roundtrip = dateutil.tz.tzical(StringIO.StringIO(str(ser))).get()
    >>> from datetime import datetime
    >>> for year in range(2001, 2010):
    ...     for month in (2, 9):
    ...         dt = datetime(year, month, 15, tzinfo = roundtrip)
    ...         if dt.replace(tzinfo=tzs.get('Santiago')) != dt:
    ...             print "Failed for:", dt
    >>> fict = icalendar.TimezoneComponent(tzs.get('US/Fictitious-Eastern'))
    >>> print fict.serialize().replace(vobject.CRLF, vobject.LF).strip()
    BEGIN:VTIMEZONE
    TZID:US/Fictitious-Eastern
    BEGIN:STANDARD
    DTSTART:20001029T020000
    RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
    TZNAME:EST
    TZOFFSETFROM:-0400
    TZOFFSETTO:-0500
    END:STANDARD
    BEGIN:DAYLIGHT
    DTSTART:20000402T020000
    RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4;UNTIL=20050403T070000Z
    TZNAME:EDT
    TZOFFSETFROM:-0500
    TZOFFSETTO:-0400
    END:DAYLIGHT
    END:VTIMEZONE
    """,

    "Serializing with timezones test" :
    
    """
    >>> import vobject, icalendar, StringIO, dateutil.tz, datetime
    >>> from dateutil.rrule import rrule, rruleset, WEEKLY
    >>> pacific = dateutil.tz.tzical(StringIO.StringIO(timezones)).get('US/Pacific')
    >>> cal = vobject.Component('VCALENDAR')
    >>> cal.setBehavior(icalendar.VCalendar2_0)
    >>> ev = cal.add('vevent')
    >>> ev.add('dtstart').value = datetime.datetime(2005, 10, 12, 9, tzinfo = pacific)
    >>> set = rruleset()
    >>> set.rrule(rrule(WEEKLY, interval=2, byweekday=[2,4], until=datetime.datetime(2005, 12, 15, 9)))
    >>> set.exdate(datetime.datetime(2005, 10, 14, 9, tzinfo = pacific))
    >>> ev.rruleset = set
    >>> ev.add('uid').value = "uid could be generated but doctest complains"
    >>> ev.add('duration').value = datetime.timedelta(hours=1)
    >>> print cal.serialize().replace(vobject.CRLF, vobject.LF).strip()
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//PYVOBJECT//NONSGML Version 1//EN
    BEGIN:VTIMEZONE
    TZID:US/Pacific
    BEGIN:STANDARD
    DTSTART:20001029T020000
    RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
    TZNAME:PST
    TZOFFSETFROM:-0700
    TZOFFSETTO:-0800
    END:STANDARD
    BEGIN:DAYLIGHT
    DTSTART:20000402T020000
    RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4
    TZNAME:PDT
    TZOFFSETFROM:-0800
    TZOFFSETTO:-0700
    END:DAYLIGHT
    END:VTIMEZONE
    BEGIN:VEVENT
    UID:uid could be generated but doctest complains
    DTSTART;TZID=US/Pacific:20051012T090000
    DURATION:PT1H
    EXDATE;TZID=US/Pacific:20051014T090000
    RRULE:FREQ=WEEKLY;BYDAY=WE,FR;INTERVAL=2;UNTIL=20051215T090000
    END:VEVENT
    END:VCALENDAR
    >>> apple = dateutil.tz.tzical(StringIO.StringIO(timezones)).get('America/Montreal')
    >>> ev.dtstart[0].value = datetime.datetime(2005, 10, 12, 9, tzinfo = apple)
    >>> print cal.serialize().replace(vobject.CRLF, vobject.LF).strip()
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//PYVOBJECT//NONSGML Version 1//EN
    BEGIN:VTIMEZONE
    TZID:US/Pacific
    BEGIN:STANDARD
    DTSTART:20001029T020000
    RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
    TZNAME:PST
    TZOFFSETFROM:-0700
    TZOFFSETTO:-0800
    END:STANDARD
    BEGIN:DAYLIGHT
    DTSTART:20000402T020000
    RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4
    TZNAME:PDT
    TZOFFSETFROM:-0800
    TZOFFSETTO:-0700
    END:DAYLIGHT
    END:VTIMEZONE
    BEGIN:VTIMEZONE
    TZID:America/Montreal
    BEGIN:STANDARD
    DTSTART:20000101T000000
    RRULE:FREQ=YEARLY;BYMONTH=1;UNTIL=20040101T050000Z
    TZNAME:EST
    TZOFFSETFROM:-0500
    TZOFFSETTO:-0500
    END:STANDARD
    BEGIN:STANDARD
    DTSTART:20051030T020000
    RRULE:FREQ=YEARLY;BYDAY=5SU;BYMONTH=10
    TZNAME:EST
    TZOFFSETFROM:-0400
    TZOFFSETTO:-0500
    END:STANDARD
    BEGIN:DAYLIGHT
    DTSTART:20050403T070000
    RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=4;UNTIL=20050403T120000Z
    TZNAME:EDT
    TZOFFSETFROM:-0500
    TZOFFSETTO:-0400
    END:DAYLIGHT
    END:VTIMEZONE
    BEGIN:VEVENT
    UID:uid could be generated but doctest complains
    DTSTART;TZID=America/Montreal:20051012T090000
    DURATION:PT1H
    EXDATE;TZID=US/Pacific:20051014T090000
    RRULE:FREQ=WEEKLY;BYDAY=WE,FR;INTERVAL=2;UNTIL=20051215T090000
    END:VEVENT
    END:VCALENDAR
    """,

    "VCARD 3.0 parse test:" :
        
    """
    >>> import vobject, vcard
    >>> card = vobject.readOne(vcardtest)
    >>> card.adr[0].value
    <Address: Haight Street 512\\nNovosibirsk,  80214\\nGnuland>
    >>> print card.adr[0].value
    Haight Street 512
    Novosibirsk,  80214
    Gnuland
    >>> card.org[0].value
    u'University of Novosibirsk, Department of Octopus Parthenogenesis'
    >>> print card.serialize().replace('\\r\\n', '\\n').strip()
    BEGIN:VCARD
    VERSION:3.0
    ACCOUNT;TYPE=HOME:010-1234567-05
    ADR;TYPE=HOME:;;Haight Street 512;Novosibirsk;;80214;Gnuland
    BDAY;VALUE=date:02-10;11-05;01-01
    FN:Daffy Duck Knudson (with Bugs Bunny and Mr. Pluto)
    N:Knudson;Daffy Duck (with Bugs Bunny and Mr. Pluto);;;
    NICKNAME:gnat and gnu and pluto
    ORG:University of Novosibirsk, Department of Octopus Parthenogenesis
    TEL;TYPE=HOME:+01-(0)2-765.43.21
    TEL;TYPE=CELL:+01-(0)5-555.55.55
    TEL;TYPE=HOME:+01-(0)2-876.54.32
    END:VCARD
    """
    }
