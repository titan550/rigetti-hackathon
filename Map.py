import City

class Map(object):
    array = None
    def __init__(self, array):
        self.array = array

    def get_distance(self, city1, city2):
        return self.array[city1][city2]