list_of_integers = [int(number) for number in input().split(" ")]
index = int(input())
sorted_list = list_of_integers.copy()
sorted_list.sort()
del sorted_list[0:index]
list_of_integers = [element for element in list_of_integers if element in sorted_list]
print(', '.join(map(str,list_of_integers)))