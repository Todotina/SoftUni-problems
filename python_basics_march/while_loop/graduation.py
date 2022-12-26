student_name = input()
current_class = 1
sum_grades = 0
failed_tries = 0
graduated = True
while current_class <= 12:
    grade = float(input())
    if grade >= 4:
        sum_grades += grade
        current_class += 1
    elif grade < 4:
        failed_tries += 1
        if failed_tries > 1:
            graduated = False
            print(f"{student_name} has been excluded at {current_class} grade")
            break
if graduated == True:
    print(f"{student_name} graduated. Average grade: {sum_grades / 12:.2f}")

# https://pastebin.com/QK2bKNS8