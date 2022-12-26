#     • Предпазен найлон - 1.50 лв. за кв. метър
#     • Боя - 14.50 лв. за литър
#     • Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички.
# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.
nylon = int(input())
paint = int(input())
dilutioner = int(input())
hours = int(input())
expenses_materials = (nylon + 2) * 1.50 + (1.1 * paint) * 14.50 + dilutioner * 5 + 0.40
expenses_labour = hours * (0.30 * expenses_materials)
total_expenses = expenses_materials + expenses_labour
print(total_expenses)