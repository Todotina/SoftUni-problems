from math import ceil

students_per_hour_first = int(input())
students_per_hour_second = int(input())
students_per_hour_third = int(input())
students_count = int(input())

total_students_per_hour = students_per_hour_third + students_per_hour_second + students_per_hour_first
time_needed = ceil(students_count / total_students_per_hour)
for hour in range(1, time_needed + 1):
    if hour % 3 == 0:
        time_needed += 1

print(f"Time needed: {time_needed}h.")

# Every fourth hour, all employees have a break, so they don't work for an hour.
# It is the only break for the employees, because they don't need rest, nor have a personal life.
# Calculate the time needed to answer all the student's questions and print it in the following format: "Time needed: {time}h."