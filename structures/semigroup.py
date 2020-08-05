from ..objects.baseobjects import *
from .baseobjects import Printable


class SemiGroup(Printable):
    def __init__(self, generators, name='G'):
        super(SemiGroup, self).__init__()

        # nombre del semigrupo
        self.name = name

        # todos los generadores deben heredar de SemiAlgebraicObject o de
        # AlgebraicObject
        for generator in generators:
            if not isinstance(generator, SemiAlgebraicObject) and \
                    not isinstance(generator, AlgebraicObject):
                raise TypeError('Invalid Type')

        # lista de los generadores del semigrupo, esta podria coincidir con la
        # lista de todos los elementos del semigrupo
        self.generators = generators

        # TODO: discutir si se guardan los elementos en un "list" o en un "set"
        self.elements = self.generate_elements(generators)

        # un semigrupo es un conjunto con una operacion binaria que ademas es
        # asociativa
        if not self.check_associativity():
            raise TypeError('No es asociativo')

        # cache for the string representation of the set of elements
        self.string = ''

    def __len__(self):
        return len(self.elements)

    def generate_orbit(self, element):
        orbit = []

        dummy = element
        while dummy not in orbit:
            orbit.append(dummy)

            dummy *= element

        return orbit

    def remove_repeating_elements(self, elements):
        dummy = []

        for element in elements:
            if element not in dummy:
                dummy.append(element)

        return dummy

    def all_posible_multiplication(self, elements):
        old_length = -1
        current_length = len(elements)

        while old_length != current_length:
            for i in range(current_length):
                for j in range(current_length):
                    left_multiplication = elements[i] * elements[j]
                    right_multiplication = elements[j] * elements[i]

                    if left_multiplication not in elements:
                        elements.append(left_multiplication)

                    if right_multiplication not in elements:
                        elements.append(right_multiplication)

            current_length, old_length = current_length, len(elements)

        return elements

    def generate_elements(self, generators):
        elements = []

        # se generan las orbitas de cada generador
        for generator in generators:
            elements.extend(self.generate_orbit(generator))

        elements = self.remove_repeating_elements(elements)
        elements = self.all_posible_multiplication(elements)

        return elements

    def add_element(self, element):
        if element not in self.elements:
            self.elements.append(element)

            self.elements = self.all_posible_multiplication(self.elements)

    def check_associativity(self):
        # TODO: buscar un algoritmo de orden menor a n^3
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if a * (b * c) != (a * b) * c:
                        return False

        return True

    def get_cayley_table(self, a=None, b=None):
        if a is None:
            a = self.elements

        if b is None:
            b = self.elements

        for i in range(len(a)):
            for j in range(len(b)):
                c = a[i] * b[j]
                print('%s * %s = %s' % (a[i], b[j], c))
