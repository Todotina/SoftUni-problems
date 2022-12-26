number_of_names = int(input())
unique_names = set()
for name in range(number_of_names):
    current_name = input()
    if current_name not in unique_names:
        unique_names.add(current_name)
for item in unique_names:
    print(item)