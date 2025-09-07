# i was experimenting with Docker images and replacing them with instead of using VMs and I created this file so that I can have a consistent .bashrc with the correct PATH in place

# ~/.bashrc for ax0ryn (Docker CTF image)

# ====== PATH ======
# Start with system PATH
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH"
# Append ~/.local/bin after system PATH
export PATH="$PATH:$HOME/.local/bin"

# ====== Aliases ======
alias ll='ls -alF --color=auto'
alias la='ls -A --color=auto'
alias l='ls -CF --color=auto'
alias grep='grep --color=auto'

# Replace ls with exa if installed
if command -v exa &> /dev/null; then
    alias ls='exa --group-directories-first --icons'
fi

# ====== Prompt ======
PS1='[\u@\h \W]\$ '

# ====== Git ======
git config --global core.editor "nano"
