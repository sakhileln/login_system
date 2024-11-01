"""
A module to validate if password is secure.
"""

# Length minimun >= 8
# At least one upper and lowercase character
# Has a digit
# Contains at least one Special characters


def check_length(password: str) -> bool:
    """
    Check if password length is greater than or equal to 8 characters.

    Parameters:
        password -> str: Password to be checked
    Return:
        Boolean -> bool: True/False
    """
    if len(password) >= 8:
        return True
    return False
