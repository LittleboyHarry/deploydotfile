from sys import argv
from os.path import abspath, exists
from ._ModuleHelper import ModuleHelper
from . import snippetsCompile
from runpy import run_path
import re

helper = ModuleHelper(argv[1])

options = helper.data.get("options") or dict()

dotfileInject = helper.data.get("dotfileInject")
if dotfileInject:
    statement = dotfileInject["template"].format(
        abspath("build/" + dotfileInject["target"])
    )
    helper.dotfile_inject(statement)

snippets = helper.data.get("snippets")
if snippets:
    snippets_dir = f"{helper.module_path}/snippets"

    pattern_str = snippets.get("pattern")
    if pattern_str:
        pattern = re.compile(pattern_str)
    else:
        pattern = None

    with open(f"build/{snippets['buildTarget']}", "w") as target:
        snippetsCompile(snippets_dir, target, dotfileInject["comment"], pattern)

autodeploy_path = f"{argv[1]}/autodeploy.py"
if exists(autodeploy_path):
    run_path(autodeploy_path)
