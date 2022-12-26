from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))
dolls = 0
trains = 0
teddy_bears = 0
bicycles = 0
presents = {}
while materials and magic_levels:
    current_product = materials[-1] * magic_levels[0]
    if current_product == 150:
        dolls += 1
        materials.pop()
        magic_levels.popleft()
        presents['Doll'] = dolls
    elif current_product == 250:
        trains += 1
        materials.pop()
        magic_levels.popleft()
        presents['Train'] = trains
    elif current_product == 300:
        teddy_bears += 1
        materials.pop()
        magic_levels.popleft()
        presents['Teddy bear'] = teddy_bears
    elif current_product == 400:
        bicycles += 1
        materials.pop()
        magic_levels.popleft()
        presents['Bicycle'] = bicycles
    elif current_product < 0:
        current_sum = materials.pop() + magic_levels.popleft()
        materials.append(current_sum)
    elif current_product > 0:
        magic_levels.popleft()
        materials[-1] += 15
    elif current_product == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic_levels[0] == 0:
            magic_levels.popleft()

if (dolls >= 1 and trains >= 1) or (teddy_bears >= 1 and bicycles >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if len(materials) > 0:
    # print(f"Materials left: {', '.join(str(materials.pop()) for item in materials)}")
    print(f"Materials left: {', '.join(str(materials.pop()))}")
if len(magic_levels) > 0:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
for present, quantity in presents.items():
    print(f"{present}: {quantity}")