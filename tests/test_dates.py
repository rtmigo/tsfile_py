import unittest
import datetime as dt

import tsfile.dates as dts


class Test(unittest.TestCase):
    def test_years(self):
        self.assertEqual(dts.years_from_2000(dt.datetime(2021, 5, 7)), 21)

    def test_half_days(self):
        self.assertEqual(
            dts.half_days_from_start_of_year(
                dt.datetime(2015, 1, 10, 21, 8, 9)),
            19)

        self.assertEqual(
            dts.half_days_from_start_of_year(
                dt.datetime(2021, 5, 7, 21, 8, 42)),
            253)

    def test_minutes_since_12h(self):
        def tm(h, m, s): return dts.minutes_since_half_day(
            dt.datetime(2015, 1, 10, h, m, s))

        self.assertEqual(tm(0, 0, 0), 0)
        self.assertEqual(tm(0, 17, 0), 17)
        self.assertEqual(tm(12, 45, 0), 45)
        self.assertEqual(tm(3, 45, 0), 225)
        self.assertEqual(tm(15, 45, 0), 225)

    def test_float_since_12h(self):
        def tm(h, m, s): return dts.float_since_half_day(
            dt.datetime(2015, 1, 10, h, m, s))

        self.assertEqual(tm(0, 0, 0), 0)
        self.assertAlmostEqual(tm(0, 17, 0), 0.02361111111111111)
        self.assertAlmostEqual(tm(12, 17, 0), 0.02361111111111111)
        self.assertAlmostEqual(tm(11, 59, 59), 0.9999768518518518)
        self.assertAlmostEqual(tm(23, 59, 59), 0.9999768518518518)
        #self.assertEqual(tm(12, 45, 0), 45)
        #self.assertEqual(tm(3, 45, 0), 225)
        #self.assertEqual(tm(15, 45, 0), 225)

