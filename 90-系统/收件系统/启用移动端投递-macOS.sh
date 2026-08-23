#!/bin/zsh
# One-time activation on the macOS primary host.
# It refuses non-fast-forward updates so local work is never overwritten.
set -euo pipefail

VAULT="/Users/mac/Documents/Obsidian Vault"
AGENT_SOURCE="$VAULT/90-系统/收件系统/com.personal.second-brain.plist"
AGENT_TARGET="$HOME/Library/LaunchAgents/com.personal.second-brain.plist"
LABEL="com.personal.second-brain"
USER_DOMAIN="gui/$(id -u)"

if [[ ! -d "$VAULT/.git" ]]; then
  print -u2 "未找到主机知识库：$VAULT"
  exit 1
fi

git -C "$VAULT" pull --ff-only origin main
install -d "$HOME/Library/LaunchAgents"
install -m 644 "$AGENT_SOURCE" "$AGENT_TARGET"
launchctl bootout "$USER_DOMAIN/$LABEL" 2>/dev/null || true
launchctl bootstrap "$USER_DOMAIN" "$AGENT_TARGET"
launchctl kickstart -k "$USER_DOMAIN/$LABEL"

print "移动端投递已启用。主机将在每日收件前只读处理 windows-inbox。"
