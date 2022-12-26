def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(sum, third_number):
    return sum_numbers(first_number, second_number) - third_number


def add_and_subtract(a, b, number):
    return (first_number + second_number) - third_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(subtract(sum_numbers(first_number,second_number), third_number))