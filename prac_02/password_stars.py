LENGTH_OF_PASSWORD = 8

password = input("Password: ")
while len(password) < LENGTH_OF_PASSWORD:
    print("Invalid password, minimum of 8 characters.")
    password = input("Password: ")
print("*" * len(password))