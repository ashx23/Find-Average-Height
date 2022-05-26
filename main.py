student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for i in student_heights:
  total_height += i


number_of_student = 0 
for student in student_heights:
  number_of_student += 1 


average = round(total_height / number_of_student)
print("Average height of student is",average)
  