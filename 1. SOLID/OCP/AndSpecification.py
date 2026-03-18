class AndSpecification:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    @staticmethod
    def filter_by_size_and_color(products, size, color):
        """Filter a product by color and size."""
        filtered_products_size_and_color = []
        for some_product in products:
            if some_product.color == color and some_product.size == size:
                filtered_products_size_and_color.append(some_product)

        return filtered_products_size_and_color