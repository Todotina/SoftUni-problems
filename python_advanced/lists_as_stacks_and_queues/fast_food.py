from collections import deque

food_quantity = int(input())
orders = deque(input().split())
orders_int = []
left_orders = []

for index in range(len(orders)):
    current_order = int(orders.popleft())
    orders_int.append(current_order)
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        food_quantity = 0
        left_orders.append(str(current_order))
print(max(orders_int))
if len(left_orders) >= 1:
    part = ' '.join(left_orders)
    print(f'Orders left: {part}')
else:
    print('Orders complete')

