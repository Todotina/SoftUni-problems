#     • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#     • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#     • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#     • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка
annual_fee = int(input())
price_shoes = 0.6 * annual_fee
price_clothing = 0.8 * price_shoes
price_ball = 0.25 * price_clothing
price_accessories = 0.20 * price_ball
total_price = annual_fee + price_accessories + price_ball + price_clothing + price_shoes
print(total_price)