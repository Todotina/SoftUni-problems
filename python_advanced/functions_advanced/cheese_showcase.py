def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key = lambda x: (-len(x[1]), x[0]))
    result_str = ''
    for key, value in result:
        sorted_el = sorted(value, reverse=True)
        result_str += key + '\n'
        result_str += '\n'.join(str(x) for x in sorted_el) + '\n'
    return result_str

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
