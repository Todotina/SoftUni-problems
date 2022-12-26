list_of_names = input().split(", ")
# sorted_list = sorted(list_of_names, key=len, reverse=True)
sorted_list = sorted(list_of_names, key= lambda name: (-len(name), name))
print(sorted_list)