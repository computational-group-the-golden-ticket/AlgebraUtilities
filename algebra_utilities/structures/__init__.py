from algebra_utilities import AlgebraUtilitiesErrors


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
