__dmd_load_zplug() {
	local zplugdir="$HOME/.deploy-my-dotfiles/zsh-plugins"
	[[ ! -d "$zplugdir" ]] && return

	local autosuggestions="$zplugdir/zsh-autosuggestions"
	if [ -d "$autosuggestions" ]; then
		source "$autosuggestions/zsh-autosuggestions.zsh"
	fi

	local syntax_highlighting="$zplugdir/zsh-syntax-highlighting"
	if [ -d "$syntax_highlighting" ]; then
		source "$syntax_highlighting/zsh-syntax-highlighting.zsh"
	fi

	if [ -d "$zplugdir/zsh-completions" ]; then
		fpath=("$zplugdir/zsh-completions" $fpath)

		rebuild_zcompdump() {
			rm -f ~/.zcompdump
			compinit
		}
	fi
}

__dmd_load_zplug
