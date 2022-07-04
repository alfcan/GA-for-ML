from random import random, randrange, uniform

from genetic_algorithm.utility import get_tree_representation, read_file, get_tree_height, \
    generate_nodes, build_tree

SIZE_POPULATION = 10
FILE_NODES = 'nodes.txt'


def initialize_population():
    features = []
    labels = []

    generate_nodes(features, labels, FILE_NODES)

    trees = []
    for i in range(SIZE_POPULATION):
        inner_nodes = features.copy()
        leafs = labels.copy()

        root = inner_nodes[randrange(len(inner_nodes))]
        inner_nodes.remove(root)
        build_tree(root, inner_nodes, leafs, leafs)
        trees.append(root)

    return trees


def fitness_func(solution, solution_idx):
    pass


def tree_crossover(node1, node2):
    iterations = randrange(get_tree_height(node1) + 1)
    for i in range(0, iterations):
        if node1.type == 0:
            if random() > 0.4:
                node1 = node1.get_child_left()
            else:
                node1 = node1.get_child_right()

    iterations = randrange(get_tree_height(node2) + 1)
    for i in range(0, iterations):
        if node2.type == 0:
            if random() <= 0.6:
                node2 = node2.get_child_left()
            else:
                node2 = node2.get_child_right()

    parent1 = node1.parent
    parent2 = node2.parent

    '''
    if node1.type == 0:
        print(f'NODE 1 Inner -> {node1.feature}')
    else:
        print(f'NODE 1 -> {node1.label}')
    if node2.type == 0:
        print(f'NODE 2 Inner -> {node2.feature}')
    else:
        print(f'NODE 2 -> {node2.label}')

    print(f'Parent NODE 1 -> {parent1.feature}')
    print(f'Parent NODE 2 -> {parent2.feature}')
    '''

    if parent1 is None:         # if parent1 is None then node is root
        parent1 = node2
    elif parent1.get_child_left() == node1:
        parent1.set_child_left(node2)
    else:
        parent1.set_child_right(node2)

    if parent2 is None:         # if parent2 is None then node is root
        parent2 = node1
    elif parent2.get_child_left() == node2:
        parent2.set_child_left(node1)
    else:
        parent2.set_child_right(node1)


def tree_mutation(root):
    iterations = randrange(get_tree_height(root) + 1)

    for i in range(0, iterations):
        if root.type == 0:
            if random() >= 0.5:
                root = root.get_child_left()
            else:
                root = root.get_child_right()

    if root.type == 0:
        if random() >= 0.5:     # change value
            value_range = [int(value) for value in root.value_range.split('-')]
            root.set_value(uniform(value_range[0], value_range[1]))
            print(f'Change value: {root.get_value()}')
        else:                   # change condition '<' <-> '>='
            if root.condition == 0:
                root.condition = 1
            else:
                root.condition = 0
            print(f'Change condition: {root.condition}')
    else:
        print('It is a label ...')
        # TODO


if __name__ == '__main__':
    population = initialize_population()
    for tree in population:
        print('\n\n\nTREE')
        get_tree_representation(tree)
