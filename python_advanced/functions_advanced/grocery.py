def grocery_store(**kwargs):
    for key, value in kwargs.items():
        sorted_elements = sorted(kwargs.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
        result = ''
        for el in sorted_elements:
            result += f'{el[0]}: {el[1]}' + '\n'
        return result

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))