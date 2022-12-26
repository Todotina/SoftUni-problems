term = input()
contract_type = input()
mobile_internet = input()
months_to_be_paid = int(input())
monthly_fee = 0
total_fee = 0

if term == "one":
    if contract_type == "Small":
        monthly_fee = 9.98
    elif contract_type == "Middle":
        monthly_fee = 18.99
    elif contract_type == "Large":
        monthly_fee = 25.98
    elif contract_type == "ExtraLarge":
        monthly_fee = 35.99
elif term == "two":
    if contract_type == "Small":
        monthly_fee = 8.58
    elif contract_type == "Middle":
        monthly_fee = 17.09
    elif contract_type == "Large":
        monthly_fee = 23.59
    elif contract_type == "ExtraLarge":
        monthly_fee = 31.79

if mobile_internet == "yes" and monthly_fee <= 10.00:
    monthly_fee += 5.50
elif mobile_internet == "yes" and monthly_fee <= 30.00:
    monthly_fee += 4.35
elif mobile_internet == "yes" and monthly_fee > 30.00:
    monthly_fee += 3.85
total_fee = monthly_fee * months_to_be_paid
if term == "two":
    total_fee *= 0.9625

print(f"{total_fee:.2f} lv.")