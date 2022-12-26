list_sequence = input().split(' ')
absolute_numbers = []
for element in list_sequence:
    absolute_numbers.append(abs(float(element)))
print(absolute_numbers)