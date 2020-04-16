import unittest

from objects.permutations import KCycle


class TestKCycle(unittest.TestCase):
    def setUp(self):
        self.kcycle = KCycle([1, 2, 3])

    def test_str_method(self):
        string = self.kcycle.__str__()

        self.assertEqual(string, '(1 2 3)')

    def test_eq_method(self):
        pass

    def test_init_method(self):
        pass


class TestPermutation(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
