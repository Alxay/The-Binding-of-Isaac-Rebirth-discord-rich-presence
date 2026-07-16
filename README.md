# Discord Rich Presence for The Binding of Isaac: Rebirth

Show your current Isaac run directly in Discord Rich Presence.

## What This Mod Shows

- Current floor and room type
- Difficulty (Normal, Hard, Greed, Greedier)
- Player stats (damage, move speed, health)
- Resources (coins, bombs, keys)
- Optional: seed and boss status

## Download

Just `git pull` the repo into this folder:

```
/home/[YOUR USERNAME]/.local/share/binding of isaac afterbirth+ mods
```

Remember to change `[YOUR USERNAME]` to your actual username.

After downloading the repo, create a Python virtual environment and install the required dependencies:

```bash
cd "/home/[YOUR USERNAME]/.local/share/binding of isaac afterbirth+ mods/the-binding-of-isaac-rebirth-discord-rich-presence"

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Steam Launch Options (Required)

In Steam, open:

`The Binding of Isaac: Rebirth -> Properties -> Launch Options`

Paste this value:

```
"/home/[YOUR USERNAME]/.local/share/binding of isaac afterbirth+ mods/the-binding-of-isaac-rebirth-discord-rich-presence/launcher.sh" && %command%
```

Important:

- IF YOU HAVE REPENTANCE INSTALLED GO TO LINE 21, COMMENT IT (`--`) AND UNCOMMENT LINE 23.
- Keep the quotes around the full path.
- Keep `%command%` exactly as shown.
- Remember to change `[YOUR USERNAME]` to your actual username.


## Requirements

- The Binding of Isaac: Rebirth
- Discord desktop app running

## Asset Note

This repository includes images and other game-related assets from The Binding of Isaac: Rebirth and its related materials. Those assets are owned by Nicalis Inc. and/or Edmund McMillen.

## How It Works

1. The Lua part of the mod collects run data in-game.
2. The launcher starts the Python integration.
3. Discord Rich Presence is updated while you play.

## Troubleshooting

- No Rich Presence visible:
  - Make sure Discord is running.
  - Re-check Steam Launch Options and path spelling.
  - Confirm you changed [YOUR USERNAME] to your username.
- Mod not loading:
  - Verify the extracted folder is inside the `mods` directory.

## Version

Current version: `0.0.5`
