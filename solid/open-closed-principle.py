from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# OCP = Open for extension, Closed for modification

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    # Imagine, your manager asks you to add a new filter.
    # This doesn't follow the OCP principle. It's modified.
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    # This doesn't follow the OCP principle. It's modified.
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

# Specification Pattern.

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Older approach to filter.
    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p.name)

    # New specification
    bf = BetterFilter()
    spec = ColorSpecification(Color.GREEN)
    print('Green products (new):')
    for p in bf.filter(products, spec):
        print(p.name)

    # New specification
    spec = SizeSpecification(Size.LARGE)
    print('Large products (new):')
    for p in bf.filter(products, spec):
        print(p.name)

    # New specification
    spec = SizeSpecification(Size.LARGE) & ColorSpecification(Color.GREEN)
    print('Large green products (new):')
    for p in bf.filter(products, spec):
        print(p.name)
















