from os import system as shell, mkdir
from os.path import dirname, exists, isdir, expanduser
from multiprocessing import Pool as ProcessPool
import json
import re

from sys import path

module_dir = dirname(__file__)
project_dir = dirname(dirname(module_dir))
path.append(project_dir)

from buildscript import openDotfile

with open(module_dir + "/metadata.json") as f:
    metadata = json.load(f)

with openDotfile(metadata["dotfile"]) as dotfile:
    fzfkb_path = "/usr/share/fzf/shell/key-bindings.zsh"
    fzfkb_statement = f'source "{fzfkb_path}"'
    fzfkb_exists = fzfkb_statement in dotfile.content
    if exists(fzfkb_path):
        if not fzfkb_exists:
            dotfile.content += f"\n{fzfkb_statement}\n"
    else:
        if fzfkb_exists:
            dotfile.content.replace(fzfkb_statement + "\n", "")


def gitclone(item):
    url = f"{url_prefix}{item}.git"
    name = item.split("/")[-1]
    return shell(
        f'cd {plugs_dir}; if [ -d "{name}" ]; then cd "{name}"; git pull -f; else git clone  --depth=1 "{url}"; fi'
    )


options = metadata.get("options")
if options:
    plugins = options.get("plugins")
    if plugins:
        global plugs_dir
        plugs_dir = expanduser(plugins["directory"])

        with open("config.json") as f:
            use_mirror = json.load(f).get("china_env") or False

        if not isdir(plugs_dir):
            mkdir(plugs_dir)

        global url_prefix
        url_prefix = (
            "https://gitclone.com/github.com/" if use_mirror else "https://github.com/"
        )

        pool = ProcessPool(3)
        results = pool.map(gitclone, plugins.get("items") or [])
        pool.close()
        pool.join()
