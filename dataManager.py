import os
from pathlib import Path
import sys

import json
class dataManager:
    def getGameData(self,saveId = 1):
        exe_path = Path(sys.executable)
        drive = exe_path.drive
        save_path = os.path.join(f"{drive}\\Program Files (x86)\\Steam\\steamapps\\common\\The Binding of Isaac Rebirth\\data\\discordrichpresence", f"save{saveId}.dat")
        if os.path.exists(save_path):
            try:
                with open(save_path, "r", encoding="utf-8") as save_file:
                    game_data = json.load(save_file)
                print(game_data)
            except json.JSONDecodeError:
                game_data = None
                print(f"Nieprawidlowy lub pusty JSON w pliku: {save_path}")
        else:
            game_data = None
            print(f"Nie znaleziono pliku: {save_path}")
        return game_data