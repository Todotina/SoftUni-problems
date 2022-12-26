def even_odd(*args):
    command = args[-1]
    even_list = []
    odd_list = []
    for ind in range(len(args)-1):
        if args[ind] % 2 == 0:
            even_list.append(args[ind])
        else:
            odd_list.append(args[ind])

    if command == "even":
        return even_list
    else:
        return odd_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))