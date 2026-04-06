class Person:
    def __init__(self, name, person_id):
        self.id = person_id
        self.name = name

class PersonFactory:
    def __init__(self):
        self.current_id = 0

    def create_person(self, name):
        new_person = Person(name, self.current_id)

        self.current_id += 1

        return new_person

factory = PersonFactory()

p1 = factory.create_person("Anna")
p2 = factory.create_person("Mark")

print(p1.id, p1.name)
print(p2.id, p2.name)
