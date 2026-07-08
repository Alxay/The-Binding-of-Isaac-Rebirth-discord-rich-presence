from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time


class discordManager:
    def __init__(self):
        self.client_id = "358420454764969994"
        self.RPC = Presence(self.client_id)
        self.RPC.connect()
        self.rooms = {
            0: "Null",
            1: "Default",
            2: "Shop",
            3: "Error",
            4: "Treasure",
            5: "Boss",
            6: "Miniboss",
            7: "Secret",
            8: "Super Secret",
            9: "Arcade",
            10: "Curse",
            11: "Challenge",
            12: "Library",
            13: "Sacrifice",
            14: "Devil",
            15: "Angel",
            16: "Dungeon",          
            17: "Boss Rush",
            18: "Isaac's",
            19: "Barren",
            20: "Chest",
            21: "Dice",
            22: "Black Market",
            23: "Greed Exit",
            24: "Planetarium",
            25: "Teleporter",
            26: "Teleporter Exit",
            27: "Secret Exit",
            28: "Blue",
            29: "Ultra Secret",
            30: "Deathmatch",
        }

    def updatePresence(self,game_data):
        if game_data is None:
            self.RPC.clear()
            return
        coins = game_data.get("coins", 0)
        bombs = game_data.get("bombs", 0)
        keys = game_data.get("keys", 0)
        seed = game_data.get("seed", "Unknown")
        difficulty = game_data.get("difficulty", "Unknown")
        char_key = game_data.get("char_key", "default_character")
        floor_key = game_data.get("floor_key", "default_floor")
        damage = game_data.get("damage", 0)
        move_speed = game_data.get("move_speed", 0)
        hearts = game_data.get("hearts", 0)
        player_name = game_data.get("player_name", "Unknown")
        boss_id = game_data.get("boss_id", "Unknown")
        current_room = game_data.get("current_room", "Unknown")
        floor_name = game_data.get("floor_name", "Unknown")

        self.RPC.update(
            activity_type=ActivityType.PLAYING,
            state = f"{hearts}❤️ |  {round(damage,2)}🗡️ | {move_speed}👟",
            #state = f"Coins: {coins} | Bombs: {bombs} | Keys: {keys}",
            details = f"{floor_name} | {self.rooms.get(current_room, 'Unknown')} | {difficulty}",
            #party_size = [2, 4],
            #name = "test",
        )