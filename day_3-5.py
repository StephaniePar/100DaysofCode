# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1 + ' ' + name2
both_names = both_names.upper()

t_count = both_names.count('T')
r_count = both_names.count('R')
u_count = both_names.count('U')
e_count = both_names.count('E')
l_count = both_names.count('L')
o_count = both_names.count('O')
v_count = both_names.count('V')

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

true_count = str(true_count)
love_count = str(love_count)
love_total = true_count + love_count
love_total = int(love_total)

if love_total > 90 or love_total < 10:
  print(f"Your score is {love_total}, you go together like coke and mentos.")
elif love_total > 40 and love_total < 50:
  print(f"Your score is {love_total}, you are alright together.")
else:
  print(f"Your score is {love_total}.")
