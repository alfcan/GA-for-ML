import copy
from random import randrange

import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.sampling import Sampling

from genetic_algorithm.TreeModel import TreeModel
from genetic_algorithm.utility import generate_nodes, build_tree

FILE_NODES = 'nodes.txt'
SIZE_POPULATION = 50
NUM_PARENTS_MATING = 2


class ProblemDecisionTree(ElementwiseProblem):
    def __init__(self, metric):
        super().__init__(n_var=1, n_obj=1, n_constr=0)
        self.metric = metric

    def _evaluate(self, x, out, *args, **kwargs):
        model = TreeModel(x[0])

        model.train()

        if self.metric == 1:
            evaluation = -model.get_precision()
        elif self.metric == 2:
            evaluation = -model.get_recall()
        elif self.metric == 3:
            evaluation = -model.get_accuracy()
        else:
            evaluation = -model.get_fmeasure()

        out['F'] = evaluation
        print(f'precision: {model.get_precision()} - recall: {model.get_recall()} - accuracy: {model.get_accuracy()}'
              f' - fmeasure: {model.get_fmeasure()} -- {x[0]}')


class Initialization(Sampling):

    def _do(self, problem, n_samples, **kwargs):
        X = np.full((n_samples, 1), None)

        i = 0
        for tree in initializate_population():
            X[i, 0] = tree
            i = i + 1

        return X


def initializate_population():
    features = []
    labels = []

    generate_nodes(features, labels, FILE_NODES)

    trees = []
    for i in range(SIZE_POPULATION):
        inner_nodes = [copy.deepcopy(node) for node in features]
        leafs = [copy.deepcopy(leaf) for leaf in labels]

        root = inner_nodes[randrange(len(inner_nodes))]
        inner_nodes.remove(root)
        build_tree(root, inner_nodes, leafs, leafs)
        trees.append(root)

    return trees
