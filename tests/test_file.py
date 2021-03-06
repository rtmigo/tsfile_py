# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


import unittest
import datetime as dt
from tsfile import TimestampFile
from dateutil.tz import tzoffset


class Test(unittest.TestCase):

    def test(self):
        tsf = TimestampFile()
        self.assertEqual(tsf.text, "2021-05-07 22:01:44 +03")
        self.assertEqual(tsf.time, dt.datetime(2021, 5, 7, 22, 1, 44,
                                               tzinfo=tzoffset(None, 10800)))

        self.assertEqual(tsf.time.isoformat(), '2021-05-07T22:01:44+03:00')
        self.assertEqual(tsf.time_utc.isoformat(), '2021-05-07T19:01:44+00:00')
        self.assertEqual(tsf.version, '21.253.585')
