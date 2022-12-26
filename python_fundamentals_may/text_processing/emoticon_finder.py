string = input().split()
for word in string:
    if ":" in word:
        print(f" {word[0]}{word[1]}")
