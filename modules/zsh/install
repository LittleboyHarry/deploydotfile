#!/bin/sh

dst=$(readlink -f .serve/zshrc-postfix.zsh)
cfg=$(dirname $0)/install.conf

cfg_zinit="${use_zinit_plugs:-$(awk -F "=" '/use_zinit_plugs/ {print $2}' $cfg)}"

[ "$cfg_zinit" = 1 ] && sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma-continuum/zinit/master/doc/install.sh)"

sed -i "/source $(echo "$dst" | sed 's/\//\\\//g')/d" ~/.zshrc
sed -i -e :a -e '/^\n*$/{$d;N;};/\n$/ba' ~/.zshrc
printf "\nsource $dst\n\n" >>~/.zshrc

[ -x "$(command -v fzf)" ] && echo "source /usr/share/fzf/shell/key-bindings.zsh"  >>~/.zshrc