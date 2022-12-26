age = int(input())
price_wm = float(input())
price_toy = int(input())
sum_money = 0
money = 0
count_toys = 0
for year in range(1, age + 1):
    if year % 2 == 0:
        money = money + 10
        sum_money = sum_money + money - 1
    else:
        count_toys += 1
sum_toys = count_toys * price_toy
total_sum = sum_money + sum_toys
if price_wm <= total_sum:
    print(f"Yes! {total_sum - price_wm:.2f}")
else:
    print(f"No! {price_wm - total_sum:.2f}")