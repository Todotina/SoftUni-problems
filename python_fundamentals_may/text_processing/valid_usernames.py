# def valid_length(string):
#     if 3 <= len(string) <= 16:
#         return True
#     return False
#
#
# def valid_character(string):
#     for character in string:
#         if character.isalnum() or character == "-" or character == "_":
#             return True
#     return False
#
#
# def no_redundant_symbols(string):
#     if " " in string:
#         return False
#     return True
#
#
# usernames = input().split(", ")
# for username in usernames:
#     if valid_length(username) and valid_character(username) and no_redundant_symbols(username):
#         print(username)

usernames = input().split(", ")
for username in usernames:
    username_is_valid = True
    if not 3 <= len(username) <= 16:
        username_is_valid = False
    for character in username:
        if not (character.isalnum() or character == "_" or character == "-"):
            username_is_valid = False
    if " " in username:
        username_is_valid = False
    if username_is_valid:
        print(username)
