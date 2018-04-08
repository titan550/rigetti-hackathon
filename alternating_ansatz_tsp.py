from pyquil.paulis import PauliTerm, exponentiate_commuting_pauli_sum, commuting_sets
from pyquil.quil import merge_programs

# hardcoded to 4 for now
def get_qubit(city, order, num_cities=4):
    return city * num_cities + order


def S_plus(qubit):
    '''
    S+ operation used in mixing hamiltonian for the Travelling Salesperson Problem found in arXiv:1709.03489

    :param qubit: qubit to apply S+ operation to
    :return:
    '''
    return PauliTerm("X", qubit, 1) + PauliTerm("Y", qubit, complex(0, 1))


def S_minus(qubit):
    '''
    S- operation used in mixing hamiltonian for the Travelling Salesperson Problem found in arXiv:1709.03489

    :param qubit: qubit to apply S- operation to
    :return:
    '''
    return PauliTerm("X", qubit, 1) + PauliTerm("Y", qubit, complex(0, -1))


def H_iuv(i, u, v):
    '''
    generates a partial mixing hamiltonian for the Travelling Salesperson Problem found in arXiv:1709.03489

    :param i: order term (e.g. the ith stop)
    :param u: source city
    :param v: destination city
    :return:
    '''
    qubit_ui = get_qubit(u, i)
    qubit_vi1 = get_qubit(v, i+1)
    qubit_ui1 = get_qubit(u, i + 1)
    qubit_vi = get_qubit(v, i)

    terms = [
        S_plus(qubit_ui) * S_plus(qubit_vi1) * S_minus(qubit_ui1) * S_minus(qubit_vi),
        S_minus(qubit_ui) * S_minus(qubit_vi1) * S_plus(qubit_ui1) * S_plus(qubit_vi)
    ]

    result = terms[0] + terms[1]

    return result


def U_biuv(i, u, v):
    '''
    exponentiates a partial mixing hamiltonian to get a unitary for the Travelling Salesperson Problem found in arXiv:1709.03489

    :param i: order term (e.g. the ith stop)
    :param u: source city
    :param v: destination city
    :return:
    '''
    H = H_iuv(i, u, v)

    if len(commuting_sets(H)) == 1:
        return exponentiate_commuting_pauli_sum(H)
    else:
        raise ValueError("cannot call exponentiate_commuting_pauli_sum if Pauli terms do not commute")
        # return exponentiate(H)


def U_partition(B, city_partition, order_partition):
    '''
    partial color parity mixer for the Travelling Salesperson Problem found in arXiv:1709.03489

    :param B: beta
    :param city_partitions: list of city partitions (which are lists themselves of tuples of cities).
                            Equivalent to the color partitions in the original algorithm
    :param order_partitions: list of order partitions (which are lists themselves of orders).
                            Equivalent to the parity partitions in the original algorithm
    :return:
    '''
    initial_qubit = get_qubit(city_partition[0][0], order_partition[0])

    programs = []

    for i in order_partition:
        for u, v in city_partition:
            exponentiated_function = U_biuv(i, u, v)
            programs.append(exponentiated_function(B))

    resulting_program = merge_programs(programs)

    return resulting_program


def color_parity_mixer(B, city_partitions, order_partitions):
    '''
    implements the full color parity mixer for the Travelling Salesperson Problem found in arXiv:1709.03489

    :param B: beta
    :param city_partitions: list of city partitions (which are lists themselves of tuples of cities).
                            Equivalent to the color partitions in the original algorithm
    :param order_partitions: list of order partitions (which are lists themselves of orders).
                            Equivalent to the parity partitions in the original algorithm
    :return:
    '''
    programs = []

    for order_partition in order_partitions:
        for city_partition in city_partitions:
            programs.append(U_partition(B, city_partition, order_partition))

    resulting_program = merge_programs(programs)
    return resulting_program


if __name__ == "__main__":
    test_B = 10
    city_partitions = [
        [(1, 2), (3, 4)],
        # [(1, 3), (2, 4)],
        # [(1, 4), (2, 3)],
    ]
    order_partitions = [
        [1, 3],
        [2, 4]
    ]

    result = color_parity_mixer(test_B, city_partitions, order_partitions)
    print(result)