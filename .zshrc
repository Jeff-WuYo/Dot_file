## Options section
#setopt correct                                                  # Auto correct mistakes
#setopt extendedglob                                             # Extended globbing. Allows using regular expressions with *
#setopt nocaseglob                                               # Case insensitive globbing
#unsetopt nomatch						# Passes the command as is instead of reporting pattern matching failure see Chrysostomus/manjaro-zsh-config#14
#setopt rcexpandparam                                            # Array expension with parameters
#setopt nocheckjobs                                              # Don't warn about running processes when exiting
#setopt numericglobsort                                          # Sort filenames numerically when it makes sense
#setopt nobeep                                                   # No beep
#setopt appendhistory                                            # Immediately append history instead of overwriting
#setopt histignorealldups                                        # If a new command is a duplicate, remove the older one
setopt autocd                                                   # if only directory path is entered, cd there.

# Command completion
autoload -Uz compinit
compinit
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}'       # Case insensitive tab completion
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"         # Colored completion (different colors for dirs/files/etc)
zstyle ':completion:*' rehash true                              # automatically find new executables in path 
# Speed up completions
zstyle ':completion:*' accept-exact '*(N)'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
zstyle ':completion:*' menu select
HISTFILE=~/.zhistory
HISTSIZE=1000
SAVEHIST=500
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
#WORDCHARS=${WORDCHARS//\/[&.;]}                                 # Don't consider certain characters part of the word

# Enable Ctrl-x-e to edit command line
autoload -U edit-command-line
zle -N edit-command-line
bindkey '^xe' edit-command-line
bindkey '^x^e' edit-command-line
# Alias section 
alias cp="cp -iv"                                               # Confirm before overwriting something
alias df='df -h'                                                # Human-readable sizes
alias du='du -h'                                                # Human-readable sizes
alias free='free -m'                                            # Show sizes in MB
alias gitu='git add . && git commit && git push'
alias ls='ls --color'
alias ll='ls -alh --color'
alias grep='grep --colour=auto'
alias egrep='egrep --colour=auto'
alias fgrep='fgrep --colour=auto'
alias mpv='mpv --hwdec=auto'
alias ytd='youtube-dl'
alias ytdmp3='youtube-dl -x --audio-format mp3 --audio-quality 0'
alias ytdaac='youtube-dl -x --audio-format aac --audio-quality 0'
alias Syu='doas pacman -Syu'
alias SyQu='doas pacman -Sy && pacman -Qu'
alias ip='ip -c=always'
alias pts='phoronix-test-suite'
alias -s {conf,txt,md}=vim

# Starship prompt 
eval "$(starship init zsh)"

# Color man pages
export LESS_TERMCAP_mb=$'\E[01;32m'
export LESS_TERMCAP_md=$'\E[01;32m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;47;34m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;36m'
export LESS=-r

## Plugins section: Enable fish style features
## Use syntax highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
## Use history substring search
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
## bind UP and DOWN arrow keys to history substring search
zmodload zsh/terminfo
bindkey "$terminfo[kcuu1]" history-substring-search-up
bindkey "$terminfo[kcud1]" history-substring-search-down
bindkey '^[[A' history-substring-search-up			
bindkey '^[[B' history-substring-search-down

# Use autosuggestion
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=20
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'
source /usr/share/nvm/init-nvm.sh
