# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:57:48 2016

@author: uapasha
"""

def azureml_main(frame1):
    import pandas as pd
    import os.path

## set a flag to detarmine the environment
    Azure = False
    
##if in azure, the data frame is passed to the function
## if in IDE - load data from the local file
    if (Azure == False):
        pathName = "D:\Pavlo\My Files\YaDisk\YandexDisk\DS&ML\MicrosoftLearning-Data-Science-and-ML-Essentials-7d2500a\Labs\Labfiles\Lab02B"
        fileName = "cadairydata.csv"
        filePath = os.path.join(pathName, fileName)
        frame1 = pd.read_csv(filePath)
## select a subset of columns
    frame1 = frame1[["Year", "Month", "Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod"]]
## filter and add a column to show totals for august
    frame1 = frame1[frame1['Month']=="Aug"]
    frame1["Total.Prod"] = frame1["Cottagecheese.Prod"] + frame1 ["Icecream.Prod"] + frame1["Milk.Prod"]
    
    return frame1
       