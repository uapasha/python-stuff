# -*- coding: utf-8 -*-
"""
Created on Tue May 03 09:35:25 2016

@author: uapasha
"""
import os
from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import sys

DIR = 'C:\\Dropbox\\machine learning\\texts\\'

vectorizer = CountVectorizer(min_df = 1)

print (vectorizer)

content = ['How to format my hard disk', 'Hard disk format problems']

X = vectorizer.fit_transform(content)

vectorizer.get_feature_names()

print (X.toarray().transpose())
# some toy posts to play with
posts = [open(os.path.join(DIR, f)).read() for f in os.listdir(DIR)]
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
print(vectorizer.get_feature_names())
new_post = 'imaging databases'
new_post_vect = vectorizer.transform([new_post])

def dist_raw(v1, v2):
    delta = v1-v2
    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = sys.maxint
best_i = None
for i, post in enumerate(posts):
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist_raw(post_vec, new_post_vect)
    print('=== Post %i with dist = %.2f: %s ' % (i, d, post))
    if d < best_dist:
        best_dist = d
        best_i = i
print('Best post is %i with distance %.2f.' % (best_i, best_dist))