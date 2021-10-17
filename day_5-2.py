# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
highest_score = 0
for scores in student_scores:
  if highest_score <= scores:
    highest_score = scores

print(f"The highest score in the class is: {highest_score}")
