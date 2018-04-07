from pyquil.paulis import exponentiate, PauliSum, PauliTerm

# hardcoded to 4 for now
def get_qubit(city, order, num_cities=4):
    return city * num_cities + order


def S_plus(qubit):
    return PauliTerm("X", qubit, 1) + PauliTerm("Y", qubit, complex(0, 1))


def S_minus(qubit):
    return PauliTerm("X", qubit, 1) + PauliTerm("Y", qubit, complex(0, -1))


def H_iuv(i, u, v):
    qubit_ui = get_qubit(u, i)
    qubit_vi1 = get_qubit(v, i+1)
    qubit_ui1 = get_qubit(u, i + 1)
    qubit_vi = get_qubit(v, i)

    terms = [
        S_plus(qubit_ui) * S_plus(qubit_vi1) * S_minus(qubit_ui1) * S_minus(qubit_vi),
        S_minus(qubit_ui) * S_minus(qubit_vi1) * S_plus(qubit_ui1) * S_plus(qubit_vi)
    ]

    return PauliSum(terms)


def U_biuv(B, i, u, v):
    H = H_iuv(i, u, v)
    term = PauliTerm("I", 0, B) * H

    return exponentiate(term)