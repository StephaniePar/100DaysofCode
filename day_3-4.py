# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == "S":
  order_price = 15
elif size == "M":
  order_price = 20
elif size == "L":
  order_price = 25

if add_pepperoni == "Y":
  if size == "S":
    order_price += 2
  elif size == "M" or "L":
    order_price += 3

if extra_cheese == "Y":
  order_price += 1

print(f"Your total pizza order is ${order_price}.")
