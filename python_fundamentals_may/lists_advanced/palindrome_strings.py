words = input().split(" ")
palindrome = input()
palindrome_list = []
for element in words:
    if element == "".join(reversed(element)):
        palindrome_list.append(element)

palindrome_count = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")