from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.factory import get_selection
from pymoo.optimize import minimize

from genetic_algorithm.ga_components import problem
from genetic_algorithm.ga_components.operators import TreeCrossover, TreeMutation, MyDuplicateElimination
from genetic_algorithm.ga_components.problem import ProblemDecisionTree, Initialization
from genetic_algorithm.utility import generate_nodes, build_tree, get_tree_representation

if __name__ == '__main__':

    print('\nRESEARCHED FOR ML\n')
    print('Select the metric for the evaluation of the individual:\n1.Precision\n2.Recall\n3.Accuracy\n4.F-measure')
    print('By default, the metric used is F-measure')
    metric = int(input('Type your choice: '))
    print('\n\n')

    algorithm = GA(pop_size=problem.SIZE_POPULATION,
                   sampling=Initialization(),
                   selection=get_selection('random'),
                   crossover=TreeCrossover(2, 2),
                   mutation=TreeMutation(),
                   eliminate_duplicates=False)

    res = minimize(ProblemDecisionTree(metric),
                   algorithm,
                   verbose=False)

    print('\n\nFINAL SOLUTION', res.X[0])
    get_tree_representation(res.X[0])
    print(res.F[0])
