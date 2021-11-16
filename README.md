Messy dotfiles? need a tool within features:

- modular organize a single dotfile into multipart files
- easily platform migration by build parameters
- centralized dotfiles generated
- no conflict with your current dotfiles
- no new syntax but only shell script
- some nice dotfiles templates

Try it out! It's my recent alpha creative implementation.

## Get Started

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
| ./build.sh       | build to .serve             |
| ./install.conf   | deploy config               |
| ./install.sh     | first run or reinstall only |

## Usage

for example, deploy zsh to new machine:

```shell
# modify ./modules/zsh/install.conf or export env vars if required
./modules/zsh/build && ./modules/zsh/install

# rebuild each time snippets change, no need install anymore
```

## ToDo

- [ ] centralized tui manage tools, batch deploy
