def palindrome(word:str, index:int):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    first, last = word[index], word[-index - 1]
    if first != last:
        return f"{word} is not a palindrome"

    return palindrome(word, index+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))