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

# i u v
    def h_all(self, side, n, city1, city2):
        result = 0
        if side == 0: # even
            for n1 in range(0, n, 2):
                for n2 in range(0, n):
                    for n3 in range(0, n):
                        result += self.h(n1, n2, n3)

        elif side == 1: # odd
            for n1 in range(0, n):
                if n1%2 == 1:
                    for n2 in range(0, n):
                        for n3 in range(0, n):
                            result += self.h(n1, n2, n3)
        else:
            raise ValueError("Side must be zero (even) or one (odd)")
        return result

    def h(self, i, u, v):
        return self.map.get_distance(u, v) * self.z(u, i) * self.z(v * i + 1)

    def h2(self, partition, i):
        result = 0
        for uv in partition:
            result += self.h(uv[0],uv[1],i)
        return result

    def z(self, city_index, row_index):
        self.program.inst(Z(city_index * 4 + row_index))