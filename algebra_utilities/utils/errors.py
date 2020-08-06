class AlgebraUtilitiesErrors(Exception):
    def __init__(self, message):
        self.message = message
        super(AlgebraUtilitiesErrors, self).__init__(self.message)


class KCycleIterInitError(AlgebraUtilitiesErrors):
    """
    Simple class to prevent not permited or gibberish initializations
    """
    pass


class KCycleRepeatInitError(AlgebraUtilitiesErrors):
    """
    Simple class to prevent not permited or gibberish initializations
    """
    pass


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
