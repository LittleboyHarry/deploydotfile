from genericpath import exists
from os import mkdir
from os.path import expanduser
from posixpath import dirname


class Dotfile:
    def __init__(self, path):
        self._path = expanduser(path)
        self.content = ""

    def __enter__(self):
        try:
            with open(self._path) as f:
                self.content = f.read()
        except FileNotFoundError:
            self.content = ""
        return self

    def __exit__(self, _, value, traceback):
        parent_dir = dirname(self._path)
        if not exists(parent_dir):
            mkdir(parent_dir)
        with open(self._path, "w") as f:
            f.write(self.content)


def open_dotfile(path):
    return Dotfile(path)
