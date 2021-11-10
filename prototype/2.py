import copy

class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip}"

class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"

class EmployeeFactory:
    main_office_employee = Employee('', Address('123 Main Street', 'Anytown', 'CA', '12345'))
    aux_office_employee = Employee('', Address('456 Second Street', 'Anytown', 'CA', '54321'))

    @staticmethod
    def __new_employee(proto, name, city):
        result = copy.deepcopy(proto)
        result.name = name 
        result.address.city = city
        return result

    @staticmethod
    def new_main_office_employee(name, city):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, city)

    @staticmethod
    def aux_main_office_employee(name, city):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, city)
