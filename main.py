from dataManager import dataManager
from discordManager import discordManager
from pypresence import Presence
import psutil
import time

dataManager = dataManager()
discordManager = discordManager()
client_id = "358420454764969994" 
start_time = int(time.time())

i = 10
while i > 0:
    running = any(p.name().lower() == "isaac-ng.exe" for p in psutil.process_iter(["name"]))
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

    running = any(p.name().lower() == "isaac-ng.exe" for p in psutil.process_iter(["name"]))
    if not running:
        print("Gra została zamknięta, kończę działanie")
        break
