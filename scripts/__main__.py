import json
import re
from os import walk
from os.path import abspath, exists, relpath, join
from runpy import run_path
from sys import argv

from . import open_dotfile

module_path = relpath(argv[1])
with open(module_path + "/metadata.json") as f:
    module_metadata = json.load(f)

options = module_metadata.get("options") or dict()

snippets_config = module_metadata.get("snippets")
if snippets_config:
    snippets_directory = f"{module_path}/snippets"

    pattern_str = snippets_config.get("pattern")
    pattern = re.compile(pattern_str) if pattern_str else None

    inject_config = snippets_config.get("postfix_inject")
    if inject_config:
        statement = inject_config["template"].format(
            abspath("build/" + inject_config["target"])
        )

        # compile snippets
        with open(f"build/{snippets_config['generate_file']}", "w") as target:
            comment = inject_config["comment"]
            for root, _, files in walk(snippets_directory):
                for file in files:
                    rel_path = join(root, file)
                    if pattern and not pattern.search(rel_path[len(snippets_directory) + 1:]):
                        continue

                    full_path = abspath(rel_path)
                    target.write(comment.format("file://" + full_path + "\n"))
                    with open(full_path) as source:
                        target.writelines(source)
                    target.write("\n\n")

        # inject postfix into dotfile
        with open_dotfile(inject_config["source"]) as dotfile:
            if not (statement in dotfile.content):
                dotfile.content += f"\n{statement}\n"

autodeploy_path = f"{argv[1]}/autodeploy.py"
if exists(autodeploy_path):
    run_path(autodeploy_path)
