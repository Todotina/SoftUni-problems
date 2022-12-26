from collections import deque

caffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])
max_caffeine = 300
caffeine_drank = 0

while caffeine:
    current_caffeine = caffeine[-1] * energy_drinks[0]
    if current_caffeine + caffeine_drank <= 300:
        caffeine_drank += current_caffeine
        caffeine.pop()
        energy_drinks.popleft()
    else:
        caffeine.pop()
        if caffeine_drank - 30 >= 0:
            caffeine_drank -= 30
        energy_drinks.append(energy_drinks.popleft())
    if len(energy_drinks) == 0:
        break

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_drank} mg caffeine.")