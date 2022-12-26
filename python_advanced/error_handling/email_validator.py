class NameTooShortError(Exception):
    """"Name must be more than 4 characters"""
    pass

class MustContainAtSymbolError(Exception):
    """Email must contain @"""

class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""

command = input()

while command != "End":
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        current_email = command.split("@")
        name = current_email[0]
        last = current_email[1].split(".")
        domain = "." + last[1]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif domain != ".com" and domain != ".bg" and domain != ".org" and domain != ".net":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    command = input()