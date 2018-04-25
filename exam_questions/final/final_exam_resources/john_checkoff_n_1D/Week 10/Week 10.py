# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:22:16 2018

@author: jon_c
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

bunchobject = datasets.load_breast_cancer()
print(bunchobject.DESCR)
print(bunchobject.feature_names)
print(bunchobject.target_names)
print(bunchobject.data.shape)
#
#column_index = 2
#print(bunchobject.feature_names[column_index])
#feature_vals_in_column = bunchobject.data[:,column_index]
#print(feature_vals_in_column)
#print( np.min(feature_vals_in_column), np.max(feature_vals_in_column))
#
#row_index = 0
#print(bunchobject.feature_names)
#record_vals_in_row = bunchobject.data[row_index,:]
#print(record_vals_in_row)
#print(bunchobject.target[row_index])



#unique, counts = np.unique(bunchobject.target, return_counts = True )
#for i in unique:
#    print(i, bunchobject.target_names[i], counts[i])

#%%
from sklearn.metrics import confusion_matrix

def get_metrics (actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    return c_matrix

def total_records(actual):
    return round((len(actual)), 3)

def accuracy(actual):
    return round(((get_metrics(actual, predicted, labels)[0][0] + get_metrics(actual, predicted, labels)[1][0]) / len(actual)), 3)

def sensitivity():
    return round(((get_metrics(actual, predicted, labels)[1][1]) / (get_metrics(actual, predicted, labels)[1][0] + get_metrics(actual, predicted, labels)[1][1])), 3)

def false_positive_rate():
    return round(((get_metrics(actual, predicted, labels)[0][1]) / ((get_metrics(actual, predicted, labels)[1][0]) + (get_metrics(actual, predicted, labels)[1][1]))), 3)

actual = [ 'cat' , 'cat' , 'cat' , 'cat' , 'bird' , 'bird' , 'bird' , 'bird' ]
predicted = [ 'cat' , 'cat' , 'bird' , 'bird' , 'cat' , 'bird' , 'bird' ,
'bird' ]
labels = [ 'bird' , 'cat' ]


output = {"confusion matrix": get_metrics(actual, predicted, labels), "total records": total_records(actual), 
          "accuracy": accuracy(actual) , "sensitivity": sensitivity(), "false positive rate": false_positive_rate()}
print(output)


#%%





