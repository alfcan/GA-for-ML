from abc import ABC, abstractmethod

class NodeInterface(ABC):
    @abstractmethod
    def get_type(self):
        pass


class Leaf(NodeInterface):
    def __init__(self, label):
        self.type = 1
        self.label = label

    def get_type(self):
        return self.type

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label


class InnerNode(NodeInterface):
    def __init__(self, child_left, child_right, feature, condition, value, range):
        self.type = 0
        self.childs = [child_left, child_right]
        self.feature = feature
        self.condition = condition      # contidion=0 : < --- condition=1 : >=
        self.value = value
        self.range = range              # range= "min_value-max_value"

    def get_type(self):
        return self.type

    '''
        Add two childs: child_left is left child (childs[0]) and child_right is right child (childs[1])
        If the condition is verify go to childs[0] else go to childs[1]
    '''
    def add_childs(self, child_left, child_right):
        self.childs[0] = child_left
        self.chilsd[1] = child_right

    def set_child_left(self, child):
        self.childs[0] = child

    def set_child_right(self, child):
        self.childs[1] = child

    def delete_childs(self):
        self.childs[0] = None
        self.chilsd[1] = None

    def get_child_left(self):
        return self.childs[0]

    def get_child_right(self):
        return self.childs[1]

    def set_feature(self, feature):
        self.feature = feature

    def get_feature(self):
        return self.feature

    def set_condition(self, condition):
        self.condition = condition

    def get_condition(self):
        return self.condition

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_range(self, range):
        self.range = range

    def get_range(self):
        return self.range