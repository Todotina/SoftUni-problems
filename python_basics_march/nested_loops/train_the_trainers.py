number_of_people = int(input())
presentation_name = input()
grade_count = 0
sum_all_grades = 0

while presentation_name != "Finish":
    sum_current_grades = 0
    current_avg_grade = 0
    for people in range(number_of_people):
        current_grade = float(input())
        grade_count += 1
        sum_current_grades += current_grade
        sum_all_grades += current_grade
        current_avg_grade = sum_current_grades / number_of_people

    print(f"{presentation_name} - {current_avg_grade:.2f}.")
    presentation_name = input()
final_avg_grade = sum_all_grades/grade_count
print(f"Student's final assessment is {final_avg_grade:.2f}.")