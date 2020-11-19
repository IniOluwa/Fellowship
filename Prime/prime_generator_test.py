import unittest
from prime_generator import nth_prime

class TestPrimeNumbers(unittest.TestCase):
    def test_when_n_is_one(self):
        self.assertEqual(nth_prime(1), 2, msg="First prime number should be 2")

    def test_when_n_is_two(self):
        self.assertEqual(nth_prime(2), 3, msg="Second prime number should be 3")

    def test_when_n_is_negative(self):
        self.assertFalse(nth_prime(-1), msg="Negative numbers should not be allowed")

    def test_when_n_is_zero(self):
        self.assertFalse(nth_prime(0), msg="Zero should not be allowed")

    def test_when_no_argument_passed(self):
        with self.assertRaises(TypeError):
            nth_prime()

if __name__ == '__main__':
    unittest.main()
