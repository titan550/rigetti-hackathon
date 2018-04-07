from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *

class Universe(object):
    state = None
    def __init__(self):
        self.state = Program()
        self.state.inst(X(1), X(0), X(0), X(0)
               , X(0), X(1), X(0), X(0)
               , X(0), X(0), X(1), X(0)
               , X(0), X(0), X(0), X(1))