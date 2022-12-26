from collections import deque

ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while customers:
    c_ramen = ramen[-1]
    c_customer = customers[0]
    if c_ramen == c_customer:
        ramen.pop()
        customers.popleft()
    elif c_ramen > c_customer:
        ramen.pop()
        customers.popleft()
        ramen.append(c_ramen - c_customer)
    elif c_ramen < c_customer:
        ramen.pop()
        customers.popleft()
        customers.appendleft(c_customer - c_ramen)
    if len(ramen) == 0 and len(customers) > 0:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f'Customers left: {", ".join(str(x) for x in customers)}')
        break

if len(customers) == 0:
    print("Great job! You served all the customers.")
if len(ramen) > 0:
    print(f'Bowls of ramen left: {", ".join(str(x) for x in ramen)}')
