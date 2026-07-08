from dataManager import dataManager
from discordManager import discordManager
from pypresence import Presence
import time

dataManager = dataManager()
discordManager = discordManager()
client_id = "358420454764969994" 
start_time = int(time.time())

while True:
    game_data = dataManager.getGameData()
    if game_data != discordManager.game_data:
        print("Powiadamiam discord")
        discordManager.updatePresence(game_data)
    time.sleep(2)
