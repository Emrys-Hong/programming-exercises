# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 00:30:57 2018

@author: jon_c
"""


from sklearn.metrics import confusion_matrix

output = {}

def get_metrics (actual_targets, predicted_targets, labels):
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    return c_matrix

def total_records(actual):
    return (len(actual))

def accuracy(actual):
    return ((get_metrics(actual, predicted, labels)[0][0] + get_metrics(actual, predicted, labels)[1][0]) / len(actual))

def sensitivity():
    return ((get_metrics(actual, predicted, labels)[1][1]) / (get_metrics(actual, predicted, labels)[1][0] + get_metrics(actual, predicted, labels)[1][1]))

def false_positive_rate():
    return ((get_metrics(actual, predicted, labels)[0][1]) / ((get_metrics(actual, predicted, labels)[1][0]) + (get_metrics(actual, predicted, labels)[1][1]))


actual = [ 'cat' , 'cat' , 'cat' , 'cat' , 'bird' , 'bird' , 'bird' , 'bird' ]
predicted = [ 'cat' , 'cat' , 'bird' , 'bird' , 'cat' , 'bird' , 'bird' , 'bird' ]
labels = [ 'bird' , 'cat' ]
print(get_metrics(actual, predicted, labels) )
print(accuracy(actual))
output = {"confusion matrix": get_metrics(actual, predicted, labels), "total records": total_records(actual), 
          "accuracy": accuracy(actual) , "sensitivity": sensitivity(), "false positive rate": false_positive_rate()}
print(output)