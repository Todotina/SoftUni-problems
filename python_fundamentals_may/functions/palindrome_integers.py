def palindrome_check(number):
    if number[::-1] == number:
        print("True")
    else:
        print("False")


list_of_numbers = [number for number in input().split(', ')]
for element in list_of_numbers:
    palindrome_check(element)