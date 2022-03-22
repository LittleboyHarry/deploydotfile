from genericpath import exists
from os import mkdir
from os.path import expanduser
from posixpath import dirname
import ntpath


class FileAsStr:
    def __init__(self, path):
        self._path = expanduser(path)
        self.string = ""

    def __enter__(self):
        try:
            with open(self._path) as f:
                self.string = f.read()
        except FileNotFoundError:
            self.string = ""
        return self

    def __exit__(self, _, value, traceback):
        parent_dir = dirname(self._path) or ntpath.dirname(self._path)
        if not exists(parent_dir):
            mkdir(parent_dir)
        with open(self._path, "w") as f:
            f.write(self.string)


def open_as_str(path):
    return FileAsStr(path)
