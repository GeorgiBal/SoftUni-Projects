def validate_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def validate_chars(username):
    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False

    return True


def validate_symbols(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if validate_length(username) and validate_chars(username) and validate_symbols(username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)