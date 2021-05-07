import datetime as dt


def years_from_2000(date: dt.datetime) -> int:
    return date.year - 2000


def days_from_start_of_year(date: dt.datetime):
    return (date - dt.datetime(date.year, 1, 1)).days


minutes_per_12h = 12 * 60
seconds_per_12h = minutes_per_12h * 60


def half_days_from_start_of_year(date: dt.datetime) -> int:
    seconds = (date - dt.datetime(date.year, 1, 1, tzinfo=date.tzinfo)).total_seconds()
    return int(seconds // seconds_per_12h)


def minutes_since_half_day(date: dt.datetime) -> int:
    t = date.time()
    minutes = t.hour * 60 + t.minute
    minutes %= minutes_per_12h

    return minutes


def float_since_half_day(t: dt.datetime) -> float:
    since_day_start = t - dt.datetime(t.year, t.month, t.day, #t.hour % 12,
                                tzinfo=t.tzinfo)

    result = (since_day_start.total_seconds()%seconds_per_12h) / seconds_per_12h
    assert 0 <= result <= 1.0
    return result
