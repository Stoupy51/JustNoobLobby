
scoreboard players set #price lobby.data 200000

function lobby:signs/check_price

data modify storage lobby:main Item set value '[{"text":"un ","color":"white"},{"text":"Legendarium Helmet","color":"gold"},{"text":" !"}]'
execute if score #success lobby.data matches 1 run loot give @s loot stardust:i/legendarium_helmet

function lobby:signs/decode
