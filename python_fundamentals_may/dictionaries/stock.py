products_and_quantities = input().split(" ")
products_to_search = input().split(" ")
products = {}
for item in range(0, len(products_and_quantities), 2):
    key = products_and_quantities[item]
    value = int(products_and_quantities[item + 1])
    products[key] = value
for item in products_to_search:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

