"""Simple class."""


class Student:
    """Creating a class named Student."""

    def __init__(self, name):
        """Class named Student."""
        self.name = name
        self.finished = False


student1 = Student("John")
print(student1.name)
print(student1.finished)