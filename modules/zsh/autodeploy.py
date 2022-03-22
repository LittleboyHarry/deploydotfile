import json
from functools import partial
from multiprocessing import Pool as ProcessPool
from os import system as shell, makedirs
from os.path import dirname, exists, expanduser
from sys import path, argv

from scripts import open_as_str

module_dir = dirname(__file__)
project_dir = dirname(dirname(module_dir))
path.append(project_dir)

with open(module_dir + "/metadata.json") as f:
    metadata = json.load(f)

with open_as_str(metadata["snippets"]["postfix_inject"]["target"]) as dotfile:
    fzfkb_path = "/usr/share/fzf/shell/key-bindings.zsh"
    fzfkb_statement = f'source "{fzfkb_path}"'
    fzfkb_exists = fzfkb_statement in dotfile.string
    if exists(fzfkb_path):
        if not fzfkb_exists:
            dotfile.string += f"\n{fzfkb_statement}\n"
    else:
        if fzfkb_exists:
            dotfile.string.replace(fzfkb_statement + "\n", "")


def gitclone(plugins_directory, items, **at_mainland):
    name, urls = items
    url = urls["url" if not at_mainland else "mainland_url"]
    return shell(
        f'cd {plugins_directory}; if [ -d "{name}" ]; then cd "{name}"; git pull -f; else git clone --depth=1 "{url}" "{name}"; fi'
    )


def main():
    options = metadata.get("options")
    if options:
        plugins = options.get("plugins")
        if plugins:
            arg = argv[2] if len(argv) > 2 else None

            plugins_directory = expanduser(plugins["directory"])
            makedirs(plugins_directory, exist_ok=True)

            pool = ProcessPool(3)
            pool.map(
                partial(gitclone, plugins_directory, at_mainland=(arg == "atmainland")),
                plugins.get("items").items() or [],
            )
            pool.close()
            pool.join()


main()
