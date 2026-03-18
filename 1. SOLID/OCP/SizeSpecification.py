class SizeSpecification:
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, product):
        return self.size == product.size