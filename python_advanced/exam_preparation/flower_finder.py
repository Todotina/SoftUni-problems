from collections import deque


def check_chr(chr, string):
    if chr in string:
        ind = string.index(chr)
        return ind


def check_flower(flower):
    string = ''
    sorted_flower = sorted(flower.items(), key= lambda x: x[1])
    for item in sorted_flower:
        string += item[1]
    if string == flower:
        return True


rose = {}
tulip = {}
lotus = {}
daffodil = {}
vowels = deque(input().split())
consonants = deque(input().split())

while vowels:
    if check_flower(rose):
        print("Word found: rose")
        break
    elif check_flower(tulip):
        print("Word found: tulip")
        break
    elif check_flower(lotus):
        print("Word found: lotus")
        break
    elif check_flower(daffodil):
        print("Word found: daffodil")
        break
    if len(consonants) == 0:
        print("Cannot find any word!")
        break
    first_chr = vowels.popleft()
    if check_chr(first_chr, rose):
        rose[first_chr] = check_chr(first_chr, rose)
    elif check_chr(first_chr, tulip):
        tulip[first_chr] = check_chr(first_chr, tulip)
    elif check_chr(first_chr, lotus):
        lotus[first_chr] = check_chr(first_chr, lotus)
    elif check_chr(first_chr, daffodil):
        daffodil[first_chr] = check_chr(first_chr, daffodil)
    last_chr = consonants.pop()
    if check_chr(last_chr, rose):
        rose[last_chr] = check_chr(last_chr, rose)
    elif check_chr(last_chr, tulip):
        tulip[last_chr] = check_chr(last_chr, tulip)
    elif check_chr(last_chr, lotus):
        lotus[last_chr] = check_chr(last_chr, lotus)
    elif check_chr(last_chr, daffodil):
        daffodil[last_chr] = check_chr(last_chr, daffodil)

if vowels:
    print(f'Vowels left: {" ".join(x for x in vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(x for x in consonants)}')