class ColorSpecification:
    """Class to represent a Specification."""
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, product):
        return self.color == product.color