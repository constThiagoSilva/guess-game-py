import unittest

def get_random_number(range):
    return 0

class TestGetRandomNumber(unittest.TestCase):
    def test_if_return_a_number(self):
        self.assertIsInstance(get_random_number(1), int)
    
    def test_it_return_a_number_in_range(self):
        mock_random_range = 10
        
        self.assertTrue(get_random_number(mock_random_range) in list(range(10)))


if __name__ == '__main__':
    unittest.main()