list_of_numbers = input().split(" ")
list_of_numbers_int = []
for element in list_of_numbers:
    list_of_numbers_int.append(int(element))
print(list(filter(lambda x: x % 2 == 0, list_of_numbers_int)))

