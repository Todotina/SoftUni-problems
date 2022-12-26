def naughty_or_nice_list(list, *args, **kwargs):
    dict = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }
    result = ''
    kids = {}
    kids_second = {}
    for el in list:
        if el[0] not in kids:
            kids[el[0]] = []
        kids[el[0]].append(el[1])
        if el[1] not in kids_second:
            kids_second[el[1]] = []
        kids_second[el[1]].append(el[0])
    for arg in args:
        number, type = arg.split("-")[0], arg.split("-")[1]
        if int(number) in kids and len(kids[int(number)]) == 1:
            dict[type].append(kids[int(number)][0])
            del kids[int(number)]
    for name, type in kwargs.items():
        if len(kids_second[name]) == 1:
            dict[type].append(name)
            del kids_second[name]
    first_kids_list = []
    for item in kids.values():
        for el in range(len(item)):
            first_kids_list.append(item[el])
    first_kids = set(first_kids_list)
    second_kids = set([x for x in kids_second.keys()])
    for item in first_kids.intersection(second_kids):
        dict['Not found'].append(item)
    for key, value in dict.items():
        if len(key) > 0:
            result += key + ":"
            result += " " + f'{", ".join(str(x) for x in value)}' + '\n'
    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))