import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_addition(self):
        self.assertEqual(sum([1, 1, 1]), 3)

    def test_subtraction(self):
        self.assertEqual((8-5), 3)

    def test_mul(self):
        self.assertEqual((8*5), 40)

    def test_divide(self):
        self.assertEqual((8/2), 4)

    def test_divide_whole(self):
        self.assertEqual((8 % 3), 2)


if __name__ == '__main__':
    unittest.main()
