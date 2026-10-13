#!/usr/bin/env bash
# Install verygoodplugins/whatsapp-mcp on macOS and link WhatsApp with a
# phone-number pairing code (no QR scan).
#
#   curl -fsSL https://raw.githubusercontent.com/alflayyeh/gifs-n-stuff/claude/wizardly-galileo-lm5fld/whatsapp-mcp/setup-mac.sh | bash -s -- +15551234567
set -euo pipefail

PHONE="${1:-}"
if [ -z "$PHONE" ]; then
  echo "usage: $0 <phone number with country code, e.g. +15551234567>" >&2
  exit 1
fi

DIR="${WHATSAPP_MCP_DIR:-$HOME/whatsapp-mcp}"
PATCH_URL="https://raw.githubusercontent.com/alflayyeh/gifs-n-stuff/claude/wizardly-galileo-lm5fld/whatsapp-mcp/pair-phone.patch"

if ! command -v brew >/dev/null; then
  echo "Homebrew is required: https://brew.sh" >&2
  exit 1
fi
command -v go >/dev/null || brew install go
command -v uv >/dev/null || brew install uv
command -v ffmpeg >/dev/null || brew install ffmpeg

if [ ! -d "$DIR/.git" ]; then
  git clone https://github.com/verygoodplugins/whatsapp-mcp "$DIR"
fi
cd "$DIR"
if ! grep -q 'pair-phone' whatsapp-bridge/main.go; then
  curl -fsSL "$PATCH_URL" | git apply
fi

cd whatsapp-bridge
go build -o whatsapp-bridge .

# Register the MCP server with Claude Code and Claude Desktop.
SERVER_DIR="$DIR/whatsapp-mcp-server"
if command -v claude >/dev/null; then
  claude mcp add --scope user whatsapp -- uv --directory "$SERVER_DIR" run main.py || true
fi
DESKTOP_CFG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
if [ -d "$(dirname "$DESKTOP_CFG")" ]; then
  python3 - "$DESKTOP_CFG" "$SERVER_DIR" <<'PY'
import json, os, sys
path, server_dir = sys.argv[1], sys.argv[2]
cfg = json.load(open(path)) if os.path.exists(path) else {}
cfg.setdefault("mcpServers", {})["whatsapp"] = {
    "command": "uv", "args": ["--directory", server_dir, "run", "main.py"]}
json.dump(cfg, open(path, "w"), indent=2)
PY
fi

echo
echo "Starting the bridge. When PAIRING CODE appears, open WhatsApp on your phone:"
echo "  Settings > Linked Devices > Link a Device > Link with phone number instead"
echo "and type the code. Keep this terminal open (or run scripts/install-launchd-macos.sh"
echo "afterwards to keep the bridge running in the background)."
echo
WHATSAPP_DEVICE_NAME="Claude WhatsApp MCP" exec ./whatsapp-bridge --pair-phone "$PHONE"
