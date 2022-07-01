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


def get_tree_representation(node):      # preorder visit of tree
    if node.get_type() == 0:
        print(node.get_feature())
        print(f'-- child left {node.get_feature()}')
        get_tree_representation(node.get_child_left())
        print(f'-- child right {node.get_feature()}')
        get_tree_representation(node.get_child_right())
    else:
        print(f"Label: {node.get_label()}")


def get_tree_height(node):
    if node.get_type() == 1:
        return 0
    return max(get_tree_height(node.get_child_left())+1, get_tree_height(node.get_child_right())+1)
