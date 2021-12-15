virustotal-scan() {
    xdg-open "https://www.virustotal.com/gui/file/$(sha256sum $1 | cut -d' ' -f1)" >/dev/null 2>&1
}
