#!/usr/bin/env python3

import os
import json
from os import path


config = json.load(open(path.dirname(__file__) + "/config.json"))

# read ~/.zshrc
zshrc_filename = path.expanduser("~/.zshrc")
with open(zshrc_filename) as f:
    lines = f.readlines()

# inject postfix
serve_filepath = path.abspath(".serve/zshrc-postfix.zsh")
postfix_statement = f'source "{serve_filepath}"\n'
if not postfix_statement in lines:
    lines.append("\n" + postfix_statement)

# inject fzf keybinds
fzf_keybind_path = "/usr/share/fzf/shell/key-bindings.zsh"
fzf_keybind_statement = f'source "{fzf_keybind_path}"\n'
fzf_keybind_exists = fzf_keybind_statement in lines
if path.exists(fzf_keybind_path):
    if not fzf_keybind_exists:
        lines.append("\n" + fzf_keybind_statement)
else:
    if fzf_keybind_exists:
        lines.remove(fzf_keybind_statement)

# save ~/.zshrc changes
with open(zshrc_filename, "w") as f:
    f.writelines(lines)

if config["zinit_plugs"]:
    # install
    os.system(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma-continuum/zinit/master/doc/install.sh)"'
    )
