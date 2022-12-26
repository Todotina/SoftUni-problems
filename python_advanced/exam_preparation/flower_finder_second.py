from collections import deque


# def check_character(chr_one, chr_two, string):
#     if chr_one in string:
#         string.replace(".", chr_one)
#     if chr_two in string:
#         string.replace(".", chr_two)
#     return string


vowels = deque(input().split())
consonants = deque(input().split())

rose = ['.', '.', '.', '.']
tulip = ['.', '.', '.', '.', '.']
lotus = ['.', '.', '.', '.', '.']
daffodil = ['.', '.', '.', '.', '.', '.', '.', '.']

while vowels:
    if len(consonants) == 0:
        print("Cannot find any word!")
        break
    f_chr = vowels.popleft()
    l_chr = consonants.pop()
    if f_chr in "rose":
        ind = 'rose'.index(f_chr)
        rose.insert(ind, f_chr)
    elif f_chr in "tulip":
        ind = 'tulip'.index(f_chr)
        tulip.insert(ind, f_chr)
    elif f_chr in "lotus":
        ind = 'lotus'.index(f_chr)
        lotus.insert(ind, f_chr)
    elif f_chr in "daffodil":
        ind = 'daffodil'.index(f_chr)
        daffodil.insert(ind, f_chr)
    if l_chr in "rose":
        ind = 'rose'.index(l_chr)
        rose.insert(ind, l_chr)
    elif l_chr in "tulip":
        ind = 'tulip'.index(l_chr)
        tulip.insert(ind, l_chr)
    elif l_chr in "lotus":
        ind = 'lotus'.index(l_chr)
        lotus.insert(ind, l_chr)
    elif l_chr in "daffodil":
        ind = 'daffodil'.index(l_chr)
        daffodil.insert(ind, l_chr)
    if f'{"".join(x for x in rose)}' == "rose":
        print("Word found: rose")
        break
    elif f'{"".join(x for x in tulip)}' == "tulip":
        print("Word found: tulip")
        break
    elif f'{"".join(x for x in lotus)}' == "lotus":
        print("Word found: lotus")
        break
    elif f'{"".join(x for x in daffodil)}' == "daffodil":
        print("Word found: daffodil")
        break

if vowels:
    print(f'Vowels left: {" ".join(x for x in vowels)}')
else:
    print("Cannot find any word!")
if consonants:
    print(f'Consonants left: {" ".join(x for x in consonants)}')