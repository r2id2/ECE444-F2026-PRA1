# import unittest module and utils class
import unittest
from utils import utils

# create the utils object (from utils.py) that we want to test
u = utils()

# create a class for testing the utils class
class TestUtils(unittest.TestCase):

    # test reversed() with an integer
    def test_reversed_int(self):
        self.assertEqual(utils().reversed(123), 321)

    # test reversed() with a string
    def test_reversed_string(self):
        with self.assertRaises(TypeError):
            utils().reversed("123")

    # test reversed() with a float
    def test_reversed_float(self):
        with self.assertRaises(TypeError):
            utils().reversed(12.3)

    # test formatter() with an integer
    def test_formatter_int(self):
        self.assertEqual(utils().formatter(10), ("0b1010", "0o12"))

    # test formatter() with a string
    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            utils().formatter("10")

    # test formatter() with a float
    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils().formatter(10.5)


# run the tests
unittest.main()