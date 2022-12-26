def even_odd_filter(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        if key == "even":
            modified_value = [x for x in value if x % 2 == 0]
            dictionary['even'] = modified_value
        else:
            modified_value = [x for x in value if x % 2 != 0]
            dictionary['odd'] = modified_value
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))
    return sorted_dict

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))