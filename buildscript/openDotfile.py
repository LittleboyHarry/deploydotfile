from os.path import expanduser


class openDotfile:
    def __init__(self, path):
        self._path = expanduser(path)
        self.content = ""

    def __enter__(self):
        with open(self._path) as f:
            self.content = f.read()
        return self

    def __exit__(self, type, value, traceback):
        with open(self._path, "w") as f:
            f.write(self.content)
