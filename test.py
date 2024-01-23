import unittest
from main import division

class TestMojProgram(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(2, 4), .5)
        self.assertEqual(division(9999, 9), 1111)
        self.assertEqual(division(0, 1.23), 0)

if __name__ == '__main__':
    unittest.main()
