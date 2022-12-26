allowed_poor_grades = int(input())
command = input()
count_problems = 0
count_poor_grades = 0
total_grade = 0
last_problem = ""
while command != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        count_poor_grades += 1
        if count_poor_grades == allowed_poor_grades:
            print(f"You need a break, {count_poor_grades} poor grades.")
            break
    total_grade += current_grade
    count_problems += 1
    last_problem = command
    command = input()
if command == "Enough":
    print(f"Average score: {total_grade/count_problems:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {last_problem}")