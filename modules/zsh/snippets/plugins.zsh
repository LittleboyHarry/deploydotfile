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
		source "$omz/lib/clipboard.zsh"
		_load_omz_plugin {copybuffer,copyfile,copydir}

		for name in \
			sudo history dirhistory command-not-found zsh-interactive-cd aliases alias-finder\
			extract systemd gitignore dnf shell-proxy colored-man-pages
		do _load_omz_plugin $name;	done

		# others: aliases common-aliases git rsync vagrant
		# https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/
	fi
}

_load_plugins
