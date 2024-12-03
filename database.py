"""
A module for handling database read and write.
"""

import sqlite3
from rot13 import encrypt


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
            (username, hashed_password),
        )
        # Write changes to the database.
        connection.commit()
    except sqlite3.DatabaseError as e:
        print(f"An error occured writing to database: {e}")

    finally:
        # Close the connection
        connection.close()


def read_the_database() -> list:
    """
    Read the usernames and passwords.

    Parameters:
        None
    Return:
        None
    """
    # Initiate database connection.
    connection = sqlite3.connect("credentials.sqlite")
    # Cursor for executing commands and reading database
    cursor = connection.cursor()

    try:
        # Read the database
        response = cursor.execute("SELECT * FROM users")
        # Retrive all credentials
        credentials = response.fetchall()
    except sqlite3.DatabaseError as e:
        print(f"An error occured reading database: {e}")

    finally:
        # Close the database connection
        connection.close()

    # Return the credentials
    return credentials


if __name__ == "__main__":
    # create_database()
    # write_to_database("steve", "Jobs2011")
    print(read_the_database())
