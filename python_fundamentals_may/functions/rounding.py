list_of_numbers = input().split(" ")
rounded_list = []
for element in list_of_numbers:
    rounded_list.append(round(float(element)))
print(rounded_list)