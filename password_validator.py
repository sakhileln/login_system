"""
A module to validate if password is secure.
"""

from string import punctuation


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


def check_punctuation(password: str) -> bool:
    """
    Check if password has special characters.

    Parameters:
        password -> str: Password to be checked
    Return:
        Boolean -> True/False
    """
    if " " in password:
        return False
    for ch in password:
        if ch in punctuation:
            return True
    return False


def is_secure(password: str) -> bool:
    """
    Check is password is secure.

    Parameters:
        password (str): Password to be checked
    Return:
        bool: True if secure, False otherwise
    """
    if (
        check_length(password)
        and check_case(password)
        and check_digit(password)
        and check_punctuation(password)
    ):
        return True
    return False


if __name__ == "__main__":
    # Test cases
    password = "sEcur3p@W0rd!"
    print(is_secure(password))  # Output: True
