import json
import re
from os import walk, makedirs
from os.path import abspath, exists, relpath, join, expanduser
from runpy import run_path
from sys import argv, platform

from . import open_as_str

module_path = relpath(argv[1])
with open(module_path + "/metadata.json") as f:
    module_metadata = json.load(f)

if module_metadata.get("windows_support") == False and platform == "win32":
    raise RuntimeError("zsh only suppport in UNIX or MSYS environment")

options = module_metadata.get("options") or dict()

snippets_config = module_metadata.get("snippets")
if snippets_config:
    snippets_directory = f"{module_path}/snippets"

    pattern_str = snippets_config.get("pattern")
    pattern = re.compile(pattern_str) if pattern_str else None

    inject_config = snippets_config.get("postfix_inject")
    if inject_config:
        with open("config.json") as f:
            generated_path = expanduser(json.load(f)["generated_path"])
        makedirs(generated_path, exist_ok=True)
        compiled_filepath = f"{generated_path}/{snippets_config['generate_file']}"

        # compile snippets
        with open(compiled_filepath, "w") as target:
            comment = inject_config["comment"]
            for root, _, files in walk(snippets_directory):
                for file in files:
                    rel_path = join(root, file)
                    if pattern and not pattern.search(
                        rel_path[len(snippets_directory) + 1 :]
                    ):
                        continue

                    full_path = abspath(rel_path)
                    target.write(comment.format("file://" + full_path + "\n"))
                    with open(full_path) as source:
                        target.writelines(source)
                    target.write("\n\n")

        # inject postfix into dotfile

        target = inject_config["target_win" if platform == "win32" else "target"]

        with open_as_str(target) as dotfile:
            statement = inject_config["template"].format(abspath(compiled_filepath))
            if not (statement in dotfile.string):
                dotfile.string += f"\n{statement}\n"

autodeploy_path = f"{argv[1]}/autodeploy.py"
if exists(autodeploy_path):
    run_path(autodeploy_path)
