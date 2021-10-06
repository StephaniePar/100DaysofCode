#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

coin_flip = random.randint(0,1)
if coin_flip == 0:
  coin_flip_clean = "TAILS"
elif coin_flip == 1:
  coin_flip_clean = "HEADS"
coin_flip_clean = coin_flip_clean.upper()
print (f"Coin landed on {coin_flip_clean}")
