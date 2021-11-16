#!/usr/bin/env python3

import json
from os import path, mkdir, walk

module_dir = path.relpath(path.dirname(__file__))

config = json.load(open(module_dir + "/config.json"))
dest_path = ".serve/zshrc-postfix.zsh"

try:
    mkdir(".serve")
except FileExistsError:
    pass

snippet_dir = module_dir + "/snippets"
local_dir = snippet_dir + "/.local"
zinit_dir = snippet_dir + "/zinit"

with open(dest_path, "w") as dst:
    for root, dirs, files in walk(snippet_dir):
        for name in files:
            if root == zinit_dir and not config["zinit_plugs"]:
                pass
            else:
                pathname = path.join(root, name)
                path_annotation = "# file://" + path.abspath(pathname) + "\n"

                dst.write(path_annotation)
                with open(pathname) as frm:
                    dst.writelines(frm)
                dst.write("\n\n")
