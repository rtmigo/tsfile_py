# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import datetime as dt
from math import floor

from .dates import years_from_2000, half_days_from_start_of_year, \
    minutes_since_half_day, float_since_half_day


def version_from_minute(d: dt.datetime) -> str:
    return ".".join(
        (str(years_from_2000(d)),
         str(half_days_from_start_of_year(d)),
         str(minutes_since_half_day(d))))


def version_from_milliday(d: dt.datetime) -> str:
    return ".".join(
        (str(years_from_2000(d)),
         str(half_days_from_start_of_year(d)),
         str(floor(float_since_half_day(d)*1000))))
