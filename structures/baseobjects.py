from abc import ABCMeta, abstractmethod


class AlgebraicClass(metaclass=ABCMeta):
    """
    Esta clase agrega estructura de algebra de frobenius a las clases
    """

    @abstractmethod
    def __repr__(self):
        """
        Este metodo permite que se pueda mostrar una clase en pantalla
        """
        pass

    @abstractmethod
    def __eq__(self, other):
        """
        Este metodo permite que se pueda hacer la comparacion entre 2 clases
        """
        pass

    @abstractmethod
    def __mul__(self, other):
        """
        Este metodo permite que se puedan multiplicar 2 clases
        """
        pass


class Printable(object):
    """
    This class implements methods to show objects tha have estructure like sets
    """

    def __init__(self):
        # si en algun momento se agrego un nuevo elemento al conjunto, se debe
        # actualizar la variable self.string
        self.it_changed = True

        # cache for the string representation of the set of elements
        self.string = ''

    def build_the_string(self):
        # En el caso de que se imprima el semigrupo sin haber generado todos
        # los elementos, se muestra en pantalla a los generadores
        elements = self.elements

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
