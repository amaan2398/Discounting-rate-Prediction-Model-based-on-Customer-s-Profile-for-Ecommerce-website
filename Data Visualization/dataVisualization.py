# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 09:25:11 2019

@author: outsi
"""

# =============================================================================
# 1)WHAT IS THE PERCENTAGE OF CUSTOMERS WHO DID MULTIPLE TRANSACTIONS  ON SAME DEPARTMENT
# =============================================================================

import os
import pandas as pd

listP=[]

for _ in range(12):
    print("data is loading...")
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(_)+".csv", usecols = ['id', 'dept'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Departments")
    deptU = transactions_data.dept.unique()
    deptU.sort()#48 52 61 66 68 76 77 80 83 84 85 86 87 88 89 90 93 this dept 
                #are not present in dataframe
    print(deptU)
    
    for i in deptU:
        T=len(transactions_data.loc[ transactions_data['dept'] == i ])
        U=len(transactions_data.loc[ transactions_data['dept'] == i ].id.unique())
        if T != 0:
            listP.append((T - U) / T)

print(str((sum(listP)/len(listP))*100)+"%")

#Answer = 85.42342560231249%

# index = np.arange(len(deptU[:10]))
# plt.bar(index , listP[:10])
# plt.xticks(index, deptU[:10], rotation=90)
# plt.show()

# df = pd.DataFrame({'percentage':listP, 'index':deptU})
# ax = df.plot.bar(x='index',y='percentage',rot= 90, figsize = (84 , 10))


# =============================================================================
# 2)What is the percentage of customers who did multiple transactions  on different department
# =============================================================================

import os
import pandas as pd

listP=[]

for _ in range(12):
    print("data is loading...")
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(_)+".csv",usecols = ['id' , 'dept'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    for i,t_df in transactions_data.groupby(['id']):
        if len(t_df)>1:
            listP.append(len(t_df.dept.unique())/len(t_df.dept))


print("Answer "+str((sum(listP)/len(listP))*100)+"%")

#Answer = 9.149506577152058%

# T=len(transactions_data.id)
# U=len(transactions_data.id.unique())
# prct = ((T - U) / T)
# print(prct)
# df = pd.DataFrame({ 'percentage' : [ prct ] })
# ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))

# print("Total multiple transactions  on different department is: "+str(mdv))
# print("Total transactions are: "+str(total))

# df = pd.DataFrame({ 'percentage' : [ mdv ] })
# ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))

# =============================================================================
# 3)What is the percentage of customers who did multiple transactions  on same category
# =============================================================================

import os
import pandas as pd

listP=[]

for _ in range(12):
    print("data is loading...")
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(_)+".csv",usecols = ['id' , 'category'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Category")
    categoryU = transactions_data.category.unique()
    categoryU.sort()# this dept are not present in dataframe
    #print(categoryU)
    
    for i in categoryU:
        T = len(transactions_data.loc[ transactions_data['category'] == i ])
        U = len(transactions_data.loc[ transactions_data['category'] == i ].id.unique())
        if T != 0:
            listP.append((T - U)/ T)

print(str((sum(listP)/len(listP))*100)+"%")

#Answer = 63.33137851495142%


# df = pd.DataFrame({'percentage':listP, 'index':categoryU})
# ax = df.plot.scatter(x='index',y='percentage',rot= 90, figsize = (50 , 10))


# =============================================================================
# 4)What is the percentage of customers who did multiple transactions  on different category
# =============================================================================
import os
import pandas as pd

listP=[]

for _ in range(12):
    print("data is loading...")
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(_)+".csv",usecols = ['id' , 'category'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())

    for i,t_df in transactions_data.groupby(['id']):
        if len(t_df)>1:
            x=len(t_df.category.unique())
            y=len(t_df.category)
            listP.append(x/y)

print(str((sum(listP)/len(listP))*100)+"%")

#Answer = 25.350171455595888%

# T=len(transactions_data.id)
# U=len(transactions_data['id'].append(transactions_data['category']).unique())
# prct = ((T - U) / T)
# print(prct)
# df = pd.DataFrame({ 'percentage' : [ prct ] })
# ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))
# g = transactions_data.groupby(['id','category'])

# for i,id_df in g:
    




# =============================================================================
# 5)What is the percentage of customers who did multiple transactions
# =============================================================================
import os
import pandas as pd

listP=[]

for _ in range(12):
    print("data is loading...")
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(_)+".csv",usecols = ['id'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    T=len(transactions_data.id)
    U=len(transactions_data.id.unique())
    if T != 0:
        listP.append((T - U) / T)

print(str((sum(listP)/len(listP))*100)+"%")

#Answer = 98.77404918992964%

# print(prct)
# df = pd.DataFrame({ 'percentage' : [ prct ] })
# ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))

# =============================================================================
# 6)Do customers change brand while repeat purchasing in same product category, what percentage?
# =============================================================================

import os
import pandas as pd

for i in range(11):
    print("data is loading...",i)
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(i)+".csv",usecols = ['id','category','brand'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Unique depertments...")
    print(len(transactions_data.brand.unique()))
    
    print("Created an csv for data id and change brand over same Category")
    f=open("id_changBrandOverSamCategory"+str(i)+".csv","w")
    
    f.write("id,changBrandOverSamCategory\n")
    
    for i,t_df_id in transactions_data.groupby(['id']):
        countY=0
        countN=0
        for j,t_df_cat in t_df_id.groupby(['category']):
            if len(t_df_cat.brand.unique())>1:
                countY+=1
            else:
                countN+=1
        if countY > 0 and countN > 0:
            if countY > countN:
                f.write(str(i)+",Y\n")
            elif countY < countN:
                f.write(str(i)+",N\n")
            elif countY == countN:
                f.write(str(i)+",C\n")
    
    f.close()
    print("t",str(i),"is done!")

import os
import pandas as pd
from collections import defaultdict

dic=defaultdict(int)

for _ in range(11):
    print("data is loading...",_)
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("id_changBrandOverSamCategory"+str(_)+".csv",usecols = ['id','changBrandOverSamCategory'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Data Converstion")
    transactions_data["changBrandOverSamCategory"]=transactions_data.changBrandOverSamCategory.astype("category")
    
    print("Data info")
    transactions_data.info()
    
    for i,d_df in transactions_data.groupby(["changBrandOverSamCategory"]):
        dic[i]+=len(d_df)

total=dic["C"]
total+=dic["N"]
total+=dic["Y"]

print("for Y ")
print(str((dic["Y"]/total)*100)+"%")

#Answer = 81.51444008490384%

print("for N ")
print(str((dic["N"]/total)*100)+"%")

#Answer = 16.620248279410816%

print("for C ")
print(str((dic["C"]/total)*100)+"%")

#Answer = 1.8653116356853412%


f=open("id_changBrandOverSamCategory.csv","w")

fl=True

for _ in range(11):
    f1=open("id_changBrandOverSamCategory"+str(_)+".csv","r")
    line = f1.readline()
    while line:
        if fl:
            f.write(line)
            fl=False
        else:
            if line != "id,changBrandOverSamCategory\n":
                f.write(line)
        line = f1.readline()
    f1.close()

f.close()
    
# =============================================================================
# 7) Do customers change Company while repeat purchasing in same product category, what percentage?
# =============================================================================

import os
import pandas as pd

for i in range(11):
    print("data is loading...",i)
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(i)+".csv",usecols = ['id','category','company'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Unique depertments...")
    print(len(transactions_data.company.unique()))
    
    print("Created an csv for data id and change brand over same Category")
    f=open("id_changCompanyOverSamCategory123"+str(i)+".csv","w")
    
    f.write("id,changCompanyOverSamCategory\n")
    
    for i,t_df_id in transactions_data.groupby(['id']):
        countY=0
        countN=0
        for j,t_df_cat in t_df_id.groupby(['category']):
            if len(t_df_cat.company.unique())>1:
                countY+=1
            else:
                countN+=1
        if countY > 0 and countN > 0:
            if countY > countN:
                f.write(str(i)+",Y\n")
            elif countY < countN:
                f.write(str(i)+",N\n")
            elif countY == countN:
                f.write(str(i)+",C\n")
    
    f.close()
    print("t",str(i),"is done!")

import os
import pandas as pd
from collections import defaultdict

dic=defaultdict(int)

for _ in range(11):
    print("data is loading...",_)
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("id_changCompanyOverSamCategory"+str(_)+".csv",usecols = ['id','changCompanyOverSamCategory'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Data Converstion")
    transactions_data["changCompanyOverSamCategory"]=transactions_data.changCompanyOverSamCategory.astype("category")
    
    print("Data info")
    transactions_data.info()
    
    for i,d_df in transactions_data.groupby(["changCompanyOverSamCategory"]):
        dic[i]+=len(d_df)

total=dic["C"]
total+=dic["N"]
total+=dic["Y"]

print("for Y ")
print(str((dic["Y"]/total)*100)+"%")

#Answer = 4.968776414703207%

print("for N ")
print(str((dic["N"]/total)*100)+"%")

#Answer = 94.80978199734528%

print("for C ")
print(str((dic["C"]/total)*100)+"%")

#Answer = 0.22144158795152066%


f=open("id_changCompanyOverSamCategory.csv","w")

fl=True

for _ in range(11):
    f1=open("id_changCompanyOverSamCategory"+str(_)+".csv","r")
    line = f1.readline()
    while line:
        if fl:
            f.write(line)
            fl=False
        else:
            if line != "id,changCompanyOverSamCategory\n":
                f.write(line)
        line = f1.readline()
    f1.close()

f.close()

# =============================================================================
# 8) Is there is a fixed or almost same duration between repeat purchases by customers for a specific product
# =============================================================================
#############################################################################
import os
import pandas as pd

for i in range(11):
    print("data is loading...",i)
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
    transactions_data = pd.read_csv("t"+str(i)+".csv",usecols = ['id','date','category'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Unique depertments...")
    print(len(transactions_data.company.unique()))
    
    print("Created an csv for data id and change brand over same Category")
    f=open("id_changCompanyOverSamCategory"+str(i)+".csv","w")
    
    f.write("id,changCompanyOverSamCategory\n")
    
    for i,t_df_id in transactions_data.groupby(['id']):
        countY=0
        countN=0
        for j,t_df_cat in t_df_id.groupby(['category']):
            l=[]
            ###
            ####
            ###
            ##
            
            
        if countY > 0 and countN > 0:
            if countY > countN:
                f.write(str(i)+",Y\n")
            elif countY < countN:
                f.write(str(i)+",N\n")
            elif countY == countN:
                f.write(str(i)+",C\n")
    
    f.close()
    print("t",str(i),"is done!")

import os
import pandas as pd
from collections import defaultdict

dic=defaultdict(int)

for _ in range(11):
    print("data is loading...",_)
    os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\id_changBrandOverSamCategory")
    transactions_data = pd.read_csv("id_changCompanyOverSamCategory"+str(_)+".csv",usecols = ['id','changCompanyOverSamCategory'])
    print("Data is loaded")
    
    print("Data info")
    transactions_data.info()
    
    print("Data Size")
    transactions_data.size
    
    print("Data Shape")
    transactions_data.shape
    
    print("Data Containg Null values count by columns")
    print(transactions_data.isnull().sum())
    
    print("Data Converstion")
    transactions_data["changCompanyOverSamCategory"]=transactions_data.changBrandOverSamCategory.astype("category")
    
    print("Data info")
    transactions_data.info()
    
    for i,d_df in transactions_data.groupby(["changCompanyOverSamCategory"]):
        dic[i]+=len(d_df)

total=dic["C"]
total+=dic["N"]
total+=dic["Y"]

print("for Y ")
print(str((dic["Y"]/total)*100)+"%")

#Answer = 

print("for N ")
print(str((dic["N"]/total)*100)+"%")

#Answer = 

print("for C ")
print(str((dic["C"]/total)*100)+"%")

#Answer = 


f=open("id_changCompanyOverSamCategory.csv","w")

fl=True

for _ in range(11):
    f1=open("id_changCompanyOverSamCategory"+str(_)+".csv","r")
    line = f1.readline()
    while line:
        if fl:
            f.write(line)
            fl=False
        else:
            if line != "id,changCompanyOverSamCategory\n":
                f.write(line)
        line = f1.readline()
    f1.close()

f.close()

# =============================================================================
# 9) What is percentage of product returns?
# =============================================================================

#NO ANSWER

# =============================================================================
# 10)   Are the product returns from the similar customers , similar category, or a similar brand?
# =============================================================================

#NO ANSWER
