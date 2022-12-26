list_of_numbers = input().split(", ")
list_of_numbers_integers = [int(number) for number in list_of_numbers]
list_of_indexes = []
for element in list_of_numbers_integers:
    if element % 2 == 0:
        index = list_of_numbers_integers.index(element)
        list_of_indexes.append(index)
print(list_of_indexes)

# number_list = list(map(int, input().split(", ")))