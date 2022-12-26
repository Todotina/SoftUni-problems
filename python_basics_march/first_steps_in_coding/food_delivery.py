#     • Пилешко меню –  10.35 лв.
#     • Меню с риба – 12.40 лв.
#     • Вегетарианско меню  – 8.15 лв.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.
chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())
main_course_price = chicken_menus * 10.35 + fish_menus * 12.40 + veggie_menus * 8.15
desert_price = main_course_price * 0.20
order_price = main_course_price + desert_price + 2.50
print(order_price)
