class City(object):
    order = None # order in which salesperson traverses
    identity = None # order in the qubit structure

    def __init__(self, identity=None, order=None):
        if (identity):
            self.identity = identity
        if (order):
            self.order = order

    def distance(self, map, neighbor):
        return map.get_distance(self.identity, neighbor.identity)