from ..objects.baseobjects import AlgebraicObject
from .baseobjects import *
from .group import Group


class ClassesElements(AlgebraicClass, Printable):
    def __init__(self, elements):
        super(ClassesElements, self).__init__()

        self.elements = elements
        for element in self.elements:
            # chequeo de tipo
            if not isinstance(element, AlgebraicObject):
                raise Exception('Invalid type')

    def __repr__(self):
        return Printable.__repr__(self)

    def __eq__(self, other):
        # el objeto actual contenido en other
        for element in self.elements:
            if element not in other.elements:
                return False

        # other contenido en el objeto actual
        for element in other.elements:
            if element not in self.elements:
                return False

        return True

    def __mul__(self, other):
        elements = []

        for right_element in self.elements:
            for left_element in other.elements:
                elements.append(right_element * left_element)

        return ClassesElements(elements)


class FrobeniusAlgebra(Group):
    def __init__(self, *args, custom_class=None, **kwargs):
        super(FrobeniusAlgebra, self).__init__(*args, **kwargs)

        if custom_class is None:
            custom_class = ClassesElements

        if not issubclass(custom_class, AlgebraicClass):
            raise Exception('Type error')

        self.custom_class = custom_class

        # the class of the identity
        C1 = self.custom_class(self.get_class_of_element(self.identity))
        self.classes = [C1]

        for element in self.elements:
            if element != self.identity:
                class_element = self.get_class_of_element(element)
                self.classes.append(self.custom_class(class_element))

    def show_classes_order(self):
        for i in range(len(self.classes)):
            print('%d -> %s' % (i + 1, self.classes[i]))

    def rearrange_classes_order(self, new_order):
        self.classes = [self.classes[i - 1] for i in new_order]

    def get_class_coefficients(self, i, j, k=None):
        result = self.classes[i - 1] * self.classes[j - 1]

        if k is not None:
            class_k = self.classes[k - 1]
            return result.elements.count(class_k.elements[0])

        coef = []
        for k in range(len(self.classes)):
            class_k = self.classes[k]
            coef.append(result.elements.count(class_k.elements[0]))

        return coef

    def get_class_arrays(self, i, j):
        return self.class_element[i - 1].elements[j - 1]

    def get_class_multiplication_matrices(self):
        length = len(self.classes)

        matrix = [[[0 for k in range(length)]
                   for j in range(length)]
                  for i in range(length)]

        for i in range(length):
            for j in range(i + 1):
                for k in range(length):
                    coef = self.get_class_coefficients(i, j, k)

                    matrix[i][j][k] = coef
                    matrix[j][i][k] = coef

        return matrix
