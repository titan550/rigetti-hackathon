from Map import Map
import numpy as np
from City import City
from Universe import Universe
from pyquil.quil import Program

map_matrix = np.matrix('1 1 1 1; 1 1 1 1; 1 1 1 1; 1 1 1 1')
map = Map(map_matrix)

cities = [City() for i in range(4)]

program = Program()

universe = Universe(cities=cities, map=map, program=program)
