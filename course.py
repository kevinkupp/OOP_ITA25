"""Course class with name and grades."""


class Course:
    """Class named course."""

    def __init__(self, name: str):
        """Class named course."""
        self.name = name
        self.grades = []
        self.courses = []
        """Create grades and courses lists."""

    def add_grades(self, student, grades: int):
        """Add grades to the course."""
        self.grades.append((student, grades))
        """Add grades to the course."""

    def get_grades(self) -> list[tuple[int]]:
        """Return grades list."""
        return self.grades

    def get_average_grade(self) -> float:
        """Return the average grade of the course."""
        if len(self.grades) == 0:
            return -1
        else:
            return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """Repr of the course."""
        return self.name