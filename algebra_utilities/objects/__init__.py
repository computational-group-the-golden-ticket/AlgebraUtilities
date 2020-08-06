from algebra_utilities import AlgebraUtilitiesErrors


class GroupElement(object):
    def __eq__(self, other):
        pass

    def __mul__(self, *args, **kwargs):
        return GroupElement()

    def inverse(self):
        return GroupElement()


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


class CallPermutationError(AlgebraUtilitiesErrors):
    """
    Simple class to prevent nonsensical calls
    """
    pass
