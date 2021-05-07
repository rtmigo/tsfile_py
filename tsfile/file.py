from pathlib import Path
from typing import Optional
import datetime as dt

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
        for parent in iter_parents(Path(__file__)):
            ts_file = parent / "timestamp.txt"
            if ts_file.exists():
                return ts_file
