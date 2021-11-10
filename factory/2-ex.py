class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def __init__(self):
        self.id = 0
    def create_person(self, name):
        person = Person(self.id, name)
        self.id += 1
        return person

