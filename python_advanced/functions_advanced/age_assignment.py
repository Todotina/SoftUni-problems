def age_assignment(*args, **kwargs):
    dict = {}
    result = ''
    for key, value in kwargs.items():
        for el in args:
            if el[0] == key:
                dict[el] = value
    sorted_items = sorted(dict.items(), key= lambda x: x[0])
    for item in sorted_items:
        result += f"{item[0]} is {item[1]} years old." + '\n'
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))