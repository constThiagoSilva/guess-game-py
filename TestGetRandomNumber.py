import unittest
from getRandomNumber import get_random_number

class TestGetRandomNumber(unittest.TestCase):
    def test_if_return_a_number(self):
        self.assertIsInstance(get_random_number(1, 1), int)
    
    def test_it_return_a_number_in_range(self):
        mock_minimum_range = 0
        mock_maximum_range = 10

        self.assertTrue(get_random_number(mock_minimum_range ,mock_maximum_range) in list(range(mock_maximum_range + 1)))

    def test_it_throws_an_error_if_parameters_are_negative(self):
        mock_minimum_range = -10
        mock_maximum_range = -1
        
        with self.assertRaises(TypeError) as error:
            get_random_number(mock_minimum_range, 10)
            self.assertEqual('mininum range cannot be negative', str(error.exception))

        with self.assertRaises(BaseException) as error:
            get_random_number(0, mock_maximum_range)
            self.assertEqual('maximum range cannot be negative', str(error.exception))

    def test_it_not_return_negative_number(self):
        self.assertFalse(get_random_number(1, 1) < 0)


if __name__ == '__main__':
    unittest.main()