# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:07:21 2020

@author: outsi
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import os
from sklearn.model_selection import StratifiedShuffleSplit,KFold
import pickle

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData")

def getDataset():
    if os.path.exists("Datasetcategory.csv"):
        print("Dataset found locally")
        df = pd.read_csv("Datasetcategory.csv")
        return df
    else:
        print("Dataset not found")
    
df = getDataset()    

cols = df.columns.tolist()
cols =cols[:9]+cols[12:]+cols[9:12]
print(cols)

df = df[cols]

df=df.drop(['id','Chain', 'Market', 'Category', 'Company', 'Brand', 'Quantity', 'Recency', 'Frequency','Offervalue'], axis=1)
df.head()
df.shape

print("loyalty:", df["Lable"].unique(), sep="\n")

def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)

df2, targets = encode_target(df, "Lable")
print("* df2.head()", df2[["Target", "Lable"]].head(),
      sep="\n", end="\n\n")
print("* df2.tail()", df2[["Target", "Lable"]].tail(),
      sep="\n", end="\n\n")
print("* targets", targets, sep="\n", end="\n\n")

df2.head()

print(df2.columns[:3])

features = list(df2.columns[:3])
print("* features:", features, sep="\n")


y = df2["Target"]
X = df2[features]


stratSplit = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
stratSplit.get_n_splits(X, y)
for train_idx, test_idx in stratSplit.split(X, y):
    X_train,X_test=X.iloc[train_idx],X.iloc[test_idx]
    y_train,y_test=y.iloc[train_idx],y.iloc[test_idx]
           


kf = KFold(n_splits=10)
kf.get_n_splits(X_train)
print(kf)
dt = DecisionTreeClassifier()
score=[]

for train_index, valid_index in kf.split(X_train):
     print("TRAIN:", train_index, "VALIDATION:", valid_index,"\n\n")
     Xv_train, X_valid = X_train.iloc[train_index], X_train.iloc[valid_index]
     yv_train, y_valid = y_train.iloc[train_index], y_train.iloc[valid_index]
     dt.fit(Xv_train, yv_train)
     yv_predict=dt.predict(X_valid)
     score.append(dt.score(X_valid, y_valid))
     print("Accuracy",score[-1])
     
finalScore=dt.score(X_test, y_test)
print(finalScore)
'''
Lst=[]
for i in range(2,7):
    for j in range(2,8):
        for k in range(370,525):
            tdf=pd.DataFrame({"R":[i],"F":[j],"M":[k]})
            if int(model.predict(tdf)[0])==2:
                Lst.append((i,j,k))
for i in range(3):
    print(Lst[random.randint(0,len(Lst))])
'''
#70-30
#0.6557808093895282
#80-20
#0.6576736210345813
os.chdir("D:\\Final project\\Program\\MLModel")
filename = 'finalized_model_with_80+20_split.sav'
pickle.dump(dt, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)