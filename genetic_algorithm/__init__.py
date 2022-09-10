from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.factory import get_selection, get_termination
from pymoo.operators.selection.tournament import TournamentSelection
from pymoo.optimize import minimize

from genetic_algorithm.TreeModel import TreeModel
from genetic_algorithm.ga_components import problem
from genetic_algorithm.ga_components.operators import TreeCrossover, TreeMutation, MyDuplicateElimination, \
    binary_tournament
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
                   selection=TournamentSelection(pressure=2, func_comp=binary_tournament),
                   crossover=TreeCrossover(2, 2),
                   mutation=TreeMutation(),
                   eliminate_duplicates=False)

    res = minimize(ProblemDecisionTree(metric),
                   algorithm,
                   get_termination('n_gen', 50),
                   # get_termination("time", "00:05:00"),
                   seed=1,
                   verbose=False)

    print('\n\nFINAL SOLUTION', res.X[0])
    get_tree_representation(res.X[0])
    print('\nEvaluation: ', res.F[0])

    model = TreeModel(res.X[0])
    model.predict()
    print('\n\nAll metrics of the model.')
    print(res.X[0])
    print('Precision: ', model.get_precision())
    print('Recall   : ', model.get_recall())
    print('Accuracy : ', model.get_accuracy())
    print('F-measure: ', model.get_fmeasure())
