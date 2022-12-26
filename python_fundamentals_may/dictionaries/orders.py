command = input()
product_dict = {}
while command != "buy":
    product_info = command.split(" ")
    name, price, quantity = product_info[0], float(product_info[1]), int(product_info[2])
    if name not in product_dict:
        product_dict[name] = {}
        product_dict[name]['price'] = price
        product_dict[name]['quantity'] = quantity
    else:
        product_dict[name]['price'] = price
        product_dict[name]['quantity'] += quantity

    command = input()

if command == "buy":
    for name in product_dict.keys():
        total_price = product_dict[name]['price'] * product_dict[name]['quantity']
        print(f"{name} -> {total_price:.2f}")