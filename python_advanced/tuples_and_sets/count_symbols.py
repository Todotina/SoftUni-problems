text = tuple(input())
unique = []
for symbol in sorted(text):
    if symbol not in unique:
        unique.append(symbol)
        count = text.count(symbol)
        print(f'{symbol}: {count} time/s')