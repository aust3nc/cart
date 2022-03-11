from tree import createnode, findleafgini, findinternalgini, findsplit, grow_tree

#pandas for dataframe creation
import pandas as pd

#making test data
data = {'featureA': [0, 1, 1, 0, 0, 0, 1], 
'featureB': [1, 0, 1, 1, 0, 1, 1], 'featureC': [0, 1, 0, 1, 0, 0, 0], 
'target': [1, 0, 1, 0, 1, 1, 0]}
test_data = pd.DataFrame(data=data)
print(test_data)

#select feature and target
feature = list(test_data.featureA)
target = list(test_data.target)

#test createnode
node = createnode(test_data, feature, target)
print(node)

#test findgini
print(findleafgini(node))

#test grow_tree
print(grow_tree(test_data))
