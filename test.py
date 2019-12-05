import unittest
from convert import convert24

class TestDateConversion(unittest.TestCase):
    def test_convert24_pm(self):
        self.assertEqual(convert24("11:20PM"), "23:20")
        self.assertEqual(convert24("12:20PM"), "12:20")

    def test_convert24_am(self):
        self.assertEqual(convert24("11:20AM"), "11:20")
        self.assertEqual(convert24("12:10AM"), "00:10")

if __name__ == '__main__':
	unittest.main()