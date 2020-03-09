# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:00:41 2020

@author: outsi
"""
import os
import pandas as pd

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\trainHistory")
dfTH = pd.read_csv("trainHistory.csv")

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\offers")
dfO = pd.read_csv("offers.csv")


df_tHistory_offer= pd.merge(dfTH,dfO,left_on='offer',right_on='offer')

df_tHistory_offer.to_csv(r'D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\meargeOFF&HISTo\\histwithOff.csv', index = False)




