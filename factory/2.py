from abc import ABC
from enum import Enum 


class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("This tea is nice but I'd prefer it with milk.")

class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious!")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount} ml, enjoy!")
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount} ml, enjoy!")
        return Coffee()

class HotDrinkMachine:

    class AvailableDrink(Enum):
        COFFEE = 1
        TEA = 2

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = globals()[factory_name]()
                self.factories.append((name, factory_instance))


    def make_drink(self):
        print("Available drinks: 1. Coffee 2. Tea")
        drink_type = int(input("Please choose a drink: "))

        if drink_type == 1:
            drink = self.factories[0][1].prepare(200)
        elif drink_type == 2:
            drink = self.factories[1][1].prepare(200)
        else:
            raise Exception("Invalid selection.")

        drink.consume()


ht = HotDrinkMachine()
ht.make_drink()


