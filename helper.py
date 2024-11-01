"""
A module for helper functions.
"""


def create_account() -> None:
    """
    Function that handles user account creation

    Parameters:
        None.
    Return:
        None.
    """
    print("")
    print("----------Create account----------")
    input_username = input("Username: ")
    input_password = input("Password: ")
    print("Please retype the passoword")
    retype_password = input("Password: ")
    if input_password == retype_password:
        with open("database.txt", "a", errors="ignore") as f:
            f.write(f"{input_username}:{input_password}\n")
        print("Account created successfully.")
    else:
        print("Passwords do not match. Please try again")


def sign_in() -> None:
    """
    Function that handles user sign in.

    Parameters:
        None.
    Return:
        None.
    """
    print("")
    print("----------Sign in----------")
    username = input("Username: ")
    password = input("Password: ")
    print("______________________________")


def exit_program() -> None:
    """
    Exit the program.

    Parameters:
        None.
    Return:
        None.
    """
    print("Thank you for using our Space Software.")
    print("See you soon...")
    exit()


if __name__ == "__main__":
    # Test run
    create_account()
    sign_in()
    exit_program()
