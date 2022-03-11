# #imports
# #%%
# import pandas as pd
# import numpy as np
# #%%

# class Cart:
#     """
#     classification and regression tree
#     """

#     class Node:
#         """
#         each node contains a sum of observations which subsets a sum of 
#         boolean Trues and a sum of boolean Falses (class A and class B)
#         """
#         def __init__(self, count):
#             self.count = count
#             self.yes = None
#             self.no = None

#     def __init__(self):
#         """
#         initialize an empty tree
#         """
#         self.root = None

#     def makeTree():
#         pass

#     def leafgini(self, count, node):
#         class_a = node.yes
#         class_b = node.no
#         return (1 - ((class_a/count)**2)-((class_b/count)**2))
    
#     def internalgini(self, count, childAgini, childBgini, node):
#         class_a = node.yes
#         class_b = node.no
#         return ((class_a/count)*childAgini)+((class_b/count)*childBgini)


#take feature array, target column, df, and return node


#contain: -count, -n(y), -n(n), -giniimpurity


# data = pd.


# def findsplit(*feature, df, target):
    # node = {feature:i.count(x) for x in}
    # for i in feature:
        
    # for df.feature in features:
    #     trueCount = 0
    #     falseCount = 0
    #     for i in df.feature:
    #         if i == 1 and df.target == 1:
    #             trueCount += 1 
    #         elif i == 0 and df.target == 0:
    #             falseCount += 1
        
    #     d = {x:i.count(x) for x in i}

#this is garbage ahahahha
# def main(data, *feature_list):
#     #instantiate an empty list to hold list of dictionaries 
#     #(each value has name of feature as key and gini as value)
#     root_iterator = []
#     gini_list = []
#     #loop over each feature, finding gini index of each
#     for feature in feature_list:
#         feature = data.feature
#         target = data.target
#         root_iterator.append(createnode(data, feature, target))
#     #find root
#     root = findsplit(root_iterator)
#     #append root to gini_list
#     gini_list.append(root)
#     #remove root feature from root_iterator
#     root_iterator.pop(root)
#     #iterate over remaining features
#     for feature in feature_list:
#         feature = data.feature
#         target = root
#         insert_left = root-1
#         insert_right = root+1
#         root_iterator.append(createnode(data, feature, target))
#     #find new root
#     new_root = findsplit(root_iterator)
#     #append root to gini_list
#     gini_list.insert(insert_left, new_root)
#     root_iterator.pop(root)
#     #go right
#     if gini_list[0:root] == len(feature_list) / 2:
#         pass
#     #base case
#     if len(root_iterator) == 0:
#         print(gini_list)
#     return main(data, feature_list)

class Cart:
    '''create a classification and regression tree (CART)'''
    class Node:
        '''inner class Node'''
        def __init__(self, gini):
            """ initialize node"""
            self.gini = gini
            self.left = None
            self.right = None
    def __init__(self):
        '''initialize an empty tree'''
        self.root = None
    def insert(self, gini):
        """
        insert 'gini' into cart; if tree
        is empty, then set the root equal to the new 
        node; otherwise, use _insert to recursively
        find the location to insert
        """
        if self.root is None:
            self.root = Cart.Node(gini)
        else:
            self._insert(gini, self.root)  

    def _insert(self, gini, node):
        if gini < node.gini:
            if node.left is None:
                node.left = Cart.Node(gini)
        else:
            self._insert(gini, self.root)
        
        def createnode(data, feature, target):
            '''return class counts, overall count, and name'''
            truecount = 0
            falsecount = 0
            for i in range(len(feature)):
                if feature[i] == 1 and target[i] == 1:
                    truecount += 1
                elif feature[i] == 0 and target[i] == 0:
                    falsecount += 1
                count = truecount+falsecount
            return [truecount, falsecount, count, data.columns[feature[0]]]

        def findgini(data, feature, target):
            '''find gini index of a feature given target and data'''
            node = Cart.createnode(data, feature, target)
            true = node[0]
            false = node[1]
            count = node[2]
            name = node[3]
            gini = (1 - ((true/count)**2)-((false/count)**2))
            return {name:gini}

        def findinternalgini(data, feature, target, childagini, childbgini):
            '''find gini index of an internal node'''
            node = createnode(data, feature, target)
            true = node[0]
            false = node[1]
            count = node[2]
            name = node[3]
            internalgini = ((true/count)*childagini)+((false/count)*childbgini)
            return {name:internalgini}

        def findsplit(**features_list):
            '''find feature to split tree from'''
            splitfeature = max(features_list.values)
            del features_list[splitfeature]
            return splitfeature

        def traintestsplit(data):
            '''split data into test and train groups'''
            pass
