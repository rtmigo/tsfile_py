# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT

import unittest
from pathlib import Path

from tsfile.file import caller_module


class Test(unittest.TestCase):

    def test_caller(self):
        self.assertEqual(caller_module().name, Path(__file__).name)
