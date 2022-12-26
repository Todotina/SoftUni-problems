# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposit_amount = float(input())
term = int(input())
annual_rate = float(input())
annual_amount = deposit_amount * (annual_rate / 100)
monthly_amount = annual_amount / 12
end_amount = deposit_amount + term * monthly_amount
print(end_amount)
