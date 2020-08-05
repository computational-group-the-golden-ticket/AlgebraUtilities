from monoid import Monoid


class Group(Monoid):
    def __init__(self, *args, **kwargs):
        super(Group, Monoid).__init__(args, kwargs)

        if not self.check_inverses():
            raise TypeError('Definir error')

    def check_inverses(self):
        for element in self.elements:
            if element * element ** -1 != self.identity:
                return False

        return True

    def get_element_order(self, element):
        result = element
        order = 1

        while True:
            result *= element

            if result == element:
                return order

            order += 1

    def get_class_of_element(self, fixed_element):
        class_elements = [fixed_element]

        for element in self.elements:
            if element != fixed_element:
                new_element = element * fixed_element * element ** -1

                if not (new_element in class_elements):
                    class_elements.append(new_element)

        return class_elements

    def get_classes(self):
        classes = []

        for element in self.elements:
            classes.append(self.get_class_of_element(element))

        return classes

    def get_class_arrays(self):
        pass

    def get_class_multiplication_matrices(self):
        pass
