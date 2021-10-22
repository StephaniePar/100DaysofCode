# First: Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle4.json
# My Robot Hurdle4 challege Solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def over_wall():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
         move()
    turn_left()

while at_goal() == False:
    if front_is_clear():
        move()
    else:
        over_wall()
