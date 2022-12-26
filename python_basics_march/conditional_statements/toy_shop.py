trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
revenue = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
number_of_toys = puzzles + dolls + bears + minions + trucks
if number_of_toys >= 50:
    revenue = revenue * 0.75
profit = revenue * 0.90
money_left = profit - trip_price
money_needed = trip_price - profit
if trip_price <= profit:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_needed:.2f} lv needed.')

