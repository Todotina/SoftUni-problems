def shopping_cart(*args):
    dict = {
        'Pizza': [],
        'Dessert': [],
        'Soup': []
    }
    result = ""
    for el in args:
        if el == "Stop":
            break
        if el[0] == "Pizza" and len(dict[el[0]]) < 4 and el[1] not in dict[el[0]]:
            dict[el[0]].append(el[1])
        elif el[0] == "Soup" and len(dict[el[0]]) < 3 and el[1] not in dict[el[0]]:
            dict[el[0]].append(el[1])
        elif el[0] == "Dessert" and len(dict[el[0]]) < 2 and el[1] not in dict[el[0]]:
            dict[el[0]].append(el[1])
    sorted_dict = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))
    if len(sorted_dict[0][1]) == 0 and len(sorted_dict[1][1]) == 0 and len(sorted_dict[2][1]) == 0:
        return "No products in the cart!"
    else:
        for item in sorted_dict:
            result += item[0] + ":" + '\n'
            for el in sorted(item[1]):
                result += " " + "-" + " " + el + '\n'
        return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))