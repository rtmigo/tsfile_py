# SPDX-FileCopyrightText: (c) 2021 Artёm IG <github.com/rtmigo>
# SPDX-License-Identifier: MIT


from pathlib import Path
from typing import Optional
import inspect
from dateutil import parser

from tsfile.version import version_from_milliday


def iter_parents(path: Path):
    path = path.absolute()

    while True:

        n = path.parent
        if n == path or not n:
            break
        path = n
        yield path


def caller_module() -> Path:
    """Returns the name of the file containing the module from which this
    function was called. This ignores all modules located directly inside the
    parent directory of the current file (tsfile/*)."""
    this_file_parent = Path(__file__).parent

    for frame in inspect.stack():
        if frame.filename.startswith('<'):
            continue
        path = Path(frame.filename)
        if path.parent == this_file_parent:
            continue
        return path

    raise RuntimeError("Failed to determine the caller module.")


class TimestampFile:

    def __init__(self):
        f = self._find_file()
        if not f:
            raise FileNotFoundError
        self.text = f.read_text().strip()
        self.time = parser.parse(self.text)

    @property
    def version(self):
        return version_from_milliday(self.time)

    def _find_file(self) -> Optional[Path]:
        for parent in iter_parents(caller_module()):
            ts_file = parent / "timestamp.txt"
            if ts_file.exists():
                return ts_file
