def start_spring(**kwargs):
    result = ''
    dict = {}
    for key, value in kwargs.items():
        if value not in dict:
            dict[value] = []
        dict[value].append(key)
    sorted_items = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for element in sorted_items:
        result += element[0] + ':' + '\n'
        for item in sorted(element[1]):
            result += "-" + item + '\n'
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))




