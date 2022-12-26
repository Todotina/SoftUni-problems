numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')

    line = input()

while line != "Remove":
    searched_line = input()
    if searched_line != "Remove" and searched_line != "End":
        print(numbers_dictionary[searched_line])

    line = input()

while line != "End":
    try:
        removed = input()
        del numbers_dictionary[removed]
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)