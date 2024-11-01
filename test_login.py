"""
Test cases for the login system module.
"""

from password_validator import check_length
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


if __name__ == "__main__":
    unittest.main()
