#!/bin/bash
if kill "$(pgrep python -af | grep 'mods/The-Binding-of-Isaac-Rebirth-discord-rich-presence/main.py' | awk '{print $1}')"; then
	echo "existing process was killed"
fi
cd "$STEAM_COMPAT_INSTALL_PATH"
python mods/The-Binding-of-Isaac-Rebirth-discord-rich-presence/main.py > /testfile &
