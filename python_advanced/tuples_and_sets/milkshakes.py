from collections import deque

chocolate = deque(int(item) for item in input().split(", "))
cups_of_milk = deque(int(item) for item in input().split(", "))
number_of_shakes = 0
while len(chocolate) > 0 and len(cups_of_milk)>0:
    if chocolate[-1] == cups_of_milk[0]:
        number_of_shakes += 1
        chocolate.pop()
        cups_of_milk.popleft()
        if number_of_shakes == 5:
            break
    elif chocolate[-1] <= 0:
        chocolate.pop()
    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolate[-1] -= 5
if number_of_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
    if len(chocolate) == 0:
        print('Chocolate: empty')
    else:
        print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
    if len(cups_of_milk) == 0:
        print('Milk: empty')
    else:
        print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Not enough milkshakes.")
    if len(chocolate) == 0:
        print('Chocolate: empty')
    else:
        print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
    if len(cups_of_milk) == 0:
        print('Milk: empty')
    else:
        print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
