def filtered_numbers(number, group):
    if number <= group:
        filtered_list.append(number)
        return True


list_of_numbers = [int(number) for number in input().split(", ")]
filtered_list = []
group = 10
while list_of_numbers:
    for number in list_of_numbers:
        if filtered_numbers(number, group):
            index = list_of_numbers.index(number)
            list_of_numbers[index] = 0
    print(f"Group of {group}'s: {filtered_list}")
    list_of_numbers = [number for number in list_of_numbers if number != 0]
    group += 10
    filtered_list.clear()

