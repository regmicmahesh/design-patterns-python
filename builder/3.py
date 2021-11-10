class Person:
    def __init__(self):
        self.street_address = None
        self.post_code = None
        self.city = None

        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f"{self.street_address}, {self.post_code}, {self.city} \
               {self.company_name}, {self.position}, {self.annual_income}"


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person


    @property
    def works(self):
        return PersonjobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, post_code):
        self.person.post_code = post_code
        return self

    def in_city(self, city):
        self.person.city = city
        return self

pb = PersonBuilder()

person = pb.lives.at('123 london road').in_city('London').with_postcode('SW12BC').build()

print(person)

