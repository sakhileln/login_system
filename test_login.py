"""
Test cases for the login system module.
"""

from password_validator import check_length, check_case, check_digit, check_punctuation
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


if __name__ == "__main__":
    unittest.main()
