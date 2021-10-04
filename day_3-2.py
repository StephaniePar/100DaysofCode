# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2
bmi = round(bmi)

if bmi < 18.5:
  print(f"Your BMI is \033[1;34m{bmi}\033[0m, you are\033[1;34m underweight.")
elif bmi >= 18.5 and bmi < 25:
  print(f"Your BMI is \033[1;34m{bmi}\033[0m, you have a\033[1;34m normal weight.")
elif bmi >= 25 and bmi < 30:
  print(f"Your BMI is \033[1;34m{bmi}\033[0m, you are\033[1;34m slightly overweight.")
elif bmi >= 30 and bmi < 35:
  print(f"Your BMI is \033[1;34m{bmi}\033[0m, you are\033[1;34m obese.")
else:
  print(f"Your BMI is \033[1;34m{bmi}\033[0m, you are\033[1;34m clinically obese.")

  # Oops, my code is more specific and unnecessarily complicated (not the colors, just the mbi checking part). It works, but I have to remember that simpler is better
