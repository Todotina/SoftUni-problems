number_of_students = int(input())
students_dict = {}
for student in range(number_of_students):
    current_student = input().split()
    name, grade = current_student[0], float(current_student[1])
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)
for student, grades in students_dict.items():
    average = sum(grades)/len(grades)
    grades_list = ' '.join(str(f'{grade:.2f}') for grade in grades)
    print(f'{student} -> {grades_list} (avg: {average:.2f})')