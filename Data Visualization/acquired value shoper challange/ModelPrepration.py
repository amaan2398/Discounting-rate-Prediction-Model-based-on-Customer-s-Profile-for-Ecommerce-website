# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:07:21 2020

@author: outsi
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import os

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData")

def getDataset():
    if os.path.exists("Datasetcategory.csv"):
        print("Dataset found locally")
        df = pd.read_csv("Datasetcategory.csv", index_col=0)
        return df
    else:
        print("Dataset not found")
    
df = getDataset()    

print("* iris types:", df["Name"].unique(), sep="\n")

def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)

df2, targets = encode_target(df, "Name")
print("* df2.head()", df2[["Target", "Name"]].head(),
      sep="\n", end="\n\n")
print("* df2.tail()", df2[["Target", "Name"]].tail(),
      sep="\n", end="\n\n")
print("* targets", targets, sep="\n", end="\n\n")

features = list(df2.columns[:4])
print("* features:", features, sep="\n")


y = df2["Target"]
X = df2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(X, y)