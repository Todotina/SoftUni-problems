def factorial_calculation(number):
    for factorial in range(1, number):
        number *= factorial
    return number


number_one = int(input())
number_two = int(input())
first_factorial = factorial_calculation(number_one)
second_factorial = factorial_calculation(number_two)
result = first_factorial/second_factorial
print(f"{result:.2f}")
