class Node:
    def __init__(self, t):
        self.type = t
        self.parent = None


class Leaf(Node):
    def __init__(self, label):
        super().__init__(1)
        self.label = label

    def __eq__(self, other):
        if isinstance(other, Leaf):
            return self.label == other.label and self.parent == other.parent
        return False


class InnerNode(Node):

    def __init__(self, feature, condition, value, value_range):
        super().__init__(0)
        self.childs = [None, None]
        self.feature = feature
        self.condition = condition  # < --- >=
        self.value = value
        self.value_range = value_range  # range= "min_value/max_value"

    '''
        Add two childs: child_left is left child (childs[0]) and child_right is right child (childs[1])
        If the condition is verify go to childs[0] else go to childs[1]
    '''
    def add_childs(self, child_left, child_right):
        child_left.parent = self
        child_right.parent = self
        self.childs[0] = child_left
        self.childs[1] = child_right

    def set_child_left(self, child):
        child.parent = self
        self.childs[0] = child

    def set_child_right(self, child):
        child.parent = self
        self.childs[1] = child

    def delete_childs(self):
        self.childs[0] = None
        self.childs[1] = None

    def get_child_left(self):
        return self.childs[0]

    def get_child_right(self):
        return self.childs[1]

    def __eq__(self, other):
        if isinstance(other, InnerNode):
            return self.feature == other.feature and self.condition == other.condition \
                   and self.value == other.value and self.value_range == other.value_range
        return False
