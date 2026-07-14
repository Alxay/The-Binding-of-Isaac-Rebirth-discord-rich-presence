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
        self.bosses = {1: {'name': 'Monstro', 'nameimage': 'BossName_20.0_Monstro.png'}, 2: {'name': 'Larry Jr.', 'nameimage': 'BossName_19.0_LarryJr.png'}, 3: {'name': 'Chub', 'nameimage': 'BossName_28.0_Chub.png'}, 4: {'name': 'Gurdy', 'nameimage': 'BossName_36.0_Gurdy.png'}, 5: {'name': 'Monstro II', 'nameimage': 'BossName_43.0_Monstro2.png'}, 6: {'name': 'Mom', 'nameimage': 'BossName_45.0_Mom.png'}, 7: {'name': 'Scolex', 'nameimage': 'BossName_62.1_Scolex.png'}, 8: {'name': "Mom's Heart", 'nameimage': 'BossName_78.0_MomsHeart.png'}, 9: {'name': 'Famine', 'nameimage': 'BossName_63.0_Famine.png'}, 10: {'name': 'Pestilence', 'nameimage': 'BossName_64.0_Pestilence.png'}, 11: {'name': 'War', 'nameimage': 'BossName_65.0_War.png'}, 12: {'name': 'Death', 'nameimage': 'BossName_66.0_Death.png'}, 13: {'name': 'Duke of Flies', 'nameimage': 'BossName_67.0_DukeOfFlies.png'}, 14: {'name': 'Peep', 'nameimage': 'BossName_68.0_Peep.png'}, 15: {'name': 'Loki', 'nameimage': 'BossName_69.0_Loki.png'}, 16: {'name': 'Blastocyst', 'nameimage': 'BossName_74.0_Blastocyst.png'}, 17: {'name': 'Gemini', 'nameimage': 'BossName_79.0_Gemini.png'}, 18: {'name': 'Fistula', 'nameimage': 'BossName_71.0_Fistula.png'}, 19: {'name': 'Gish', 'nameimage': 'BossName_43.1_Gish.png'}, 20: {'name': 'Steven', 'nameimage': 'BossName_79.1_Steven.png'}, 21: {'name': 'C.H.A.D.', 'nameimage': 'BossName_28.1_CHAD.png'}, 22: {'name': 'Headless Horseman', 'nameimage': 'BossName_82.0_HeadlessHorseman.png'}, 23: {'name': 'The Fallen', 'nameimage': 'BossName_81.0_TheFallen.png'}, 24: {'name': 'Satan', 'nameimage': 'BossName_84.0_Satan.png'}, 25: {'name': 'It Lives!', 'nameimage': 'BossName_78.1_ItLives.png'}, 26: {'name': 'The Hollow', 'nameimage': 'BossName_19.1_TheHollow.png'}, 27: {'name': 'The Carrion Queen', 'nameimage': 'BossName_28.2_CarrionQueen.png'}, 28: {'name': 'Gurdy Jr.', 'nameimage': 'BossName_99.0_GurdyJr.png'}, 29: {'name': 'The Husk', 'nameimage': 'BossName_67.1_TheHusk.png'}, 30: {'name': 'The Bloat', 'nameimage': 'BossName_68.1_Bloat.png'}, 31: {'name': 'Lokii', 'nameimage': 'BossName_69.1_Lokii.png'}, 32: {'name': 'The Blighted Ovum', 'nameimage': 'BossName_79.2_BlightedOvum.png'}, 33: {'name': 'Teratoma', 'nameimage': 'BossName_71.1_Teratoma.png'}, 34: {'name': 'The Widow', 'nameimage': 'BossName_100.0_Widow.png'}, 35: {'name': 'Mask of Infamy', 'nameimage': 'BossName_97.0_MaskOfInfamy.png'}, 36: {'name': 'The Wretched', 'nameimage': 'BossName_100.1_TheWretched.png'}, 37: {'name': 'Pin', 'nameimage': 'BossName_62.0_Pin.png'}, 38: {'name': 'Conquest', 'nameimage': 'BossName_65.1_Conquest.png'}, 39: {'name': 'Isaac', 'nameimage': 'PlayerName_01_Isaac.png'}, 40: {'name': '???', 'nameimage': 'BossName_102.1_BlueBaby.png'}, 41: {'name': 'Daddy Long Legs', 'nameimage': 'BossName_101.0_DaddyLongLegs.png'}, 42: {'name': 'Triachnid', 'nameimage': 'BossName_101.1_Triachnid.png'}, 43: {'name': 'The Haunt', 'nameimage': 'BossName_260.0_TheHaunt.png'}, 44: {'name': 'Dingle', 'nameimage': 'BossName_261.0_Dingle.png'}, 45: {'name': 'Mega Maw', 'nameimage': 'BossName_262.0_MegaMaw.png'}, 46: {'name': 'Mega Maw II', 'nameimage': 'BossName_263.0_MegaMaw2.png'}, 47: {'name': 'Mega Fatty', 'nameimage': 'BossName_264.0_MegaFatty.png'}, 48: {'name': 'Mega Fatty II', 'nameimage': 'BossName_265.0_Fatty2.png'}, 49: {'name': 'Mega Gurdy', 'nameimage': 'BossName_266.0_MamaGurdy.png'}, 50: {'name': 'Dark One', 'nameimage': 'BossName_267.0_DarkOne.png'}, 51: {'name': 'Dark One II', 'nameimage': 'BossName_268.0_DarkOne2.png'}, 52: {'name': 'Polycephalus', 'nameimage': 'BossName_269.0_Polycephalus.png'}, 53: {'name': 'Mega Fred', 'nameimage': 'BossName_270.0_MegaFred.png'}, 54: {'name': 'The Lamb', 'nameimage': 'BossName_273.0_TheLamb.png'}, 55: {'name': 'Mega Satan', 'nameimage': 'BossName_274.0_MegaSatan.png'}, 56: {'name': 'Gurglings', 'nameimage': 'BossName_276.0_Gurglings.png'}, 57: {'name': 'The Stain', 'nameimage': 'BossName_401.0_TheStain.png'}, 58: {'name': 'Brownie', 'nameimage': 'BossName_402.0_Brownie.png'}, 59: {'name': 'The Forsaken', 'nameimage': 'BossName_403.0_TheForsaken.png'}, 60: {'name': 'Little Horn', 'nameimage': 'BossName_404.0_LittleHorn.png'}, 61: {'name': 'Rag Man', 'nameimage': 'BossName_405.0_RagMan.png'}, 62: {'name': 'Ultra Greed', 'nameimage': 'BossName_406.0_UltraGreed.png'}, 63: {'name': 'Hush', 'nameimage': 'BossName_407.0_Hush.png'}, 64: {'name': 'Dangle', 'nameimage': 'BossName_Dangle.png'}, 65: {'name': 'Turdling', 'nameimage': 'BossName_Turdlings.png'}, 66: {'name': 'The Frail', 'nameimage': 'BossName_TheFrail.png'}, 67: {'name': 'Rag Mega', 'nameimage': 'BossName_RagMega.png'}, 68: {'name': 'Sisters Vis', 'nameimage': 'BossName_SisterssVis.png'}, 69: {'name': 'Big Horn', 'nameimage': 'BossName_BigHorn.png'}, 70: {'name': 'Delirium', 'nameimage': 'BossName_Delirium.png'}, 71: {'name': 'Ultra Greedier', 'nameimage': 'BossName_406.0_UltraGreed.png'}, 72: {'name': 'The Matriarch', 'nameimage': 'BossName_Matriarch.png'}, 73: {'name': 'The Pile', 'nameimage': 'BossName_Polycephalus2.png'}, 74: {'name': 'Reap Creep', 'nameimage': 'BossName_ReapCreep.png'}, 75: {'name': 'Beelzeblub', 'nameimage': 'BossName_Beelzeblub.png'}, 76: {'name': 'Wormwood', 'nameimage': 'BossName_Wormwood.png'}, 77: {'name': 'The Rainmaker', 'nameimage': 'BossName_Rainmaker.png'}, 78: {'name': 'The Visage', 'nameimage': 'BossName_Visage.png'}, 79: {'name': 'The Siren', 'nameimage': 'BossName_Siren.png'}, 80: {'name': 'Tuff Twins', 'nameimage': 'BossName_TuffTwins.png'}, 81: {'name': 'The Heretic', 'nameimage': 'BossName_Heretic.png'}, 82: {'name': 'Hornfel', 'nameimage': 'BossName_Hornfel.png'}, 83: {'name': 'Great Gideon', 'nameimage': 'BossName_Gideon.png'}, 84: {'name': 'Baby Plum', 'nameimage': 'BossName_BabyPlum.png'}, 85: {'name': 'The Scourge', 'nameimage': 'BossName_Scourge.png'}, 86: {'name': 'Chimera', 'nameimage': 'BossName_Chimera.png'}, 87: {'name': 'Rotgut', 'nameimage': 'BossName_Rotgut.png'}, 88: {'name': 'Mother', 'nameimage': 'BossName_Mother.png'}, 89: {'name': 'Mom (Mausoleum)', 'nameimage': 'BossName_45.0_Mom.png'}, 90: {'name': "Mom's Heart (Mausoleum)", 'nameimage': 'BossName_78.0_MomsHeart.png'}, 91: {'name': 'Min-Min', 'nameimage': 'BossName_MinMin.png'}, 92: {'name': 'Clog', 'nameimage': 'BossName_Clog.png'}, 93: {'name': 'Singe', 'nameimage': 'BossName_Singe.png'}, 94: {'name': 'Bumbino', 'nameimage': 'BossName_Bumbino.png'}, 95: {'name': 'Colostomia', 'nameimage': 'BossName_Colostomia.png'}, 96: {'name': 'The Shell', 'nameimage': 'BossName_Shell.png'}, 97: {'name': 'Turdlet', 'nameimage': 'BossName_Turdlet.png'}, 98: {'name': 'Raglich', 'nameimage': 'BossName_Raglich.png'}, 99: {'name': 'Dogma', 'nameimage': 'BossName_Dogma.png'}, 100: {'name': 'The Beast', 'nameimage': 'BossName_The_Beast.png'}, 101: {'name': 'Horny Boys', 'nameimage': 'BossName_HornyBoys.png'}, 102: {'name': 'Clutch', 'nameimage': 'BossName_Clutch.png'}, 103: {'name': 'Cadavra', 'nameimage': 'BossName_Cadavra.png'}}

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
        if boss_id != 0 and boss_id in self.bosses:
            #https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Bosses/portrait_67.0_dukeofflies.png
            #https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Bosses/BossName_67.0_DukeOfFlies.png
            large_image_url = self.getBossImage(boss_id)
            boss_name = self.bosses[boss_id]["name"]
            text_large = f"{boss_name} | {floor_name}"
        else:
            large_image_url = self.getFloorImage(floor_name)
            text_large = f"{floor_name} | {self.rooms.get(current_room, 'Unknown Room')} "
        #print("BOSS ID: {}".format(boss_id))
        print(large_image_url)

        #print(f"https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Characters/{self.changes.get(player_name, player_name)}.png")

        self.RPC.update(
            activity_type=ActivityType.PLAYING,
            details = f"{hearts}❤️ |  {round(damage,2)}🗡️ | {round(shotSpeed,2)}💦",
            state = f"Coins: {coins} | Bombs: {bombs} | Keys: {keys}",
            #state = f"Coin: {coins}🪙 | Bomb: {bombs}💣 | Key: {keys}🔑",
            #state = f"{floor_name} | {self.rooms.get(current_room, 'Unknown Room')} | {difficulty}", 
            #https://github.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/blob/main/Images/Characters/playerportrait_apollyon.png
            #large_image = "https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Rooms/Default/Basement.png",
            large_image = large_image_url,
            large_text = text_large,
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

    def getFloorImage(self, floor_name):
        url_floor_name = floor_name.replace("I","").replace("II","").replace("III","").replace("IV","").replace("V","").replace("VI","").replace("VII","").replace("VIII","").replace("IX","").replace("X","").replace(" ", "_").replace(" ","").rstrip("_").replace("???","Blue_Womb")
        floor_image_url = f"https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Rooms/Default/{url_floor_name}.png"
        return floor_image_url
    
    def getBossImage(self, boss_id):
        if boss_id in self.bosses:
            image_name = self.bosses[boss_id]["nameimage"].lower().replace("bossname","portrait")
            boss_image_url = f"https://raw.githubusercontent.com/Alxay/The-Binding-of-Isaac-Rebirth-discord-rich-presence/refs/heads/main/Images/Bosses/{image_name}"
            return boss_image_url
        else:
            return None

    def updatePresencePause(self):
        self.RPC.update(
            activity_type=ActivityType.PLAYING,
            state = "Paused",
            details = "Game is paused",
        )