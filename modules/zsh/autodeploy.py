import json
from functools import partial
from multiprocessing import Pool as ProcessPool
from os import system as shell, makedirs
from os.path import dirname, exists, isdir, expanduser
from sys import path, argv

module_dir = dirname(__file__)
project_dir = dirname(dirname(module_dir))
path.append(project_dir)

from scripts import openDotfile

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


def gitclone(use_mirror, items):
    name, urls = items
    url = urls['url' if not use_mirror else 'url_git']
    return shell(
        f'cd {plugs_dir}; if [ -d "{name}" ]; then cd "{name}"; git pull -f; else git clone --depth=1 "{url}" "{name}"; fi')


def main():
    options = metadata.get("options")
    if options:
        plugins = options.get("plugins")
        if plugins:
            global plugs_dir
            plugs_dir = expanduser(plugins["directory"])

            arg = argv[2] if len(argv) > 2 else None
            use_mirror = arg == 'atmainland'

            if not isdir(plugs_dir):
                makedirs(plugs_dir)

            pool = ProcessPool(3)
            pool.map(partial(gitclone, use_mirror), plugins.get("items").items() or [])
            pool.close()
            pool.join()


main()
