import unittest

def get_random_number():
    return 0

class TestGetRandomNumber(unittest.TestCase):
    def test_if_return_a_number(self):
        self.assertIsInstance(get_random_number(), int)


if __name__ == '__main__':
    unittest.main()