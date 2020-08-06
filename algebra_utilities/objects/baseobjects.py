from abc import ABCMeta, abstractmethod


class SemiAlgebraicObject(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __eq__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __pow__(self):
        pass


class AlgebraicObject(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __eq__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def inverse(self):
        pass

    @abstractmethod
    def __pow__(self):
        pass
