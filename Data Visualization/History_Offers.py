# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:10:36 2020

@author: outsi
"""

import os
import pandas as pd

print("data is loading...")
offers_data = pd.read_csv("offers.csv")
print("Data is loaded")

print("data is loading...")
history_data = pd.read_csv("trainHistory.csv")
print("Data is loaded")

merge_data=pd.merge(history_data,offers_data,on="offer")
merge_data.to_csv('merge_data.csv',index=False)
