LENGTH_OF_PASSWORD = 8


def main():
    password = get_valid_password()
    print_asteriks(password)


def get_valid_password():
    password = input("Password: ")
    while len(password) < LENGTH_OF_PASSWORD:
        print("Invalid password, minimum of 8 characters.")
        password = input("Password: ")
    return password


def print_asteriks(password):
    print("*" * len(password))


main()
