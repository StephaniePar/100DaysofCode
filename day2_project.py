#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill_subtotal = input("What was the total of your bill?\n")
tip_amount = input("How much do you want to tip? \n (most tip 10%, 12%, 15% or 20%)\n")
bill_split = input("How many people will split this bill?\n")

bill_subtotal = float(bill_subtotal) 
tip_amount = float(tip_amount) 
bill_split = int(bill_split)
tip_amount = tip_amount/100
bill_total = (bill_subtotal * tip_amount + bill_subtotal) * 1.00
your_total =  bill_total / bill_split

# I tried using rounded, but it would only give one decimal place, so I'm using format instead
print(f"The total bill is ${format(bill_total, '.2f')} \n Your total is $ {format(your_total, '.2f')} ")
