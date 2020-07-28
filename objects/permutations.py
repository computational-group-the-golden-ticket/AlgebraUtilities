from .baseobjects import *


class InitializationError(Exception):
    """
    Simple class to prevent not permited or gibberish initializations
    """
    pass


class KCycle(AlgebraicObject):
    """
    A K-Cycle represents the replacement of K elements, such that each element
      that replaces another also gets replaced. One possible representation:
      e.g. given a tuple (a,b,c...,r,k), this one can be understood as a cycle,
      when it represents the change of the element a for b, b for c, .., r for
      k, and k for a.
    """

    def __init__(self, iterable_object):
        # Cycle is assumed to have tuple representation as above
        self.setkcycle(iterable_object)

        # In the case the input tuple is void of elements it will change it by
        #   for default.
        self.kcycle = tuple(self.kcycle or (1,))

        # Identify all the cycle elements
        self.elements = set(self.kcycle)

        # Define lenght of cycle
        self.length = len(self.kcycle)

        # Will define opration to be made to a given element, see kcycl2dict
        #  method.
        self.operations = self.kcycle2dict(self.kcycle)

    def setkcycle(self, iterable_object):
        """
        Set atribute kcycle in the case of not repeated elements.
        """
        # Check if in fact object is iterable
        if not hasattr(iterable_object, '__iter__'):
            message = ("The input of KCycle must be an iterable object")
            raise InitializationError(message)

        self.kcycle = tuple(iterable_object)

        # Check that initialization is in fact a kcycle
        for i in self.kcycle:
            if(self.kcycle.count(i) > 1):
                message = ("Check that the kcycle does not have repeated "
                           "elements")
                raise InitializationError(message)

    def kcycle2dict(self, kcycle):
        # This will say what number (key) is changed by the other in the cycle
        #   (values)
        operations = {}

        # Assing the i-th by the (i+1)-th
        for i in range(len(kcycle) - 1):
            operations[kcycle[i]] = kcycle[i + 1]

        # Last one is changed by first
        operations[kcycle[-1]] = kcycle[0]

        # Return directory of operations to be made
        return operations

    def __repr__(self):
        # Value to be printed as print(KCycle object) is called, cycle to be
        #   perfomed

        quote = isinstance(self.kcycle[0], str)
        string = '(' + quote * '"' + str(self.kcycle[0]) + '"' * quote

        for i in range(1, self.length):
            quote = isinstance(self.kcycle[i], str)
            string += ' ' + quote * '"' + str(self.kcycle[i]) + '"' * quote

        string += ')'

        return string

    def __eq__(self, other):
        if isinstance(other, KCycle):
            # KCycle of one element is by operational definition the identity,
            #   note nevertheless that kcycles are define over a given space,
            #   so, it must be checked taht such space is the same.
            if self.length == 1:
                return other.length == 1 and \
                    isinstance(self.kcycle[0], type(other.kcycle[0]))

            # Note that operations (over a type of variables) are the ones that
            #  uniquely define a Kcycle, the tuple that represent could really
            #  be in several orders and stil define the same cycles.
            return self.operations == other.operations

        # A permutation is understood as list of cycles, in the case this one
        #  is of lenght 1 this will be an equivalent condition
        else:
            return other.length == 1 and other.kcycles[0] == self

        return False

    def __call__(self, element):
        # This will return to what value was the input element was changed
        return self.operations.get(element, element)

    def __mul__(self, other):
        # In the case that is multiplied by a Permutation, this one is first
        #   decomposed into Kcycles.
        if isinstance(other, Permutation):
            kcycles = simplify((self, ) + other.kcycles)
        else:
            kcycles = simplify((self, other))

        # In general the result of this is a permutation
        return Permutation(kcycles)

    def inverse(self):
        """
        This will return the inverse
        """
        # Note that the inverse is naturally the tuple in reverse order, since
        #  the element (i+1)-th is now to the left of i. So, it will map i+1 to
        #  i and then again to i-th, when applied inverse and the Kcycle then.
        #  Similar for multiplication in the other order.
        return KCycle(reversed(self.kcycle))

    def __pow__(self, p):
        """
        This will return the cycle applied many times
        """
        return power(self, p)


class Permutation(AlgebraicObject):
    def __init__(self, iterable_objects_list, serialize=True):
        # In case the input is not an iterable of Kcyle initializations.
        if serialize:
            kcycles = tuple(KCycle(iterable_object) for iterable_object in
                            iterable_objects_list)
        else:
            kcycles = iterable_objects_list

        # Do initialization of permutation by initializing kcycles
        self.kcycles = tuple(KCycle(kcycle) for kcycle in simplify(kcycles))

        # minimum number of kcycles that represent the permutation
        self.length = len(self.kcycles)

    def __repr__(self):
        # Value to be printed as print(Permutation object) is called, set of
        #  cycles to be perfomed
        string = ''

        for kcycle in self.kcycles:
            string += str(kcycle)

        return string

    def __eq__(self, other):
        """
        For equivalence to have sense, input must be Permitation instances, or
          one given by Kcycle instance; other cases will give false by
          notation.
        """
        if isinstance(other, Permutation):
            # Compare one by one by iterable objects property
            return self.kcycles == other.kcycles
        else:
            # Compare permutation(double iteration and Kcycle
            return self.length == 1 and self.kcycles[0] == other

    def __call__(self, element):
        """
        This will return to what value was the input element was changed
        """
        return apply(self.kcycles, element)

    def __mul__(self, other):
        # Add only a Kcycle element in case other is Kcycle type, in the other
        #  case add the complete list.
        if isinstance(other, KCycle):
            kcycles = simplify(self.kcycles + (other, ))
        else:
            kcycles = simplify(self.kcycles + other.kcycles)

        # Case where simplify have lead to cycles of length 1
        if len(kcycles) == 0:
            return KCycle([1])
        else:
            return Permutation(kcycles, serialize=False)

    def inverse(self):
        """
        This will return the inverse of the permutation with the minima number
          of Kcycles represent it.
        """
        kcycles = []

        # Note that reverse Kcycles is not necessary since they are abelian
        #  thanks to simplify.
        for kcycle in self.kcycles:
            kcycles.append(kcycle ** -1)

        return Permutation(tuple(kcycles), serialize=False)

    def __pow__(self, p):
        """
        Apply several time a given permulation
        """
        return power(self, p)


def power(permutation, p):
    """
    This will return the cycle applied many times
    """

    # In case of p=0, the result is the identity
    if p == 0:
        return KCycle([1])

    result = permutation

    # By definition the inverse is to the -1, so integer times the
    #  multiplication of the inverse
    if p < 0:
        p = abs(p)
        result = permutation.inverse()

    # Do integer times the permutation in question
    for i in range(1, p):
        result *= permutation

    return result


def apply(kcycles, element):
    """
    Given a set of kcycles inside variable kcycles, apply would give the result
      for which element will be change in the process.
    """
    result = element  # result defined for aesthetic and debug purposes

    # Go over the Kcycle elements, applying the ones to the right first
    for i in range(len(kcycles) - 1, -1, -1):
        result = kcycles[i](result)

    return result


def simplify(kcycle_objects):
    """
    Given a tuple of Kcycle objects, this function will simplify them to the
      minimum number of kcycle procceses.
    input
        kcycle_objects: iterable over kycycle objects (e.g tuple of them)
    output:
        kcycles: reduced version of them in a list of lists; note that it is
          given in this way because the result in general is a permutation.
    """

    # Get all the elements considered in the kcycles
    elements = set({})
    for kcycle in kcycle_objects:
        elements = elements.union(kcycle.elements)

    # List to save the kcycles that will repesent the permutation
    kcycles = []
    # Move through each element, and when this one is not already in one of the
    #   kcycle in kcycles add resultant kcycle departing from the element in
    #   question (the result must be close off course; see while below).
    for element in sorted(elements):
        it_element_broke = False
        # Verify if element is already in one of the kcycles constructed; in
        #  case it is true break iteration over actual element.
        for kcycle in kcycles:
            if element in kcycle:
                # Set true to jump to next element
                it_element_broke = True
                break
        # True indicate already included as was explained.
        if it_element_broke:
            continue

        # Generate kcycle departing from element not yet in kcycles.
        kcycles.append([element])

        # The Kcycle for the element in consideration is constructed, while the
        #   Kcycle does not close again with the first element apply process.
        while apply(kcycle_objects, kcycles[-1][-1]) != kcycles[-1][0]:
            kcycles[-1].append(apply(kcycle_objects, kcycles[-1][-1]))

    # Kcycles of len==1 are eliminated
    kcycles = [kcycle for kcycle in kcycles if len(kcycle) > 1]

    # List of kcycles of simplification of a single reduntant one
    return kcycles if len(kcycles) > 0 else [[1, ]]


def get_permutation_from_string(string):
    pass
