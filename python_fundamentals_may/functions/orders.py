product = input()
quantity = int(input())
price = 0
def total_price(product,quantity):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2
    return f"{quantity * price:.2f}"
print(total_price(product, quantity))
# • coffee - 1.50
# • water - 1.00
# • coke - 1.40
# • snacks - 2.00