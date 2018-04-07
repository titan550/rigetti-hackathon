from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import *
import numpy as np


qvm = QVMConnection()
p = Program()
p.inst(X(1), X(0), X(0), X(0)
       ,X(0), X(1), X(0), X(0)
       ,X(0), X(0), X(1), X(0)
       ,X(0), X(0), X(0), X(1))

print(p)