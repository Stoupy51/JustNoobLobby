
# Reset the timestamp to 0
scoreboard players set seconds jn_lobby.timestamp 0

# Start the loop at 1 billion (Length of the value is 10)
scoreboard players set #multiplier jn_lobby.data 1000000000
execute if data storage suso.str:io out.time[0] run function jn_lobby:utils/update_timestamp_loop

