_load_plugins() {
	local zplugins_dir="$HOME/.zplugins"

	[ ! -d "$zplugins_dir" ] && return

	local autosuggestions="$zplugins_dir/zsh-autosuggestions"
	if [ -d "$autosuggestions" ]; then
		source "$autosuggestions/zsh-autosuggestions.zsh"
	fi

	local syntax_highlighting="$zplugins_dir/zsh-syntax-highlighting"
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

	local omz="$zplugins_dir/ohmyzsh"
	if [ -d "$omz" ]; then
		_load_omz_plugin() {
			source "$omz/plugins/$1/$1.plugin.zsh"
		}

		source "$omz/lib/key-bindings.zsh"
		_load_omz_plugin sudo
		_load_omz_plugin history
		_load_omz_plugin dirhistory
		_load_omz_plugin systemd
		source "$omz/lib/clipboard.zsh"
		_load_omz_plugin copybuffer
		_load_omz_plugin copyfile
	fi
}

_load_plugins
