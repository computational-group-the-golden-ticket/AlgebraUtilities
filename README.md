# Algebra Utilities

En este repositorio se implementan herramientas algebraicas, que facilitan el estudio
de las propiedades tensoriales de la materia.

Las estructuras implementadas son semigrupos, monoides, grupos y algebras de frobenius
(en proximas actualizaciones se iran agregaran mas).

### Semigrupo:
    Un semigrupo es un par ordenado (S, *), donde S es un cojunto no vacio y * es una
    operacion binaria *:S x S --> S tal que la operacion binaria * es asociativa.

### Monoide:
    Un monoide es un semigrupo (M, *) en el que existe un elemento neutro bajo la
    operacion binaria *, esto es, existe 'e' en M tal que e * a = a * e = a para todo
    elemento a en M.

### Grupo:
    Un grupo es un Monoide (G, *) en el que para todo elemento g en G, existe un elemento
    a en G tal que a * g = g * a = e, y se denota a = g^-1.

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
Dada la estructura gerarquica en las definiciones de semigrupo, monoide, grupo, ... se
opto por usar programacion orientada a objetos para el desarrollo de la libreria, de esta
forma se definieron los siguientes objetos:

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

