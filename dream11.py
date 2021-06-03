wicket_keeper = list( input('Enter player name and his credit score : ').split(" ") for i in range(int(input("How many no. of wicket keeper you want to enter : "))))
Batsmen = list( input('Enter player name and his credit score : ').split(" ") for i in range(int(input("How many no. of batsmen you want to enter : "))))
All_rounder = list( input('Enter player name and his credit score : ').split(" ") for i in range(int(input("How many no. of all rounder you want to enter : "))))
Baller = list( input('Enter player name and his credit score : ').split(" ") for i in range(int(input("How many no. of baller you want to enter : "))))

count1 = 0
for i in wicket_keeper:
    if len(i) > 2:
        wicket_keeper.remove(i)
        count1 +=1

count2 = 0
for i in Batsmen:
    if len(i) > 2:
        Batsmen.remove(i)
        count2 +=1

count3 = 0
for i in All_rounder:
    if len(i) > 2:
        All_rounder.remove(i)
        count3 +=1

count4 = 0
for i in Baller:
    if len(i) > 2:
        Baller.remove(i)
        count4 +=1



from itertools import combinations

wk_comn = list(combinations(wicket_keeper, int(input('how many WK you want in your team : '))))
bat_comn = list(combinations(Batsmen, int(input('how many batsmen you want in your team : '))))
all_comn = list(combinations(All_rounder, int(input('how AR WK you want in your team : '))))
ball_comn = list(combinations(Baller, int(input('how many bowlers you want in your team : '))))





wk_credits = []
for i in wk_comn:
    temp = []
    sums = 0
    for j in i:
        sums = sums + float(j[1])
        temp.append(j[0])
    wk_credits.append([temp, sums])

# print(wk_credits)

bat_credits = []
for i in bat_comn:
    temp = []
    sums = 0
    for j in i:
        sums = sums + float(j[1])
        temp.append(j[0])
    bat_credits.append([temp, sums])

# print(bat_credits)

all_credits = []
for i in all_comn:
    temp = []
    sums = 0
    for j in i:
        sums = sums + float(j[1])
        temp.append(j[0])
    all_credits.append([temp, sums])

# print(all_credits)

ball_credits = []
for i in ball_comn:
    temp = []
    sums = 0
    for j in i:
        sums = sums + float(j[1])
        temp.append(j[0])
    ball_credits.append([temp, sums])

# print(ball_credits)



print("================================================================================================================================================")

final_teams = []
for i in wk_credits:
    for j in bat_credits:
        for k in all_credits:
            for l in ball_credits:
                if i[1]+j[1]+k[1]+l[1] <= 100:
                    # final_quads.append([ i[1], j[1], k[1], l[1] ])
                    final_teams.append([i[0] + j[0]+ k[0]+ l[0], i[1] + j[1] + k[1] + l[1]])
# print(final_quads)
for i in final_teams:
    print('{}, total credit used : {}'.format(i[0], i[1]))
print("================================================================================================================================================")
print("Total possible teams  : " , len(final_teams))





# a = int(input())
# Wk  = list(range(1,a+1))

# Bat = [3,4,5]
# All = [1,2,3,4]
# Ball = [3,4,5]

# final = []
# for i in Wk:
#     for j in Bat:
#         for k in All:
#             for l in Ball:
#                 if i+j+k+l == 11:
#                     final.append([i,j,k,l])

# print(final)

# print("================================================================================================================================================")

# wicket_keeper = [10.5,9]
# Batsmen = [9.5,8.5,8.5]
# All_rounder = [9,8.5,9.5]
# Baller = [9,9,8.5,8.5,8]

# [1, 3, 2, 5], [1, 3, 3, 4], [1, 3, 4, 3], [1, 4, 1, 5], [1, 4, 2, 4], [1, 4, 3, 3], [1, 5, 1, 4], [1, 5, 2, 3], [2, 3, 1, 5], [2, 3, 2, 4], [2, 3, 3, 3], [2, 4, 1, 4], [2, 4, 2, 3], [2, 5, 1, 3]

# print(wk_comn)
# print(bat_comn)
# print(all_comn)
# print(ball_comn)

# print("================================================================================================================================================")


# wk_credits = []
# for i in wk_comn:
#     wk_credits.append(sum(list(i[1])))
# print(wk_credits)

# bat_credits = []
# for i in bat_comn:
#     bat_credits.append(sum(list(i[1])))
# print(bat_credits)

# all_credits = []
# for i in all_comn:
#     all_credits.append(sum(list(i[1]))
# print(all_credits)

# ball_credits = []
# for i in ball_comn:
#     ball_credits.append(sum(list(i[1]))
# print(ball_credits)