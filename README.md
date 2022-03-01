Messy dotfiles? need a tool within features:

- modular organize a single dotfile into multipart files
- easily platform migration by build parameters
- centralized dotfiles generated
- no conflict with your current dotfiles
- only using python script make without any other new syntax
- some nice dotfiles templates

Try it out! It's my recent alpha creative implementation.

## Get Started

require: `python3` `stow`

```
git clone https://github.com/LittleboyHarry/create-my-dotfiles
cd create-my-dotfiles
```

## Structure

| File/Directory       | Description           |
| -------------------- | --------------------- |
| metadata.schema.json | JSON Schema           |
| static/              | stow directly         |
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

```shell
# for example, deploy zsh to new machine:
# modify ./modules/zsh/metadata.json if required
./deploy modules/zsh/

# static by stow
./deploy-static
```

## Built-in Auto Script Function

- multipart snippets compile
- scriptable dotfile `source` link to `./build`

config all in your new module with `metadata.json` like example modules obeying the JSON-Schema, no more script need to write.

anymore, you can write your own `autodeploy.py` in modules.

## FAQ

Q: deploy into other machine?

A:

Method 1: change makefile parameters then build dotfiles locally, copy the fresh build directory into remote.

Method 2: sync this modified project into remote by tool like git, change makefile parameters, then do **order** steps.

Q: Slow Make

A: avoid huge binary file output.

PS: 中国大陆环境修改 config.json

## ToDo

- [ ] centralized tui manage tools, batch deploy

**Any Issues or Fork are welcome! It's Alpha**
