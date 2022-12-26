command = input()
companies = {}
while command != "End":
    current_input = command.split(" -> ")
    company, id = current_input[0], current_input[1]
    if company not in companies:
        companies[company] = []
    if id not in companies[company]:
        companies[company].append(id)
    command = input()
for company, value in companies.items():
    print(f"{company}")
    new_line = '\n-- '
    print(f"-- {new_line.join(value)}")
