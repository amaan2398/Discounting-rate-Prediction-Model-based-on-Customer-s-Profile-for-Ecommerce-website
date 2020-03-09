# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:38:39 2020

@author: outsi
"""

# =============================================================================
# 1) What percentage of customers who are repeat purchasers as per the analysis from transactions.csv have availed the offers
# =============================================================================

# =============================================================================
# 2) Find the categories , most number of offers are given
# =============================================================================

import os
import pandas as pd

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\offers")
offers_data = pd.read_csv("offers.csv", usecols = ['category', 'offer'])
print("Data is loaded")

print("Data info")
offers_data.info()
    
print("Data Size")
offers_data.size
    
print("Data Shape")
offers_data.shape
    
print("Data Containg Null values count by columns")
print(offers_data.isnull().sum())

f=open("CategoryRespectiveCountOfOffer.csv","w")

f.write("category,countOffer\n")

offerC=0

for i,t_df in offers_data.groupby(['category']):
    count = len(t_df.offer.unique())
    if offerC < count:
        categoryM=i
        offerC=count        
    f.write(str(i)+","+str(count)+"\n")

print(categoryM,offerC)

# =============================================================================
# 3) Find the brands , most number of offers are given
# =============================================================================

import os
import pandas as pd

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\offers")
offers_data = pd.read_csv("offers.csv", usecols = ['brand', 'offer'])
print("Data is loaded")

print("Data info")
offers_data.info()
    
print("Data Size")
offers_data.size
    
print("Data Shape")
offers_data.shape
    
print("Data Containg Null values count by columns")
print(offers_data.isnull().sum())

f=open("BrandRespectiveCountOfOffer.csv","w")

f.write("brand,countOffer\n")

offerC=0

for i,t_df in offers_data.groupby(['category']):
    count = len(t_df.offer.unique())
    if offerC < count:
        brandM=i
        offerC=count        
    f.write(str(i)+","+str(count)+"\n")

print(brandM,offerC)

# =============================================================================
# 4) Are the customers who mostly avail the offer from a specific market area?
# =============================================================================

import os
import pandas as pd

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\trainHistory")
offers_data = pd.read_csv("trainHistory.csv", usecols = ['market'])
print("Data is loaded")

from collections import defaultdict

dic=defaultdict(int)

for i,t_df in offers_data.groupby(['market']):
    dic[i]=len(t_df)

print(dic)

#output = 
    

# =============================================================================
# 5) Do customers avail the offer or repeat purchases at same chain? What percentage?
# =============================================================================

import os
import pandas as pd

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\trainHistory")
offers_data = pd.read_csv("trainHistory.csv", usecols = ['id','market', 'offer'])
print("Data is loaded")



# =============================================================================
# 6) Do customers avail the offer or repeat purchases at different chain? What percentage?
# =============================================================================



