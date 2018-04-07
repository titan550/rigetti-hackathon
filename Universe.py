from pyquil.quil import Program
from pyquil.gates import *
import City, Map

class Universe(object):
    state = None
    cities = None

    def __init__(self, cities, map):
        self.state = Program()
        self.state.inst(X(0), X(5), X(10), X(15))
        self.cities = cities
        self.map = map

    def H(self, side, n, city1, city2, index):
        if side == 0: # even
            pass

        elif side == 1: # odd
            pass

        else:
            raise ValueError("Must be zero (even) or one (odd)")