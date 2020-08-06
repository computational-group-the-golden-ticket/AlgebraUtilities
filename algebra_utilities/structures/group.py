from algebra_utilities.objects.baseobjects import AlgebraicObject
from algebra_utilities.structures.monoid import Monoid

from algebra_utilities.utils.errors import UnexpectedTypeError
from algebra_utilities.utils.errors import ElementWithoutInverse


class Group(Monoid):
    """
    Esta clase representa un grupo finito, un grupo finito es un monoide
    en el que todos los elementos son invertibles.

    Atributos
    ---------
    identity: identidad del monoide
    generators: lista con los elementos generadores del semigrupo
    name: nombre del semigrupo
    """

    def __init__(self, *args, **kwargs):
        # en la inicializacion se generan todos los elementos
        super(Group, self).__init__(*args, **kwargs)

        # en un grupo todos los elementos deben ser invertibles
        if not self.check_inverses():
            raise ElementWithoutInverse('Element without inverse was found in Group initialization')

    def check_inverses(self):
        """
        Este metodo verifica que todos los elementos del grupo sean en
        realidad invertible
        """
        for element in self.elements:
            # chequeo de tipo
            if not isinstance(element, AlgebraicObject):
                raise UnexpectedTypeError('The objects has an invalid type on Group initialization')

            # chequeo conceptual
            if element * element ** -1 != self.identity:
                return False

        return True

    def get_element_order(self, element):
        """
        Este metodo retorna el orden de un elemento dado
        """
        result = element
        order = 1

        while True:
            result *= element

            if result == element:
                return order

            order += 1

    def get_class_of_element(self, fixed_element):
        """
        Este metodo retorna la clase de un elemento dado
        """
        class_elements = [fixed_element]

        # TODO: this can be optimized
        for element in self.elements:
            if element != fixed_element:
                # se realiza la operacion de conjugacion para obtener todos
                # los elementos
                new_element = element * fixed_element * element ** -1

                if new_element not in class_elements:
                    class_elements.append(new_element)

        return class_elements

    def get_classes(self):
        """
        Este metodo retorna todas las clases del grupo
        """
        classes = []

        for element in self.elements:
            in_some_class = False

            for class_i in classes:
                if element in class_i:
                    in_some_class = True
                    break

            if not in_some_class:
                classes.append(self.get_class_of_element(element))

        return classes
