command = input()
results = {}
languages = {}

while command != "exam finished":
    current_command = command.split("-")
    if len(current_command) > 2:
        username, language, points = current_command[0], current_command[1], int(current_command[2])
        if username not in results:
            results[username] = {}
            results[username]['language'] = language
            results[username]['points'] = []
            results[username]['points'].append(points)
            languages[language] = []
            languages[language].append(points)
        else:
            results[username]['points'].append(points)
            languages[language].append(points)
    else:
        username = current_command[0]
        del results[username]
    command = input()
print(results)
print(languages)