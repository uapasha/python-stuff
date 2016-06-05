# -*- coding: utf-8 -*-
"""
Created on Mon May 02 10:50:22 2016

@author: uapasha
"""

from matplotlib import pyplot as plt
import numpy as np


# load iris data 
from sklearn.datasets import load_iris
data = load_iris()

features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'
    elif t == 1:
        c = 'g'
        marker = 'o'
    elif t == 2:
        c = 'b'
        marker = 'x'
    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker = marker,
                c = c)
#use NumPy indexing to get array of labels
labels = target_names[target]

#length of stables is the second argument
plength = features[:, 2]
# make an array of bool values
is_setosa = (labels == 'setosa')
#this is an important steP
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print ('Maximum of Setosa: {0}.'.format(max_setosa))
print ('Minimun of others: {0}.'.format(min_non_setosa))

# ~  - this is operator of logical negative
features = features[~is_setosa]
labels = labels[~is_setosa]
# add new target variable is_virginica
is_virginica = (labels == 'virginica')

#initialize best_acc value being the lest possible
best_acc  = -1.0
for fi in range(features.shape[1]):
    # we are going to check all possible corner cases
    thresh = features[:, fi]
    for t in thresh:
        # get vector for 'fi' feature
        feature_i = features[:, fi]
        # imply thresh t
        pred = (feature_i > t)
        acc = (pred == is_virginica).mean()
        rev_acc = (pred == ~is_virginica).mean()
        if rev_acc > acc:
            reverse = True
            acc = rev_acc
        else:
            reverse = False
            
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
            best_reverse = reverse

def is_virginica_test (fi, t, reverse, example):
    "Apply threshold model to a new example"
    test = example[fi] > t
    if reverse:
        test = not test
    return test
    
#correct = 0.0
#for ei in range(len(features)):
#    # keep all elements except those in "ei" position
#    training = np.ones(len(features), bool)
#    training[ei] = False
#    testing = ~training
#    model = np.fit_model(features[training], is_virginica[training])
#    predictions = np.predict(model, features[testing])
#    correct += np.sum(predictions == is_virginica[testing])


