def add_songs(*args):
    titles = {}
    result = ''
    for song in args:
        title = song[0]
        if title not in titles:
            titles[title] = []
        if len(song[1]) > 0:
            for line in song[1]:
                titles[title].append(line)
    for key, value in titles.items():
        result += (f'- {key}') + '\n'
        if len(value) > 0:
            for item in value:
                result += (f'{item}') + '\n'
    return result

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))