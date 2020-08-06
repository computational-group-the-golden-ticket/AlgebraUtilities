import unittest

from objects.permutations import KCycle, Permutation
from structures.semigroup import SemiGroup


class TestSemiGroup(unittest.TestCase):
    def test_get_order(self):
        pass

    def test_generate_elements(self):
        # s = SemiGroup([KCycle([2, 3, 1]), KCycle([2, 1, 3])])
        # print(s)

        # s.generate_elements()
        # print(s)

        # s2 = SemiGroup([Permutation([[1, 3, 5], [2, 4, 6]]),
        #                 KCycle([1, 6, 5, 4, 3, 2])])
        # print(s2)

        # s2.generate_elements()
        # print(s2)

        s3 = SemiGroup([KCycle([1, 2]), KCycle([1, 2, 3, 4, 5, 6])])
        print(s3)

        s3.generate_elements()
        print(s3)


if __name__ == '__main__':
    unittest.main()
