__load_my_plugins() {
	local omz_plugins=()

    lsb_release -si | grep -qi "^Arch" && omz_plugins+=(archlinux)
	(( $+commands[dpkg] )) && omz_plugins+=(debian)
	(( $+commands[dnf] )) && omz_plugins+=(dnf)

	(( $+commands[yarn] )) && omz_plugins+=(yarn)
	omz_plugins+=(nvm)

	(( $+commands[rsync] )) && omz_plugins+=(rsync)
	(( $+commands[git] )) && omz_plugins+=(git gitignore)
	(( $+commands[systemctl] )) && omz_plugins+=(systemd)

	if (( $+commands[xclip] || $+commands[wl-copy] )); then
		omz_plugins+=(copybuffer copyfile copypath)
	fi

	omz_plugins+=(
		extract z dirhistory shell-proxy
		command-not-found
		aliases alias-finder
		sudo history
	)

	# other: zsh-interactive-cd
	local omz_hint=(adb fd pip yarn docker rust)

	local zplugins_dir="$HOME/.deploy-my-dotfiles/zsh-plugins"
	local autosuggestions="$zplugins_dir/zsh-autosuggestions"
	local syntax_highlighting="$zplugins_dir/zsh-syntax-highlighting"
	omz="$zplugins_dir/ohmyzsh"

	[ ! -d "$zplugins_dir" ] && return

	if [ -d "$autosuggestions" ]; then
		source "$autosuggestions/zsh-autosuggestions.zsh"
	fi

	if [ -d "$syntax_highlighting" ]; then
		source "$syntax_highlighting/zsh-syntax-highlighting.zsh"
	fi

	if [ -d "$zplugins_dir/zsh-completions" ]; then
		fpath=("$zplugins_dir/zsh-completions" $fpath)

		rebuild_zcompdump() {
			rm -f ~/.zcompdump
			compinit
		}
	fi

	if [ -d "$omz" ]; then
	  __load_omzplug__dir="$omz"
		loadomzplug() {
			source "$__load_omzplug__dir/plugins/$1/$1.plugin.zsh"
		}

		source "$omz/lib/functions.zsh"
		source "$omz/lib/completion.zsh"
		source "$omz/lib/key-bindings.zsh"
		source "$omz/lib/clipboard.zsh"

		for plugin in $omz_plugins; do loadomzplug $plugin; done
		for hint_plug in $omz_hint; do fpath=("$__load_omzplug__dir/plugins/$hint_plug" $fpath); done

		autoload -U compinit
		compinit

		# others: common-aliases git rsync vagrant
		# https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/
	fi
}

__load_my_plugins

unalias acs 2> /dev/null
