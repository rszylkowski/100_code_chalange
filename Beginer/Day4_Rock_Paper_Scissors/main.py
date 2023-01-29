"""
Rock, Paper, Scissors
"""
import random
from Beginer.Day4_Rock_Paper_Scissors import images_dict as imd

player_select = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
cpu_select = random.randint(0, 2)
print(f"Player selected {imd.images_dict[player_select]}\n")
print(f"CPU selected{imd.images_dict[cpu_select]}\n")

if player_select == 0:
    if cpu_select == 0:
        print("Draw")
    elif cpu_select == 1:
        print("CPU Win!!")
    elif cpu_select == 2:
        print("You Win!!")

if player_select == 1:
    if cpu_select == 1:
        print("Draw")
    elif cpu_select == 2:
        print("CPU Win!!")
    elif cpu_select == 0:
        print("You Win!!")

if player_select == 2:
    if cpu_select == 2:
        print("Draw")
    elif cpu_select == 0:
        print("CPU Win!!")
    elif cpu_select == 1:
        print("You Win!!")



