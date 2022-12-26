command = input()
sum_simple_numbers = 0
sum_non_simple_numbers = 0

while command != "stop":
    current_number = int(command)
    count_divisors = 0
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue
    for divisor in range(1, current_number + 1):
        if current_number % divisor == 0:
            count_divisors += 1
    if count_divisors == 2:
        sum_simple_numbers += current_number
    else:
        sum_non_simple_numbers += current_number
    command = input()
print(f"Sum of all prime numbers is: {sum_simple_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_simple_numbers}")