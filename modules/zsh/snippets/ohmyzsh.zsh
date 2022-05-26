__ddf_load_omz() {
    local omzdir="$HOME/.deploydotfile/zsh-plugins/ohmyzsh"
    [[ ! -d "$omzdir" ]] && return

    local pluglst=()

    lsb_release -si | grep -qi "^Arch" && pluglst+=(archlinux)
    (( $+commands[dpkg] )) && pluglst+=(debian)
    (( $+commands[dnf] )) && pluglst+=(dnf)

    (( $+commands[yarn] )) && pluglst+=(yarn)
    pluglst+=(nvm)

    (( $+commands[rsync] )) && pluglst+=(rsync)
    (( $+commands[git] )) && pluglst+=(git gitignore)
    (( $+commands[systemctl] )) && pluglst+=(systemd)

    if (( $+commands[xclip] || $+commands[wl-copy] )); then
        pluglst+=(copybuffer copyfile copypath)
    fi

    pluglst+=(
        extract z dirhistory shell-proxy
        command-not-found
        aliases alias-finder
        sudo history
    )

    local omz_hint=(adb fd pip yarn docker rust)

    loadomzplug() {
        source "$omzdir/plugins/$1/$1.plugin.zsh"
    }

    source "$omzdir/lib/functions.zsh"
    source "$omzdir/lib/completion.zsh"
    source "$omzdir/lib/key-bindings.zsh"
    source "$omzdir/lib/clipboard.zsh"

    for plugname in $pluglst; do loadomzplug $plugname; done
    unalias acs 2>/dev/null

    for hintfile in $omz_hint; do fpath=("$omzdir/plugins/$hintfile" $fpath); done
    autoload -U compinit
    compinit

    source "$omzdir/lib/git.zsh"
    source "$omzdir/lib/prompt_info_functions.zsh"
    source "$omzdir/lib/theme-and-appearance.zsh"

    # others: common-aliases vagrant
    # https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/

}

__ddf_load_omz
