#pandas for data loading/frame creation
import pandas as pd

def metric(real, predicted):
    '''return accuracy'''
    #init empty int
    correct = 0
    #loop over list of true values, comparing to 
    #predicted values same index
    for index in range(len(real)):
        #for every same value, add 1 point
        if real[index] == predicted[index]:
            correct += 1
    #divide the number of correct predictions
    #by the amount of total predictions, and 
    #multiply by 100 to return accuracy
    return correct / float(len(real)) * 100

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

def findleafgini(node):
    '''find gini index of leaf node'''
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

def grow_tree(data):
    rows = {}
    for row in data:
        feature = list(data[row])
        rows[row] = feature
    target = input(f"pick the target variable from the following: {list(data.columns)} ")
    del rows[target]
    for r in rows:
        t = list(data.target)
        feature = rows[r]
        print(createnode(data, feature, t))

def findsplit(**features_list):
    '''find feature to split tree from'''
    splitfeature = max(features_list.values)
    del features_list[splitfeature]
    return splitfeature



