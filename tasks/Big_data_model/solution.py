# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 17:55:31 2016

@author: uapasha
"""
import pandas as pd
import os.path
import matplotlib
matplotlib.use('agg')
#import matplotlib.pyplot as plt # used in acalisys - now commented
#from pandas.tools.plotting import scatter_matrix # used in acalisys - now commented
#import numpy as np # used in acalisys - now commented
#from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.ensemble import GradientBoostingClassifier

###############################################################################
###############################################################################
## Define helpers functions
    
def hex_to_int(x):
    """
    Converts hex to ints
    """
    try:
        return int(x, 16)
    except ValueError:
        return float('nan')    

def apply_transform(frame1):
    """
    Converts data to acceptable format and deals with residual data in
    training dataset
    """
    ## Replace comas for dots to understand float values
    frame1 = frame1.replace({",":"."}, regex = True)
    
    ##Clear some residual data    
    frame1 = frame1.dropna(subset=["V6"])  
    convert_cols = range(9,33)

    for i in convert_cols:
        frame1["V"+str(i)] = pd.to_numeric(frame1["V"+str(i)], errors='coerce')
    frame1 = frame1[(frame1["V20"] < 48.0) & \
        (frame1["V28"]<400.0)] # & (frame1["V32"]<130.0)] & \
        #        (frame1["V9"]<600.0) & \
        #       (frame1["V10"]<1000.0)]

    ## Convert hex to int  
    frame1["V7"] = frame1["V7"].apply(hex_to_int)
    frame1["V8"] = frame1["V8"].apply(hex_to_int)
    
    ## Drop Unused column
    columns_to_drop = ["subs_id"]
    
    ## Define and drop columns with least feature importance
    frame1.drop(columns_to_drop, axis = 1, inplace = True) 
    columns = ['V1',
                #'V2',
                #'V3',
                #'V4',
                #'V5',
               'V6',
                #'V7',
                #'V8',
                'V9',
                #'V10',
               'V11',
                'V12',
                #'V13',
               'V14',
                #'V15',
               'V16',
               'V17',
               'V18',
               'V19',
                #'V20',
               'V21',
               'V22',
                'V23',
               'V24',
               'V25',
                #'V26',
               'V27',
               #'V28',
                #'V29',
                #'V30',
               'V31',
                #'V32',
               "Gender"]         
    
    ## Apply additional transformation necessary to do sklearn           
    tdata = frame1.copy()
    tdata["V1"] = pd.to_datetime(tdata["V1"], errors='coerce')
    tdata["V2"] = pd.to_datetime(tdata["V2"], errors='coerce')
    tdata["V6"] = pd.to_datetime(tdata["V6"], errors='coerce')
    tdata["V1"] = pd.to_numeric(tdata["V1"], errors='coerce')
    tdata["V2"] = pd.to_numeric(tdata["V2"], errors='coerce')
    tdata["V6"] = pd.to_numeric(tdata["V6"], errors='coerce')
    tdata = tdata[columns]
    
    ## Deal with NaN data
    tdata = tdata.dropna(how="all")
    tdata = tdata.fillna(0)

    
    ## return tansformed dataset    
    return tdata

def apply_test_transform(dtest):
    """
    Converts data to acceptable format and deals with residual data in
    test dataset
    """
    ## Replace comas for dots to understand float values
    dtest = dtest.replace({",":"."}, regex = True)
    
    ##Clear some residual data 
    convert_cols = range(9,33)
    for i in convert_cols:
        dtest["V"+str(i)] = pd.to_numeric(dtest["V"+str(i)], errors='coerce')
    
    ## Convert hex to int  
    dtest["V7"] = frame1["V7"].apply(hex_to_int)
    dtest["V8"] = frame1["V8"].apply(hex_to_int)
    
    ## Drop Unused column
    columns_to_drop = ["subs_id"]
    
    ## Define and drop columns with least feature importance
    dtest.drop(columns_to_drop, axis = 1, inplace = True) 
    columns = ['V1',
                #'V2',
                #'V3',
                #'V4',
                #'V5',
               'V6',
                #'V7',
                #'V8',
                'V9',
                #'V10',
               'V11',
                'V12',
                #'V13',
               'V14',
                #'V15',
               'V16',
               'V17',
               'V18',
               'V19',
                #'V20',
               'V21',
               'V22',
                'V23',
               'V24',
               'V25',
                #'V26',
               'V27',
               #'V28',
                #'V29',
                #'V30',
               'V31',
                #'V32',
               ]      
    ## Apply additional transformation necessary to do sklearn          
    tdata = dtest.copy()
    tdata["V1"] = pd.to_datetime(tdata["V1"], errors='coerce')
    tdata["V2"] = pd.to_datetime(tdata["V2"], errors='coerce')
    tdata["V6"] = pd.to_datetime(tdata["V6"], errors='coerce')
    tdata["V1"] = pd.to_numeric(tdata["V1"], errors='coerce')
    tdata["V2"] = pd.to_numeric(tdata["V2"], errors='coerce')
    tdata["V6"] = pd.to_numeric(tdata["V6"], errors='coerce')
    tdata = tdata[columns]
    
    ## Deal with NaN data
    tdata = tdata.fillna(0)
    
    ## return tansformed dataset
    return tdata
###############################################################################
###############################################################################
## Load training data set

pathName = "D:\Pavlo\My Files\YaDisk\YandexDisk\DS&ML\Kyivstar"
fileName = "Train.csv"
filePath = os.path.join(pathName, fileName)
frame1 = pd.read_csv(filePath, sep = ";", decimal = ",")



###############################################################################
## Analise data
   
#    ## Create a scatter plot matrix to analyize dataset
#fig1 = plt.figure(1, figsize = (20,20))
#ax = fig1.gca()
#scatter_matrix(frame1, alpha=0.2, figsize=(20, 20), diagonal='kde', ax=ax)
#
#
#
# ## Create a series of bar plots for the various levels of the
# ## non-numeric columns in the data frame by Gender.
#names = list(frame1)
#num_cols = frame1.shape[1]
#for indx in range(num_cols - 1):
#    if(frame1.ix[:, indx].dtype in [np.int64, np.int32, np.float64]):
#        temp1 = frame1.ix[frame1.Gender == 'Male', indx].value_counts()
#        temp0 = frame1.ix[frame1.Gender == 'Female', indx].value_counts()
#        
#        fig = plt.figure(figsize = (12,6))
#        fig.clf()
#        ax1 = fig.add_subplot(1, 2, 1)
#        ax0 = fig.add_subplot(1, 2, 2)
#        temp1.plot(kind = 'bar', ax = ax1)
#        ax1.set_title('Values of ' + names[indx] + '\n for Male')
#        temp0.plot(kind = 'bar', ax = ax0)
#        ax0.set_title('Values of ' + names[indx] + '\n for Female')
#    
#    ## Now make some box plots of the columns with numerical values.
#for indx in range(num_cols):
#    if(frame1.ix[:, indx].dtype in [np.int64, np.int32, np.float64]):
#        temp1 = frame1.ix[frame1.Gender == 'Male', indx]
#        temp0 = frame1.ix[frame1.Gender == 'Female', indx]
#        fig = plt.figure(figsize = (12,6))
#        fig.clf()
#        ax1 = fig.add_subplot(1, 2, 1)
#        ax0 = fig.add_subplot(1, 2, 2)
#        ax1.boxplot(temp1.as_matrix())
#        ax1.set_title('Box plot of ' + names[indx] + '\n for Male')
#        ax0.boxplot(temp0.as_matrix())
#        ax0.set_title('Box plot of ' + names[indx] + '\n for Female')
###############################################################################

## Transform dataset           
tdata = apply_transform(frame1)

## Create copy for parametrical value
pdata = tdata.copy()

## Create datasets for sklearn fit
tdata.drop(["Gender"], axis = 1, inplace = True) 
data, param = shuffle(tdata, pdata.Gender, random_state=13)
offset = int(data.shape[0] * 0.7)
data_train, param_train = data[:offset], param[:offset]
data_test, param_test = data[offset:], param[offset:]

###############################################################################
# Fit classification model

clf = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1,
                                 max_depth=1, random_state=0, 
                                 max_leaf_nodes=2).fit(data_train,
                                param_train)

clf.fit(data_train, param_train)

## Analyze result
clf.score(data_test, param_test) 

clf.feature_importances_ 

###############################################################################
## Predict values

## Open test file
pathName = "D://Pavlo\My Files\YaDisk\YandexDisk\DS&ML\Kyivstar\Task"
fileName = "Test.csv"
filePath = os.path.join(pathName, fileName)
dtest = pd.read_csv(filePath, sep = ";", decimal = ",")

## Transform dataset      
tdata = apply_test_transform(dtest)

## Predict values
result = clf.predict_proba(tdata)

result = pd.DataFrame(result[:,0], columns = ["prob"])

## Create dataset with consumers ID
headers = dtest["subs_id"].copy()
headers = headers.to_frame()

## Join IDs with predictions
headers = headers.join(result, how = "outer")

## write output file
headers.to_csv("./PaulBrunko.csv", sep = ";", index = False)
    
