student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}



# TODO-2: Write your code below to add the grades to student_grades.👇
for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80 and student_scores[i] < 91:
        student_grades[i] = "Exceeds Expectation"
    elif student_scores[i] > 70 and student_scores[i] < 81:
        student_grades[i] = "Acceptable"
    elif student_scores[i] < 71:
        student_grades[i] = "Fail"



# 🚨 Don't change the code below 👇
print(student_grades)
