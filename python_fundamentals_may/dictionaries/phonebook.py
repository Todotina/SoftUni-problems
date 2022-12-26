command = input()
phone_book = {}
while "-" in command:
    contact = command.split("-")
    name = contact[0]
    tel = contact[1]
    if name not in phone_book:
        phone_book[name] = 0
    phone_book[name] = tel
    command = input()

for search in range(int(command)):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")