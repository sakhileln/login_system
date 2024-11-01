"""
A module for username validation.
"""

from re import match, search


def check_length_user(username: str) -> bool:
    """
    Check password length

    Parameters:
        username (str): Username to be checked
    Return:
        bool: True if within range, False otherwise
    """
    if 3 <= len(username) <= 20:
        return True
    return False


def check_allowed_characters(username: str) -> bool:
    """
    Check if username has lower and uppercase, numbers, underscores, dot,
    and hyphens

    Parameters:
        username (str): Username to be checked
    Return:
        bool: True if contain valid characters, False otherwise
    """
    if match("^[a-zA-Z0-9._-]*$", username):
        return True
    return False


def check_offensive_content(username: str) -> bool:
    """
    Check if username contains any offensive words.

    Parameters:
        username (str): Username to check
    Return:
        bool: True if contains offensice words
    """
    with open("offensive_content.txt", "r", errors="ignore") as f:
        offensive_words = f.read().split()
    for word in offensive_words:
        if word == username:
            return True
    return False


def check_spaces(username: str) -> bool:
    """
    Check for spaces in a username.

    This function checks if the provided username contains any leading,
    trailing, or consecutive spaces within the username. A valid username
    should not start or end with spaces and should not contain multiple
    consecutive spaces.

    Paramaters:
        username (str): The username to check
    Return:
        bool: True if unsername has no spaces, False otherwise
    """
    if " " in username:
        return False
    return True


def check_consecutive_punctuation(username: str) -> bool:
    """
    Check repeated special characters

    Parameters:
        username (str): The username to check
    Return:
        bool: True if username has no repeated special characters, else False
    """
    # Regex pattern for consecutive special characters
    pattern = r"[^a-zA-Z0-9]{2,}"
    return not bool(search(pattern, username))  # Search for pattern in username


def is_valid_username(username: str) -> bool:
    """
    Check is username is valid according to criteria

    Parameters:
        username (str): The username to be checked
    Return:
        bool: True if valid, False otherwise
    """
    if (
        check_length_user(username)
        and check_allowed_characters(username)
        and check_offensive_content(username)
        and check_spaces(username)
        and check_consecutive_punctuation(username)
    ):
        return True
    return False


if __name__ == "__main__":
    # Test cases
    check_offensive_content("wacky")  # Output: True
