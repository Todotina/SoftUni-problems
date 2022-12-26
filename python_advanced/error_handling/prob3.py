text = input()
times = input()
try:
    result = text * int(times)
    print(result)
except ValueError:
    print('Variable times must be an integer')
