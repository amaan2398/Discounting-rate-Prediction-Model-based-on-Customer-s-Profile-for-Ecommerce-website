import os
import pandas as pd
import numpy as np

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\meargeOFF&HISTo")
dataTH = pd.read_csv("histwithOff.csv")
dataTH['offerdate']=pd.to_datetime(dataTH['offerdate'])

print(dataTH.loc[0].id)
print(dataTH.isnull().sum())

print(dataTH.columns.tolist())

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\t")

LstID=[]
LstChain=[]
LstMarket=[]
LstCategory=[]
LstCompany=[]
LstBrand=[]
LstQuantity=[]
LstR=[]
LstF=[]
LstM=[]
LstOffervalue=[]

count=0
for i in range(11):
    df = pd.read_csv("t"+str(i)+".csv",usecols=['id','company','date','purchaseamount'])
    df['date'] = pd.to_datetime(df['date'])
    DF=None
    DF=pd.DataFrame(columns = df.columns.tolist())
    #print(df.dtypes)
    #print(df.isnull().sum())
    for j, dataF in df.groupby('id'):
        dfTmp = dataTH.loc[dataTH['id']==j]
        for _ in range(dfTmp.id.shape[0]):
            xy=dfTmp.iloc[_].loc['company']
            ttt=dataF.loc[dataF['company'] == xy]
            size=ttt.shape[0]
            ttdata={'offerdate':[dfTmp.iloc[_].offerdate]}
            ttdf=pd.DataFrame(ttdata)
            if size>0:
                if ttt.purchaseamount.sum()>=0:
                    ttt.sort_values(by=['date'])
                    LstID.append(dfTmp.iloc[_].id)
                    LstChain.append(dfTmp.iloc[_].chain)
                    LstMarket.append(dfTmp.iloc[_].market)
                    LstCategory.append(dfTmp.iloc[_].category)
                    LstCompany.append(dfTmp.iloc[_].company)
                    LstBrand.append(dfTmp.iloc[_].brand)
                    LstQuantity.append(dfTmp.iloc[_].quantity)
                    LstR.append((ttdf.offerdate.sub(ttt.iloc[size-1].date)/np.timedelta64(1,'D')).iloc[0])
                    LstF.append(size)
                    LstM.append(ttt.purchaseamount.sum())
                    LstOffervalue.append(dfTmp.iloc[_].offervalue)
                    count+=1

data={'id':LstID,'Chain':LstChain,'Market':LstMarket,'Category':LstCategory,'Company':LstCompany,'Brand':LstBrand,'Quantity':LstQuantity,'Recency':LstR,'Frequency':LstF,'Monetary':LstM,'Offervalue':LstOffervalue}
pd.DataFrame(data).to_csv(r'D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData\\DatasetComp.csv'.format(i), index = False)

print(count)
#86654


#87471



#-ve values of amount removed 39/63152

            #print(ttt.purchaseamount.iloc[:].sum())
    #print(1)
    #DF.to_csv(r'D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData\\ROWdata{}.csv'.format(i), index = False)
    #print(1)
# for i in range(2):
#     dataf = pd.read_csv("t"+str(i)+".csv",usecols=['id','date','purchaseamount'])
#     dataf['date']=pd.to_datetime(dataf['date']) 
#     print(dataf.dtypes)
#     print(dataf.isnull().sum())
    
#     for j,tdata in dataf.groupby('id'):
#         df=dataTH.loc[dataTH['id']==j]
#         if df.id.count()>0:
#             tdata.sort_values(by=['date'])
#             size = tdata.shape[0]
#             R = (df.offerdate.sub(tdata.loc[size-1].date)/np.timedelta64(1,'D'))[0]
#             F = tdata.date.unique().shape[0]
#             M = tdata.purchaseamount.sum()
#             print(R,F,M)
#         break
#     break        

# print(tdata.date.unique())
# #print(dic)
# #print(len(dic))
# print(dataf.head(20))
# #print(datesUn)
# #print(amot)
# #print(it)
# print(len(tdata))
# print(tdata.head(1044))
# #c=0
# #for i in amot:
#     #if i==0:
#         #c+=1
# #print(c)
# #24-04-2013



os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData")
df = pd.read_csv("DatasetComp.csv")

k=df.Recency.unique()
np.sort(k)
k

LstLable=[]
for i in df.Offervalue:
    if i <= 1:
        LstLable.append('low')
    elif i<=1.5:
        LstLable.append('medium')
    else:
        LstLable.append('high')

df['Lable']=LstLable


LstRLable=[]
for i in df.Recency:
    LstRLable.append(i//10)
    
df['RLable']=LstRLable

LstFLable=[]
for i in df.Frequency:
    LstFLable.append(i//12)
    
df['FLable']=LstFLable




df.info()
df.Offervalue=df.Offervalue.astype('category')
df.info()
df.shape
pd.DataFrame(df).to_csv(r'D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData\\DatasetComp.csv', index = False)

#######################################################################


os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData")
df = pd.read_csv("DatasetComp.csv")



LstBrand=[]
for i in df.Brand:
    LstBrand.append('B'+str(i))

df['CBrand']=LstBrand


LstCategory=[]
for i in df.Category:
    LstCategory.append('CA'+str(i))
    
df['CCategory']=LstCategory

LstCompany=[]
for i in df.Company:
    LstCompany.append('CO'+str(i))
    
df['CCompany']=LstCompany




df.info()
df.Offervalue=df.Offervalue.astype('category')
df.info()
df.shape
pd.DataFrame(df).to_csv(r'D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\ModelData\\DatasetComp.csv', index = False)
