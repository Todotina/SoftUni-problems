from collections import deque

elves = deque([int(x) for x in input().split()])
boxes = deque([int(x) for x in input().split()])
toys = 0
energy = 0
turn = 0

while boxes and elves:
    current_elf, current_box = elves[0], boxes[-1]
    if current_elf < 5:
        elves.popleft()
        continue
    turn += 1
    if turn % 5 == 0:
        if turn % 3 == 0 and current_elf >= 2 * current_box:
            energy += 2 * current_box
            current_elf -= (2 * current_box)
            elves.append(current_elf)
            elves.popleft()
            boxes.pop()
        elif current_elf >= current_box:
            current_elf -= current_box
            elves.append(current_elf)
            elves.popleft()
            energy += current_box
            boxes.pop()
        else:
            elves.append(2 * current_elf)
            elves.popleft()
    elif turn % 3 == 0:
        if current_elf >= 2 * current_box:
            current_elf -= (2 * current_box) - 1
            elves.append(current_elf)
            elves.popleft()
            toys += 2
            energy += 2 * current_box
            boxes.pop()
        else:
            elves.append(2 * current_elf)
            elves.popleft()
    else:
        if current_elf >= current_box:
            current_elf -= current_box - 1
            elves.append(current_elf)
            elves.popleft()
            energy += current_box
            boxes.pop()
            toys += 1
        else:
            elves.append(2 * current_elf)
            elves.popleft()


print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elves:
    print(f'Elves left: {", ".join(str(x) for x in elves)}')
if boxes:
    print(f'Boxes left: {", ".join(str(x) for x in boxes)}')