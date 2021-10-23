#My solution for Maze Go to: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# It even solves the 3 problem world examples she gives
# My Maze Project Solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    else:
        turn_left()
