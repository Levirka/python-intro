import unittest
from app import is_valid_email, add, get_even_numbers, reverse_date, is_palindrome

class TestFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid.com"))
        self.assertFalse(is_valid_email(""))

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(2, 2), 5)

    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(get_even_numbers([]), [])
        self.assertEqual(get_even_numbers([1, 3, 5]), [])

    def test_reverse_date(self):
        self.assertEqual(reverse_date("2024-05-01"), "01.05.2024")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("Kobyła ma mały bok"))
        self.assertFalse(is_palindrome("pies"))

if __name__ == '__main__':
    unittest.main()
