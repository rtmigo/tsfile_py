import unittest
from pathlib import PosixPath, WindowsPath
from tsfile.file import iter_parents

try:
    PosixPath("/path/to/file.txt")
    can_create_posix = True
except NotImplementedError:
    can_create_posix = False

try:
    WindowsPath(r"c:\path\to\file.txt")
    can_create_windows = True
except NotImplementedError:
    can_create_windows = False


class Test(unittest.TestCase):
    @unittest.skipUnless(can_create_posix, 'Cannot create PosixPath')
    def test_parents_posix(self):
        self.assertEqual(len(list(iter_parents(PosixPath("/file/sub/x.txt")))),
                         3)
        self.assertEqual(len(list(iter_parents(PosixPath("/")))),
                         0)
        self.assertGreater(len(list(iter_parents(PosixPath("zz")))),
                           0)

    @unittest.skipUnless(can_create_windows, 'Cannot create WindowsPath')
    def test_parents_windows(self):
        self.assertEqual(
            len(list(iter_parents(PosixPath("c:/file/sub/x.txt")))),
            3)
        self.assertEqual(len(list(iter_parents(PosixPath("c:/")))),
                         0)
        self.assertGreater(len(list(iter_parents(PosixPath("zz")))),
                           0)
