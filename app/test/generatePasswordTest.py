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
        # Test hashing with SHA-256
        test_cases = [
            {"password": "password123",
             "expected_hash": "3c1e1c0ec2b72e4b152f3b8a3c1d5b5d8f2886bf8c2a7c0b9f7d3c24d1d8f4d6"},
            {"password": "test123",
             "expected_hash": "3b6dd2b8f4c09565a8a0b6c1c0a4853e4dc1e1f7c4baabf77d5b8b9a3a6e09cc"},
            {"password": "", "expected_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
            # Empty password case
        ]

        for case in test_cases:
            with self.subTest(case=case):
                hashed_password = hash_password(case["password"], "sha256")
                self.assertEqual(hashed_password, case["expected_hash"])

    def test_hash_password_md5(self):
        # Test hashing with MD5
        test_cases = [
            {"password": "password123", "expected_hash": "482c811da5d5b4bc6d497ffa98491e38"},
            {"password": "test123", "expected_hash": "098f6bcd4621d373cade4e832627b4f6"},
            {"password": "", "expected_hash": "d41d8cd98f00b204e9800998ecf8427e"}  # Empty password case
        ]

        for case in test_cases:
            with self.subTest(case=case):
                hashed_password = hash_password(case["password"], "md5")
                self.assertEqual(hashed_password, case["expected_hash"])


if __name__ == '__main__':
    unittest.main()
