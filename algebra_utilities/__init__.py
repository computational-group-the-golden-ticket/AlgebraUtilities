class AlgebraUtilitiesErrors(Exception):
    def __init__(self, message):
        self.message = message
        super(AlgebraUtilitiesErrors, self).__init__(self.message)


class UnexpectedTypeError(AlgebraUtilitiesErrors):
    pass


class NonAssociativeSetError(AlgebraUtilitiesErrors):
    pass


class ElementsOverflow(AlgebraUtilitiesErrors):
    pass


class IdentityElementNotFoundError(AlgebraUtilitiesErrors):
    pass


class ElementWithoutInverse(AlgebraUtilitiesErrors):
    pass
