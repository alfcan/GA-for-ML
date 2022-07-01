from random import random, randrange, uniform

from genetic_algorithm.utility import get_tree_representation, read_file, get_tree_height


def initialize_population(filename):
    return read_file(filename)


def fitness_func(solution, solution_idx):
    pass


def tree_crossover(node1, node2):
    iterations = randrange(get_tree_height(node1) + 1)
    for i in range(0, iterations):
        if node1.get_type() == 0:
            if random() > 0.4:
                node1 = node1.get_child_left()
            else:
                node1 = node1.get_child_right()

    iterations = randrange(get_tree_height(node2) + 1)
    for i in range(0, iterations):
        if node2.get_type() == 0:
            if random() <= 0.6:
                node2 = node2.get_child_left()
            else:
                node2 = node2.get_child_right()

    parent1 = node1.get_parent()
    parent2 = node2.get_parent()

    '''
    if node1.get_type() == 0:
        print(f'NODE 1 Inner -> {node1.get_feature()}')
    else:
        print(f'NODE 1 -> {node1.get_label()}')
    if node2.get_type() == 0:
        print(f'NODE 2 Inner -> {node2.get_feature()}')
    else:
        print(f'NODE 2 -> {node2.get_label()}')

    print(f'Parent NODE 1 -> {parent1.get_feature()}')
    print(f'Parent NODE 2 -> {parent2.get_feature()}')
    '''

    if parent1 is None:         # parent1 == None if node is root
        parent1 = node2
    elif parent1.get_child_left() == node1:
        parent1.set_child_left(node2)
    else:
        parent1.set_child_right(node2)

    if parent2 is None:         # parent2 == None if node is root
        parent2 = node1
    elif parent2.get_child_left() == node2:
        parent2.set_child_left(node1)
    else:
        parent2.set_child_right(node1)


def tree_mutation(tree):
    iterations = randrange(get_tree_height(tree) + 1)

    for i in range(0, iterations):
        if tree.get_type() == 0:
            if random() >= 0.5:
                tree = tree.get_child_left()
            else:
                tree = tree.get_child_right()

    if tree.get_type() == 0:
        if random() >= 0.5:     # change value
            value_range = [int(value) for value in tree.get_range().split('-')]
            tree.set_value(uniform(value_range[0], value_range[1]))
            print(f'Change value: {tree.get_value()}')
        else:                   # change condition '<' <-> '>='
            if tree.get_condition() == 0:
                tree.set_condition(1)
            else:
                tree.set_condition(0)
            print(f'Change condition: {tree.get_condition()}')
    else:
        print('It is a label ... FUCK I DO?')


if __name__ == '__main__':
    tree1 = initialize_population('tree.txt')
    tree2 = initialize_population('tree2.txt')

    tree_mutation(tree1)