synonyms = {}
word_count = int(input())
for x in range(word_count):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key in synonyms.keys():
    print(f"{key} - {', '.join(synonyms[key])}")