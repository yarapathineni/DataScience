# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:01:02 2018

@author: ayarapat
"""

import pandas as pd
import os
from sklearn import tree
import pydot
import io

# reading the Titanic Data set.
os.chdir('D:/Datascience/Practicals/inputFiles')
titanic_train=pd.read_csv('Titanic_Train.csv')
titanic_train.shape
titanic_train.info()

#build the features
features = ['Pclass']
tartget=['Survived']

X_train = titanic_train[features]
Y_train =titanic_train[tartget]

dt_estimator = tree.DecisionTreeClassifier()
dt_estimator.fit(X_train,Y_train)

#visualize the deciion tree

#visualize the deciion tree
dot_data = io.StringIO() 
tree.export_graphviz(dt_estimator, out_file = dot_data, feature_names = X_train.columns)
graph = pydot.graph_from_dot_data(dot_data.getvalue())[0] 
graph.write_pdf("decision-tree.pdf")

titanic_test = pd.read_csv('titanic_test.csv')
titanic_test.shape
titanic_test.info()

X_test = titanic_test[features]
titanic_test['Survived'] = dt_estimator.predict(X_test)
titanic_test.to_csv('submission.csv', columns=['PassengerId','Survived'],index=False)