from enum import Enum
class Product:

    def __init__(self, name, color, size):
        """Name, color and size."""
        self.name = name
        self.color = color
        self.size = size

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
