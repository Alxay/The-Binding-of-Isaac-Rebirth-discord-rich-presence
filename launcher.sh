#!/bin/bash
if kill "$(pgrep python -af | grep 'mods/the-binding-of-isaac-rebirth-discord-rich-presence/main.py' | awk '{print $1}')"; then
	echo "existing process was killed"
fi

cd "$(dirname "$0")" || exit 1
./venv/bin/python main.py &



