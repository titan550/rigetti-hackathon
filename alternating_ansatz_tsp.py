from pyquil.paulis import exponentiate, PauliSum, PauliTerm, check_commutation, exponentiate_commuting_pauli_sum

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

    # TODO: how much will check_commutation slow down the computations?
    if check_commutation(term):
        return exponentiate_commuting_pauli_sum(term)
    else:
        return exponentiate(term)


# assumption that the partition includes tuples of (i, u, v)
def U_partition(B, partition):
    result = PauliTerm("I", 0, 1)

    for entry in partition:
        i = entry[0]
        u = entry[1]
        v = entry[2]
        result *= U_biuv(B, i, u, v)

    return result


def color_parity_mixer(B, partitions):
    result = PauliTerm("I", 0, 1)

    for partition in partitions:
        result *= U_partition(B, partition)