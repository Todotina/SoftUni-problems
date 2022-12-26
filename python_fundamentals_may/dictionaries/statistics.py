command = input()
products = {}
sum = 0
count = 0
while command != "statistics":
    current_product = command.split(": ")
    key = current_product[0]
    value = int(current_product[1])
    sum += value
    if key not in products:
        products[key] = 0
        count += 1
    products[key] += value
    # if key in products:
    #     products[key] += value
    command = input()
if command == "statistics":
    print("Products in stock:")
    for key in products.keys():
        print(f"- {key}: {products[key]}")
print(f"Total Products: {count}")
print(f"Total Quantity: {sum}")