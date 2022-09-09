import pandas as pd
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score


class TreeModel:
    def __init__(self, tree):
        self.tree = tree
        self.expected = []
        self.predicted = []
        self.df = pd.read_csv('df.csv')
        self.df.drop('Unnamed: 0', axis=1, inplace=True)

    def predict(self):
        self.expected = []
        self.predicted = []
        for index, row in self.df.iterrows():
            self.expected.append(row['target'])
            '''
            the decision_of_tree function takes care of following 
            the path of the tree by checking the various conditions
            '''
            self.predicted.append(self.__decision_of_tree(self.tree, row))

    def __decision_of_tree(self, tree, row):
        if tree.type == 1:
            return int(tree.label)

        if tree.type == 0:
            if tree.condition == '<=':
                if row[tree.feature] <= tree.value:
                    return self.__decision_of_tree(tree.get_child_left(), row)
                else:
                    return self.__decision_of_tree(tree.get_child_right(), row)
            else:
                if row[tree.feature] > tree.value:
                    return self.__decision_of_tree(tree.get_child_left(), row)
                else:
                    return self.__decision_of_tree(tree.get_child_right(), row)

    def get_precision(self):
        return precision_score(self.expected, self.predicted)

    def get_recall(self):
        return recall_score(self.expected, self.predicted)

    def get_accuracy(self):
        return accuracy_score(self.expected, self.predicted)

    def get_fmeasure(self):
        return f1_score(self.expected, self.predicted)
