"""
Test cases for the login system module.
"""

from password_validator import check_length, check_case
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


if __name__ == "__main__":
    unittest.main()
