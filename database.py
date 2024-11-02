"""
A module for handling database read and write.
"""

import sqlite3
from rot13 import encrypt, decrypt


def create_database() -> None:
    """
    The function will create the database tables once.

    Parameters:
        None
    Return:
        None
    """
    # Initiate connection to the database
    connection = sqlite3.connect("credentials.sqlite")

    # Cursor is used to execute SQL commands and fetch data
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")

    # Close the connection once done
    connection.close()


def write_to_database(username: str, password: str) -> None:
    """
    Write given credentials to the database.

    Parameters:
        username (str): The username to be written
        password (str): The password for new user
    Return:
        None
    """
    # Hash the password (Can use bcrypt)
    hashed_password = encrypt(password)

    # Initiate connection to the database.
    connection = sqlite3.connect("credentials.sqlite")
    # Cursor to execute commands and fetch data.
    cursor = connection.cursor()

    try:
        # Create the new user
        cursor.execute(
            "INSERT INTO users (username, password) VALUES(?, ?)",
            (username, hashed_password)
        )
        # Write changes to the database.
        connection.commit()
    except Exception as e:
        print(f"An error occured: {e}")
    
    finally:
        # Close the connection
        connection.close()


if __name__ == "__main__":
    # create_database()
    write_to_database("steve", "Jobs2011")
