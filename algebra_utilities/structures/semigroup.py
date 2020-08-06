from algebra_utilities.objects.baseobjects import *
from algebra_utilities.structures.baseobjects import Printable

from algebra_utilities.utils.errors import UnexpectedTypeError
from algebra_utilities.utils.errors import NonAssociativeSetError
from algebra_utilities.utils.errors import ElementsOverflow


class SemiGroup(Printable):
    """
    Esta clase representa un semigrupo, un semigrupo es un conjunto no vacio
    S con una operacion binaria multiplicacion (*): S x S -> S que es
    asociativa

    Atributos
    ---------
    generators: lista con los elementos generadores del semigrupo
    name: nombre del semigrupo
    """

    def __init__(self, generators, name='G'):
        super(SemiGroup, self).__init__()

        # nombre del semigrupo
        self.name = name

        # todos los generadores deben heredar de SemiAlgebraicObject o de
        # AlgebraicObject, para asegurar la definicion de operaciones basicas
        for generator in generators:
            if not isinstance(generator, SemiAlgebraicObject) and \
                    not isinstance(generator, AlgebraicObject):
                raise UnexpectedTypeError('The objects has an invalid type in SemiGroup initialization')

        # lista de los generadores del semigrupo, esta podria coincidir con la
        # lista de todos los elementos del semigrupo
        self.generators = generators

        # TODO: discutir si se guardan los elementos en un "list" o en un "set"
        self.elements = self.generate_elements(generators)

        # un semigrupo es un conjunto con una operacion binaria que ademas es
        # asociativa
        if not self.check_associativity():
            raise NonAssociativeSetError('The operation defined is not associative')

    def __len__(self):
        return len(self.elements)

    def generate_orbit(self, element):
        """
        Este metodo genera (de forma iterativa) todas las potencias (bajo la
        operacion) de un elemento dado hasta llegar a la identidad
        """
        orbit = []

        pow_element = element
        while pow_element not in orbit:
            orbit.append(pow_element)

            # potencias
            pow_element *= element

        return orbit

    def remove_repeating_elements(self, elements):
        """
        Este metodo elimina elementos repetidos en la lista pasada como
        argumento
        """
        dummy = []

        for element in elements:
            if element not in dummy:
                dummy.append(element)

        return dummy

    def all_posible_multiplication(self, elements, limit=-1):
        """
        Este metodo realiza todas las posibles multiplicaciones entre los
        elementos pasados como argumentos y aquellos que se van generando
        """
        old_length = -1
        current_length = len(elements)

        # la longitud de la lista cambia siempre que aparezcan nuevos elementos
        while old_length != current_length:
            # TODO: this is a bottle and must be reimplemented
            for i in range(current_length):
                for j in range(current_length):
                    # no siempre el producto es conmutativo
                    left_multiplication = elements[i] * elements[j]
                    right_multiplication = elements[j] * elements[i]

                    if left_multiplication not in elements:
                        elements.append(left_multiplication)

                    if right_multiplication not in elements:
                        elements.append(right_multiplication)

            # se actualiza el valor de la longitud
            current_length, old_length = len(elements), current_length

            if limit > 0 and current_length > limit:
                raise ElementsOverflow('Limit of allowed elements exceeded in the generation of elements')

        return elements

    def generate_elements(self, generators):
        """
        Este metodo genera todos los elementos del grupo
        """
        elements = []

        # se generan las orbitas de cada generador
        for generator in generators:
            elements.extend(self.generate_orbit(generator))

        # se eliminan elementos repetidos y se realizan todas las posibles
        # multiplicaciones
        elements = self.remove_repeating_elements(elements)
        elements = self.all_posible_multiplication(elements)

        return elements

    def add_element(self, element):
        """
        Este metodo agrega un nuevo generador al grupo y genera los nuevos
        elementos
        """
        # chequeo de tipo
        if not isinstance(generator, SemiAlgebraicObject) and \
                not isinstance(generator, AlgebraicObject):
            raise UnexpectedTypeError('The objects has an invalid type in element aggregation')

        if element not in self.elements:
            self.elements.extend(self.generate_orbit(element))
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
        """
        Este metodo muestra todas las posibles multiplicaciones
        """
        if a is None:
            a = self.elements

        if b is None:
            b = self.elements

        for i in range(len(a)):
            for j in range(len(b)):
                c = a[i] * b[j]
                print('%s * %s = %s' % (a[i], b[j], c))
