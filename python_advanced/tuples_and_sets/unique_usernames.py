number_of_usernames = int(input())
unique = set()
for name in range(number_of_usernames):
    current_name = input()
    if current_name not in unique:
        unique.add(current_name)
for name in unique:
    print(name)