# Discord Rich Presence for The Binding of Isaac: Rebirth

Show your current Isaac run directly in Discord Rich Presence.

## What This Mod Shows

- Current floor and room type
- Difficulty (Normal, Hard, Greed, Greedier)
- Player stats (damage, shoot speed, health)
- Resources (coins, bombs, keys)
- Optional: seed and boss status

---

# 🪟 Windows

## Download

[![Latest Release](https://img.shields.io/github/v/release/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence?style=for-the-badge&logo=github)](https://github.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/total?style=for-the-badge&label=%E2%AC%87%EF%B8%8F%20DOWNLOADS&color=2ea44f)](https://github.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/releases)

## Installation

### Option 1 (Recommended) – Installer

Download and run **installer.exe** from the latest release. The installer will automatically set up the mod for you.

### Option 2 – Manual Installation

1. Download the ZIP from the latest release.
2. Extract it to:

```
C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods
```

3. If your Steam library is on another drive, replace the drive letter (for example `C:` → `D:`).

## Steam Launch Options (Required)

Open:

```
The Binding of Isaac: Rebirth → Properties → Launch Options
```

Paste:

```text
"C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods\discordrichpresence\launcher\launcher.exe" %command%
```

### Important

- Keep the quotes around the full path.
- Keep `%command%` exactly as shown.
- If your Steam library is on another drive, change the drive letter accordingly.

### Requirements

- The Binding of Isaac: Rebirth
- Discord desktop app running

---

# 🐧 Linux

## Download

Clone the Linux branch directly into your Isaac `mods` directory:

```bash
git clone -b linux --single-branch https://github.com/Alxay/the-binding-of-isaac-rebirth-discord-rich-presence.git
```

Clone it into:

```text
/home/[YOUR USERNAME]/.steam/debian-installation/steamapps/common/The Binding of Isaac Rebirth/mods
```

Replace `[YOUR USERNAME]` with your actual username.

## Installation

Create a Python virtual environment and install the required dependencies:

```bash
cd "/home/[YOUR USERNAME]/.steam/debian-installation/steamapps/common/The Binding of Isaac Rebirth/mods/the-binding-of-isaac-rebirth-discord-rich-presence"

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Steam Launch Options (Required)

Open:

```
The Binding of Isaac: Rebirth → Properties → Launch Options
```

Paste:

```text
"$STEAM_COMPAT_INSTALL_PATH/mods/The-Binding-of-Isaac-Rebirth-discord-rich-presence/launcher.sh" && %command%
```

### Important

- Keep the quotes around the full path.
- Keep `%command%` exactly as shown.
- Replace `[YOUR USERNAME]` with your actual username.
- Make sure you have created the Python virtual environment before launching the game.

### Requirements

- Python 3
- The Binding of Isaac: Rebirth
- Discord desktop app running

---

## How It Works

1. The Lua part of the mod collects run data in-game.
2. The launcher starts the Python integration.
3. Discord Rich Presence is updated while you play.

---

## Troubleshooting

### No Rich Presence visible
- Re-check your Steam Launch Options and path spelling.
- Make sure the mod is enabled in the in-game Mods menu.
- Make sure the Discord **desktop** app is running (browser version is not supported).
- Open the debug console (`~`) and check for any errors.
- Check the game log for any `[discordrichpresence]` entries or error messages.
  - **Windows:** `Documents\My Games\Binding of Isaac Repentance+\log.txt`
  - Search for `discordrichpresence` using `Ctrl + F`.
  - If there are no matching entries, the mod is most likely not being loaded.
- If you play without Repentance, you may need to modify `main.lua` (remove the `player:GetRotterHearts()` call because that function does not exist in Afterbirth and will cause a crash).

### Windows
- Verify the launcher path.
- If Steam is installed on another drive, update the drive letter.

### Linux
- Verify you replaced `[YOUR USERNAME]` with your username.
- Make sure the Python virtual environment has been created.
- Run `./launcher.sh` from the mod directory to check for errors.

### Mod not loading

- Verify the mod folder is located inside the game's `mods` directory.

---

## Asset Note

This repository includes images and other game-related assets from **The Binding of Isaac: Rebirth** and its related materials. Those assets are owned by Nicalis Inc. and/or Edmund McMillen.

---

## Version

Current version: **0.0.5**
