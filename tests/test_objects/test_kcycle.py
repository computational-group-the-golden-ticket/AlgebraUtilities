import unittest
from objects.permutations import KCycle, Permutation


class TestKCycle(unittest.TestCase):
    def setUp(self):
        self.kcycle = KCycle([1, 2, 3])

    def test_repr_method(self):
        string_1 = self.kcycle.__repr__()
        self.assertEqual(string_1, '(1 2 3)')

        kcycle_2 = KCycle(['Pera', 'Uva', 'Manzana'])
        string_2 = kcycle_2.__repr__()
        self.assertEqual(string_2, '("Pera" "Uva" "Manzana")')

        kcycle_3 = KCycle([1, 8, 'Manzana podrida\n'''])
        string_3 = kcycle_3.__repr__()
        self.assertEqual(string_3, '(1 8 "Manzana podrida\n")')

    def test_call_method(self):
        change_input_to = self.kcycle(1)
        self.assertEqual(change_input_to, 2)

        change_input_to = self.kcycle(2)
        self.assertEqual(change_input_to, 3)

        change_input_to = self.kcycle(3)
        self.assertEqual(change_input_to, 1)

    def test_eq_method(self):
        kcycle1 = KCycle((1,))
        kcycle2 = KCycle((783,))
        self.assertEqual(kcycle1, kcycle2)

        kcycle1 = KCycle(('a',))
        kcycle2 = KCycle(('\n',))
        self.assertEqual(kcycle1, kcycle2)

        kcycle1 = KCycle(('a',))
        kcycle2 = KCycle((1,))
        self.assertEqual(kcycle1 == kcycle2, 0)

        kcycle1 = KCycle((1, 2, 3))
        self.assertEqual(kcycle1, self.kcycle)

        kcycle1 = KCycle((2, 3, 1))
        self.assertEqual(kcycle1, self.kcycle)

        kcycle1 = KCycle(('a', 'perro mio'))
        kcycle2 = KCycle(('perro mio', 'a'))
        self.assertEqual(kcycle1, kcycle2)

    def test_mul_method(self):
        calculation = KCycle((3, 2, 1)) * self.kcycle
        expected_result = Permutation(((1,),))
        self.assertEqual(calculation, expected_result)

        calculation = KCycle((1, 2)) * self.kcycle
        expected_result = Permutation(((2, 3),))
        self.assertEqual(calculation, expected_result)

        kcycle1 = KCycle((4, 5))
        calculation = self.kcycle * kcycle1
        expected_result = Permutation((self.kcycle.kcycle, kcycle1.kcycle))
        self.assertEqual(calculation, expected_result)

    def test_init_method(self):
        self.assertEqual(self.kcycle.kcycle, tuple((1, 2, 3)))
        self.assertEqual(self.kcycle.elements, {1, 2, 3})
        self.assertEqual(self.kcycle.length, 3)
        dict_op = {1: 2, 2: 3, 3: 1}
        self.assertEqual(self.kcycle.operations, dict_op)


if __name__ == '__main__':
    unittest.main()
