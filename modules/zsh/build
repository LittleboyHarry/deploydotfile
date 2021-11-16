#!/bin/sh

dst=./.serve/zshrc-postfix.zsh
cfg=$(dirname $0)/install.conf
snippets=$(readlink -f $(dirname $0))/snippets

cfg_zinit="${use_zinit_plugs:-$(awk -F "=" '/use_zinit_plugs/ {print $2}' $cfg)}"

[ "$cfg_zinit" != 1 ] && zinit_path_if="$snippets/zinit*"

mkdir -p $(dirname $dst)
find "$snippets" -name '*.zsh' \
	-not \( -path "$zinit_path_if" \) \
    -exec echo "# file://"{} \; -exec cat {} \; -exec printf "\n\n" \; >$dst
sed -i -e :a -e '/^\n*$/{$d;N;};/\n$/ba' $dst
