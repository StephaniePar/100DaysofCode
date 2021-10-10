# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
number_names = len(names) - 1
random_number = random.randint(0,number_names)
print(names[random_number])
