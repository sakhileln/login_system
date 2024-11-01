"""
A module for helper functions.
"""

from banner import display_exit_banner
from password_validator import is_secure


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

    # Check if password is valid
    while not is_secure(input_password):
        print("")
        print("Invalid password.")
        print(
            "Password must be, at least 8 characters, one upper and lowercase, one digit, one punctuation"
        )
        input_password = input("Password: ")
        print("Please retype the password")
        retype_password = input("Password: ")
        # Check if passwords match
        while input_password != retype_password:
            print("")
            print("Passwords do not match, please try again...")
            input_password = input("Password: ")
            print("Please retype the password")
            retype_password = input("Password: ")

    if input_password == retype_password:
        with open("database.txt", "a", errors="ignore") as f:
            f.write(f"{input_username}:{input_password}")
            f.write("\n")
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
    input_username = input("Username: ")
    input_password = input("Password: ")
    print("______________________________")
    with open("database.txt", "r", errors="ignore") as f:
        database = f.read().split()
    for line in database:
        stored_username, stored_password = line.split(":")
        if input_username == stored_username and input_password == stored_password:
            print("Login successful.")
            print(f"Welcome, {input_username}")


def exit_program() -> None:
    """
    Exit the program.

    Parameters:
        None.
    Return:
        None.
    """
    print("")
    print("        See you soon...")
    display_exit_banner()
    exit()


if __name__ == "__main__":
    # Test run
    create_account()
    # sign_in()
    # exit_program()
