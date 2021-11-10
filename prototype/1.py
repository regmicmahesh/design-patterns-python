import copy
class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"

john = Person("John", Address("123 Main St", "Anytown", "CA", "12345"))

jane = copy.deepcopy(john)
