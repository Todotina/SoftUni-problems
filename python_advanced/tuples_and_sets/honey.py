from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())
total_honey = 0
while len(working_bees) > 0 and len(nectar) > 0:
    if working_bees[0] <= nectar[-1]:
        bee, symbol, current_nectar = working_bees.popleft(), symbols.popleft(), nectar.pop()
        if symbol == "+":
            honey_made = abs(bee + current_nectar)
        elif symbol == "-":
            honey_made = abs(bee - current_nectar)
        elif symbol == "*":
            honey_made = abs(bee * current_nectar)
        elif symbol == "/":
            honey_made = abs(bee / current_nectar)
        total_honey += honey_made
    else:
        nectar.pop()
        continue
print(f"Total honey made: {total_honey}")
if len(working_bees) > 0:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if len(nectar) > 0:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")