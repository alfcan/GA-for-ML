import numpy as np
import pandas as pd


class TreeModel:
    def __init__(self, tree):
        self.tree = tree

        from sklearn.datasets import load_iris
        iris = load_iris()

        # transform dataset in dataframe
        df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                          columns=iris['feature_names'] + ['target'])
        self.df = df

    def predict(self):
        for index, row in self.df.iterrows():
            target = self.__decision_of_tree(self.tree, row)

            # construct confusion matrix for a multiclass classification
            # if row['target'] == target:

    # private method -> prefix __
    def __decision_of_tree(self, tree, row):
        if tree.type == 1:
            return tree.label

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
