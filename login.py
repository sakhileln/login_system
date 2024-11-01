print("______________________________")
print("     A Simple Login System   ")
print("******************************")
print()

print("1. Login")
print("2. Create account")
print("3. Exit")
choice = input("Please choose 1, 2, or 3: ")
while choice not in ["1", "2", "3"]:
    print("")
    print(f"Incorrect input: {choice}. Please try again...")
    choice = input("Please choose 1, 2, or 3: ")
choice = int(choice)


def create_account() -> None:
    """
    Function that handles user account creation

    Parameters:
        None.
    Return:
        None.
    """
    input_username = input("Username: ")
    input_password = input("Password: ")
    print("Please retype the passoword")
    retype_password = input("Password: ")


def sign_in() -> None:
    """
    Function that handles user sign in.

    Parameters:
        None.
    Return:
        None.
    """
    username = input("Username: ")
    password = input("Password: ")
    print("______________________________")


# print(username, password)
