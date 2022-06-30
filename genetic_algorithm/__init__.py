from individual.Nodes import InnerNode, Leaf

filename = 'tree.txt'


def read_file():
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


def build_tree(nodes, node):
    if node.get_type() == 0:
        node.set_child_left(nodes[f"{node.get_feature()}_sx"])
        node.set_child_right(nodes[f"{node.get_feature()}_dx"])
        print(node.get_feature())
        build_tree(nodes, node.get_child_left())
        build_tree(nodes, node.get_child_right())
    elif node.get_type() == 1:
        return True


def initialize_population():
    read_file()


def fitness_func(solution, solution_idx):
    pass


if __name__ == '__main__':
    initialize_population()
