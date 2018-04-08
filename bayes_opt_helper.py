import numpy as np

def neg_cost_vector(qaoa_output, num_cities=4):
    trials = qaoa_output.shape[0]

    if qaoa_output.shape[1] <> num_cities^2:
        ValueError("The input samples have the wrong number of cities")

    cost_vector = np.empty(trials)

    for trial in range(trials):
        qaoa_trial = qaoa_output[trial]
        cities_order = np.empty(num_cities)

        cost = 0

        for n in range(num_cities):
            cities_order[n] = np.nonzero(qaoa_trial[n: n + (num_cities - 1)])[0]

            city_1 = cities_order[n % num_cities]
            city_2 = cities_order[(n + 1) % num_cities]
            cost += map.get_distance(city_1, city_2)

        cost_vector[trial] = cost

     return -cost_vector


def first_order_mean(neg_cost_vector):
    '''
    :param cost_vector: a vector containing samples from the cost distribution
    :return: Montecarlo estimate of the first order statistic based on cost distribution
    '''

    trials = len(neg_cost_vector)
    first_order_trial = np.empty(trials)


    for n in range(trials):
        cum_prob_n = np.sum(np.less_equal(neg_cost_vector, neg_cost_vector[n] * np.ones(trials)))/float(trials)
        first_order_trial = neg_cost_vector[n] * (1- cum_prob_n)**(trials - 1)

    first_order_mean = np.sum(first_order_trial)

    return first_order_mean


def first_order_actual(neg_cost_vector):
    return np.min(neg_cost_vector)