banned_words = input().split(", ")
text = input()
for word in banned_words:
    if word in text:
        symbol = len(word) * "*"
        text = text.replace(word, symbol)
print(text)