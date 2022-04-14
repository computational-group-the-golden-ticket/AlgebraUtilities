# Algebra Utilities
In this repository algebraic tools are implemented, which facilitate the study
of the tensor properties of matter.

The implemented structures are semigroups, monoids, groups and frobenius algebras
(more will be added in future updates).

### Semigroup:
     A semigroup is an ordered pair (S, *), where S is a nonempty set and * is a
     binary operation *:S x S --> S such that the binary operation * is associative.

### Monoid:
     A monoid is a semigroup (M, *) in which a neutral element exists under the
     binary operation *, that is, there is 'e' in M such that e * a = a * e = a for all
     element a in M.

### Group:
     A group is a Monoid (G, *) in which for every element g in G, there exists an element
     a in G such that a * g = g * a = e, and is denoted a = g^-1.

## Documentation

### Funciones
    
   **simplify**: Given a tuple of Kcycle objects, this function will simplify them to the
    minimum number of kcycle procceses.
    
    input
        kcycle_objects: iterable over kycycle objects (e.g tuple of them)

    output:
        kcycles: reduced version of them in a list of lists; note that it is
          given in this way because the result in general is a permutation.

### Objetos
Given the hierarchical structure in the definitions of semigroup, monoid, group, ...
opted to use object-oriented programming for the development of the library, so
way the following objects were defined:
    
SemiAlgebraicObject
AlgebraicObject
KCycle
Permutation

SemiGroup
Monoid
Group
AlgebraicClass
Printable
ClassesElements
FrobeniusAlgebra

### Mensajes de error
   **AlgebraUtilitiesErrors**: De este error heredan todos los demas.

   **KCycleIterInitError**:

   **KCycleRepeatInitError**:

   **CallPermutationError**:

   **UnexpectedTypeError**: Este error es lanzado cuando no se pasa los argumentos con el tipo adecuado.

   **NonAssociativeSetError**: Este error es lanzado cuando se trata de crear una estructura asociativa
   con una operacion que no cumple la asociatividad.

   **ElementsOverflow**: Este error es lanzado cuando se pasa el limite establecido para la generacion
   de nuevos elementos.

   **IdentityElementNotFoundError**: Este error es lanzado cuando se intenta crear una estructura con una
   operacion que no tiene elemento identidad cuando deberia tenerlo.

   **ElementWithoutInverse**: Este error es lanzado cuando se intenta crear una estructura con en donde
   algunos elementos no tienen inverso, aun cuando es necesario.

## Installation

To install simply run the following line of code inside the directory algebra_utilities/

sudo python3 setup.py install

To unistall simply run the following lines of code:

sudo python3 setup.py install --record files.txt
sudo xargs rm -rf < files.txt

## Tests

## Examples

