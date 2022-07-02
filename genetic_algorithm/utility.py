from random import randrange, random, uniform

from individual.Nodes import InnerNode, Leaf


def generate_nodes(inner_nodes, leafs, filename):
    inner_nodes.clear()
    leafs.clear()

    with open(filename) as file:
        for line in file:
            node = line.split()
            if node[0] == '0':
                node = InnerNode(node[1], get_condition(), get_value(node[2]), node[2])
                inner_nodes.append(node)
            else:
                leaf = Leaf(node[1])
                leafs.append(leaf)


def build_tree(node, inner_nodes, leafs, leafs_copy):
    rand = random()

    # only one inner node -> the childs of parent node can be: 2 label nodes or 1 inner node and 1 label node
    if len(inner_nodes) == 1:
        if rand < 0.33:
            rand = rand + 0.33
    # zero inner nodes -> the childs of parent node can be: 2 label nodes
    if len(inner_nodes) == 0:
        if rand < 0.66:
            rand = rand + 0.66
    # if there are less than 2 leaf nodes then we add a "copy" lead node
    if len(leafs) == 1:
        leaf1 = randrange(len(leafs_copy))
        leafs.add(leafs_copy[leaf1])
    elif len(leafs) < 1:
        leaf1 = randrange(len(leafs_copy))
        leaf2 = randrange(len(leafs_copy))
        if leaf1 == leaf2:
            leaf2 = randrange(len(leafs_copy))
        leafs.add(leafs_copy[leaf1])
        leafs.add(leafs_copy[leaf2])

    if rand < 0.33:
        feature_l = inner_nodes[randrange(len(inner_nodes))]
        inner_nodes.remove(feature_l)
        feature_r = inner_nodes[randrange(len(inner_nodes))]
        inner_nodes.remove(feature_r)

        node.set_child_left(feature_l)
        node.set_child_right(feature_r)

        build_tree(feature_l, inner_nodes, leafs, leafs_copy)
        build_tree(feature_r, inner_nodes, leafs, leafs_copy)
    elif 0.33 <= rand < 0.66:
        feature = inner_nodes[randrange(len(inner_nodes))]
        inner_nodes.remove(feature)
        label = leafs[randrange(len(leafs))]
        leafs.remove(label)

        if randrange(2) == 0:
            node.set_child_left(feature)
            node.set_child_right(label)
        else:
            node.set_child_right(label)
            node.set_child_left(feature)

        build_tree(feature, inner_nodes, leafs, leafs_copy)
    else:
        label_l = leafs[randrange(len(leafs))]
        label_r = leafs[randrange(len(leafs))]

        node.set_child_left(label_l)
        node.set_child_right(label_r)


def get_condition():
    if randrange(2) == 0:
        return '>='
    else:
        return '<'


def get_value(value_range):
    value_range = [int(v) for v in value_range.split('-')]
    return uniform(value_range[0], value_range[1])


def get_tree_representation(node):      # preorder visit of tree
    if node.type == 0:
        print(node.feature)
        print(f'-- child left {node.feature}')
        get_tree_representation(node.get_child_left())
        print(f'-- child right {node.feature}')
        get_tree_representation(node.get_child_right())
    else:
        print(f"Label: {node.label}")


def get_tree_height(node):
    if node.type == 1:
        return 0
    return max(get_tree_height(node.get_child_left())+1, get_tree_height(node.get_child_right())+1)


def build_tree_file(nodes, node):
    if node.type == 0:
        child_left = nodes[f"{node.feature}_l"]
        child_left.parent = node
        child_right = nodes[f"{node.feature}_r"]
        child_right.parent = node

        node.set_child_left(child_left)
        node.set_child_right(child_right)
        build_tree_file(nodes, node.get_child_left())
        build_tree_file(nodes, node.get_child_right())
    elif node.type == 1:
        return True


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
        build_tree_file(nodes, tree)

        return tree


'''def generate_tree_file(features, labels, filename):
    with open(filename, 'w') as file:
        idx = randrange(len(features))
        root = features[idx].split()
        file.write(f'root 0 {root[0]} {get_condition()} {get_value(root[1])} {root[1]}\n')
        parent = root
        while len(features) > 1:
            features.remove(f'{parent[0]} {parent[1]}')
            idx1 = randrange(len(features))
            idx2 = randrange(len(features))
            if idx1 == idx2:
                idx2 = randrange(len(features))
            l1 = randrange(len(labels))
            l2 = randrange(len(labels))
            if l1 == l2:
                l2 = randrange(len(labels))

            feature1 = []
            feature1_str = features[idx1].split()
            feature1.append(feature1_str[0])
            feature1.append(get_condition())
            feature1.append(get_value(feature1_str[1]))
            feature1.append(feature1_str[1])

            feature2 = []
            feature2_str = features[idx2].split()
            feature2.append(feature2_str[0])
            feature2.append(get_condition())
            feature2.append(get_value(feature2_str[1]))
            feature2.append(feature2_str[1])

            label1 = labels[l1]
            label2 = labels[l2]

            rand = random()
            if rand < 0.13:
                file.write(f'{parent[0]}_l 0 {feature1[0]} {feature1[1]} {feature1[2]} {feature1[3]}\n')
                file.write(f'{parent[0]}_r 0 {feature2[0]} {feature2[1]} {feature2[2]} {feature2[3]}\n')
            elif 0.13 <= rand < 0.26:
                file.write(f'{parent[0]}_l 0 {feature1[0]} {feature1[1]} {feature1[2]} {feature1[3]}\n')
                file.write(f'{parent[0]}_r 0 {feature2[0]} {feature2[1]} {feature2[2]} {feature2[3]}\n')
            elif 0.26 <= rand < 0.39:
                file.write(f'{parent[0]}_l 1 {label1}\n')
                file.write(f'{parent[0]}_r 0 {feature2[0]} {feature2[1]} {feature2[2]} {feature2[3]}\n')
            elif 0.39 <= rand < 0.52:
                file.write(f'{parent[0]}_l 1 {label1}\n')
                file.write(f'{parent[0]}_l 0 {feature1[0]} {feature1[1]} {feature1[2]} {feature1[3]}\n')
            elif 0.52 <= rand < 0.65:
                file.write(f'{parent[0]}_l 0 {feature1[0]} {feature1[1]} {feature1[2]} {feature1[3]}\n')
                file.write(f'{parent[0]}_r 1 {label2}\n')
            elif 0.65 <= rand < 0.78:
                file.write(f'{parent[0]}_r 0 {feature2[0]} {feature2[1]} {feature2[2]} {feature2[3]}\n')
                file.write(f'{parent[0]}_r 1 {label2}\n')
            elif 0.78 <= rand < 0.90:
                file.write(f'{parent[0]}_l 1 {label1}\n')
                file.write(f'{parent[0]}_r 1 {label2}\n')
            else:
                file.write(f'{parent[0]}_l 1 {label2}\n')
                file.write(f'{parent[0]}_r 1 {label1}\n')

            parent = features[randrange(len(features))].split()

        feature = features[0].split()
        l1 = randrange(len(labels))
        l2 = randrange(len(labels))
        if l1 == l2:
            l2 = randrange(len(labels))
        file.write(f'{feature[0]}_r 1 {labels[l1]}\n')
        file.write(f'{feature[0]}_l 1 {labels[l2]}\n')
'''