from algebra_utilities.objects import baseobjects


class AlgebraUtilitiesErrors(Exception):
    def __init__(self, message):
        self.message = message
        super(AlgebraUtilitiesErrors, self).__init__(self.message)
