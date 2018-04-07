from pyquil.quil import Program
from pyquil.gates import *
import City, Map
from pyquil.quil import Program

class Universe(object):
    state = None
    cities = None
    map = None
    program = None

    def __init__(self, cities, map, program):
        self.state = Program()
        self.state.inst(X(0), X(5), X(10), X(15))
        self.cities = cities
        self.map = map
        self.program = program

    def H(self, side, n, city1, city2, index):
        if side == 0: # even
            for n1 in range(0, n, 2):
                for n2 in range(0, n):
                    for n3 in range(0, n):
                        map.get_distance(city1, city2)*self.z(n2,n1)*self.z(n3*n1+1)

        elif side == 1: # odd
            for n1 in range(0, n):
                if(n1%2 == 1):
                    for n2 in range(0, n):
                        for n3 in range(0, n):
                            map.get_distance(city1, city2) * self.z(n2, n1) * self.z(n3 * n1 + 1)


        else:
            raise ValueError("Must be zero (even) or one (odd)")

    def z(self, city_index, row_index):
        self.program.inst(Z(city_index * 4 + row_index))