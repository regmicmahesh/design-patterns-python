from enum import Enum
import math


class CoordinateSystem(Enum):
    cartesian = 1
    polar = 2

class Point:
    #def __init__(self, a, b, system=CoordinateSystem.cartesian):
    #    if system == CoordinateSystem.cartesian:
    #        self.x = a
    #        self.y = b
    #    elif system == CoordinateSystem.polar:
    #        self.x = a * math.cos(b)
    #        self.y = a * math.sin(b)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    class PointFactory:
        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p

        def new_polar_point(self, rho, theta):
            return Point(rho * math.cos(theta), rho * math.sin(theta))
    
    factory = PointFactory()


if __name__ == '__main__':
    p1 = Point.factory.new_cartesian_point(3, 4)
    print(p1.x, p1.y)

    p2 = Point.factory.new_polar_point(5, math.pi / 6)
    print(p2.x, p2.y)
