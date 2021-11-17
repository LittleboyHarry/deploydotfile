from os import walk
from os.path import abspath, join


def snippetsCompile(snippets_dir, target, pattern=None):
    for root, _, files in walk(snippets_dir):
        for file in files:
            rel_path = join(root, file)
            if pattern and not pattern.search(rel_path[len(snippets_dir) + 1 :]):
                continue

            full_path = abspath(rel_path)
            target.write("# file://" + full_path + "\n")
            with open(full_path) as source:
                target.writelines(source)
            target.write("\n\n")
