from algebra_utilities.objects.baseobjects import AlgebraicObject
from algebra_utilities.structures.group import Group
from algebra_utilities.structures.frobeniusalgebra import FrobeniusAlgebra


class Zn(AlgebraicObject):
    def __init__(self, a, n):
        self.a = a % n
        self.n = n

    def __repr__(self):
        return repr(self.a)

    def __eq__(self, other):
        return self.a == other.a

    def __mul__(self, other):
        return Zn((self.a + other.a) % self.n, self.n)

    def inverse(self):
        return Zn(self.n - self.a, self.n)

    def __pow__(self, p):
        if p == 0:
            return Zn(0, self.n)

        if p < 0:
            return self.inverse() ** -p

        result = self
        for i in range(1, p):
            result *= self

        return result


def main():
    a = Zn(2, 5)

    s = FrobeniusAlgebra([a])

    s.show_classes_order()

    print(s.get_class_multiplication_matrices())


if __name__ == '__main__':
    main()
