from Map import Map
import numpy as np
from City import City
from Universe import Universe
from pyquil.quil import Program
from pyquil import api

map_matrix = np.matrix('1 1 1 1; 1 1 1 1; 1 1 1 1; 1 1 1 1')
map = Map(map_matrix)

cities = [City(identity=i) for i in range(4)]

program = Program()

universe = Universe(cities=cities, map=map, program=program)


city_partitions =  [[[1,2],[3,4]],[[1,3],[2,4]],[[1,4],[2,3]]]
order_partitions = [[1,3],[2,4]]

from pyquil.paulis import PauliTerm
from pyquil.api import QVMConnection
p = PauliTerm("X", 0).program.measure(0,0)
qvm = QVMConnection()
qvm.run(p,[0,1])