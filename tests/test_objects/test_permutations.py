import unittest

from objects.permutations import KCycle


class TestKCycle(unittest.TestCase):
    def setUp(self):
        self.kcycle = KCycle([1, 2, 3])

    def test_repr_method(self):
        kcycle_1 = self.kcycle([1, 2, 3])
        kcycle_2 = KCycle(['Pera', 'Uva', 'Manzana'])

        string_1 = kcycle_1.str()
        string_2 = kcycle_2.str()

        self.assertEqual(string_1, '(1 2 3)')
        self.assertEqual(string_2, '(Pera Uva Manzana)')

    def test_str_method(self):
        string = self.kcycle.__str__()

        self.assertEqual(string, '(1 2 3)')

    def test_eq_method(self):
        pass

    def test_init_method(self):
        pass



    # def test_eq_method(self):
    #     kcycle = KCycle([1, 2, 3])
    #     target = KCycle([3, 1, 2])

    #     self.assertEqual(True, target == kcycle)

    # def test_init_method(self):
    #     pass

    # def test_inverse(self):
    #     kcycle = KCycle([1, 2, 3])
    #     target = KCycle([3, 2, 1])

    #     self.assertEqual(kcycle.inverse(), target)

    # def test_power(self):
    #     kcycle = KCycle([1, 2, 3])

    #     self.assertEqual(kcycle ** 2, )

    # def test_call(self):
    #     kcycle = KCycle([1, 2, 3])

    #     self.assertEqual(kcycle(3), 1)

class TestPermutation(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
