"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def set_name(self, name):
        self.__name = name
        return name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_status(self, status):
        status_list = ["Active", "Expelled", "Finished", "Inactive"]
        if status in status_list:
            self.__status = status
            pass

    def get_status(self):
        return self.__status

    if __name__ == '__main__':
        student = Student("Kevin", "1")
        id_student = student.get_id()
        student.name = student.get_name()
        status_student = student.get_status()
        student_set_name = student.set_name("")
