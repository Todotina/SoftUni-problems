import re

pattern = r'\b\_([a-zA-Z0-9]+)\b'
names = input()
matches = re.findall(pattern, names)
if matches:
    print(','.join(matches))