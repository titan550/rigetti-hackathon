from pyquil.quil import Program
from pyquil.gates import *
import pyquil.api as api

def initialize():

    # Hard-code node=4 for our specific case
    node = 4

    qvm = api.QVMConnection()
    p = Program()

    # qubits 0 through 15
    qbits = [ ii for ii in range(node**2) ]

    # each node gets four qubits; label of node is initialized to 1-state
    logical = [[ 1 if ii==jj else 0 for jj in range(node) ] for ii in range(node)]
    logical = [ ii for jj in logical for ii in jj  ]

    pp = [ p.inst(X(ii)).measure(ii,ii) if logical[ii] == 1 else p.inst(I(ii)).measure(ii,ii) for ii in qbits]

    out = [ qvm.run(pp[ii],[ii]) for ii in range(len(qbits))   ]

    return out

def main():

    initialize()

main()
