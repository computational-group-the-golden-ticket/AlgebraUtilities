from "Tensorial-Properties-of-Matter" import AlgebraUtilitiesErrors


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
    print("The input of KCycle must be an iterable object")


class KCycleRepeatInitError(AlgebraUtilitiesErrors):
    """
    Simple class to prevent not permited or gibberish initializations
    """
    print("Check that the kcycle does not have repeated elements")


class CallPermutationError(AlgebraUtilitiesErrors):
    """
    Simple class to prevent nonsensical calls
    """
    print("There is not value to be returned")
