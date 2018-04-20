from generate_leaders_db import get_db
database = get_db()

mvp = ""
mvp_t = 0
mvp1 = ""
mvp_t1 = 0
mvp2 = ""
mvp_t2 = 0

for player in database:
    mvp_new_total = 0
    for i in range(1, len(database[player])):
        mvp_new_total += database[player][i][1]

    if mvp_new_total > mvp_t :
        mvp2 = mvp1
        mvp_t2 = mvp_t1
        mvp1 = mvp
        mvp_t1 = mvp_t
        mvp = player
        mvp_t = mvp_new_total
    elif mvp_new_total > mvp_t1:
        mvp2 = mvp1
        mvp_t2 = mvp_t1
        mvp1 = player
        mvp_t1 = mvp_new_total
    elif mvp_new_total > mvp_t2:
        mvp2 = player
        mvp_t2 = mvp_new_total


file = open("MVP.txt", "w")
mvp_str = str(database[mvp])
mvp_str1 = str(database[mvp1])
mvp_str2 = str(database[mvp2])

file.write(str(mvp) + " " + mvp_str + "\n" + str(mvp1) + " " + mvp_str1 + "\n" + str(mvp2) + " " + mvp_str2)

