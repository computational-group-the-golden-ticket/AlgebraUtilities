class KCycle(object):
    def __init__(self, iterable_object):
        self.kcycle = tuple(iterable_object)

        self.kcycle = tuple(self.kcycle or (1,))
        self.elements = set(self.kcycle)

        self.length = len(self.kcycle)
        self.operations = self.kcycle2dict(self.kcycle)

    def kcycle2dict(self, kcycle):
        operations = {}

        for i in range(len(kcycle) - 1):
            operations[kcycle[i]] = kcycle[i + 1]

        operations[kcycle[-1]] = kcycle[0]

        return operations

    def __repr__(self):
        string = '(' + str(self.kcycle[0])

        for i in range(1, self.length):
            string += ' ' + str(self.kcycle[i])

        string += ')'

        return string

    def __eq__(self, other):
        if isinstance(other, KCycle):
            if self.length == 1:
                return other.length == 1

            return self.operations == other.operations
        else:
            return other.length == 1 and other.kcycles[0] == self

        return False

    def __call__(self, element):
        return self.operations.get(element, element)

    def __mul__(self, other):
        if isinstance(other, Permutation):
            kcycles = simplify((self, ) + other.kcycles)
        else:
            kcycles = simplify((self, other))

        if len(kcycles) == 0:
            return KCycle([1])
        elif len(kcycles) == 1:
            return KCycle(kcycles[0])
        else:
            return Permutation(kcycles)

    def inverse(self):
        return KCycle(reversed(self.kcycle))

    def __pow__(self, p):
        return power(self, p)


class Permutation(object):
    def __init__(self, iterable_objects_list, serialize=True):
        if serialize:
            kcycles = tuple(KCycle(iterable_object) for iterable_object in
                            iterable_objects_list)
        else:
            kcycles = iterable_objects_list

        self.kcycles = tuple(KCycle(kcycle) for kcycle in simplify(kcycles))

        self.length = len(self.kcycles)

    def __repr__(self):
        string = ''

        for kcycle in self.kcycles:
            string += str(kcycle)

        return string

    def __eq__(self, other):
        if isinstance(other, Permutation):
            return self.kcycles == other.kcycles
        else:
            return self.length == 1 and self.kcycles[0] == other

    def __call__(self, element):
        return apply(self.kcycles, element)

    def __mul__(self, other):
        if isinstance(other, KCycle):
            kcycles = simplify(self.kcycles + (other, ))
        else:
            kcycles = simplify(self.kcycles + other.kcycles)

        if len(kcycles) == 0:
            return KCycle([1])
        elif len(kcycles) == 1:
            return KCycle(kcycles[0])
        else:
            return Permutation(kcycles)

    def inverse(self):
        kcycles = []

        for kcycle in reversed(self.kcycles):
            kcycles.append(kcycle ** -1)

        return Permutation(tuple(kcycles), serialize=False)

    def __pow__(self, p):
        return power(self, p)


def power(permutation, p):
    if p == 0:
        return KCycle([1])

    result = permutation

    if p < 0:
        p = abs(p)
        result = permutation.inverse()

    for i in range(1, p):
        result *= permutation

    return result


def apply(kcycles, element):
    result = element

    for i in range(len(kcycles) - 1, -1, -1):
        result = kcycles[i](result)

    return result


def simplify(kcycle_objects):
    elements = set({})

    for kcycle in kcycle_objects:
        elements = elements.union(kcycle.elements)

    kcycles = []

    for element in sorted(elements):
        # se verifica si el elemento ya esta en un kcycle
        it_broke = False
        for kcycle in kcycles:
            if element in kcycle:
                it_broke = True
                break

        if it_broke:
            continue

        kcycles.append([element])

        # se llena el kcyclo
        while apply(kcycle_objects, kcycles[-1][-1]) != kcycles[-1][0]:
            kcycles[-1].append(apply(kcycle_objects, kcycles[-1][-1]))

    # se eliminan los kcyclos de longitud 1
    kcycles = [kcycle for kcycle in kcycles if len(kcycle) > 1]

    return kcycles


def get_permutation_from_string(string):
    pass
