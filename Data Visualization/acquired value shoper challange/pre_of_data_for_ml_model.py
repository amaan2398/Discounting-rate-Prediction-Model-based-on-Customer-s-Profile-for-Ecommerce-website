# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:43:11 2020

@author: outsi
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import json

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData")
df = pd.read_csv("Datasetcategory.csv",usecols=['id','CBrand','CCategory','CCompany','Recency','Frequency','Monetary'])

rcdic=dict()
rmaxdic=dict()
for i in range(df.shape[0]):
    if df.CCategory.iloc[i] in rcdic:
        if int(df.Recency.iloc[i]) in rcdic[df.CCategory.iloc[i]]:
            rcdic[df.CCategory.iloc[i]][int(df.Recency.iloc[i])]+=1
        else:
            rcdic[df.CCategory.iloc[i]][int(df.Recency.iloc[i])]=1
    else:
        rcdic[df.CCategory.iloc[i]]=dict()
        rcdic[df.CCategory.iloc[i]][int(df.Recency.iloc[i])]=1

for i in rcdic.keys():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x=list(rcdic[i].keys())
    x=list(sorted(x))
    y=[rcdic[i][k] for k in x]
    a=max(y)
    b=max(x)
    print(a,'#')
    plt.title(i)
    ax.plot(x,y, color='lightblue', linewidth=3)
    ax.plot([x[y.index(a)]], [a], 'o')
    ax.annotate("MAX",xy=(x[y.index(a)],a),xytext=(b, a),arrowprops=dict(facecolor='black', shrink=0.05))
    avg=sum(y)//len(y)
    absolute_difference_function = lambda list_value : abs(list_value - avg)
    ax.plot([x[y.index(min(y, key=absolute_difference_function))]], [min(y, key=absolute_difference_function)], 'o')    
    ax.annotate("AVG",xy=(x[y.index(min(y, key=absolute_difference_function))],min(y, key=absolute_difference_function)),xytext=(b-6, a-6),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

json_object = json.dumps(rcdic, indent = 4) 

with open("json/RecencyCount.json", "w") as outfile: 
    outfile.write(json_object) 

for i in rcdic:
    k=list(rcdic[i].keys())
    v=list(rcdic[i].values())
    rmaxdic[i]=k[v.index(max(v))]

r=[]
for i in range(df.shape[0]):
    if rmaxdic[df.CCategory.iloc[i]]>=df.Recency.iloc[i]:
        r.append(1)
    else:
        r.append(0)


fcdic=dict()
fmaxdic=dict()
for i in range(df.shape[0]):
    if df.CCategory.iloc[i] in fcdic:
        if int(df.Frequency.iloc[i]) in fcdic[df.CCategory.iloc[i]]:
            fcdic[df.CCategory.iloc[i]][int(df.Frequency.iloc[i])]+=1
        else:
            fcdic[df.CCategory.iloc[i]][int(df.Frequency.iloc[i])]=1
    else:
        fcdic[df.CCategory.iloc[i]]=dict()
        fcdic[df.CCategory.iloc[i]][int(df.Frequency.iloc[i])]=1


for i in fcdic.keys():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x=list(fcdic[i].keys())
    x=list(sorted(x))
    y=[fcdic[i][k] for k in x]
    a=max(y)
    b=max(x)
    print(a,'#')
    ax.plot(x,y, color='lightblue', linewidth=3)
    plt.title(i)
    ax.plot([x[y.index(a)]], [a], 'o')
    ax.annotate("MAX",xy=(x[y.index(a)],a),xytext=(b, a),arrowprops=dict(facecolor='black', shrink=0.05))
    avg=sum(y)//len(y)
    absolute_difference_function = lambda list_value : abs(list_value - avg)
    ax.plot([x[y.index(min(y, key=absolute_difference_function))]], [min(y, key=absolute_difference_function)], 'o')    
    ax.annotate("AVG",xy=(x[y.index(min(y, key=absolute_difference_function))],min(y, key=absolute_difference_function)),xytext=(b-6, a-6),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

json_object = json.dumps(fcdic, indent = 4) 
  
with open("json/FrequencyCount.json", "w") as outfile: 
    outfile.write(json_object)

for i in fcdic:
    k=list(fcdic[i].keys())
    v=list(fcdic[i].values())
    fmaxdic[i]=k[v.index(max(v))]

f=[]
for i in range(df.shape[0]):
    if fmaxdic[df.CCategory.iloc[i]]<=df.Frequency.iloc[i]:
        f.append(1)
    else:
        f.append(0)


mcdic=dict()
mmaxdic=dict()
for i in range(df.shape[0]):
    if df.CCategory.iloc[i] in mcdic:
        if int(df.Monetary.iloc[i]) in mcdic[df.CCategory.iloc[i]]:
            mcdic[df.CCategory.iloc[i]][int(df.Monetary.iloc[i])]+=1
        else:
            mcdic[df.CCategory.iloc[i]][int(df.Monetary.iloc[i])]=1
    else:
        mcdic[df.CCategory.iloc[i]]=dict()
        mcdic[df.CCategory.iloc[i]][int(df.Monetary.iloc[i])]=1


for i in mcdic.keys():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x=list(mcdic[i].keys())
    x=list(sorted(x))
    y=[mcdic[i][k] for k in x]
    a=max(y)
    b=max(x)
    print(a,'#')
    ax.plot(x,y, color='lightblue', linewidth=3)
    plt.title(i)
    ax.plot([x[y.index(a)]], [a], 'o')
    ax.annotate("MAX",xy=(x[y.index(a)],a),xytext=(b, a),arrowprops=dict(facecolor='black', shrink=0.05))
    avg=sum(y)//len(y)
    absolute_difference_function = lambda list_value : abs(list_value - avg)
    ax.plot([x[y.index(min(y, key=absolute_difference_function))]], [min(y, key=absolute_difference_function)], 'o')    
    ax.annotate("AVG",xy=(x[y.index(min(y, key=absolute_difference_function))],min(y, key=absolute_difference_function)),xytext=(b-6, a-6),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()

json_object = json.dumps(mcdic, indent = 4) 
  
with open("json/FrequencyCount.json", "w") as outfile: 
    outfile.write(json_object)

for i in mcdic:
    k=list(mcdic[i].keys())
    v=list(mcdic[i].values())
    avg=sum(v)//len(v)
    absolute_difference_function = lambda list_value : abs(list_value - avg)
    mmaxdic[i]=k[v.index(min(v, key=absolute_difference_function))]

m=[]
for i in range(df.shape[0]):
    if mmaxdic[df.CCategory.iloc[i]]<=df.Monetary.iloc[i]:
        m.append(1)
    else:
        m.append(0)