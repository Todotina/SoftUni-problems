import re

pattern = r'((w{3})\.([a-z0-9\-]+)(\.[a-z]+)+)'
text = input()
found_urls = []
while text:
    match = re.search(pattern, text)
    if match:
        found_urls.append(match.group(0))
    text = input()
for url in found_urls:
    print(url)

# import re
#
# valid_urls = []
# pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
# sentence = input()
# while sentence:
#     matches = re.search(pattern, sentence)
#     if matches:
#         valid_urls.append(matches.group(0))
#     sentence = input()
# for valid_url in valid_urls:
#     print(valid_url)