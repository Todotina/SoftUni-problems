from collections import deque

egg_sizes = deque([int(x) for x in input().split(", ")])
paper_sizes = deque([int(x) for x in input().split(", ")])
number_of_boxes = 0

while egg_sizes:
    current_egg = egg_sizes.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == 13:
        last_item = paper_sizes.pop()
        paper_sizes.append(paper_sizes.popleft())
        paper_sizes.appendleft(last_item)
        continue
    if paper_sizes:
        current_paper = paper_sizes.pop()
        if current_paper + current_egg <= 50:
            number_of_boxes += 1
    if len(egg_sizes) > 0 and len(paper_sizes) == 0:
        break

if number_of_boxes >= 1:
    print(f"Great! You filled {number_of_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if egg_sizes:
    print(f'Eggs left: {", ".join(str(x) for x in egg_sizes)}')
if paper_sizes:
    print(f'Pieces of paper left: {", ".join(str(x) for x in paper_sizes)}')

