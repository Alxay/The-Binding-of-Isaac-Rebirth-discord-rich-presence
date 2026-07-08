local DRPMod = RegisterMod("Discord Rich Presence", 1)
local json = require("json")

local frameCounter = 0

function DRPMod:OnUpdate()
    frameCounter = frameCounter + 1
    
    if frameCounter % 30 == 0 then
        local player = Isaac.GetPlayer(0)
        local game = Game()
        local room = game:GetRoom()
        local level = game:GetLevel()
        
        if player and game then
            -- 0. GRACZ
            local damage = player.Damage
            local moveSpeed = player.MoveSpeed
            --                   red + bone             soul + black                  rotten                                 eternal
            local heartsAmount = (player:GetHearts() + player:GetSoulHearts() + player:GetRottenHearts() + player:GetEternalHearts()) * 0.5
            local playerName = player:GetName()

            -- 1. ZASOBY
            local currentCoins = player:GetNumCoins()
            local currentBombs = player:GetNumBombs()
            local currentKeys = player:GetNumKeys()
            
            -- 2. GRA
            local floorName = level:GetName()
            local currentRoom = room:GetType()
            local bossId = room:GetBossID()
            local seedString = game:GetSeeds():GetStartSeedString()
        
            
            -- 3. POZIOM TRUDNOŚCI
            local diffString = "Normal"
            if game.Difficulty == 1 then
                diffString = "Hard"
            elseif game.Difficulty == 2 then
                diffString = "Greed"
            elseif game.Difficulty == 3 then
                diffString = "Greedier"
            end
        

            
            -- 4. KLUCZE GRAFIK
            -- local charId = player:GetPlayerType()
            -- local stageId = level:GetStage()
            
            -- local charImageKey = "char_" .. tostring(charId)
            -- local floorImageKey = "floor_" .. tostring(stageId)
            
            -- 5. PAKOWANIE DANYCH
            local dataToSave = {
                coins = currentCoins,
                bombs = currentBombs,
                keys = currentKeys,
                seed = seedString,
                difficulty = diffString,
                --char_key = charImageKey,
                --floor_key = floorImageKey,
                damage = damage,
                move_speed = moveSpeed,
                hearts = heartsAmount,
                player_name = playerName,
                boss_id = bossId,
                current_room = currentRoom,
                floor_name = floorName,
                game_state = 1
            }
            
            -- 6. WYSYŁKA
            local jsonText = json.encode(dataToSave)
            DRPMod:SaveData(jsonText)
        end
    end 
end

DRPMod:AddCallback(ModCallbacks.MC_POST_UPDATE, DRPMod.OnUpdate)
DRPMod:AddCallback(ModCallbacks.MC_PRE_GAME_EXIT, function(_, shouldSave)
    DRPMod:SaveData(json.encode({game_state = 0}))
end)
