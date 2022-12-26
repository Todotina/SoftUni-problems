def password_check(password):
    password_is_valid = True
    if 6 > len(password) or len(password) > 10:
        password_is_valid = False
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        password_is_valid = False
        print("Password must consist only of letters and digits")
    digits_counter = 0
    for character in password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        password_is_valid = False
        print("Password must have at least 2 digits")
    return password_is_valid


password = input()
is_valid = password_check(password)
if is_valid:
    print("Password is valid")