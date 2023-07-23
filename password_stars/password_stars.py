def get_password():
    while True:
        password = input("Enter a password (minimum length of 10 characters): ")
        if len(password) >= 10:
            return password
        else:
            print("Password is too short. Please try again.")


def print_asterisks(password):
    print(".Pythonista " + "*" * (len(password)))


def main():
    password = get_password()
    print_asterisks(password)


main()
