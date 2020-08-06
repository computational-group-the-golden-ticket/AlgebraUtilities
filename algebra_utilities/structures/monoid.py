from algebra_utilities.structures.semigroup import SemiGroup
from algebra_utilities.utils.errors import IdentityElementNotFoundError


class Monoid(SemiGroup):
    """
    Esta clase representa un monoide finito, un monoide es un semigrupo con
    unidad

    Atributos
    ---------
    identity: identidad del monoide
    generators: lista con los elementos generadores del semigrupo
    name: nombre del semigrupo
    """

    def __init__(self, *args, identity=None, **kwargs):
        # en la inicializacion se generan todos los elementos
        super(Monoid, self).__init__(*args, **kwargs)

        self.identity = identity

        # es necesario que se tenga una identidad
        if not self.check_identity(self.identity):
            self.identity = self.get_identity()

    def get_identity(self):
        """
        Este metodo retorna la identidad del monoide si la hay
        """
        for element in self.elements:
            if self.check_identity(element):
                return element

        raise IdentityElementNotFoundError('The identity element was not found on Monoid initialization')

    def check_identity(self, candidate):
        """
        Este metodo verifica que la identidad que se haya pasado, sea en
        realidad una identidad, en cuyo caso se retorna True, False en caso
        contrario
        """
        if candidate is None:
            return False

        for element in self.elements:
            right_multiplication = candidate * element
            left_multiplication = element * candidate

            if right_multiplication != element:
                return False

            if left_multiplication != element:
                return False

        return True
