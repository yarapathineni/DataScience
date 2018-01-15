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
print(titanic_train.groupby(['Sex','Survived']).size())
print(titanic_train.groupby(['Pclass','Survived']).size())
print(titanic_train.groupby(['Sex','Pclass','Survived']).size())
print(titanic_train.groupby(['Embarked','Survived']).size())
print(titanic_train.groupby(['Sex','Embarked','Survived']).size())

titanic_test=pd.read_csv('Titanic_Test.csv')
titanic_test.shape
titanic_test.info()
titanic_test['Survived'] = 0

titanic_test.loc[((titanic_test['Sex']=='female') & ((titanic_test['Pclass']==1) | (titanic_test['Pclass']==2)) & ((titanic_test['Embarked']=='C') | (titanic_test['Embarked']=='Q'))), 'Survived'] = 1
#titanic_test.loc[titanic_test.Sex=='male','Survived'] = 0
titanic_test.to_csv('submission.csv', columns=['PassengerId','Survived'],index=False)