def encrypt(string: str) -> str:
    """
    Encrypt given string using ROT13 cipher.

    Parameters:
        string (str): The string to encrypt
    Return:
        string (str): Encrypted string
    """
    encrypted_string = ""
    for ch in string:
        shift = 13
        if ch.isalpha():
            if ch.islower():
                character = (((ord(ch) - ord("a")) + 13) % 26) + ord("a")
                encrypted_string += chr(character)
            elif ch.isupper():
                character = (((ord(ch) - ord("A")) + 13) % 26) + ord("A")
                encrypted_string += chr(character)
        else:
            encrypted_string += ch

    return encrypted_string


def decrypt(string: str) -> str:
    """
    Decrypt given string using ROT13 cipher

    Parameters:
        string (str): The string to decrpyt
    Return:
        string (str): Decrypted string
    """
    pass
