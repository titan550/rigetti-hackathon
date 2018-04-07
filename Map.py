class Map(object):
    matrix = None

    def __init__(self, matrix):
        self.matrix = matrix

    def get_distance(self, city1, city2):
        return self.matrix[city1, city2]