import iso8601

def test_iso8601_regex():
    assert iso8601.ISO8601_REGEX.match("2006-10-11T00:14:33Z")

def test_timezone_regex():
    assert iso8601.TIMEZONE_REGEX.match("+01:00")
    assert iso8601.TIMEZONE_REGEX.match("+00:00")
    assert iso8601.TIMEZONE_REGEX.match("+01:20")
    assert iso8601.TIMEZONE_REGEX.match("-01:00")

def test_parse_date():
    d = iso8601.parse_date("2006-10-20T15:34:56Z")
    assert d.year == 2006
    assert d.month == 10
    assert d.day == 20
    assert d.hour == 15
    assert d.minute == 34
    assert d.second == 56
    assert d.tzinfo == iso8601.UTC

def test_parse_date_fraction():
    d = iso8601.parse_date("2006-10-20T15:34:56.123Z")
    assert d.year == 2006
    assert d.month == 10
    assert d.day == 20
    assert d.hour == 15
    assert d.minute == 34
    assert d.second == 56
    assert d.microsecond == 123
    assert d.tzinfo == iso8601.UTC

def test_parse_date_tz():
    d = iso8601.parse_date("2006-10-20T15:34:56.123+02:30")
    assert d.year == 2006
    assert d.month == 10
    assert d.day == 20
    assert d.hour == 15
    assert d.minute == 34
    assert d.second == 56
    assert d.microsecond == 123
    assert d.tzinfo.tzname(None) == "+02:30"
    offset = d.tzinfo.utcoffset(None)
    assert offset.days == 0
    assert offset.seconds == 60 * 60 * 2.5

def test_parse_invalid_date():
    try:
        iso8601.parse_date(None)
    except iso8601.ParseError:
        pass
    else:
        assert 1 == 2

def test_parse_invalid_date2():
    try:
        iso8601.parse_date("23")
    except iso8601.ParseError:
        pass
    else:
        assert 1 == 2
