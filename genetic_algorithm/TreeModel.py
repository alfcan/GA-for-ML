import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

class TreeModel:
    def __init__(self, tree):
        self.tree = tree

        from sklearn.datasets import load_iris
        iris = load_iris()

        # transform dataset in dataframe
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                          columns=iris['feature_names'] + ['target'])
        self.df = df
        # indicate number of classes for calculate TP,FP,FN,TN
        self.num_classes = 3

        self.confusion_matrix = None
        self.TP = []
        self.FP = []
        self.FN = []
        self.TN = []

    def predict(self):
        expected = []
        predicted = []
        for index, row in self.df.iterrows():
            expected.append(row['target'])
            predicted.append(self.__decision_of_tree(self.tree, row))

        self.confusion_matrix = confusion_matrix(expected, predicted)
        self.calculate_TP_FP_FN_TN()

    def __decision_of_tree(self, tree, row):
        if tree.type == 1:
            return int(tree.label)

        if tree.type == 0:
            if tree.condition == '<':
                if row[tree.feature] < tree.value:
                    return self.__decision_of_tree(tree.get_child_left(), row)
                else:
                    return self.__decision_of_tree(tree.get_child_right(), row)
            else:
                if row[tree.feature] >= tree.value:
                    return self.__decision_of_tree(tree.get_child_left(), row)
                else:
                    return self.__decision_of_tree(tree.get_child_right(), row)

    def calculate_TP_FP_FN_TN(self):
        self.TP = np.diag(self.confusion_matrix)
        self.FP = np.sum(self.confusion_matrix, axis=0) - self.TP
        self.FN = np.sum(self.confusion_matrix, axis=1) - self.TP

        self.TN = []
        for i in range(self.num_classes):
            temp = np.delete(self.confusion_matrix, i, 0)   # delete ith row
            temp = np.delete(temp, i, 1)                    # delete ith column
            self.TN.append(sum(sum(temp)))

    def get_precision(self):
        return np.sum(self.TP)/(np.sum(self.TP)+np.sum(self.FP))

    def get_recall(self):
        return np.sum(self.TP)/(np.sum(self.TP)+np.sum(self.FN))