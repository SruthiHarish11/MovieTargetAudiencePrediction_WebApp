# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:36:31 2020

@author: Sruthi Harish
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import warnings

warnings.filterwarnings("ignore")
dataset = pd.read_csv('moviedataset.csv',encoding= 'unicode_escape')
print(dataset.head(180))

X=dataset.iloc[:,1:27].values
y=dataset.iloc[:,27].values

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy="most_frequent")

imputer=imputer.fit(X[:,0:27])
X[:,0:27]=imputer.transform(X[:,0:27])
from sklearn.preprocessing import LabelEncoder
le_y=LabelEncoder()
y=le_y.fit_transform(y)
le_X0=LabelEncoder()
le_X1=LabelEncoder()
le_X2=LabelEncoder()
le_X3=LabelEncoder()
le_X4=LabelEncoder()
le_X5=LabelEncoder()
le_X6=LabelEncoder()
le_X7=LabelEncoder()
le_X8=LabelEncoder()
le_X9=LabelEncoder()
le_X10=LabelEncoder()
le_X11=LabelEncoder()
le_X12=LabelEncoder()
le_X13=LabelEncoder()
le_X14=LabelEncoder()
le_X15=LabelEncoder()
le_X16=LabelEncoder()
le_X17=LabelEncoder()
le_X18=LabelEncoder()
le_X19=LabelEncoder()
le_X20=LabelEncoder()
le_X21=LabelEncoder()
le_X22=LabelEncoder()
le_X23=LabelEncoder()
le_X24=LabelEncoder()
le_X25=LabelEncoder()
#for i in range(0,26):
X[:,0]=le_X0.fit_transform(X[:,0])
X[:,1]=le_X1.fit_transform(X[:,1])
X[:,2]=le_X2.fit_transform(X[:,2])
X[:,3]=le_X3.fit_transform(X[:,3])
X[:,4]=le_X4.fit_transform(X[:,4])
X[:,5]=le_X5.fit_transform(X[:,5])
X[:,6]=le_X6.fit_transform(X[:,6])
X[:,7]=le_X7.fit_transform(X[:,7])
X[:,8]=le_X8.fit_transform(X[:,8])
X[:,9]=le_X9.fit_transform(X[:,9])
X[:,10]=le_X10.fit_transform(X[:,10])
X[:,11]=le_X11.fit_transform(X[:,11])
X[:,12]=le_X12.fit_transform(X[:,12])
X[:,13]=le_X13.fit_transform(X[:,13])
X[:,14]=le_X14.fit_transform(X[:,14])
X[:,15]=le_X15.fit_transform(X[:,15])
X[:,16]=le_X16.fit_transform(X[:,16])
X[:,17]=le_X17.fit_transform(X[:,17])
X[:,18]=le_X18.fit_transform(X[:,18])
X[:,19]=le_X19.fit_transform(X[:,19])
X[:,20]=le_X20.fit_transform(X[:,20])
X[:,21]=le_X21.fit_transform(X[:,21])
X[:,22]=le_X22.fit_transform(X[:,22])
X[:,23]=le_X23.fit_transform(X[:,23])
X[:,24]=le_X24.fit_transform(X[:,24])
X[:,25]=le_X25.fit_transform(X[:,25])
#print(le_y.classes_)  
#print(le_X0.classes_)

le_name_mapping = dict(zip(le_X0.classes_, le_X0.transform(le_X0.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X1.classes_, le_X1.transform(le_X1.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X2.classes_, le_X2.transform(le_X2.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X3.classes_, le_X3.transform(le_X3.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X4.classes_, le_X4.transform(le_X4.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X5.classes_, le_X5.transform(le_X5.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X6.classes_, le_X6.transform(le_X6.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X7.classes_, le_X7.transform(le_X7.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X8.classes_, le_X8.transform(le_X8.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X9.classes_, le_X9.transform(le_X9.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X10.classes_, le_X10.transform(le_X10.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X11.classes_, le_X11.transform(le_X11.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X12.classes_, le_X12.transform(le_X12.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X13.classes_, le_X13.transform(le_X13.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X14.classes_, le_X14.transform(le_X14.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X15.classes_, le_X15.transform(le_X15.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X16.classes_, le_X16.transform(le_X16.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X17.classes_, le_X17.transform(le_X17.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X18.classes_, le_X18.transform(le_X18.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X19.classes_, le_X19.transform(le_X19.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X20.classes_, le_X20.transform(le_X20.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X21.classes_, le_X21.transform(le_X21.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X22.classes_, le_X22.transform(le_X22.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X23.classes_, le_X23.transform(le_X23.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X24.classes_, le_X24.transform(le_X24.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_X25.classes_, le_X25.transform(le_X25.classes_)))
print(le_name_mapping)

le_name_mapping = dict(zip(le_y.classes_, le_y.transform(le_y.classes_)))
print(le_name_mapping)



from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=10)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, criterion="gini",random_state=0)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)
print(score)

pickle.dump(classifier,open('model_one.pkl','wb'))
model_one=pickle.load(open('model_one.pkl','rb'))

