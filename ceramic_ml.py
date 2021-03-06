# -*- coding: utf-8 -*-
"""ceramic_ml.ipynb

Prediction of surface roughness for abrasive waterjet milling of alumina ceramic
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.svm import SVR

#loading the dataset
df = pd.DataFrame(pd.read_csv("/content/ceramic.csv"))

import seaborn as sns
# calculate correlation matrix
corr = df.corr()# plot the heatmap
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))

#data visualisation
sns.pairplot(df)

#extracting output feature
Y = df["Ra"]

#extracting input features
df.drop(["Ra"],axis=1)

from sklearn.model_selection import GridSearchCV

#hyperparameter tuning using GridSearchCV

clf = GridSearchCV(SVR(gamma='scale'), {
    'C': [1,5,10],
    'kernel': ['linear', 'rbf', 'sigmoid']},cv=5)

clf.fit(df,Y)
dfr = pd.DataFrame(clf.cv_results_)
dfr

clf2 = GridSearchCV(SVR(gamma='scale'), {
    'C': [0.1, 10, 100],
    'kernel': ['linear']},cv=5)

clf2.fit(df,Y)
dfr2 = pd.DataFrame(clf2.cv_results_)
dfr2

from sklearn.model_selection import train_test_split

import pandas as pd

#splitting data

X_train, X_test, Y_train, Y_test = train_test_split(df, Y, test_size = 0.33, random_state = 0)

from sklearn.svm import SVR

#fitting data

regressor = SVR(kernel = 'linear', C = 1)
regressor.fit(X_train, Y_train)

#making predictions

Y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error

# Calculating mean squared error 

mean_squared_error(Y_test, Y_pred)
