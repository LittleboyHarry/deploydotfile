Messy dotfiles? need a tool within features:

- modular organize a single dotfile into multipart files
- easily platform migration by build parameters
- centralized dotfiles generated
- no conflict with your current dotfiles
- no new syntax but only shell script
- some nice dotfiles templates

Try it out! It's my recent alpha creative implementation.

## Get Started

require python3

```
git clone https://github.com/LittleboyHarry/create-my-dotfiles
cd create-my-dotfiles
```

## Structure

| File/Directory | Description       |
| -------------- | ----------------- |
| modules/       | all modules       |
| .serve/        | auto build result |

### Each Module

| File/Directory   | Description                 |
| ---------------- | --------------------------- |
| snippets/        | all your zshrc snippet      |
| snippets/.local/ | localize code gitignore     |
| ./build.py       | build to .serve             |
| ./config.json    | deploy config               |
| ./install.py     | first run or reinstall only |

## Usage

for example, deploy zsh to new machine:

```shell
# modify ./modules/zsh/config.json if required
./modules/zsh/build.py && ./modules/zsh/install.py

# rebuild each time snippets change, no need install anymore
```

## ToDo

- [ ] centralized tui manage tools, batch deploy
