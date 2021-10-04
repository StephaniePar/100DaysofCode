# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 and year % 100 != 0:
  print("This is a Leap Year!")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print ("This is a Leap Year!")
else:
  print("This is not a Leap Year")
