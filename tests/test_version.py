import unittest
import datetime as dt

import tsfile.version


class Test(unittest.TestCase):
    def test_version_minutes(self):
        def g(*args): return tsfile.version.version_from_minute(
            dt.datetime(*args))

        self.assertEqual(g(2021, 5, 7, 21, 8, 42), '21.253.548')
        self.assertEqual(g(2015, 10, 21, 17, 25, 23), '15.587.325')

    def test_version_milliday(self):
        def g(*args): return tsfile.version.version_from_milliday(
            dt.datetime(*args))

        self.assertEqual(g(2015, 10, 21, 17, 25, 23), '15.587.451')
        self.assertEqual(g(2015, 12, 30, 23, 59, 59), '15.727.999')
        self.assertEqual(g(2015, 12, 31, 23, 59, 59), '15.729.999')
        self.assertEqual(g(2015, 1, 1, 0, 0, 0), '15.0.0')
