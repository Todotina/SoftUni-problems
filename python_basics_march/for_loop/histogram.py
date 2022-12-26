count_of_numbers = int(input())
count_below_200 = 0
count_below_399 = 0
count_below_599 = 0
count_below_799 = 0
count_above_799 = 0
for numbers in range(1, count_of_numbers + 1):
    current_number = int(input())
    if current_number < 200:
        count_below_200 += 1
    elif current_number <= 399:
        count_below_399 += 1
    elif current_number <= 599:
        count_below_599 += 1
    elif current_number <= 799:
        count_below_799 += 1
    else:
        count_above_799 += 1
p1 = count_below_200 / count_of_numbers * 100
p2 = count_below_399 / count_of_numbers * 100
p3 = count_below_599 / count_of_numbers * 100
p4 = count_below_799 / count_of_numbers * 100
p5 = count_above_799 / count_of_numbers * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")