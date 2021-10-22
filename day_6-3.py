# First: Go to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle3.json
# My Robot Hurdle3 challege Solution:
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_around()
    turn_left()

def over_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    while front_is_clear() and not at_goal():
        move()
    while wall_in_front():
        over_wall()
