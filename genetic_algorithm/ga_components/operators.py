import copy
from random import randrange, random, uniform

import numpy as np
from pymoo.core.crossover import Crossover
from pymoo.core.duplicate import ElementwiseDuplicateElimination
from pymoo.core.mutation import Mutation

from genetic_algorithm.utility import get_root, get_tree_height


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
                    if random() > 0.4:
                        offspring1 = offspring1.get_child_left()
                    else:
                        offspring1 = offspring1.get_child_right()

            iterations = randrange(get_tree_height(offspring2) + 1)
            for i in range(0, iterations):
                if offspring2.type == 0:
                    if random() <= 0.6:
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

            iterations = randrange(get_tree_height(offspring) + 1)

            for j in range(iterations):
                if offspring.type == 0:
                    if random() >= 0.5:
                        offspring = offspring.get_child_left()
                    else:
                        offspring = offspring.get_child_right()

            if offspring.type == 0:
                if random() >= 0.5:  # change value
                    value_range = [int(value) for value in offspring.value_range.split('-')]
                    new_value = uniform(value_range[0], value_range[1])
                    offspring.value = new_value
                    print(f'Change value: {offspring.value}')
                else:  # change condition '<' <-> '>='
                    if offspring.condition == 0:
                        offspring.condition = 1
                    else:
                        offspring.condition = 0
                    print(f'Change condition: {offspring.condition}')
            else:
                print('It is a label ...')
                # TODO

        return X


class MyDuplicateElimination(ElementwiseDuplicateElimination):

    def is_equal(self, a, b):
        return a.X[0] == b.X[0]
