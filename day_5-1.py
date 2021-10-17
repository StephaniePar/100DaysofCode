# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

totsum = 0
count = 0

for students in student_heights:
  totsum = totsum + students
  count = count + 1
print(round(totsum/count))
