from __init__ import *
from algebra_utilities.objects.permutations import KCycle, Permutation
from algebra_utilities.structures.group import Group

e1 = Permutation((1,),)
e2 = Permutation(((3, 2), (1, 3)))
e3 = Permutation((2, 3),)

g1 = Group((e1, e2, e3))

for cycle in g1.elements:
    for i in range(1, 4):
        print(cycle(i), end=" ")
    print("\n")
