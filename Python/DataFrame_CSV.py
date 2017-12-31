# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:58:45 2017

@author: ayarapat
"""

import pandas as pd
import numpy as np
import os

cols =['PassengerId','Survived','Pclass',	'Name','Sex']
print(os.getcwd())

os.chdir("D:/Datascience/Python")
np.abs(11);
csvDF = pd.read_csv("train.csv")
print(csvDF.shape)
print(csvDF.info())

# print first row of all columns
# here 0, defines the number of rows and : after defining the columns .. nothing specified.. so all
# columns will print..

df1 =csvDF.loc[0,: ]
print(df1)

'''
print(df1)
PassengerId                          1
Survived                             0
Pclass                               3
Name           Braund, Mr. Owen Harris
Sex                               male
Age                                 22
SibSp                                1
Parch                                0
Ticket                       A/5 21171
Fare                              7.25
Cabin                              NaN
Embarked                             S
Name: 0, dtype: object
'''

df1.shape
df1.info()
print(df1)

print(csvDF.loc[0:4,:cols])

# rows allways inclusive with start and end index.

print(csvDF.loc[0:4,['PassengerId','Survived','Pclass','Sex']])

# here, 0:4 --> denotes the number of rows.
# After , denotes the list of columns  you want to retrive.
#the output is as follows.
'''
   PassengerId  Survived  Pclass     Sex
0            1         0       3    male
1            2         1       1  female
2            3         1       3  female
3            4         1       1  female
4            5         0       3    male
'''

print(csvDF.loc[0:4,'PassengerId':'Sex'])
# another way of doing it instead of specifies all the columns.
# not working .. need to check how to pass more than one column
dfCond=csvDF.loc[(csvDF.Sex=='male' & str(csvDF.PassengerId)=='1') ,:]
print(csvDF.iloc[:,0:4])

# loc for labels..
#iloc is index based or integer side.

