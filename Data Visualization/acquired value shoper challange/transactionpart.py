# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:30:31 2020

@author: outsi
"""

import os
import pandas as pd

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\offers")

def catagOffer():
    cat = []
    data = pd.read_csv("offers.csv",usecols = ['category'])
    for i in data.category.unique():
        cat.append(i)
    return cat


def compOffer():
    cat = []
    data = pd.read_csv("offers.csv",usecols = ['company'])
    for i in data.company.unique():
        cat.append(i)
    return cat


def bndOffer():
    cat = []
    data = pd.read_csv("offers.csv",usecols = ['brand'])
    for i in data.brand.unique():
        cat.append(i)
    return cat

print(catagOffer())
categoryOffer = catagOffer()

print(compOffer())
companyOffer = compOffer()

print(bndOffer())
brandOffer = bndOffer()
# =============================================================================
#  
# =============================================================================
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")


f = open("transactions.csv","r")
line = f.readline()
words = line.strip().split(",")

colNum = 0
for i,_ in enumerate(words):
    if _ == "category":
        colNum=i
        break

fw = open("oneGbTransactionsCategory.csv","w")
fw.write(line+"\n")

line = f.readline()
_=0

while line:
    words = line.strip().split(",")
    if int(words[colNum]) in categoryOffer:
        fw.write(line+"\n")
    print(_)
    _ += 1
    line = f.readline()

fw.close()
f.close()
# =============================================================================
# 
# =============================================================================


f = open("transactions.csv","r")
line = f.readline()
words = line.strip().split(",")

colNum = 0
for _ in words:
    if _ == "company":
        break
    colNum += 1
fw = open("oneGbTransactionsCompany.csv","w")
fw.write(line+"\n")
_=0
while True:
    line = f.readline()
    if not line:
        break
    words = line.strip().split(",")
    if words[colNum] in companyOffer:
        fw.write(line+"\n")
    print(_)
    _+=1
fw.close()
f.close()
# =============================================================================
# 
# =============================================================================


colNum = 0
for _ in words:
    if _ == "brand":
        break
    colNum += 1
fw = open("oneGbTransactionsBrand.csv","w")
fw.write(line+"\n")
_=0
while True:
    line = f.readline()
    if not line:
        break
    words = line.strip().split(",")
    if words[colNum] in brandOffer:
        fw.write(line+"\n")
    print(_)
    _ += 1
fw.close()
f.close()