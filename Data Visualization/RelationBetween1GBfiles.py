# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:32:16 2020

@author: outsi
"""

import os
import pandas as pd

os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")


dataBrand = pd.read_csv("oneGbBrand.csv")
dataCompany = pd.read_csv("oneGbCompany.csv")
dataCategory = pd.read_csv("oneGbCategory.csv")

print(dataBrand.head())
print(dataCompany.head())
print(dataCategory.head())

interSectDF = pd.merge(dataBrand, dataCompany , how = "inner")
print(" INN Brand and Comp")
print((len(interSectDF)/len(dataBrand))*100)
#60.18350081294751

interSectDF = pd.merge(dataBrand, dataCategory, how = "inner")
print(" INN Brand and Category")
print((len(interSectDF)/len(dataBrand))*100)
#42.326288868968206

interSectDF1 = pd.merge(dataCategory, dataCompany, how = "inner")
interSectDF = pd.merge(dataBrand, interSectDF1, how = "inner")
print(" INN Brand and Comp and Categ")
print((len(interSectDF)/len(dataBrand))*100)
#28.265479639028612



interSectDF = pd.merge(dataCategory, dataCompany, how = "inner")
print(" INN Categ and Comp")
print((len(interSectDF)/len(dataCategory))*100)
#22.01449307085962

interSectDF = pd.merge(dataCategory, dataBrand, how = "inner")
print(" INN Categ and Brand")
print((len(interSectDF)/len(dataCategory))*100)
#25.51542167286994

interSectDF1 = pd.merge(dataBrand, dataCompany, how = "inner")
interSectDF = pd.merge(dataCategory, interSectDF1, how = "inner")
print(" INN Categ and Comp and Brand")
print((len(interSectDF)/len(dataCategory))*100)
#17.039188907121297




interSectDF = pd.merge(dataCompany, dataBrand, how = "inner")
print(" INN Comp and Brand")
print((len(interSectDF)/len(dataCompany))*100)
#35.26032399868481

interSectDF = pd.merge(dataCompany, dataCategory, how = "inner")
print(" INN Comp and Categ")
print((len(interSectDF)/len(dataCompany))*100)
#21.395625275065715

interSectDF1 = pd.merge(dataCategory, dataCompany, how = "inner")
interSectDF = pd.merge(dataCompany, interSectDF1, how = "inner")
print(" INN Comp and Categ and Brand")
print((len(interSectDF)/len(dataCompany))*100)
#21.395625275065715

