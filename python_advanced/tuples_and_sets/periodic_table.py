lines = int(input())
unique = set()
for line in range(lines):
    current_element = input().split()
    for element in current_element:
        if element not in unique:
            unique.add(element)
for element in unique:
    print(element)