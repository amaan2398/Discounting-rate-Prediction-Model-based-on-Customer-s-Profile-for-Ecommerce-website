import os
import pandas as pd

os.chdir("D:\\Final project\\Datasets\\discount-prediction\\")

print(os.listdir("D:\\Final project\\Datasets\\discount-prediction\\"))

data=pd.read_csv('product_details.csv',usecols=['Product_Name'],encoding="cp437")
print(data)

Unique_Product=data.Product_Name.unique()
print(len(Unique_Product))
#722

for i in range(722):
    Unique_Product[i]=Unique_Product[i].strip()
    
Unique_Product.sort()

print(len(Unique_Product))
#722

count_dict={}
for i in Unique_Product:
    x=i
    i="".join(i.split("0"))
    i="".join(i.split("1"))
    i="".join(i.split("2"))
    i="".join(i.split("3"))
    i="".join(i.split("4"))
    i="".join(i.split("5"))
    i="".join(i.split("6"))
    i="".join(i.split("7"))
    i="".join(i.split("8"))
    i="".join(i.split("9"))
    i="".join(i.split("-"))
    i="".join(i.split("á"))
    temp=i.split(" ")[0]
    try:
        count_dict[temp]+=[x]
    except:
        count_dict[temp]=[x]
print(count_dict)

print(len(count_dict))
#352

f = open("mergeProduct.csv",'w')

for i in count_dict:
    st=i
    st+=','
    for j in count_dict[i]:
        f.write(st+j+"\n")
        if st == i+",":
            st=" ,"

f.close()














