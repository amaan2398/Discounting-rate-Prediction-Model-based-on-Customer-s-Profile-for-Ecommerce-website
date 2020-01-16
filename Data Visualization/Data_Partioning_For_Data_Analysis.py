# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 01:25:11 2019

@author: outsi
"""

# import os
# import pandas as pd

# print("data is loading...")
# os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
# transactions_data = pd.read_csv("transactions.csv", usecols = ['id', 'dept'])
# print("Data is loaded")

# print("Data is getting sorted")
# transactions_data.sort_values(by=['id'])
# print("Sort is done")

# print('Print of head data:',transactions_data.head())
# print('Print of tail data',transactions_data.tail())

# print(transactions_data.id[2])
# f = open("transactions_id_dept0.csv","w")
# k=1
# x=485359873
# con=485359873
# for i in range(349655789):
#     if x < transactions_data.id[i]:
#         print(str(k)+" part is done...")
#         f.close()
#         x+=con
#         f = open("transactions_id_dept"+str(k)+".csv","w")
#         k+=1
#     f.write(str(transactions_data.at[i,'id'])+","+str(transactions_data.at[i,'dept'])+"\n")
# f.close()

"""Creating Parts of data:"""
import os
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")

f=open("transactions.csv","r")

fl=[open("t"+str(x)+".csv","w") for x in range(12) ]

line1=f.readline()

for i in fl:
    i.write(line1+"\n")

for i in fl:
    i.flush()

for i in range(349655789):
    line = f.readline()
    words=line.strip().split(",")
    fl[int(words[0])//485359873].write(line+"\n")
    if i%100 == 99:
        for z in fl:
            z.flush()

for i in fl:
    i.close()

