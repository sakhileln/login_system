"""
A module for handling database read and write.
"""

import sqlite3


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


if __name__ == "__main__":
    create_database()