# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:22:29 2018

@author: jon_c
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix

#question 1

def display_box_plots (data, feature_names, title_name= "default"):
    plt.xkcd()
    num_of_features = feature_names.shape[0]
    print(num_of_features)
    tick_marks = list(range(1, num_of_features + 1))
    print(tick_marks)
    print(feature_names)
    plt.boxplot(data)
    plt.xticks(tick_marks, feature_names)
    plt.title(title_name)
    plt.show()
    
  

bunchobject = datasets.load_breast_cancer()
feature_range = [ 0 , 1 ]
data_subset = bunchobject.data[:,feature_range]
feature_names_subset = bunchobject.feature_names[feature_range]
display_box_plots(data_subset,feature_names_subset)

#%%
def display_histogram (data, nbins, feature_names, title_name= 'default'):
    plt.hist(data, nbins, color = "pink")
    plt.title(title_name)
    plt.ylabel("Frequency")
    plt.xlabel(feature_names)
    plt.show()
    
    
feature_col = 0
one_col_data = data_subset[:,feature_col]
feature_name_selected = bunchobject.feature_names[feature_col]
number_of_bins = 10 #please specify a suitable value
title_string = "Distribution of " + feature_name_selected + " of tumor" #please provide a suitable title string
[number, bins] = display_histogram(one_col_data, number_of_bins, feature_name_selected, title_string)




#%%
def display_scatter (x, y, xlabel = 'x' , ylabel = 'y' ,title_name = 'default' ):
    plt.scatter(x, y, s = 1, color = "grey")
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(xlabel + " vs " + ylabel)
    plt.show()
    

x_index = 15        #pick a label from 1-29
y_index = 13        #pick a label from 1-29
x = bunchobject.data[:,x_index]
y = bunchobject.data[:,y_index]
x_label = bunchobject.feature_names[x_index]
y_label = bunchobject.feature_names[y_index]
display_scatter(x, y, x_label, y_label)



#%%

def display_bar_chart (positions, counts, names, title_name = 'default' ):
    plt.bar(positions, counts, color = "purple")
    plt.title(names)
    plt.show()
    

unique, counts = np.unique(bunchobject.target, return_counts = True )
display_bar_chart(unique, counts, bunchobject.target_names)

#%%

#question 2
def five_number_summary (x):
    lst = []
    for i in range(len(x[0])):
        dic = {"minimum" : np.min(x[:,i]), "first quartile" : np.percentile(x[:,i], 25), 
              "median" : np.median(x[:,i]), "third quartile" : np.percentile(x[:,i], 75),
              "maximum" : np.max(x[:,i])}
        lst.append(dic)
    return lst



first_column = bunchobject.data[:,np.newaxis, 1 ]
print( five_number_summary(first_column) )

col_no = [ 0 , 1 , 2 ]
some_columns = bunchobject.data[:,col_no]
print( five_number_summary(some_columns) )

#%%
#question 3
def normalize_minmax1(data):

	for i in range(len(data[0])):
		true_min = np.min(data[:,i])
		true_max = np.max(data[:,i])
		for j in range(len(data[:,i])):
			data[:,i][j] = (data[:,i][j] - true_min) / (true_max - true_min)
	return data




#%%
#question 4
from sklearn.model_selection import train_test_split 
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np

bunchobject = datasets.load_breast_cancer()

def normalize_minmax(data):

	for i in range(len(data[0])):
		true_min = np.min(data[:,i])
		true_max = np.max(data[:,i])
		for j in range(len(data[:,i])):
			data[:,i][j] = (data[:,i][j] - true_min) / (true_max - true_min)
	return data

def get_metrics(actual_targets, predicted_targets, labels):            
    c_matrix = confusion_matrix(actual_targets, predicted_targets,labels)      
    output = {}      
    output["confusion matrix"] = c_matrix     
    
    record_count = 0      
    correct = 0      
    correctpositive = 0      
    correctnegative = 0      
    falsepositive = 0      
    falsenegative = 0      
    positivecount = 0      
    negativecount = 0 
    
    for i in range(len(predicted_targets)):          
        if predicted_targets[i] == actual_targets[i]:              
            if predicted_targets[i] == labels[1]:                  
                correctpositive += 1              
            elif predicted_targets[i] == labels[0]:                  
                correctnegative += 1          
        else:              
            if predicted_targets[i] == labels[1]:                  
                falsepositive += 1              
            elif predicted_targets[i] == labels[0]:                  
                falsenegative += 1            
        if actual_targets[i] == labels[1]:              
            positivecount += 1          
        elif actual_targets[i] == labels[0]:              
            negativecount += 1 
            
        record_count += 1   
        
    correct = correctpositive + correctnegative      
    accuracy = correct/record_count      
    sensitivity = correctpositive/positivecount      
    false_positive_rate = falsepositive/negativecount    
    
    output["confusion matrix"] = c_matrix      
    output["total records"] = record_count      
    output["accuracy"] = round(accuracy, 3)      
    output["sensitivity"] = round(sensitivity, 3)      
    output["false positive rate"] = round(false_positive_rate, 3)        
    return output


def knn_classifier(bunchobject, feature_list, size, seed, k): 
    
    
    data = bunchobject.data[:, feature_list]
    norm_data = normalize_minmax(data)
    target = bunchobject.target
    
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = size, random_state = seed)
    
    clf = neighbors.KNeighborsClassifier(k)
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(data_test)
    results = get_metrics(target_test, target_predicted, [0,1])
    return results 

#%%
#question 5
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split 
import numpy as np

bunchobject = datasets.load_breast_cancer()

def linear_regression(bunchobject, x_index, y_index, size, seed):
    data = bunchobject.data
    x = data[:, np.newaxis, x_index]
    y = data[:, np.newaxis, y_index]
    
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = size, random_state = seed)
    
    regr = linear_model.LinearRegression()
    
    regr.fit(x_train, y_train)
    
    y_predicted = regr.predict(x_test)
    
    mse = mean_squared_error(y_test, y_predicted)
    r2s = r2_score(y_test, y_predicted)
    
    results = {}
    results["coefficients"] = regr.coef_
    results["intercept"] = regr.intercept_
    results["mean squared error"] = mse
    results["r2 score"] = r2s
    
    return x_train, y_train, x_test, y_predicted, results

#%%
#question 6
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def multiple_linear_regression(bunchobject, x_index, y_index, order, size, seed):
    
    data = bunchobject.data
    x = data[:, np.newaxis, x_index]
    y = data[:, np.newaxis, y_index]
    
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = size, random_state = seed)
    
    poly = PolynomialFeatures(order, include_bias = False)
    x_train_poly = poly.fit_transform(x_train)
    x_test_poly = poly.fit_transform(x_test)
    
    
    regr = linear_model.LinearRegression()
    regr.fit(x_train_poly, y_train)
    
    y_predicted = regr.predict(x_test_poly)
    
    
    mse = mean_squared_error(y_test, y_predicted)
    r2s = r2_score(y_test, y_predicted)
    
    
    results = {}
    results['coefficients'] = regr.coef_
    results['intercept'] = regr.intercept_
    results['mean squared error'] = mse
    results['r2 score'] = r2s
    
    return x_train[:,0], y_train, x_test[:,0], y_predicted, results
    
        
#%%
#question 7
from sklearn.model_selection import train_test_split 
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np


bunchobject = datasets.load_breast_cancer()

def normalize_minmax(data):

	for i in range(len(data[0])):
		true_min = np.min(data[:,i])
		true_max = np.max(data[:,i])
		for j in range(len(data[:,i])):
			data[:,i][j] = (data[:,i][j] - true_min) / (true_max - true_min)
	return data

def get_metrics(actual_targets, predicted_targets, labels):            
    c_matrix = confusion_matrix(actual_targets, predicted_targets,labels)      
    output = {}      
    output["confusion matrix"] = c_matrix     
    
    record_count = 0      
    correct = 0      
    correctpositive = 0      
    correctnegative = 0      
    falsepositive = 0      
    falsenegative = 0      
    positivecount = 0      
    negativecount = 0 
    
    for i in range(len(predicted_targets)):          
        if predicted_targets[i] == actual_targets[i]:              
            if predicted_targets[i] == labels[1]:                  
                correctpositive += 1              
            elif predicted_targets[i] == labels[0]:                  
                correctnegative += 1          
        else:              
            if predicted_targets[i] == labels[1]:                  
                falsepositive += 1              
            elif predicted_targets[i] == labels[0]:                  
                falsenegative += 1            
        if actual_targets[i] == labels[1]:              
            positivecount += 1          
        elif actual_targets[i] == labels[0]:              
            negativecount += 1 
            
        record_count += 1   
        
    correct = correctpositive + correctnegative      
    accuracy = correct/record_count      
    sensitivity = correctpositive/positivecount      
    false_positive_rate = falsepositive/negativecount    
    
    output["confusion matrix"] = c_matrix      
    output["total records"] = record_count      
    output["accuracy"] = round(accuracy, 3)      
    output["sensitivity"] = round(sensitivity, 3)      
    output["false positive rate"] = round(false_positive_rate, 3)        
    return output


def knn_classifier_full(bunchobject, feature_list, size, seed): 
    
    data = bunchobject.data[:, feature_list]
    norm_data = normalize_minmax(data)
    
    target = bunchobject.target
    
    norm_data_train, norm_data_part2, target_train, target_part2 = train_test_split(norm_data, target, test_size = size, random_state = seed)
    norm_data_validation, norm_data_test, target_validation, target_test = train_test_split(norm_data_part2, target_part2, test_size = 0.5, random_state = seed)
    
    accuracy_data = [-1]
    for k in range(1,21):
        clf = neighbors.KNeighborsClassifier(k)
        clf.fit(norm_data_train, target_train)
        target_predicted = clf.predict(norm_data_validation)
        results = get_metrics(target_validation, target_predicted, [0,1])
        accuracy_data.append( results['accuracy'])
    
    best_accuracy = max(accuracy_data)
    best_k = accuracy_data.index(best_accuracy)
    
    clf_final = neighbors.KNeighborsClassifier(best_k)
    clf_final.fit(norm_data_train, target_train)
    predicted_valid = clf_final.predict(norm_data_validation)
    predicted_test = clf_final.predict(norm_data_test)
    metrics_valid = get_metrics(target_validation, predicted_valid, [0,1])
    metrics_test = get_metrics(target_test, predicted_test, [0,1])
    
    results = {}
    results['best k'] = best_k
    results['validation set'] = metrics_valid
    results['test set'] = metrics_test
    
    return results
























































