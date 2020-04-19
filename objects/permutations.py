class KCycle(object):
    """
    A K-Cycle represents the replacement of K elements, such that each element
      that replaces another also gets replaced. One possible representation:
      e.g. given a tuple (a,b,c...,r,k), this one can be understood as a cycle,
      when it represents the change of the element a for b, b for c, .., r for
      k, and k for a.
    """

    def __init__(self, iterable_object):
        # Cycle is assumed to have tuple representation as above
        self.kcycle = tuple(iterable_object)

        # In case only as number is given as input, it will indicate pos 1
        #   remains the same
        self.kcycle = tuple(self.kcycle or (1,))

        # Identify all the cycle elements
        self.elements = set(self.kcycle)

        # Define lenght of cycle
        self.length = len(self.kcycle)

        # Will define opration to be made to a given element, see kcycl2dict
        #  method.
        self.operations = self.kcycle2dict(self.kcycle)

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
        string = '(' + str(self.kcycle[0])

        for i in range(1, self.length):
            string += ' ' + str(self.kcycle[i])

        string += ')'

        return string

    def __eq__(self, other):
        if isinstance(other, KCycle):
            # KCycle of one element is by operational definition the identity,
            #   note nevertheless that operations dictionary will be the same.
            if self.length == 1:
                return other.length == 1

            # Note that operations are the one that uniquely define a Kcycle,
            #  the tuple that represent could really be in several orders and
            #  still define the same cycle.
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

        # Case where simplify have lead to cycles of length 1
        if len(kcycles) == 0:
            return KCycle([1])
        # Naturally, several Kcycles represent a general permutation
        else:
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


class Permutation(object):
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
            string += (' ' + str(kcycle))

        # Ommit first blank value
        return string[1:]

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

    # By definition the inverse is to the -1, so integer times the
    #  multiplication of the inverse
    if p < 0:
        try:
            p = abs(p)
            result = permutation.inverse()
        except TypeError:
            print("The exponent must be an integer")

    # Do integer times the permutation in question
    try:
        for i in range(1, p):
            result *= permutation
    except TypeError:
        print("The exponent must be an integer")

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
    """

    # Get all the elements considered in the kcycles
    elements = set({})

    # Get the kcyle attribute in the class and do an union
    for kcycle in kcycle_objects:
        elements = elements.union(kcycle.elements)

    # List to save the kcycles that will repesent the permutation
    kcycles = []

    ######
    # Move through each element, and when this one is not already in the
    #   Kcycles constructed apply the operations defined for the interchange
    for element in sorted(elements):
        # Verify it element is already in a Kcycle
        it_broke = False
        for kcycle in kcycles:
            if element in kcycle:
                # Set true to jump over next element in the element for
                it_broke = True
                break

        # If true, it will mean the kycycle for such an element is included
        if it_broke:
            continue

        kcycles.append([element])

        # The Kcycle for the element in consideration is constructed, while the
        #   Kcycle does not close again with the first element apply process.
        while apply(kcycle_objects, kcycles[-1][-1]) != kcycles[-1][0]:
            kcycles[-1].append(apply(kcycle_objects, kcycles[-1][-1]))
    ####

    # Kcycles of len==1 are eliminated
    kcycles = [kcycle for kcycle in kcycles if len(kcycle) > 1]

    return kcycles


def get_permutation_from_string(string):
    pass
