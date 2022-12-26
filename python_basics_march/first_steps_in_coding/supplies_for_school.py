number_pen_packages = int(input())
number_marker_packages = int(input())
detergent_liters = int(input())
discount = int(input())
    #• Пакет химикали - 5.80 лв.
    #• Пакет маркери - 7.20 лв.
    #• Препарат - 1.20 лв (за литър)
amount = number_pen_packages * 5.80 + number_marker_packages * 7.20 + detergent_liters * 1.20
amount_discount = amount * (discount/100)
final_amount = amount - amount_discount
print(final_amount)
