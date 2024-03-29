import copy
from random import randrange, random, uniform

import numpy as np
from pymoo.core.crossover import Crossover
from pymoo.core.duplicate import ElementwiseDuplicateElimination
from pymoo.core.mutation import Mutation

from genetic_algorithm.utility import get_root, get_tree_height, get_leafs


class TreeCrossover(Crossover):
    def __init__(self, num_parents, num_offspings):
        # define the crossover: number of parents and number of offsprings
        super().__init__(num_parents, num_offspings)

    def _do(self, problem, X, **kwargs):
        _, n_matings, n_var = X.shape

        Y = np.full_like(X, None)

        for k in range(n_matings):
            offspring1 = copy.deepcopy(X[0, k, 0])
            offspring2 = copy.deepcopy(X[1, k, 0])

            iterations = randrange(get_tree_height(offspring1) + 1)
            for i in range(iterations):
                if offspring1.type == 0:
                    if random() <= 0.5:
                        offspring1 = offspring1.get_child_left()
                    else:
                        offspring1 = offspring1.get_child_right()

            iterations = randrange(get_tree_height(offspring2) + 1)
            for i in range(0, iterations):
                if offspring2.type == 0:
                    if random() <= 0.5:
                        offspring2 = offspring2.get_child_left()
                    else:
                        offspring2 = offspring2.get_child_right()

            node_parent_1 = offspring1.parent
            node_parent_2 = offspring2.parent

            if node_parent_1 is None:  # if parent1 is None then node is root
                node_parent_1 = offspring2
            elif node_parent_1.get_child_left() == offspring1:
                node_parent_1.set_child_left(offspring2)
            else:
                node_parent_1.set_child_right(offspring2)

            if node_parent_2 is None:  # if parent2 is None then node is root
                node_parent_2 = offspring1
            elif node_parent_2.get_child_left() == offspring2:
                node_parent_2.set_child_left(offspring1)
            else:
                node_parent_2.set_child_right(offspring1)

            root_1 = get_root(offspring1)
            root_2 = get_root(offspring2)

            Y[0, k, 0] = root_1
            Y[1, k, 0] = root_2

        return Y


class TreeMutation(Mutation):
    def __init__(self):
        super().__init__()

    def _do(self, problem, X, **kwargs):
        for i in range(len(X)):
            offspring = X[i, 0]
            leafs = get_leafs('nodes.txt')

            iterations = randrange(get_tree_height(offspring) + 1)

            for j in range(iterations):
                if offspring.type == 0:
                    if random() >= 0.5:
                        offspring = offspring.get_child_left()
                    else:
                        offspring = offspring.get_child_right()

            if offspring.type == 0:  # it is a Inner Node
                if random() >= 0.5:  # change value
                    value_range = [float(value) for value in offspring.value_range.split('/')]
                    new_value = uniform(value_range[0], value_range[1])
                    offspring.value = new_value
                    print(f'Change value: {offspring.value}')
                else:  # change condition '<=' <-> '>'
                    if offspring.condition == '<=':
                        offspring.condition = '>'
                    else:
                        offspring.condition = '<='
                    print(f'Change condition: {offspring.condition}')
            else:  # it is a label and change value of leaf
                old_label = offspring.label
                new_leafs = copy.copy(leafs)
                new_leafs.remove(old_label)
                offspring.label = new_leafs[randrange(len(new_leafs))]
                print(f'Change Label value: {offspring.label} - old label {old_label}')

        return X


class MyDuplicateElimination(ElementwiseDuplicateElimination):

    def is_equal(self, a, b):
        return a.X[0] == b.X[0]


# Function for tournament selection
def binary_tournament(pop, P, **kwargs):
    # The P input defines the tournaments and competitors
    n_tournaments, n_competitors = P.shape

    if n_competitors != 2:
        raise Exception("Only pressure=2 allowed for binary tournament!")

    # the result this function returns
    S = np.full(n_tournaments, -1, dtype=np.int)

    # now do all the tournaments
    for i in range(n_tournaments):
        a, b = P[i]

        # if the first individual is better, choose it
        if pop[a].F < pop[b].F:
            S[i] = a

        # otherwise take the other individual
        else:
            S[i] = b

    return S
