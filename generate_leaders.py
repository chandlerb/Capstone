from data_scrape import main
clean_db = {}
data_base = main()
for stat in data_base:
    for player in range(len(data_base[stat])):
        
        if data_base[stat][player][0] in clean_db:
            clean_db[data_base[stat][player][0]].append((stat, data_base[stat][player][1]))
        else: 
            clean_db[data_base[stat][player][0]] = [data_base[stat][player][2], (stat, data_base[stat][player][1])]

for player in clean_db:
    print(player, clean_db[player])