number = int(input())
result = []

for number in range(number):
    current_integer = int(input())
    result.append(current_integer)

command = input()
if command == "even":
    result = [element for element in result if element % 2 == 0]
elif command == "odd":
    result = [element for element in result if element % 2 != 0]
elif command == "negative":
    result = [element for element in result if element < 0]
elif command == "positive":
    result = [element for element in result if element >= 0]

print(result)