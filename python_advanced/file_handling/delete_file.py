import os

# file_path = "text.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)

try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')