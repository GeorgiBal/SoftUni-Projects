def validate(password_v):
    valid = True
    if len(password_v) < 6 or len(password_v) > 10:
        print("Password must be between 6 and 10 characters")
        valid = False

    for i in password_v:
        if not i.isalnum():
            print("Password must consist only of letters and digits")
            valid = False
            break

    digits = 0
    for i in password_v:
        if i.isdigit():
            digits += 1

    if digits < 2:
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


password = input()
validate(password)
