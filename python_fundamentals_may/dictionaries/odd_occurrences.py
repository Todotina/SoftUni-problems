words = input().split(" ")
result = {}
for element in words:
    element_lower = element.lower()
    if element_lower not in result:
        result[element_lower] = 0
    result[element_lower] += 1

for key in result.keys():
    if result[key] % 2 != 0:
        print(key, end=" ")

