import json
from os.path import relpath

from scripts import open_dotfile


class ModuleHelper:
    def __init__(self, module_path):
        self.module_path = relpath(module_path)
        with open(self.module_path + "/metadata.json") as f:
            self.data = json.load(f)

    def dotfile_inject(self, statement):
        with open_dotfile(self.data["dotfile"]) as dotfile:
            if not statement in dotfile.content:
                dotfile.content += f"\n{statement}\n"

    def dotfile_remove(self, statement):
        with open_dotfile(self.data["dotfile"]) as dotfile:
            dotfile.content.replace(f"{statement}\n", "")
