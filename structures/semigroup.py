from ..objects.baseobjects import *


class SemiGroup(object):
    def __init__(self, generators, name='G'):
        # nombre del semigrupo
        self.name = name

        # todos los generadores deben heredar de SemiAlgebraicObject o de
        # AlgebraicObject
        for generator in generators:
            if not isinstance(generator, SemiAlgebraicObject) and \
                    not isinstance(generator, AlgebraicObject):
                raise TypeError('No se asegura definicion de operaciones basicas')

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
        # si en algun momento se agrego un nuevo elemento al conjunto, se debe
        # actualizar la variable self.string
        self.it_changed = True

    def build_the_string(self):
        # En el caso de que se imprima el semigrupo sin haber generado todos
        # los elementos, se muestra en pantalla a los generadores
        elements = self.elements or self.generators

        # Se muestran los elementos usando la notacion de conjunto
        string = '{' + str(elements[0])
        for element in elements[1:]:
            string += ', ' + str(element)

        string += '}'

        return string

    def __repr__(self):
        # en caso de que se haya agregado un nuevo elemento, se debe
        # reconstruir el string
        if self.it_changed:
            self.string = self.build_the_string()
            self.it_changed = False

        return self.string

    def iterate_element(self, generators, new_element):
        # en este caso se ha iterado sobre el primer generador
        if len(generators) == 0:
            return [new_element]

        # en caso de que hayan elementos en generators, se deben hacer todas
        # las posibles multiplicaciones a derecha y a izquierda
        new_generators = []
        for generator in generators:
            right_multiplication = generator * new_element
            left_multiplication = new_element * generator

            new_generators.append(generator)
            new_generators.append(new_element)

            if not (right_multiplication in new_generators):
                new_generators.append(right_multiplication)

            if not (left_multiplication in new_generators):
                new_generators.append(left_multiplication)

        return new_generators

    def add_element(self, *elements):
        """
        Este metodo agrega un elemento al semigrupo
        """
        generators = self.elements

        for element in elements:
            generators = self.iterate_element(generators, element)

        self.elements = generators[:]
        self.it_changed = True

    def generate_elements(self, generators):
        elements = generators[:]

        # TODO: se debe revisar que en la lista no hayan generadores repetidos
        for fixed_element in generators:
            for element in generators:
                right_multiplication = element * fixed_element
                left_multiplication = fixed_element * element

            if not (right_multiplication in elements):
                elements.append(right_multiplication)

            if not (left_multiplication in elements):
                elements.append(left_multiplication)

        return elements

    def check_associativity(self):
        # TODO: buscar un algoritmo de orden menor a n^3
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if a * (b * c) != (a * b) * c:
                        return False

        return True

    def get_cayley_table(self):
        pass
