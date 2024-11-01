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


def check_case(password: str) -> bool:
    """
    Check if password has upper and lowercase characters.

    Parameters:
        password-> str: Password to be checked
    Rturn:
        Boolean-> bool: True/Fale
    """

    # Check if there is a lowercase
    def check_lowercase(string):
        for ch in string:
            if ch.islower():
                return True
        return False

    # Check if there is an uppercase
    def check_uppercase(string):
        for ch in string:
            if ch.isupper():
                return True
        return False

    # Check for lowercase and uppercase
    if check_lowercase(password) and check_uppercase(password):
        return True

    return False


def check_digit(password: str) -> bool:
    """
    Check if password has digit.

    Parameters:
        password -> str: Passwrod to be checked
    Return:
        Boolean -> True/False
    """
    for ch in password:
        if ch.isdigit():
            return True
    return False
