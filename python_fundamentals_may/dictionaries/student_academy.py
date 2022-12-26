number = int(input())
students_dict = {}
for student in range(number):
    current_student = input()
    current_grade = float(input())
    if current_student not in students_dict:
        students_dict[current_student] = []
    students_dict[current_student].append(current_grade)

for key in students_dict:
    average_grade = sum(students_dict[key]) / len(students_dict[key])
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
