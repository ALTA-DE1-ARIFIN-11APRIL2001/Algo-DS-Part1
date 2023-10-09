import unittest
from main import generate_primes_grid

class TestGeneratePrimesGrid(unittest.TestCase):
    def test_case_1(self):
        expected_output = '17 19\n23 29\n31 37\n'
        actual_output = generate_primes_grid(2, 3, 13)
        self.assertEqual(actual_output, expected_output)

    def test_case_2(self):
        expected_output = '2  3  5  7  11\n13 17 19 23 29\n'
        actual_output = generate_primes_grid(5, 2, 1)
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
