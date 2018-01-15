# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 08:47:11 2018

@author: ayarapat
"""

#importing the respective packages
import pandas as pd
import os
# reading the Titanic Data set.
os.chdir('D:/Datascience/Practicals/inputFiles')
titanic_train=pd.read_csv('Titanic_Train.csv')
titanic_train.shape
titanic_train.info()
print(titanic_train.groupby(['Survived']).size())
#get only survived column from CSV file.

columns =['Survived']

Survived_csv=titanic_train.loc[:,columns]
Survived_csv.shape
Survived_csv.info()
print(Survived_csv.groupby(columns).size())

#read the test_CSV file from kaggle site

titanic_test=pd.read_csv('Titanic_Test.csv')
titanic_test.shape
titanic_test.info()

titanic_test['Survived']=0
titanic_test.to_csv('submission.csv', columns=['PassengerId','Survived'],index=False)