string = input()
my_list = string.split()
modified_list = []
for element in my_list:
    modified_list.append(-int(element))
print(modified_list)