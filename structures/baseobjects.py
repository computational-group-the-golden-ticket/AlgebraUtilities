from abc import ABCMeta, abstractmethod


class AlgebraicClass(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass


class Printable(object):
    def __init__(self):
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
