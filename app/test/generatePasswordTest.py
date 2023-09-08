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


class TestHashPassword(unittest.TestCase):

    def test_hash_password_sha256(self):
        # Test password hashing with SHA-256
        test_password = "testpassword"
        hashed_password = hash_password(test_password, "sha256")
        self.assertTrue(isinstance(hashed_password, str))
        self.assertEqual(len(hashed_password), 64)

    def test_hash_password_md5(self):
        # Test password hashing with MD5
        test_password = "testpassword"
        hashed_password = hash_password(test_password, "md5")
        self.assertTrue(isinstance(hashed_password, str))
        self.assertEqual(len(hashed_password), 32)

    def test_hash_password_invalid_algorithm(self):
        # Test password hashing with invalid algorithm
        test_password = "testpassword"
        with self.assertRaises(ValueError):
            hash_password(test_password, "invalid_algorithm")


if __name__ == '__main__':
    unittest.main()
