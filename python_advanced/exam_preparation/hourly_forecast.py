def forecast(*args):
    sunny = []
    cloudy = []
    rainy = []
    result = ""
    for el in args:
        location = el[0]
        weather = el[1]
        if weather == "Sunny":
            sunny.append(location)
        elif weather == "Cloudy":
            cloudy.append(location)
        elif weather == "Rainy":
            rainy.append(location)
    for el in sorted(sunny):
        result += el + " " + "-" + " " + "Sunny" + '\n'
    for el in sorted(cloudy):
        result += el + " " + "-" + " " + "Cloudy" + '\n'
    for el in sorted(rainy):
        result += el + " " + "-" + " " + "Rainy" + '\n'
    return result

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

