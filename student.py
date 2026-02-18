"""Student class with student name and grades."""


class Student:
    """Class named Student."""

    def __init__(self, name):
        """Init grades, name and id."""
        self.grades = []
        self.name = name
        self.id = None

    def set_id(self, id: int):
        """Set student id."""
        if self.id is None:
            self.id = id
        else:
            return

    def get_id(self) -> int:
        """Get student id."""
        return self.id

    def add_grade(self, course, grade):
        """Add a grade."""
        self.grades.append((course, grade))

    def get_grades(self) -> list:
        """Get grades."""
        return self.grades

    def get_average_grade(self):
        """Get the average grade."""
        if len(self.grades) == 0:
            return -1
        else:
            return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self) -> str:
        """Repr of the student class."""
        return self.name