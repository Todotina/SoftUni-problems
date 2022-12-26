command = input()
total_taxes = 0
total_price_without_tax = 0
total_price = 0
while command != "special" and command != "regular":
    current_price_without_tax = float(command)
    if current_price_without_tax < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price_without_tax += current_price_without_tax
    tax = 0.2 * current_price_without_tax
    total_taxes += tax
    total_price += 1.2 * current_price_without_tax

    command = input()

if command == "special":
    total_price = 0.9 * total_price

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_tax:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

