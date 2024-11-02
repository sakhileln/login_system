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

    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users(username, password)")
    res = cursor.execute("SELECT * FROM sqlite_master")

    # Close the connection once done
    connection.close()


if __name__ == "__main__":
    # create_database()