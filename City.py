class City(object):
    order = -1
    identity = -1

    def __init__(self, identity=None, order=None):
        if (identity):
            self.identity = identity
        if (order):
            self.order = order

    def distance(self, map, neighbor):
        return map.get_distance(self.identity, neighbor.identity)

    def z(self, index, program):
        program.inst(Z(identity*4 + index))