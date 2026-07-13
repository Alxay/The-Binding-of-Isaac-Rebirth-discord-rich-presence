from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time


class discordManager:
    def __init__(self):
        self.client_id = "358420454764969994"
        self.game_data = None
        self.RPC = Presence(self.client_id)
        self.RPC.connect()
        self.changes = {
            "???": "Blue_Baby",
            "The Lost": "The_Lost",
            "The Forgotten": "The_Forgotten",
            "Jacob and Esau": "Jacob_and_Esau",
        }
        self.rooms = {
            0:  "Null Room",
            1:  "Default Room",
            2:  "Shop Room",
            3:  "Error Room",
            4:  "Treasure Room",
            5:  "Boss Room",
            6:  "Miniboss Room",
            7:  "Secret Room",
            8:  "Super Secret Room",
            9:  "Arcade Room",
            10: "Curse Room",
            11: "Challenge Room",
            12: "Library Room",
            13: "Sacrifice Room",
            14: "Devil Room",
            15: "Angel Room",
            16: "Dungeon Room",
            17: "Boss Rush Room",
            18: "Isaac's Room",
            19: "Barren Room",
            20: "Chest Room",
            21: "Dice Room",
            22: "Black Market Room",
            23: "Greed Exit Room",
            24: "Planetarium Room",
            25: "Teleporter Room",
            26: "Teleporter Exit Room",
            27: "Secret Exit Room",
            28: "Blue Room",
            29: "Ultra Secret Room",
            30: "Deathmatch Room",
        }

    def updatePresence(self,game_data):
        self.game_data = game_data
        if game_data is None:
            self.RPC.clear()
            return
        
        if game_data.get("game_state") == 0:
            self.updatePresenceMenu()
            return
        elif game_data.get("game_state") == 2:
            self.updatePresencePause()
            return
        
        self.updatePresencePlaying()

    def updatePresencePlaying(self):
        coins = self.game_data.get("coins", 0)
        bombs = self.game_data.get("bombs", 0)
        keys = self.game_data.get("keys", 0)
        seed = self.game_data.get("seed", "Unknown")
        difficulty = self.game_data.get("difficulty", "Unknown")
        char_key = self.game_data.get("char_key", "default_character")
        floor_key = self.game_data.get("floor_key", "default_floor")
        damage = self.game_data.get("damage", 0)
        #move_speed = self.game_data.get("move_speed", 0)
        shotSpeed = self.game_data.get("shotSpeed", 0)
        hearts = self.game_data.get("hearts", 0)
        player_name = self.game_data.get("player_name", "Unknown")
        boss_id = self.game_data.get("boss_id", "Unknown")
        current_room = self.game_data.get("current_room", "Unknown")
        floor_name = self.game_data.get("floor_name", "Unknown")

        #print(f"https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Characters/{self.changes.get(player_name, player_name)}.png")

        self.RPC.update(
            activity_type=ActivityType.PLAYING,
            details = f"{hearts}❤️ |  {round(damage,2)}🗡️ | {round(shotSpeed,2)}💦",
            state = f"Coins: {coins} | Bombs: {bombs} | Keys: {keys}",
            #state = f"Coin: {coins}🪙 | Bomb: {bombs}💣 | Key: {keys}🔑",
            #state = f"{floor_name} | {self.rooms.get(current_room, 'Unknown Room')} | {difficulty}", 
            #https://github.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/blob/main/Images/Characters/playerportrait_apollyon.png
            #large_image = "https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Rooms/Default/Basement.png",
            large_image = self.getFloorImage(floor_name),
            large_text = f"{floor_name} | {self.rooms.get(current_room, 'Unknown Room')} ",
            small_image = f"https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Characters/{self.changes.get(player_name, player_name)}.png",
            small_text = f"{player_name}",
            #party_size = [2, 4],
            #name = "test",
        )   
    def updatePresenceMenu(self):
        self.RPC.update(
            activity_type=ActivityType.PLAYING,
            details = "In Menu",
            state = "Navigating menus",
    
        )

    def getFloorImage(floor_name):
        url_floor_name = floor_name.replace(" ", "_").replace("I","").replace("II","").replace("III","").replace("IV","").replace("V","").replace("VI","").replace("VII","").replace("VIII","").replace("IX","").replace("X","")
        floor_image_url = f"https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Rooms/Default/{url_floor_name}.png"
        return floor_image_url

    def updatePresencePause(self):
        self.RPC.update(
            activity_type=ActivityType.PLAYING,
            state = "Paused",
            details = "Game is paused",
        )