# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
row_num =  position[0]
col_num =  position[1]
col_num = int(col_num)
col_num = col_num - 1
if row_num == '1':
  row1[col_num] = 'X'
elif row_num == '2':
  row2[col_num] = 'X'
elif row_num == '3':
  row3[col_num] = 'X'
else:
  print("Error, a two digit number with the first number between 1-3 for the row and the second a number between 1-3 for the column!")

# The teacher's code was only four lines 😞


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
