class City(object):
    order = None
    identity = None

    def __init__(self, identity=None, order=None):
        if (identity):
            self.identity = identity
        if (order):
            self.order = order

    def distance(self, map, neighbor):
        return map.get_distance(self.identity, neighbor.identity)