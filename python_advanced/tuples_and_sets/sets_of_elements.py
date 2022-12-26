set_of_elements = input().split()
length_first_set = int(set_of_elements[0])
length_second_set = int(set_of_elements[1])
first_set = set()
second_set = set()
for element in range(length_first_set):
    current_element = int(input())
    first_set.add(current_element)
for element in range(length_second_set):
    current_element = int(input())
    second_set.add(current_element)
intersection = first_set.intersection(second_set)
for element in intersection:
    print(element)
