# Snake-Water-Gun Game------------------>>>>>>>>>

import random

print("Welcome to Snake-Water-Gun Game, you have 10 chances")
options = ["S", "W", "G"]
print("S for Snake, W for Water and G for Gun ")
no_of_chance = 0
com_point = 0
player_point = 0
while no_of_chance < 11:
    u_i = input("Your choice : ")
    c_i = random.choice(options)
    print(f"Computer choice : {c_i}")
    if u_i == c_i:
        print("No Points!!")
    elif (u_i == "S" and c_i == "W") or (u_i == "W" and c_i == "G") or (u_i == "G" and c_i == "S"):
        print("One point for you!!")
        player_point = player_point + 1
    else:
        print("One point for computer!!")
        com_point = com_point + 1
    no_of_chance = no_of_chance + 1
    print(f"Number of chances left are {11-no_of_chance}\n")

if player_point>com_point:
    print(f"Your points,{player_point}:{com_point},computer points")
    print("Congratulations, You Won!!")
elif player_point<com_point:
    print(f"Your points,{player_point}:{com_point},computer points")
    print("Oops, You Lose!!")
    print("Better luck next time!")
else:
    print(f"Your points,{player_point}:{com_point},computer points")
    print("It's a Tie!!")
