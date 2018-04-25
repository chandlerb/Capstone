from generate_leaders_db import get_db
database = get_db()

mvp = ""
mvp_t = 0

defense_mvp = ""
defense_t = 0

rookie = ""
rookie_t = 0

sixth_man = ""
sixth_man_t = 0

for player in database:
    mvp_new_total = 0
    defense_new_t = 0
    new_sixth_man = 0
    rookie_bool = False  
    sixth_man_bool = False

    for i in range(1, len(database[player])):
        
        # Handling MVP
        if database[player][i][0] == "minutes":
            mvp_new_total += database[player][i][1]*.2
        elif database[player][i][0] == "games_played":
            mvp_new_total += database[player][i][1]*.0
        elif database[player][i][0] == "points":
            mvp_new_total += database[player][i][1]*2
        elif database[player][i][0] == "assists":
            mvp_new_total += database[player][i][1]*2
        elif database[player][i][0] == "plus_minus":
            mvp_new_total += database[player][i][1]*5
        else: 
            mvp_new_total += database[player][i][1]

        #Handling Sixthman
        if database[player][i][0] == "games_played":
            sixth_man_bool = True 



        # Handling Rookie
        if database[player][i][0] == "rookie":
            rookie_bool = True
            mvp_new_total -= database[player][i][1] # Removing double point count 

        # Handeling Defense 
        if (database[player][i][0] == "rebounds" or 
            database[player][i][0] == "blocks" or 
            database[player][i][0] == "steals" or 
            database[player][i][0] == "minutes"):
            defense_new_t += database[player][i][1]

    # sixthman assertion
    if (sixth_man_bool and new_sixth_man > sixth_man_t):
        sixth_man = player
        sixth_man_t = new_sixth_man

    # rookie assertion
    if (rookie_bool and mvp_new_total > rookie_t):
        rookie = player
        rookie_t = mvp_new_total

    # defense assertion
    if (defense_new_t > defense_t):
        defense_mvp = player
        defense_t = defense_new_t

    # MVP assertion 
    if mvp_new_total > mvp_t:
        mvp = player
        mvp_t = mvp_new_total

    if new_sixth_man > sixth_man_t:
        sixth_man = player
        sixth_man_t = new_sixth_man

#file = open("MVP.txt", "w")
mvp_str = str(database[mvp])

print(database[mvp])
print()
print(database[defense_mvp])
print()
print(database[rookie])
print()
print(database[sixth_man])


#file.write(str(mvp) + " " + mvp_str + "\n" + str(mvp1) + " " + mvp_str1 + "\n" + str(mvp2) + " " + mvp_str2)

