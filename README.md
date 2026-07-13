# Discord Rich Presence for The Binding of Isaac: Rebirth

Show your current Isaac run directly in Discord Rich Presence.

## What This Mod Shows

- Current floor and room type
- Difficulty (Normal, Hard, Greed, Greedier)
- Player stats (damage, move speed, health)
- Resources (coins, bombs, keys)
- Optional: seed and boss status

## Download

[![Latest Release](https://img.shields.io/github/v/release/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence?style=for-the-badge&logo=github)](https://github.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/releases/latest) [![Downloads](https://img.shields.io/github/downloads/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/total?style=for-the-badge&label=%E2%AC%87%EF%B8%8F%20DOWNLOADS&color=2ea44f)](https://github.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/releases)

## Installation (Windows)

1. Download the ZIP from the release page above.
2. Extract the ZIP to:

   `C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods`

3. If your Steam library is on another drive, replace the drive letter in path (for example `C:` -> `D:`).

## Steam Launch Options (Required)

In Steam, open:

`The Binding of Isaac: Rebirth -> Properties -> Launch Options`

Paste this value:

`"C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods\discordrichpresence\launcher\launcher.exe" %command%`

Important:

- Keep the quotes around the full path.
- Keep `%command%` exactly as shown.
- If your game is installed on a different drive, change the drive letter (for example `C:` -> `D:`).

## Requirements

- The Binding of Isaac: Rebirth
- Discord desktop app running
- Windows

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
  - Confirm you changed the drive letter if needed.
- Mod not loading:
  - Verify the extracted folder is inside the `mods` directory.

## Version

Current version: `0.0.3`
