from __init__ import *
from algebra_utilities.objects.permutations import KCycle, Permutation,\
    simplify

# KCycle(8)
# KCycle((8, 8))

a = Permutation([[1, 2], [3, 4]])
print(a(4))
# print(a(7))

Permutation(((1,),))

a = (1, 2, 3)
a = KCycle(a)
print(a)
print(a(1))

# a = (1, 1)
# a = KCycle(a)
# print(a.operations)

a = (1, 2, 3)
a = KCycle(a)
print(a)


a = (1, 2)
b = ('a', )

a = KCycle(a)
b = KCycle(b)

print(a == b)


a = (1, 2, 3)
b = (4, 1, 3)

a = KCycle(a)
b = KCycle(b)

print(simplify((a, b)))

a, b = (1, 2, 6), (2, 1)

a = KCycle(a)
b = KCycle(b)

print(simplify((a, b)))
print(KCycle((1,)).operations)

a, b = (1, ), (2, )

a = KCycle(a)
b = KCycle(b)
print(simplify((a, b)))

print(a * b)

a, b = (1, 2), (2, 1)

a = KCycle(a)
b = KCycle(b)

print(a * b)


# a = ((3, 4), (1, 2))
# b = ((4, 3), (2, 1))
# print(Permutation(a))
# a = Permutation(a)
# b = Permutation(b)
# print(a == b)

# a = ((1, ), (2, ))
# b = ((3, ), (4, ))
# a = Permutation(a)
# b = Permutation(b)
# print(a == b)
