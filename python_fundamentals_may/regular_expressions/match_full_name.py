import re

pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
names = input()
matches = re.findall(pattern, names)
print(' '.join(matches))
