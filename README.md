# Discord Rich Presence for The Binding of Isaac: Rebirth

Show your current Isaac run directly in Discord Rich Presence.

## What This Mod Shows

- Current floor and room type
- Difficulty (Normal, Hard, Greed, Greedier)
- Player stats (damage, move speed, health)
- Resources (coins, bombs, keys)
- Optional: seed and boss status

## Download

Just `git clone -b linux --single-branch https://github.com/Alxay/the-binding-of-isaac-rebirth-discord-rich-presence.git` into this folder:

```
/home/[YOUR USERNAME]/.steam/debian-installation/steamapps/common/The Binding of Isaac Rebirth/mods
```

Remember to change `[YOUR USERNAME]` to your actual username.

After downloading the repo, create a Python virtual environment and install the required dependencies:

```bash
cd "/home/[YOUR USERNAME]/.steam/debian-installation/steamapps/common/The Binding of Isaac Rebirth/mods/the-binding-of-isaac-rebirth-discord-rich-presence"

python3 -m venv venv

source venv/bin/activate

pip install -r ./requirements
```

## Steam Launch Options (Required)

In Steam, open:

`The Binding of Isaac: Rebirth -> Properties -> Launch Options`

Paste this value:

```
"$STEAM_COMPAT_INSTALL_PATH/mods/The-Binding-of-Isaac-Rebirth-discord-rich-presence/launcher.sh" && %command%
```

Important:

- Keep the quotes around the full path.
- Keep `%command%` exactly as shown.
- Remember to change `[YOUR USERNAME]` to your actual username.
- MAKE SURE YOU'VE CREATED VENV


## Requirements
- python
- The Binding of Isaac: Rebirth
- Discord desktop app running

## Asset Note

This repository includes images and other game-related assets from The Binding of Isaac: Rebirth and its related materials. Those assets are owned by Nicalis Inc. and/or Edmund McMillen.

## How It Works

1. The Lua part of the mod collects run data in-game.
2. The launcher starts the Python integration.
3. Discord Rich Presence is updated while you play.

## Troubleshooting

Remember that you can run ./launcher.sh from the mod's directory to check for any problems.
- No Rich Presence visible:
  - Make sure Discord is running.
  - Re-check Steam Launch Options and path spelling.
  - Confirm you changed [YOUR USERNAME] to your username.
  - Make sure you've created venv
- Mod not loading:
  - Verify the extracted folder is inside the `mods` directory.

## Version

Current version: `0.0.5`
