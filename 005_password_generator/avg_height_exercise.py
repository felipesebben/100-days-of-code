student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for student_height in student_heights:
    total_height += student_height
# print(total_height)

num_students = 0
for student in student_heights:
    num_students += 1
# print(num_students)

avg_height = round(total_height / num_students)
print(avg_height)
