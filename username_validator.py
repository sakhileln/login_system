# 1. Length
# Minimum Length: Typically between 3 to 6 characters.
# Maximum Length: Often capped at around 15 to 30 characters.

# 2. Allowed Characters
# Letters: Typically allow both uppercase and lowercase letters (A-Z, a-z).
# Numbers: Usually allow digits (0-9).
# Special Characters: Decide if you want to allow characters like underscores (_), hyphens (-), or dots (.) and define a clear set.

# 3. No Offensive Content
# Profanity Filtering: Block usernames that contain offensive or inappropriate words.
# Cultural Sensitivity: Avoid names that might be culturally insensitive or offensive.

# 4. No Leading or Trailing Spaces
# Ensure there are no leading or trailing whitespace characters.

# 5. No Consecutive Special Characters
# Restrict repeated special characters (e.g., “__” or “--”).

# 6. Case Sensitivity
# Decide if usernames are case-sensitive. Commonly, they are not (e.g., "UserName" and "username" are treated as the same).\


"""
A module for username validation.
"""

from re import match


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


def username_validator(username: str) -> bool:
    """
    Validate provided username according to a set rules.

    Parameters:
        username (str): Username to be checked
    Return:
        bool: True if valid, False otherwise
    """
    if check_length_user(username):
        return True
    return False
