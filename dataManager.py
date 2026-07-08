import os
import json
class dataManager:
    def getGameData(self,saveId = 1):
        save_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "discordrichpresence", f"save{saveId}.dat")
        if os.path.exists(save_path):
            with open(save_path, "r", encoding="utf-8") as save_file:
                game_data = json.load(save_file)
            print(game_data)
        else:
            game_data = None
            print(f"Nie znaleziono pliku: {save_path}")
        return game_data