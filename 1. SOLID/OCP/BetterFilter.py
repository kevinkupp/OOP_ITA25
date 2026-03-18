class BetterFilter:
    """Better filter class."""
    def filter(self, products, spec):
        filtered_products = []
        for product in products:
            if spec.is_satisfied(product):
                filtered_products.append(product)

        return filtered_products