class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name} {self.position} {self.date_of_birth}"

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

class PersonBirthdateBuilder(PersonJobBuilder):
    def born_on(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

pb = PersonBirthdateBuilder()

me = pb.called("John").works_as_a("Programmer").born_on("01/01/1990").build()

print(me)
