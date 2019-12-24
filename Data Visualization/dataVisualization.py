import os
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#transactions_data.loc[j,'id'],transactions_data.loc[j,'dept']


# =============================================================================
# WHAT IS THE PERCENTAGE OF CUSTOMERS WHO DID MULTIPLE TRANSACTIONS  ON SAME DEPARTMENT
# =============================================================================

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
transactions_data = pd.read_csv("transactions.csv", usecols = ['id', 'dept'])
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
deptU.sort()#48 52 61 66 68 76 77 80 83 84 85 86 87 88 89 90 93 this dept are not present in dataframe
print(deptU)

listP=[]
for i in deptU:
    T=len(transactions_data.loc[ transactions_data['dept'] == i ])
    U=len(transactions_data.loc[ transactions_data['dept'] == i ].id.unique())
    if T != 0:
        listP.append((T - U) / T)
    
'''
index = np.arange(len(deptU[:10]))
plt.bar(index , listP[:10])
plt.xticks(index, deptU[:10], rotation=90)
plt.show()
'''
df = pd.DataFrame({'percentage':listP, 'index':deptU})
ax = df.plot.bar(x='index',y='percentage',rot= 90, figsize = (84 , 10))

# =============================================================================
# What is the percentage of customers who did multiple transactions  on different department
# =============================================================================

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
transactions_data = pd.read_csv("transactions.csv",usecols = ['id' , 'dept'])
print("Data is loaded")

print("Data info")
transactions_data.info()

print("Data Size")
transactions_data.size

print("Data Shape")
transactions_data.shape

print("Data Containg Null values count by columns")
print(transactions_data.isnull().sum())

# T=len(transactions_data.id)
# U=len(transactions_data.id.unique())
# prct = ((T - U) / T)
# print(prct)
# df = pd.DataFrame({ 'percentage' : [ prct ] })
# ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))
mdv=0
totel=0
for i,t_df in transactions_data.groupby(['id']):
    if len(t_df)>1:
        mdv+=len(t_df.dept.unique())
    totel+=len(t_df)
print("Total multiple transactions  on different department is: "+str(mdv))
print("Total transactions are: "+str(total))

df = pd.DataFrame({ 'percentage' : [ mdv ] })
ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))

# =============================================================================
# What is the percentage of customers who did multiple transactions  on same category
# =============================================================================

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
transactions_data = pd.read_csv("transactions.csv",usecols = ['id' , 'category'])
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
print(categoryU)

listP=[]
for i in categoryU:
    T = len(transactions_data.loc[ transactions_data['category'] == i ])
    U = len(transactions_data.loc[ transactions_data['category'] == i ].id.unique())
    if T != 0:
        listP.append((T - U)/ T)

df = pd.DataFrame({'percentage':listP, 'index':categoryU})
ax = df.plot.scatter(x='index',y='percentage',rot= 90, figsize = (50 , 10))


# =============================================================================
# What is the percentage of customers who did multiple transactions  on different category
# =============================================================================

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
transactions_data = pd.read_csv("transactions.csv",usecols = ['id' , 'category'])
print("Data is loaded")

print("Data info")
transactions_data.info()

print("Data Size")
transactions_data.size

print("Data Shape")
transactions_data.shape

print("Data Containg Null values count by columns")
print(transactions_data.isnull().sum())

# T=len(transactions_data.id)
# U=len(transactions_data['id'].append(transactions_data['category']).unique())
# prct = ((T - U) / T)
# print(prct)
# df = pd.DataFrame({ 'percentage' : [ prct ] })
# ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))
g = transactions_data.groupby(['id','category'])

for i,id_df in g:
    




# =============================================================================
# What is the percentage of customers who did multiple transactions
# =============================================================================

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
transactions_data = pd.read_csv("transactions.csv",usecols = ['id'])
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
prct = ((T - U) / T)
print(prct)
df = pd.DataFrame({ 'percentage' : [ prct ] })
ax = df.plot.bar( y = 'percentage', rot = 0 , figsize=(10 , 20))




df = pd.DataFrame({'A':[1,2,3,4,4,4,5],'B':[11,12,12,12,13,13,11]})
print(df)
x=df.groupby(['A'])
print(len(x))
k=[]
for a,b in x:
    if len(b)>1:
        print(a,b)

print(df)
