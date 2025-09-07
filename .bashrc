# i was experimenting with Docker images and replacing them with instead of using VMs and I created this file so that I can have a consistent .bashrc with the correct PATH in place

# ~/.bashrc for Docker container

# ====== PATH ======
export PATH="$PATH:$HOME/.local/bin"

# ====== Aliases ======
alias ll='ls -alF --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'
alias ls='ls --color=auto'

# ====== Prompt ======
# Colored like typical Linux distros
if [ "$TERM" != "dumb" ]; then
    # Green user@host, blue directory, $ at the end
    PS1='\[\e[0;32m\]\u@\h\[\e[0;34m\]\w\[\e[0m\]\$ '
fi

# ====== Misc ======
HISTCONTROL=ignoredups:erasedups
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend
