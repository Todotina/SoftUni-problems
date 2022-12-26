budget = float(input())
number_of_actors = int(input())
costume_price_per_actor = float(input())
price_decor = budget * 0.10
costume_price = number_of_actors * costume_price_per_actor

if number_of_actors > 150:
    costume_price = 0.9 * costume_price
money_below_budget = abs(budget - price_decor - costume_price)
money_above_budget = abs(price_decor + costume_price - budget)
if price_decor + costume_price > budget:
    print("Not enough money!")
    print(f'Wingard needs {money_below_budget:.2f} leva more.')
elif price_decor + costume_price <= budget:
    print("Action!")
    print(f'Wingard starts filming with {money_above_budget:.2f} leva left.')

