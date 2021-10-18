#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rand_letts = random.sample(letters, k=nr_letters) 
rand_num = random.sample(numbers, k=nr_numbers)
rand_sym = random.sample(symbols, k=nr_symbols) 

rand_list_gen = rand_letts + rand_num + rand_sym
password = "".join(rand_list_gen)
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


random.shuffle(rand_list_gen)
password2 = "".join(rand_list_gen)
print(password2)

# Oops forgot to use for Loops; the teacher's solution to I can keep note of it:
# password3 = ""

# for char in range(1, nr_letters + 1):
#   password3 += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password3 += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password3 += random.choice(numbers)

# print(password3)
# 🔺 That's for Easy Lvl, her hard lvl vers. was similar to mine👍🏾
