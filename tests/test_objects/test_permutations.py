import unittest

from objects.permutations import KCycle
from objects.permutations import Permutation


class TestKCycle(unittest.TestCase):
    pass


class TestPermutation(unittest.TestCase):
    @unittest.skip("skipping")
    def test_repr_method_iterable_objects_numbers(self):
        iterable_objects = [(1, 2, 3), (5, 4), (8, 7)]

        permutation = Permutation(iterable_objects)

        self.assertEqual(permutation.__repr__(), '(1 2 3)(4 5)(8 7)')

    @unittest.skip("skipping")
    def test_repr_method_iterable_objects_strings(self):
        iterable_objects = [('banana', 'fresa'), ('guayaba', 'uva', 'limon')]

        permutation = Permutation(iterable_objects)

        self.assertEqual(permutation.__repr__(),
                         '(banana fresa)(guayaba uva limon)')

    @unittest.skip("skipping")
    def test_repr_method_kcycle_objects_numbers(self):
        kcycle1 = KCycle([1, 2, 3])
        kcycle2 = KCycle([5, 4])

        permutation = Permutation([kcycle1, kcycle2], False)

        self.assertEqual(permutation.__repr__(), '(1 2 3)(5 4)')

    @unittest.skip("skipping")
    def test_repr_method_kcycle_objects_strings(self):
        kcycle1 = KCycle(('banana', 'fresa'))
        kcycle2 = KCycle(('guayaba', 'uva', 'limon'))

        permutation = Permutation([kcycle1, kcycle2], False)

        self.assertEqual(permutation.__repr__(),
                         '(banana fresa)(guayaba uva limon)')

    @unittest.skip("skipping")
    def test_eq_method_permuted_kcycle_equals(self):
        iterable_objects1 = [(1, 2, 3), (5, 4), (8, 7)]
        iterable_objects2 = [(1, 2, 3), (8, 7), (4, 5)]
        iterable_objects3 = [(8, 7), (1, 2, 3), (4, 5)]

        permutation1 = Permutation(iterable_objects1)
        permutation2 = Permutation(iterable_objects2)
        permutation3 = Permutation(iterable_objects3)

        self.assertTrue(permutation1 == permutation2)
        self.assertTrue(permutation1 == permutation3)

    @unittest.skip("skipping")
    def test_eq_method_permuted_kcycle_diferents(self):
        iterable_objects1 = [(1, 2, 3), (5, 1, 4), (8, 7, 1)]
        iterable_objects2 = [(1, 2, 3), (8, 7)]
        iterable_objects3 = [(8, 7, 1), (1, 2, 3), (4, 5, 1)]

        permutation1 = Permutation(iterable_objects1)
        permutation2 = Permutation(iterable_objects2)
        permutation3 = Permutation(iterable_objects3)

        self.assertFalse(permutation1 == permutation2)
        self.assertFalse(permutation1 == permutation3)

    @unittest.skip("skipping")
    def test_call_method_disjoint_kcycles(self):
        iterable_objects = [(2, 3), (5, 1, 4), (8, 7)]

        permutation = Permutation(iterable_objects)

        self.assertEqual(permutation(1), 4)
        self.assertEqual(permutation(2), 3)
        self.assertEqual(permutation(3), 2)
        self.assertEqual(permutation(4), 5)
        self.assertEqual(permutation(5), 1)
        self.assertEqual(permutation(7), 8)
        self.assertEqual(permutation(8), 7)

    @unittest.skip("skipping")
    def test_call_method(self):
        iterable_objects = [(4, 3), (3, 2, 1)]

        permutation = Permutation(iterable_objects)

        self.assertEqual(permutation(1), 4)
        self.assertEqual(permutation(2), 1)
        self.assertEqual(permutation(3), 2)
        self.assertEqual(permutation(4), 3)

    def test_mul_method_disjoint_kcycles_case_1(self):
        iterable_objects1 = [(1, 2, 3), (5, 4), (8, 7)]
        iterable_objects2 = [(8, 7), (4, 5)]

        iterable_objects3 = [(1, 2, 3), (4, 5)]

        permutation1 = Permutation(iterable_objects1)
        permutation2 = Permutation(iterable_objects2)
        permutation3 = Permutation(iterable_objects3)

        self.assertTrue(permutation1 * permutation2 == permutation3)

    @unittest.skip("skipping")
    def test_mul_method_disjoint_kcycles_case_2(self):
        iterable_objects1 = [(1, 2, 3), (5, 4), (8, 7)]
        iterable_objects2 = [(1, 2, 3), (8, 7), (4, 5)]
        iterable_objects3 = [(8, 7), (1, 2, 3), (4, 5)]

        permutation1 = Permutation(iterable_objects1)
        permutation2 = Permutation(iterable_objects2)
        permutation3 = Permutation(iterable_objects3)

        self.assertTrue(permutation1 == permutation2)
        self.assertTrue(permutation1 == permutation3)

    @unittest.skip("skipping")
    def test_mul_method(self):
        iterable_objects1 = [(1, 2, 3), (5, 4), (8, 7)]
        iterable_objects2 = [(1, 2, 3), (8, 7), (4, 5)]
        iterable_objects3 = [(8, 7), (1, 2, 3), (4, 5)]

        permutation1 = Permutation(iterable_objects1)
        permutation2 = Permutation(iterable_objects2)
        permutation3 = Permutation(iterable_objects3)

        self.assertTrue(permutation1 == permutation2)
        self.assertTrue(permutation1 == permutation3)



if __name__ == '__main__':
    unittest.main()
