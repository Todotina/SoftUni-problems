command = input()
courses_dict = {}
while command != "end":
    current_course = command.split(" : ")
    course, name = current_course[0], current_course[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(name)
    command = input()
if command == "end":
    for course in courses_dict:
        print(f"{course}: {len(courses_dict[course])}")
        new_line = '\n-- '
        print(f"-- {new_line.join(courses_dict[course])}")