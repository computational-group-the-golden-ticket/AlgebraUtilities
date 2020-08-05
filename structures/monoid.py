from .semigroup import SemiGroup


class Monoid(SemiGroup):
    def __init__(self, *args, identity=None, **kwargs):
        super(Monoid, self).__init__(*args, **kwargs)

        self.identity = identity

        if not self.check_identity(self.identity):
            self.identity = self.get_identity()

    def get_identity(self):
        for element in self.elements:
            if self.check_identity(element):
                return element

        raise TypeError('Not identity')

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
