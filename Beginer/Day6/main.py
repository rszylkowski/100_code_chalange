"""
Escaping the maze (Reeborg's World)
Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
Paste code below in Python Code and click Play
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Below while is for starting on x=3 y=4 facing down because you will enter infinite loop without it
# (there is always right clear so the robot will be walking in square infinitely)
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
