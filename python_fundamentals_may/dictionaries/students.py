# command = input()
# students = {}
# while ":" in command:
#     current_student = command.split(":")
#     name = current_student[0]
#     id = current_student[1]
#     course = current_student[2]
#     students[current_student] = name, id, course
#     command = input()
#
# if ":" not in command:
#     filtered_course = command
#     if "_" in filtered_course:
#         filtered_course = command.split("_")
# for course in students.keys():
#     if course == filtered_course:
#         print(f"{students[name]} - {students[id]}")


command = input()
students_dict = {}
while ":" in command:
    list_of_students = command.split(":")
    name, id, course = list_of_students[0], list_of_students[1], list_of_students[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')