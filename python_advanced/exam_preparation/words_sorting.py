def words_sorting(*args):
    dict = {}
    total_sum = 0
    result = ''
    for item in args:
        sum = 0
        for chr in item:
            sum += ord(chr)
            total_sum += sum
        dict[item] = sum
    if total_sum % 2 == 0:
        sorted_dict = sorted(dict.items(), key= lambda x: x[0])
    else:
        sorted_dict = sorted(dict.items(), key= lambda x: -x[1])
    for el in sorted_dict:
        result += f"{el[0]} - {el[1]}" + '\n'
    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))