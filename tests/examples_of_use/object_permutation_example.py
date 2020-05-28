from __init__ import*
from objects.permutations import*

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

a = (1, 1)
a = KCycle(a)
print(a.operations)

a, b = (1, ), (2, )

a = KCycle(a)
b = KCycle(b)
print(simplify((a, b)))

print(a * b)

a = ((3, 4), (1, 2))
b = ((4, 3), (2, 1))
print(Permutation(a))
a = Permutation(a)
b = Permutation(b)
print(a == b)

a = ((1, ), (2, ))
b = ((3, ), (4, ))
a = Permutation(a)
b = Permutation(b)
print(a == b)
