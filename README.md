# Discord Rich Presence for The Binding of Isaac: Rebirth

A mod that displays rich presence information in Discord while playing The Binding of Isaac: Rebirth.

## Features

- **Live Game Status**: Display current floor, room type, and difficulty in your Discord status
- **Player Stats**: Show player damage, move speed, and health in real-time
- **Resources Tracking**: Display coins, bombs, and keys
- **Seed Information**: Share the current run's seed (Not shown by default)
- **Boss Detection**: Show when you're facing a boss (Not shown by default)
- **Difficulty Indication**: Display difficulty level (Normal, Hard, Greed, Greedier)

## Project Structure

- **main.lua** - Lua mod that collects game data from Isaac
- **main.py** - Python script that manages Discord integration and updates presence
- **dataManager.py** - Handles game data collection and formatting
- **discordManager.py** - Manages Discord API communication
- **metadata.xml** - Mod metadata for Isaac mod loader

## Requirements

- The Binding of Isaac: Rebirth
- Python 3.x
- pypresence library (`pip install pypresence`)
- Lua 5.3+

## Installation

1. Clone or download this mod into your Isaac mods directory:
   - Windows: `C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods\`

2. Install Python dependencies:
   ```bash
   pip install pypresence
   ```

3. Start Isaac - the mod will automatically load

4. Run the Python script to sync with Discord:
   ```bash
   python main.py
   ```

## How It Works

1. The Lua mod (`main.lua`) hooks into Isaac's game loop and collects player/room/difficulty data every 30 frames
2. The Python script (`main.py`) reads this data and updates your Discord Rich Presence status
3. Discord displays the information in your profile and to your friends

## Configuration

The Discord Application ID is configured in `main.py`:
```python
client_id = "358420454764969994"
```

## Build and Test

Run tests using Maven:
```bash
mvn test
```

Verify the build:
```bash
mvn verify
```

## Version

Current version: 0.0.1

## License

Public mod for The Binding of Isaac: Rebirth community
