import string
import unittest
from app.utils.generate_password import generate_password, hash_password


class TestGeneratePassword(unittest.TestCase):

    def test_geration_pass_password_with_digits_and_symbols(self):
        password = generate_password(12, use_digits=True, use_symbols=True)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_password_with_digits_only(self):
        password = generate_password(10, use_digits=True, use_symbols=False)
        self.assertEqual(len(password), 10)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_generate_password_with_symbols_only(self):
        password = generate_password(15, use_digits=False, use_symbols=True)
        self.assertEqual(len(password), 15)
        self.assertFalse(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_password_without_digits_and_symbols(self):
        password = generate_password(8, use_digits=False, use_symbols=False)
        self.assertEqual(len(password), 8)
        self.assertFalse(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_generate_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(6, use_digits=True, use_symbols=True)
if __name__ == '__main__':
    unittest.main()
