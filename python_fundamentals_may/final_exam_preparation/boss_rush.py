import re

pattern = r'([\|])([A-Z]{4,})\1\:(\#)([A-Za-z]+\s[A-Za-z]+)\#'

number = int(input())
for string in range(number):
    current_string = input()
    match = re.search(pattern, current_string)
    if match:
        boss_name = match.group(2)
        title = match.group(4)
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")


