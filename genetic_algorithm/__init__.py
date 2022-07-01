from random import random

from individual.Nodes import InnerNode, Leaf


def read_file(filename):
    nodes = {}
    with open(filename) as file:
        for line in file:
            str_node = line.split()
            if str_node[1] == '0':
                nodes[str_node[0]] = InnerNode(str_node[2], str_node[3], str_node[4], str_node[5])
            else:
                nodes[str_node[0]] = Leaf(str_node[2])

        '''
        for node in nodes:
            if nodes[node].get_type() == 0:
                print(f"Parent {node}:", nodes[node].get_feature())
            else:
                print(f"Parent {node}:", nodes[node].get_label())
        '''

        tree = nodes['root']
        build_tree(nodes, tree)

        return tree


def build_tree(nodes, node):
    if node.get_type() == 0:
        child_left = nodes[f"{node.get_feature()}_l"]
        child_left.set_parent(node)
        child_right = nodes[f"{node.get_feature()}_r"]
        child_right.set_parent(node)

        node.set_child_left(child_left)
        node.set_child_right(child_right)
        build_tree(nodes, node.get_child_left())
        build_tree(nodes, node.get_child_right())
    elif node.get_type() == 1:
        return True


def initialize_population(filename):
    return read_file(filename)


def fitness_func(solution, solution_idx):
    pass


def tree_crossover(node1, node2):

    stop = False
    while not stop:
        if random() > 0.4:
            node1 = node1.get_child_left()
        else:
            node1 = node1.get_child_right()

        if random() <= 0.6:
            node2 = node2.get_child_left()
        else:
            node2 = node2.get_child_right()

        if node1.get_type() == 1 or node2.get_type() == 1 or random() >= 0.5:
            stop = True

    parent1 = node1.get_parent()
    parent2 = node2.get_parent()

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

    if parent1.get_child_left() == node1:
        parent1.set_child_left(node2)
    else:
        parent1.set_child_right(node2)

    if parent2.get_child_left() == node2:
        parent2.set_child_left(node1)
    else:
        parent2.set_child_right(node1)


def tree_mutation(tree):
    pass


def get_tree_representation(node):
    if node.get_type() == 0:
        print(node.get_feature())
        print(f'-- child left {node.get_feature()}')
        get_tree_representation(node.get_child_left())
        print(f'-- child right {node.get_feature()}')
        get_tree_representation(node.get_child_right())
    else:
        print(f"Label: {node.get_label()}")


if __name__ == '__main__':
    tree1 = initialize_population('tree.txt')
    tree2 = initialize_population('tree2.txt')

    tree_crossover(tree1, tree2)
    print("\n\n\nTREE1")
    get_tree_representation(tree1)
    print("\n\n\nTREE2")
    get_tree_representation(tree2)
