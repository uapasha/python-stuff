# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 11:22:40 2016

@author: uapasha
"""

def azureml_main(frame1):
  import pandas as pd
  import os.path
  import matplotlib
  matplotlib.use('agg')
  import numpy as np

  import matplotlib.pyplot as plt
  
  from pandas.tools.plotting import scatter_matrix
## Set a flag to define the environment
  Azure = False 

## If in Azure, the data frame is passed to the function,
## If running in the IDE, load it from a local file
  if(Azure == False):
    pathName = "D://Pavlo\My Files\YaDisk\YandexDisk\DS&ML\Kyivstar\Task"
    fileName = "Train.csv"
    filePath = os.path.join(pathName, fileName)
    frame1 = pd.read_csv(filePath, sep = ";", decimal = ",")
    
   ## df = frame1.apply(pd.to_numeric, args=('coerce',))    
    
   ## frame1["V9"] = frame1["V9"].astype(float) 
    

## Gonvert gender to category 
    frame1["Gender"] = frame1["Gender"].astype('category')
    frame1["V3"] = frame1["V3"].astype('category')
## Remove unwanted columns
    frame1.drop(["subs_id",], axis = 1, inplace = True)
    ##frame1.drop(["V14", "V31", "V3", "V28", "V27", "V30", "V4", "V15", "V25", "V10"], axis = 1, inplace = True)
## Filter out outliers
    frame1 = frame1[(frame1["V20"] < 48.0) ]
    ##(frame1["V28"]<400.0)]
## Create a scatter plot matrix
        
    
    fig1 = plt.figure(1, figsize = (20,20))
    ax = fig1.gca()
    scatter_matrix(frame1, alpha=0.2, figsize=(20, 20), diagonal='kde', ax=ax)
    fig1.savefig('scatter2.png')    
    
    
    ## Create a series of bar plots for the various levels of the
    ## non-numeric columns in the data frame by Gender.
    names = list(frame1)
    num_cols = frame1.shape[1]
    for indx in range(num_cols - 1):
        if(frame1.ix[:, indx].dtype not in [np.int64, np.int32, np.float64]):
            temp1 = frame1.ix[frame1.Gender == 'Male', indx].value_counts()
            temp0 = frame1.ix[frame1.Gender == 'Female', indx].value_counts()
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            ax1 = fig.add_subplot(1, 2, 1)
            ax0 = fig.add_subplot(1, 2, 2)
            temp1.plot(kind = 'bar', ax = ax1)
            ax1.set_title('Values of ' + names[indx] + '\n for Male')
            temp0.plot(kind = 'bar', ax = ax0)
            ax0.set_title('Values of ' + names[indx] + '\n for Female')
            ##if(Azure == True): fig.savefig('bar_' + names[indx] + '.png')    
    
    ## Now make some box plots of the columbns with numerical values.
    for indx in range(num_cols):
        if(frame1.ix[:, indx].dtype in [np.int64, np.int32, np.float64]):
            temp1 = frame1.ix[frame1.Gender == 'Male', indx]
            temp0 = frame1.ix[frame1.Gender == 'Female', indx]
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            ax1 = fig.add_subplot(1, 2, 1)
            ax0 = fig.add_subplot(1, 2, 2)
            ax1.boxplot(temp1.as_matrix())
            ax1.set_title('Box plot of ' + names[indx] + '\n for Male')
            ax0.boxplot(temp0.as_matrix())
            ax0.set_title('Box plot of ' + names[indx] + '\n for Female')
    
    
## Select a subset of columns
  frame1 = frame1[["Year", "Month", "Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod"]]

## Filter and add a column to show totals for August
  frame1 = frame1[frame1['Month']=='Aug']
  frame1["Total.Prod"] = frame1["Cottagecheese.Prod"] + frame1["Icecream.Prod"] + frame1["Milk.Prod"]
  return frame1
