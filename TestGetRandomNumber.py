import unittest
from random import randint

def get_random_number(minimal_range ,maximum_range):
    return randint(minimal_range, maximum_range)

class TestGetRandomNumber(unittest.TestCase):
    def test_if_return_a_number(self):
        self.assertIsInstance(get_random_number(1, 1), int)
    
    def test_it_return_a_number_in_range(self):
        mock_minimum_range = 0
        mock_maximum_range = 10

        self.assertTrue(get_random_number(mock_minimum_range ,mock_maximum_range) in list(range(10)))

    def test_it_not_return_negative_number(self):
        self.assertFalse(get_random_number(1, 1) < 0)


if __name__ == '__main__':
    unittest.main()