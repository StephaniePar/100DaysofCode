print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first_choice = input("As you walk down the path, you reach a crossroads. You have two choices left or right, which direction do you take?\n")

first_choice = first_choice.lower()

if first_choice == "left":
  second_choice = input("You see the volcano that hides the treasure in the distance, so you start heading that way. The path continues for a long while. You are getting tired of walking. Finally you reach a long river that stretches further than you can see. Now there are two choices: you can swim across or wait. What will you choose to do?\n")
elif first_choice == "right":
  print("You decide to go right. unfortunately you go distracted when a spider near landed on you and fell down a giant pit. You are dead. \n GAME OVER")
else:
  print("Welp, the world isn't fair and what you chose is not an option. You confused yourself and looked at the two paths undecided until you starved to death. How about next time, you choose one of the options I gave you? Maybe you'll live, maybe you won't. Oh well, you died. \n GAME OVER")

  
if first_choice == "left":
  second_choice = second_choice.lower()
  if second_choice == "wait":
    third_choice = input("You decided to wait. You're tired, you've been travelling quite a while. You relax, get your breath back, after about an hour, a log floats by. It looks sturdy and large, so you grab it before it floats away. Look at that, now you have transportation. You look around and you see a nice stick that widens at the bottom, looks kinda like a paddle, man is it your lucky day. You get on the log and with your stick, you get across the river easily. Woah, that was easier than swimming. You continue walking until you are at the base of the volcano. There are three doors. Which to choose? Red? Blue? Or yellow?\n")
  elif first_choice == "left" and second_choice == "swim":
    print("You decided to swim for it. The water is harder to swim across, than you expected. You don't get far, before your clothes start weighing you down, as well. You are already tired, and the rough waters and all these clothes, are just making it harder. You regret rushing impatiently to the treasure without taking at least a few minutes break. You are about halfway across when you really start sinking, unable to continue on. As you are about to give up a trout starts tugging on your clothes. Then another appears and another and more until there are over 20 trouts pulling you. You let them pull you, too tired to try and swim anymore. When you are nearly at the shore the trouts turn and pull you away from your destination to a cave. The trout leave you on the shores of the cave. You struggle to lift your head and when you finally do it's to the mouth of an alligator as it snaps closed on your head killing you instantly. You are dead. \n GAME OVER")
  else:
    print("No. Bad. This is not an option. you have to pick one of the options I gave you. You aren't the smartest pickle in the jar, love(derogatory). That is why I'm giving you options to begin with, you know. Oh well, in your confused state, you walk to a tree, where a snake comes down and bites you. It's not poisonous thankfully, so you back away quickly falling into the water and quickly sinking to the bottom. You try to swim up, but you are tired and drown. Dying, alone, halfway to the treasure you sought. You are dead. \n GAME OVER")

if first_choice == "left" and second_choice == "wait":  
  third_choice = third_choice.lower()
  if third_choice == "yellow":
    print("The door opens to a dark hallway, the walls look like they were carved into the volcano and you can just about make out a torch on a bracket. You walk in and the torch lights up and further down you can just about make out another. You walk down the hallway and as you walk torches light up on either side of you. You make it to the end where there is another door. You pull it and it opens easily. Inside it covered in gold and gems and chests. You made it to the treasure you were looking for. I don't know how you are going to get the treasure home, but at least you made it to the end of your adventure richer than you started it! \n YOU WIN")
  elif third_choice == "red":
    print("You choose the red door. It looks dark. You can just about make out a torch on the wall. As you step into the room the door slams shut behind you. That freaks you out, so you spin around to get it open and start yanking on the door. You don't realize that lava is pouring into the room, you are so focused on trying to get the door open. The room is getting hotter and brighter, you look behind you just as the lava reaches your foot. You get burned by it, you back a step, but the panic mixed with the worst burning pain you have ever expiernce cause you to fall forward, into the lava. You are dying, burning in pain, unable to think, unable to move. You died. \n GAME OVER")
  elif third_choice == "blue":
    print("You choose the blue door. Blue is a great color. It's a calming color and a color of confidence. Why would you choose those other doors? You walk right in. It's brightly lit. You see an odd hole on the ceiling. It might be dangerous, but you are already in the room. You know you chose the right color, so you walk over to it and stand underneath it, looking up at it. It covered in webs. You think to yourself 'Maybe this isn't the right room.' You walk back to the door a bit more hesitant than you were walking into it. But your fear made you slower. Before you could reach the door a giant spider drops down the hole and grabs you. And climbs back up the hole into the webs biting into your arms as it does it. You try to punch it, to get away, but the venom has made you sluggish and you can't hurt the spider enough for it to drop you. It bites you again injecting more venom and taking a chunck out of your shoulder. You cry out in pain and fear. The spider killed you and ate you. You are delicious and very dead. \n GAME OVER")
  else:
    print("Of course, you don't pick one of the options I gave you. You look around. You decide against picking one the doors for now. The island is prettier than you expected. You decide to look around a bit. In a tree not far from the door you see some cherries in a tree. You are absolutely starving. You'll go back to the doors in a second and decide to climb the tree and eat some cherries first. You safely climb up, I mean, you are a cahmpion tree climber after all. You fold up the bottom of your shirt and grab as many cherries filling it up. You climb back down, no problems for you. and sit at the base and start chowing down. You look around and notice some birds on the ground not far from where you are sitting. You walk over to them and they are dead and have been for a while. Their beaks are covered in red bits. Wait, that looks a bit like the skins from the cherries you are currently eating. You died obviously. Oh well, the fruit of the not cherries, they are something else, but they taste and look like cherries are fine. But their skins are toxic. if you had sat by the water and pulled off the skin rinsing your hands before touching the fruit of the cherry you wouldn't have died. Too bad. You are dead. \n GAME OVER")
