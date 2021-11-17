Messy dotfiles? need a tool within features:

- modular organize a single dotfile into multipart files
- easily platform migration by build parameters
- centralized dotfiles generated
- no conflict with your current dotfiles
- only using python script make without any other new syntax
- some nice dotfiles templates

Try it out! It's my recent alpha creative implementation.

## Get Started

require python3

```
git clone https://github.com/LittleboyHarry/create-my-dotfiles
cd create-my-dotfiles
```

## Structure

| File/Directory       | Description           |
| -------------------- | --------------------- |
| metadata.schema.json | JSON Schema           |
| modules/             | all modules           |
| build/               | auto build result     |
| buildscript/         | builtin script helper |
| ./deploy             | install script        |

### Each Module

| File/Directory   | Description             |
| ---------------- | ----------------------- |
| snippets/        | components of dotfiles  |
| snippets/.local/ | localize code gitignore |
| ./metadata.json  | config                  |

## Usage

for example, deploy zsh to new machine:

```shell
# modify ./modules/zsh/metadata.json if required
./deploy.py modules/zsh/
```

## Built-in Autoscript Function

- multipart snippets compile
- scriptable dotfile `source` link to `./build`

config all in your new module with `metadata.json` like example modules obeying the JSON-Schema, no more script need to write.

anymore, you can write your own `autorun.py` in modules.

## FAQ

Q: deploy into other machine?

A:

Method 1: change makefile parameters then build dotfiles locally, copy the fresh build directory into remote.

Method 2: sync this modified project into remote by tool like git, change makefile parameters, then do **order** steps.

Q: Slow Make

A: avoid huge binary file output.

## ToDo

- [ ] centralized tui manage tools, batch deploy

**Any Issues or Fork are welcome! It's Alpha**
