from datamanager import dataManager #lower case letters only, game for some reason lower cases everything in the game folder
from discordmanager import discordManager #same case as above
from pypresence import Presence
import psutil
import time

dataManager = dataManager()
discordManager = discordManager()
client_id = "358420454764969994" 
start_time = int(time.time())

i = 30
while i > 0:
    running = any(p.name().lower() == "isaac.x64" for p in psutil.process_iter(["name"])) #different proccess name than on widnows
    i -= 1
    print("Waiting for the game to start... ({}s)".format(i))
    time.sleep(1)
    if running:
        break

while True:
    game_data = dataManager.getGameData()
    if game_data != discordManager.game_data:
        print("Powiadamiam discord")
        discordManager.updatePresence(game_data)
    time.sleep(2)

    running = any(p.name().lower() == "isaac.x64" for p in psutil.process_iter(["name"])) #different proccess name than on widnows
    if not running:
        print("Gra została zamknięta, kończę działanie")
        break
