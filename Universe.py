from pyquil.quil import Program
from pyquil.gates import *

class Universe(object):
    state = None
    def __init__(self):
        self.state = Program()
        self.state.inst(X(0), X(5), X(10), X(15))