"""
A module for helper functions.
"""

from getpass import getpass
import sys
from banner import (
    display_exit_banner,
    display_lightsaber,
    display_login_banner,
)
from database import read_the_database, write_to_database
from password_validator import is_secure
from rot13 import encrypt, decrypt
from username_validator import is_valid_username


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
    while True:
        input_username = input("Username: ")

        # Check if the username is valid
        if not is_valid_username(input_username):
            print("")
            print("Invalid username. Please try again...")
            print("Username can contain alphabets, underscores, hyphens, and dots.")
            continue  # Prompt for username again

        # Read the database
        database = read_the_database()
        # Check if username already exists
        username_exists = any(
            stored_username == input_username
            for stored_username, stored_password in database
        )

        if username_exists:
            print(
                f"Username '{input_username}' is not available, please choose another one."
            )
        else:
            print(
                f"Username '{input_username}' is available! Proceeding to create account..."
            )
            break  # Exit the loop when a valid and unique username is found

    input_password = getpass("Password: ")
    print("Please retype the passoword")
    retype_password = getpass("Password: ")

    # Check if password is valid
    while not is_secure(input_password):
        print("")
        print("Invalid password.")
        print(
            """Password must be, at least 8 characters, one upper and lowercase,
            one digit, one punctuation"""
        )
        input_password = getpass("Password: ")
        print("Please retype the password")
        retype_password = getpass("Password: ")
        # Check if passwords match
        while input_password != retype_password:
            print("")
            print("Passwords do not match, please try again...")
            input_password = getpass("Password: ")
            print("Please retype the password")
            retype_password = getpass("Password: ")

    # Write the new username and password to the database
    write_to_database(input_username, encrypt(input_password))
    print("Account created successfully.")

    # Prompt user to sign in or exit
    print("")
    print("1. Sign in")
    print("2. Exit")
    choice = input("Please choose option 1, or 2: ")
    while choice not in ["1", "2"]:
        print("")
        print(f"Incorect input: {choice}. Please try again...")
        choice = input("Please choose option 1, or 2: ")
    choice = int(choice)

    match choice:
        case 1:
            sign_in()
        case 2:
            exit_program()
        case _:
            print("Invalid choice")


def landing_page() -> None:
    """
    Print landing page after succeful login.

    Parameters:
        None
    Return:
        None
    """
    # Implement a greeting, like, "Welcome, {username}"
    print("Your mission log is empty, young Padawan.")
    print("Time to recharge your lightsaber!")
    display_lightsaber()
    exit_program()


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
    input_password = getpass("Password: ")
    print("______________________________")

    # Read the database
    database = read_the_database()
    # Go through the credentials from database and chek if user exists
    for stored_username, stored_password in database:
        if input_username == stored_username and input_password == decrypt(
            stored_password
        ):
            display_login_banner()
            print("")
            print(f"Welcome, {input_username}")
            landing_page()


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
    sys.exit()


if __name__ == "__main__":
    # Test run
    create_account()
    # sign_in()
    # exit_program()
    # landing_page()
