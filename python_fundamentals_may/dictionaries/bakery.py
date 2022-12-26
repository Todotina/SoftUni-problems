food = input().split(" ")
bakery = {}

for element in range(0, len(food), 2):
    key = food[element]
    value = int(food[element + 1])
    bakery[key] = value
print(bakery)