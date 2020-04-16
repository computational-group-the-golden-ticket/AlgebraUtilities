class SemiGroup(object):
    def __init__(self, generators, name='G'):
        self.name = name
        self.generators = generators

        self.elements = []

    def __str__(self):
        elements = self.elements or self.generators
        string = '{' + str(elements[0])

        for element in elements[1:]:
            string += ', ' + str(element)

        string += '}'

        return string

    def get_element_order(self, element):
        result = element
        order = 1

        while True:
            result *= element

            if result == element:
                return order

            order += 1

    def generate_elements(self):
        # se itera sobre los generadores
        for generator in self.generators:
            if not (generator in self.elements):
                # se realizan todas las posibles operaciones con los elementos
                # en el conjunto, si se encuentra un elemento que no esta
                # se agrega
                order = self.get_element_order(generator)

                for i in range(order + 1):
                    candidate = generator ** i

                    for element in self.elements.copy():
                        product_1 = candidate * element
                        product_2 = element * candidate

                        if not(product_1 in self.elements):
                            self.elements.append(product_1)

                        if not(product_2 in self.elements):
                            self.elements.append(product_2)

                    if not(candidate in self.elements):
                        self.elements.append(candidate)

    def get_table(self):
        elements = self.elements or self.generators

        for right in elements:
            for left in elements:
                print(str(right) + ' * ' + str(left) + ' = ' +
                      str(right * left))

    def get_classes(self):
        pass
