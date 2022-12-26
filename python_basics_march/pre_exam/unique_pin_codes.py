max_value_first_number = int(input())
max_value_second_number = int(input())
max_value_third_number = int(input())

first_valid_number = 0
second_valid_number = 0
third_valid_number = 0
for x1 in range(1, max_value_first_number + 1):
    if x1 % 2 == 0:
        first_valid_number = x1
    for x2 in range(1, max_value_second_number + 1):
        if x2 == 2 or x2 == 3 or x2 == 5:
            second_valid_number = x2
        for x3 in range(1, max_value_third_number + 1):
            if x3 % 2 == 0:
                third_valid_number = x3
                if first_valid_number == x1 and second_valid_number == x2 and third_valid_number == x3:
                    print(f"{first_valid_number} {second_valid_number} {third_valid_number}")