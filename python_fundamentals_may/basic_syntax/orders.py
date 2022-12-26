number_of_orders = int(input())
total_price = 0
for orders in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price = price_per_capsule * days * capsules_per_day
    total_price += price
    if price > 0:
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")