"""School class which stores information about courses and students."""
import random


class School:
    """Class named school."""

    def __init__(self, name):
        """Class named school."""
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course):
        """Add a course."""
        if course not in self.courses:
            self.courses.append(course)
        else:
            return

    def add_student(self, student):
        """Add a student."""
        id = random.randint(0, 10000)
        for school_student in self.students:
            if school_student.id == id:
                id = random.randint(0, 10000)
        if student not in self.students:
            student.set_id(id)
            self.students.append(student)
        else:
            return

    def get_students(self):
        """Get all students."""
        return self.students

    def get_courses(self):
        """Get all courses."""
        return self.courses

    def add_student_grade(self, student, course, grade: int):
        """Add a student grade."""
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grades(student, grade)
        else:
            return

    def get_students_ordered_by_average_grade(self):
        """Get students ordered by average grade."""
        ordered_students = sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)
        return ordered_students

    def __repr__(self):
        """Repr of the course."""
        return self.name