"""
Test cases for the login system module.
"""

from password_validator import (
    check_length,
    check_case,
    check_digit,
    check_punctuation,
    is_secure,
)
from rot13 import encrypt, decrypt
from username_validator import (
    check_length_user,
    check_allowed_characters,
    check_offensive_content,
    check_spaces,
    check_consecutive_punctuation,
    is_valid_username,
)
import unittest


class TestLoginSystem(unittest.TestCase):
    """
    Test cases for modules
    """

    def test_short_password(self):
        """
        Test short password
        """
        self.assertFalse(check_length("short"))

    def test_long_passowrd(self):
        """
        Test long password
        """
        self.assertTrue("longpassword")

    def test_only_lowercase(self):
        """
        Test lowercase password
        """
        self.assertEqual(check_case("lowercase"), False)

    def test_only_uppercase(self):
        """
        Test uppercase password.
        """
        self.assertEqual(check_case("UPPERCASE"), False)

    def test_mix_case(self):
        """
        Test uppercase and lowercase
        """
        self.assertEqual(check_case("miXcAsE"), True)

    def test_no_digit(self):
        """
        Test password without a digit
        """
        self.assertEqual(check_digit("nodigit"), False)

    def test_with_digit(self):
        """
        Test password with digit
        """
        self.assertEqual(check_digit("withdigit9"), True)

    def test_no_punctuation(self):
        """
        Test password without special characters.
        """
        self.assertEqual(check_punctuation("nopunctuation"), False)

    def test_spaces_check(self):
        """
        Test for password with spaces.
        """
        self.assertEqual(check_punctuation("with spaces "), False)

    def test_with_punctuation(self):
        """
        Test for password with punctuation
        """
        self.assertEqual(check_punctuation("with!punc%tuation@"), True)

    def test_not_sucure(self):
        """
        Test not secure password
        """
        self.assertFalse(is_secure("No#t Secu!r3"))

    def test_secure_pasword(self):
        """
        Test secure password
        """
        self.assertTrue(is_secure("sEcur3p@W0rd"))

    def test_short_usernames(self):
        """
        Test short username
        """
        self.assertEqual(check_length_user("sl"), False)

    def test_long_username(self):
        """
        Test long username
        """
        self.assertFalse(check_length_user("abcdefghijklmnopqrstuvxyz"))

    def test_valid_length_username(self):
        """
        Test valid valid length password
        """
        self.assertTrue(check_length_user("sakhile"))

    def test_invalid_characters(self):
        """
        Test invalid characters
        """
        self.assertFalse(check_allowed_characters("user@!"))

    def test_valid_characters(self):
        """
        Test valid characters
        """
        self.assertTrue(check_allowed_characters("aA0._-"))

    def test_normal_words(self):
        """
        Test normal words
        """
        self.assertFalse(check_offensive_content("user"))

    def test_offensive_word(self):
        """
        Test offensive word
        """
        self.assertTrue(check_offensive_content("wacky"))

    def test_no_spaces_username(self):
        """
        Test username valid no space username
        """
        self.assertTrue(check_spaces("valid"))

    def test_spaces_username(self):
        """
        Test username with spaces
        """
        self.assertFalse(check_spaces(" spa ces  "))

    def test_repeated_special_characters(self):
        """
        Test username with repeated special charavters
        """
        self.assertFalse(check_consecutive_punctuation("__repeated"))

    def test_no_repeated_special(self):
        """
        Test username with no repeated special characters
        """
        self.assertTrue(check_consecutive_punctuation("_valid."))

    def test_valid_username(self):
        """
        Test for valid username
        """
        self.assertEqual(is_valid_username("abc"), True)

    def test_invalid_username(self):
        """
        Test invalid username
        """
        self.assertFalse(is_valid_username("abc__"))

    def test_alpha_encrypt(self):
        """
        Test ecnryption of a given string
        """
        self.assertEqual(encrypt("abC"), "noP")

    def test_alpha_numeric_encrypt(self):
        """
        Test encryption with alpha numeric strings
        """
        self.assertEqual(encrypt("12345xyZ"), "12345klM")

    def test_sample_passwords(self):
        """
        Test sample password encryption.
        """
        self.assertEqual(encrypt("sd3nJnK@NS@NDn0"), "fq3aWaX@AF@AQa0")

    def test_alpha_decrypt(self):
        """
        Test decryption of simple string
        """
        self.assertEqual(decrypt("noP"), "abC")

    def test_alpha_numeric(self):
        """
        Test encryption with alphanumeric strings
        """
        self.assertEqual(decrypt("123klM456"), "123xyZ456")

    def test_sample_password_decrypt(self):
        """
        Test decryption of sample password
        """
        self.assertEqual(decrypt("fq3aWaX@AF@AQa0"), "sd3nJnK@NS@NDn0")


if __name__ == "__main__":
    unittest.main()
