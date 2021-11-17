from os import system as shell
from os.path import dirname, exists, isdir, expanduser
import json

from sys import path

modir = dirname(__file__)
path.append(dirname(dirname(modir)))

from buildscript import openDotfile, snippetsCompile

with open(modir + "/metadata.json") as f:
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

options = metadata.get("options")
if options:
    if options.get("zinitPlugs"):
        if not isdir(expanduser("~/.zinit")):
            shell(
                'sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma-continuum/zinit/master/doc/install.sh)"'
            )

        with open(f"build/{metadata['snippets']['buildTarget']}", "a") as target:
            snippetsCompile(f"{modir}/zinit-plugs", target)
