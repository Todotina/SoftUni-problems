number = int(input())

for first_number in range(1, 10):
    for second_number in range(1, 10):
        for third_number in range(1, 10):
            for fourth_number in range(1, 10):
                if number % first_number == 0 and number % second_number == 0 and number % third_number == 0 and number % fourth_number == 0:
                    print(f"{first_number}{second_number}{third_number}{fourth_number}", end = " ")