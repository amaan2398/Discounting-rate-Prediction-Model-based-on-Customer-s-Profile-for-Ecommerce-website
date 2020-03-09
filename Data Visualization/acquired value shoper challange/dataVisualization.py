
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

'''oneGbBrand'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id', 'dept'])
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
deptU.sort()

print(deptU)
#[ 3  4  6  7  8  9 10 14 15 16 17 18 21 22 25 26 27 30 32 33 35 42 44 45 46 
#47 51 55 56 58 62 63 65 69 70 72 73 91 96 97 99]

print(len(deptU))
#41

for i in deptU:
    T=len(transactions_data.loc[ transactions_data['dept'] == i ])
    U=len(transactions_data.loc[ transactions_data['dept'] == i ].id.unique())
    if T != 0:
        listP.append((T - U) / T)

print(listP)
#[0.37376721860315026, 0.3554817275747508, 0.5055743397605775,
# 0.8034541274919809, 0.18081761006289307, 0.8545162329721693, 
# 0.7428981544222897, 0.6642559326190861, 0.5442064799560681, 
# 0.16981132075471697, 0.6226449854701687, 0.39635881426637565, 
# 0.6650342738312238, 0.6454882218844985, 0.8446734491420703, 
 # 0.22191011235955055, 0.743374509325586, 0.0, 0.5140769020168527, 
 # 0.5667877122386887, 0.7040205853972339, 0.15725806451612903, 
 # 0.6323722250505237, 0.597149710737971, 0.5617970093952627, 
 # 0.5144334532374101, 0.614113913159857, 0.500576943249764, 0.836090090570006, 
 # 0.7644737167147746, 0.4968491288768071, 0.6611797334429008, 
 # 0.3940551235448396, 0.502724358974359, 0.17341040462427745, 
 # 0.6947764626487052, 0.389040497762253, 0.721832286664204, 
 # 0.4793463086146013, 0.3598458304134548, 0.9033129405642646]

'''oneGbCategory'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id', 'dept'])
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
deptU.sort()

print(deptU)
#[ 7 17 21 22 32 35 44 45 51 55 56 58 62 72 91 99]

print(len(deptU))
#16

for i in deptU:
    T=len(transactions_data.loc[ transactions_data['dept'] == i ])
    U=len(transactions_data.loc[ transactions_data['dept'] == i ].id.unique())
    if T != 0:
        listP.append((T - U) / T)

print(listP)
# [0.76578224716245, 0.7923052250387997, 0.9048257332058149, 0.5939251146204788, 
#  0.6012440590344368, 0.8759223921261384, 0.5741285801795879, 
#  0.6875138319262046, 0.7675078357309331, 0.8208273601636888, 
#  0.8657229455358032, 0.8565381973266165, 0.7112114112807331, 
#  0.8088936015161552, 0.8740663295567641, 0.9377710091066456]

'''oneGbCompany'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id', 'dept'])
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
deptU.sort()

print(deptU)
#[ 2  3  4  5  6  7  8  9 10 14 16 17 18 20 21 22 24 25 26 27 29 32 33 34
# 35 36 37 40 41 44 45 46 47 50 51 54 55 56 58 62 63 64 65 67 69 71 72 73
# 74 75 91 92 97 99]
print(len(deptU))
#54
for i in deptU:
    T=len(transactions_data.loc[ transactions_data['dept'] == i ])
    U=len(transactions_data.loc[ transactions_data['dept'] == i ].id.unique())
    if T != 0:
        listP.append((T - U) / T)

print(listP)
#[0.12727272727272726, 0.37376721860315026, 0.3501683501683502, 
# 0.5054818234275822, 0.7715753424657534, 0.7802488009678467, 
# 0.7341000286455962, 0.5132139812446718, 0.44, 0.0, 0.16981132075471697, 
# 0.685476828879917, 0.726456178551987, 0.7762088841036551, 
# 0.7473451057690353, 0.7696642740471279, 0.5931616033267876, 
# 0.8445903236469285, 0.8804237044163172, 0.7976130030404941, 
# 0.8363533709339317, 0.5140769020168527, 0.7655646935963383, 
# 0.6096940506071501, 0.8526368993516424, 0.44806007509386736, 
# 0.8873722697768704, 0.36726893676164, 0.6337651568865442, 
# 0.6323722250505237, 0.597149710737971, 0.5617888330246097,
# 0.4801412180052957, 0.7060347060347061, 0.7182787693553548,
# 0.7851922661815042, 0.28787205686361617, 0.8362023183750683,
# 0.7650184934681638, 0.4968491288768071, 0.6278849567996213,
# 0.8373785651349843, 0.3940551235448396, 0.19607843137254902,
# 0.5379158512720157, 0.5199868938401049, 0.7266165709327356,
# 0.6488843704853122, 0.16184971098265896, 0.435847208619001,
# 0.8198446717311039, 0.24675905230219045, 0.50814332247557,
# 0.8943566514474315]


# =============================================================================
# 2)What is the percentage of customers who did multiple transactions  on different department
# =============================================================================

import os
import pandas as pd

'''oneGbBrand'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id', 'dept'])
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
        T=len(t_df.dept)
        U=len(t_df.dept.unique())
        listP.append((T-U)/T)

print((sum(listP)/len(listP))*100)
#64.09135737470703
print(len(listP))
#293650
#print(listP)

'''oneGbCategory'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id', 'dept'])
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
        T=len(t_df.dept)
        U=len(t_df.dept.unique())
        listP.append((T-U)/T)

print((sum(listP)/len(listP))*100)
#75.3117733497687
print(listP)

'''oneGbCompany'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id', 'dept'])
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
        T=len(t_df.dept)
        U=len(t_df.dept.unique())
        listP.append((T-U)/T)

print((sum(listP)/len(listP))*100)
#66.97797838665971
print(listP)

# =============================================================================
# 3)What is the percentage of customers who did multiple transactions  on same category
# =============================================================================

import os
import pandas as pd

'''oneGbBrand'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id', 'category'])
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
categoryU.sort()
print(categoryU)
# [ 305  410  419  423  601  610  703  706  708  709  799  805  904  905
#   907  908  910  912  913  914  918 1010 1013 1404 1411 1414 1415 1417
#  1504 1506 1604 1703 1704 1706 1707 1708 1709 1712 1719 1724 1726 1822
#  1823 1827 1828 1841 1842 1850 1854 1890 2106 2112 2113 2118 2119 2201
#  2202 2207 2211 2214 2503 2506 2507 2610 2620 2710 2712 2715 3001 3203
#  3301 3303 3307 3315 3317 3319 3504 3509 4220 4401 4404 4405 4517 4606
#  4705 4706 5119 5122 5558 5559 5604 5607 5610 5612 5613 5614 5616 5617
#  5619 5620 5621 5812 5813 5823 5824 5830 5837 6202 6203 6305 6311 6312
#  6327 6399 6503 6901 7001 7203 7205 7208 7209 7212 7215 7305 7311 9115
#  9632 9724 9799 9904 9908 9909]

for i in categoryU:
    T = len(transactions_data.loc[ transactions_data['category'] == i ])
    U = len(transactions_data.loc[ transactions_data['category'] == i ].id.unique())
    if T != 0:
        listP.append((T - U)/ T)

print(sum(listP)/len(listP)*100)
#46.12753682343489

print(listP)
# [0.37376721860315026, 0.34523809523809523, 0.33488372093023255, 0.5,
#  0.20195838433292534, 0.5462455688043829, 0.628560620389635,
#  0.7597626236147018, 0.7713679592107325, 0.73028934425131,
#  0.554006968641115, 0.18081761006289307, 0.4839022498060512,
#  0.3503392186559887, 0.8256960232312508, 0.0, 0.5592889822245556,
#  0.5504314192204701, 0.6319237641453246, 0.3365943136655457,
#  0.7487388216798841, 0.25, 0.7429099555331016, 0.3903293622985284,
#  0.5749875767578888, 0.0, 0.5254144777239544, 0.6467994526379809,
#  0.5556534508076358, 0.49805636540330417, 0.16981132075471697,
#  0.42207088685961924, 0.47483214565226345, 0.18122977346278318,
#  0.193033381712627, 0.39162772956994374, 0.4278663568624309,
#  0.16912972085385877, 0.44639600729436607, 0.24358974358974358,
#  0.5199294673188615, 0.0, 0.43959633181190066, 0.3148148148148148,
#  0.28658976207642395, 0.11659192825112108, 0.12952419682797886,
#  0.07692307692307693, 0.0, 0.2894817540631708, 0.0, 0.5185169808187329,
#  0.5271437628784277, 0.6564930396706098, 0.6463104887691322,
#  0.6113039996127562, 0.4223512336719884, 0.5260267615438162,
#  0.4794569745726189, 0.5725007505253678, 0.5766258471049815,
#  0.8460525058501349, 0.13333333333333333, 0.22580645161290322,
#  0.06666666666666667, 0.7385615491009682, 0.4404040404040404,
#  0.6714055793991416, 0.0, 0.5140769020168527, 0.4483870967741935,
#  0.3684210526315789, 0.4616252821670429, 0.5248494744361669,
#  0.6758664955070603, 0.1852340145023072, 0.5430974071478627,
#  0.7046549018401133, 0.15725806451612903, 0.5416479297104708,
#  0.5924856437020434, 0.5396208070004861, 0.597149710737971,
#  0.5617970093952627, 0.6013346043851286, 0.4801412180052957,
#  0.5519246190858059, 0.6006974532389305, 0.28787205686361617,
#  0.5212607790663099, 0.5283018867924528, 0.4431818181818182,
#  0.5232352290329719, 0.8347826086956521, 0.49148523388661347,
#  0.6654967675620114, 0.7737078227196524, 0.7682243848696291,
#  0.41935483870967744, 0.7078616377757371, 0.42264515649394097,
#  0.7046220181872762, 0.58214949795463, 0.7505375120149744,
#  0.1925272444213804, 0.7855530474040632, 0.5609271523178808,
#  0.4550947541884098, 0.29839704069050554, 0.43888415672913117,
#  0.6669581497550421, 0.5404725992961287, 0.4700493305144468, 0.4,
#  0.3940551235448396, 0.502724358974359, 0.17341040462427745,
#  0.5236947111656304, 0.6641757508056957, 0.1800046937338653,
#  0.2740740740740741, 0.3321486551709008, 0.25927106577409414,
#  0.38641376268195854, 0.6129032258064516, 0.721832286664204,
#  0.4793463086146013, 0.3338391502276176, 0.40250855188141393,
#  0.6070073758484145, 0.7066670645815925, 0.9004577197294577]

'''oneGbCategory'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id', 'category'])
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
categoryU.sort()
print(categoryU)
#[ 706  799 1703 1726 2119 2202 3203 3504 3509 4401 4517 5122 5558 5616
#5619 5824 6202 7205 9115 9909]

for i in categoryU:
    T = len(transactions_data.loc[ transactions_data['category'] == i ])
    U = len(transactions_data.loc[ transactions_data['category'] == i ].id.unique())
    if T != 0:
        listP.append((T - U)/ T)

print(str((sum(listP)/len(listP))*100)+"%")
#74.84170129901584%
print(listP)
# [0.7671176024581986, 0.5771567436208992, 0.7413904959567212,
#  0.6616913554536671, 0.9048257332058149, 0.5939251146204788,
#  0.6012440590344368, 0.7706704881952349, 0.8349660258268122,
#  0.5741285801795879, 0.6875138319262046, 0.7675078357309331,
#  0.8208273601636888, 0.8621614500379499, 0.6147330346056255,
#  0.8565381973266165, 0.7112114112807331, 0.8088936015161552,
#  0.8740663295567641, 0.9377710091066456]

'''oneGbCompany'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id', 'category'])
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
categoryU.sort()
print(categoryU)
# [ 201  305  410  419  423  519  520  522  601  610  703  706  708  709
#   799  803  805  809  817  818  829  901  902  918 1010 1099 1415 1604
#  1701 1703 1704 1706 1707 1708 1709 1710 1712 1719 1721 1724 1726 1799
#  1822 1823 1827 1828 1829 1835 1836 1841 1842 1854 2002 2106 2117 2118
#  2119 2201 2202 2207 2210 2211 2214 2403 2503 2505 2506 2507 2509 2610
#  2613 2614 2620 2628 2629 2630 2631 2632 2633 2634 2710 2712 2715 2902
#  2903 2905 2914 2930 3203 3301 3302 3303 3307 3312 3315 3317 3319 3351
#  3402 3403 3405 3406 3410 3411 3499 3504 3506 3507 3508 3509 3510 3513
#  3611 3703 3705 3706 3707 3711 4004 4005 4105 4107 4108 4109 4110 4121
#  4401 4404 4405 4517 4606 4706 5002 5119 5122 5127 5199 5403 5558 5604
#  5607 5610 5612 5613 5614 5616 5617 5618 5619 5620 5621 5812 5813 5823
#  5824 5830 5837 6202 6203 6314 6315 6316 6320 6323 6327 6330 6406 6407
#  6408 6409 6410 6503 6708 6901 7102 7106 7107 7110 7113 7114 7203 7205
#  7208 7209 7210 7211 7212 7215 7303 7309 7318 7344 7410 7501 9106 9110
#  9115 9120 9122 9131 9134 9206 9213 9215 9716 9753 9799 9908 9909]

for i in categoryU:
    T = len(transactions_data.loc[ transactions_data['category'] == i ])
    U = len(transactions_data.loc[ transactions_data['category'] == i ].id.unique())
    if T != 0:
        listP.append((T - U)/ T)

print(str((sum(listP)/len(listP))*100)+"%")
#50.51997013626925%
print(listP)
# [0.12727272727272726, 0.37376721860315026, 0.325, 0.33488372093023255,
#  0.5, 0.5912961210974456, 0.2962962962962963, 0.32973805855161786,
#  0.07246376811594203, 0.7745509600165165, 0.628560620389635,
#  0.683894544505351, 0.771366581286726, 0.7312187190366098,
#  0.554006968641115, 0.4715274081958489, 0.37760607168983173,
#  0.6404286770140428, 0.8277777777777777, 0.7387704402204891,
#  0.0625, 0.33980582524271846, 0.49645390070921985, 0.5025641025641026,
#  0.25, 0.47619047619047616, 0.0, 0.16981132075471697, 0.0, 0.5493653401421053,
#  0.40890804597701147, 0.18122977346278318, 0.2845714285714286,
#  0.39162772956994374, 0.432960187205515, 0.38866590937776097,
#  0.4487654320987654, 0.44639600729436607, 0.23692523692523693,
#  0.24358974358974358, 0.5199541741382746, 0.291005291005291,
#  0.42271712106527326, 0.43959633181190066, 0.4850090493427319
#  , 0.5802350634630505, 0.46601256893677057, 0.6398141354854487,
#  0.42986265993661227, 0.6121295185883159, 0.14922571562646644,
#  0.08333333333333333, 0.7762088841036551, 0.7412119546348802,
#  0.4080604534005038, 0.6564930396706098, 0.6418676133165938,
#  0.6113039996127562, 0.4223512336719884, 0.5501267984350907,
#  0.7225193356687339, 0.5483162149922003, 0.38719010325734526,
#  0.5931616033267876, 0.5766258471049815, 0.6785714285714286,
#  0.8460465589102368, 0.13333333333333333, 0.6040609137055838,
#  0.22580645161290322, 0.7832919434405432, 0.6931477869055142,
#  0.06666666666666667, 0.771197105796138, 0.6320896190518823,
#  0.7057029128380641, 0.5869289812951785, 0.6755948380158624,
#  0.5769225084615498, 0.7622689348581734, 0.793264399428783,
#  0.5967261904761905, 0.6731275747957047, 0.5971232971440426,
#  0.8248132568611939, 0.5912199934232161, 0.5769509543367963,
#  0.7344123438138521, 0.5140769020168527, 0.4483870967741935,
#  0.4332853504595283, 0.3684210526315789, 0.4616252821670429,
#  0.7617758862903892, 0.3810810810810811, 0.6603032004491859,
#  0.6397923875432526, 0.5210357449500655, 0.7430340557275542,
#  0.49198822759973837, 0.5123804415839814, 0.5341995385122514,
#  0.5451157011958379, 0.5782060336999294, 0.5, 0.6774032548017788,
#  0.631223527381457, 0.24650660569105692, 0.7554763470942074,
#  0.7306542635034236, 0.40555555555555556, 0.5546936976641692,
#  0.44806007509386736, 0.8219290275638682, 0.7600039794835515,
#  0.47147642270778733, 0.6709974412248445, 0.6941272612045675,
#  0.3179791976225854, 0.23748544819557627, 0.599336518494758,
#  0.35714285714285715, 0.11475409836065574, 0.6539979231568016,
#  0.6147110332749562, 0.37914452037458873, 0.5416479297104708,
#  0.5924856437020434, 0.5396208070004861, 0.597149710737971,
#  0.5617888330246097, 0.4801412180052957, 0.7060347060347061,
#  0.5519246190858059, 0.5998162039708491, 0.7429855739075893,
#  0.5883180858550316, 0.7851922661815042, 0.28787205686361617,
#  0.5714285714285714, 0.45, 0.5230565077960854, 0.6385542168674698,
#  0.4914853612677948, 0.6654967675620114, 0.7737078227196524,
#  0.7676914021822792, 0.5038167938931297, 0.48846153846153845,
#  0.707942558859841, 0.42264515649394097, 0.705861629766131,
#  0.58214949795463, 0.7505375120149744, 0.1925272444213804,
#  0.7855530474040632, 0.5609271523178808, 0.4550947541884098,
#  0.29839704069050554, 0.5768063145112325, 0.7546722040937407, 0.0,
#  0.5757575757575758, 0.7209775967413442, 0.4700493305144468,
#  0.4264705882352941, 0.5859705792483304, 0.6792524952219154,
#  0.8185780669144982, 0.7503922355602584, 0.5894192696876375,
#  0.3940551235448396, 0.19607843137254902, 0.5379158512720157,
#  0.0, 0.5197943015320002, 0.1473063973063973, 0.20351676978183003,
#  0.2136299984440641, 0.2157545080670674, 0.5656754941130715,
#  0.6816071085854964, 0.2182350787257415, 0.4840173136124806,
#  0.5667563651417926, 0.3397548161120841, 0.4858784107228339,
#  0.258979004582756, 0.0, 0.5804694238888637, 0.5446197991391679,
#  0.6754279728977775, 0.16184971098265896, 0.435847208619001,
#  0.8063973063973064, 0.7954290835760699, 0.721832286664204,
#  0.6409010600706714, 0.232, 0.7068965517241379, 0.8229957415293464,
#  0.2622298065984073, 0.14977973568281938, 0.04, 0.0, 0.3111760409057706,
#  0.6144931488172336, 0.7208692394155114, 0.8941857928551108]

# =============================================================================
# 4)What is the percentage of customers who did multiple transactions  on different category
# =============================================================================
import os
import pandas as pd

'''oneGbBrand'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id', 'category'])
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
        T=len(t_df.category)
        U=len(t_df.category.unique())
        listP.append((T-U)/T)

print(str((sum(listP)/len(listP))*100))
#57.486209607495056

'''oneGbCategory'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id', 'category'])
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
        T=len(t_df.category)
        U=len(t_df.category.unique())
        listP.append((T-U)/T)

print((sum(listP)/len(listP))*100)
#73.01150828346093

'''oneGbCompany'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id', 'category'])
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
        T=len(t_df.category)
        U=len(t_df.category.unique())
        listP.append((T-U)/T)

print((sum(listP)/len(listP))*100)
#56.29765950594251
   




# =============================================================================
# 5)What is the percentage of customers who did multiple transactions
# =============================================================================
import os
import pandas as pd

'''oneGbBrand'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id'])
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
#96.73013006619755%


'''oneGbCategory'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id'])
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
#97.97611797714599%

'''oneGbCompany'''

listP=[]

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id'])
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
#98.04349170850388%



# =============================================================================
# 6)Do customers change brand while repeat purchasing in same product category, what percentage?
# =============================================================================

import os
import pandas as pd

'''oneGbBrand'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id','category','brand'])
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
f=open("id_changBrandOverSamCategoryBRAND.csv","w")

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
print("done!")

'''oneGbCategory'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id','category','brand'])
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
f=open("id_changBrandOverSamCategoryCATEGORY.csv","w")

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
print("done!")

'''oneGbCompany'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id','category','brand'])
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
f=open("id_changBrandOverSamCategoryCOMPANY.csv","w")

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
print("done!")


import os
import pandas as pd
from collections import defaultdict

'''oneGbBrand'''

dic=defaultdict(int)

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("id_changBrandOverSamCategoryBRAND.csv",usecols = ['id','changBrandOverSamCategory'])
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
#0.024991480177212314%

print("for N ")
print(str((dic["N"]/total)*100)+"%")
#98.4687038509599%

print("for C ")
print(str((dic["C"]/total)*100)+"%")
#1.5063046688628876%

dic.clear()

'''oneGbCategory'''

dic=defaultdict(int)

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("id_changBrandOverSamCategoryCATEGORY.csv",usecols = ['id','changBrandOverSamCategory'])
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
#39.81670241619542%

print("for N ")
print(str((dic["N"]/total)*100)+"%")
#45.65031642764709%

print("for C ")
print(str((dic["C"]/total)*100)+"%")
#14.532981156157486%

dic.clear()

'''oneGbCompany'''

dic=defaultdict(int)

print("data is loading...",_)
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("id_changBrandOverSamCategoryCOMPANY.csv",usecols = ['id','changBrandOverSamCategory'])
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
#0.019022105271500923%

print("for N ")
print(str((dic["N"]/total)*100)+"%")
#99.6908907893381%

print("for C ")
print(str((dic["C"]/total)*100)+"%")
#0.29008710539038907%

dic.clear()



# f=open("id_changBrandOverSamCategory.csv","w")

# fl=True

# for _ in range(11):
#     f1=open("id_changBrandOverSamCategory"+str(_)+".csv","r")
#     line = f1.readline()
#     while line:
#         if fl:
#             f.write(line)
#             fl=False
#         else:
#             if line != "id,changBrandOverSamCategory\n":
#                 f.write(line)
#         line = f1.readline()
#     f1.close()

# f.close()
    
# =============================================================================
# 7) Do customers change Company while repeat purchasing in same product category, what percentage?
# =============================================================================

import os
import pandas as pd

'''oneGbBrand'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id','category','company'])
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

print("Created an csv for data id and change company over same Category")
f=open("id_changCompanyOverSamCategoryBRAND.csv","w")

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
print("done!")

'''oneGbCategory'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id','category','company'])
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
f=open("id_changCompanyOverSamCategoryCATEGORY.csv","w")

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
print("done!")

'''oneGbCompany'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id','category','company'])
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

print("Created an csv for data id and change company over same Category")
f=open("id_changCompanyOverSamCategoryCOMPANY.csv","w")

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
print("done!")


import os
import pandas as pd
from collections import defaultdict

'''oneGbBrand'''

dic=defaultdict(int)

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("id_changCompanyOverSamCategoryBRAND.csv",usecols = ['id','changCompanyOverSamCategory'])
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
#0.03617363344051447%

print("for N ")
print(str((dic["N"]/total)*100)+"%")
#98.56310289389067%

print("for C ")
print(str((dic["C"]/total)*100)+"%")
#1.4007234726688103%

dic.clear()

'''oneGbCategory'''

dic=defaultdict(int)

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("id_changCompanyOverSamCategoryCATEGORY.csv",usecols = ['id','changCompanyOverSamCategory'])
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
#37.34510885011084%

print("for N ")
print(str((dic["N"]/total)*100)+"%")
#48.165463536633894%

print("for C ")
print(str((dic["C"]/total)*100)+"%")
#14.489427613255272%

dic.clear()

'''oneGbCompany'''

dic=defaultdict(int)

print("data is loading...",_)
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("id_changCompanyOverSamCategoryCOMPANY.csv",usecols = ['id','changCompanyOverSamCategory'])
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
#0.005217368620136434%

print("for N ")
print(str((dic["N"]/total)*100)+"%")
#99.7860878865744%

print("for C ")
print(str((dic["C"]/total)*100)+"%")
#0.20869474480545736%

dic.clear()


# import os
# import pandas as pd

# for i in range(11):
#     print("data is loading...",i)
#     os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
#     transactions_data = pd.read_csv("t"+str(i)+".csv",usecols = ['id','category','company'])
#     print("Data is loaded")
    
#     print("Data info")
#     transactions_data.info()
    
#     print("Data Size")
#     transactions_data.size
    
#     print("Data Shape")
#     transactions_data.shape
    
#     print("Data Containg Null values count by columns")
#     print(transactions_data.isnull().sum())
    
#     print("Unique depertments...")
#     print(len(transactions_data.company.unique()))
    
#     print("Created an csv for data id and change brand over same Category")
#     f=open("id_changCompanyOverSamCategory123"+str(i)+".csv","w")
    
#     f.write("id,changCompanyOverSamCategory\n")
    
#     for i,t_df_id in transactions_data.groupby(['id']):
#         countY=0
#         countN=0
#         for j,t_df_cat in t_df_id.groupby(['category']):
#             if len(t_df_cat.company.unique())>1:
#                 countY+=1
#             else:
#                 countN+=1
#         if countY > 0 and countN > 0:
#             if countY > countN:
#                 f.write(str(i)+",Y\n")
#             elif countY < countN:
#                 f.write(str(i)+",N\n")
#             elif countY == countN:
#                 f.write(str(i)+",C\n")
    
#     f.close()
#     print("t",str(i),"is done!")

# import os
# import pandas as pd
# from collections import defaultdict

# dic=defaultdict(int)

# for _ in range(11):
#     print("data is loading...",_)
#     os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions")
#     transactions_data = pd.read_csv("id_changCompanyOverSamCategory"+str(_)+".csv",usecols = ['id','changCompanyOverSamCategory'])
#     print("Data is loaded")
    
#     print("Data info")
#     transactions_data.info()
    
#     print("Data Size")
#     transactions_data.size
    
#     print("Data Shape")
#     transactions_data.shape
    
#     print("Data Containg Null values count by columns")
#     print(transactions_data.isnull().sum())
    
#     print("Data Converstion")
#     transactions_data["changCompanyOverSamCategory"]=transactions_data.changCompanyOverSamCategory.astype("category")
    
#     print("Data info")
#     transactions_data.info()
    
#     for i,d_df in transactions_data.groupby(["changCompanyOverSamCategory"]):
#         dic[i]+=len(d_df)

# total=dic["C"]
# total+=dic["N"]
# total+=dic["Y"]

# print("for Y ")
# print(str((dic["Y"]/total)*100)+"%")

# #Answer = 4.968776414703207%

# print("for N ")
# print(str((dic["N"]/total)*100)+"%")

# #Answer = 94.80978199734528%

# print("for C ")
# print(str((dic["C"]/total)*100)+"%")

# #Answer = 0.22144158795152066%


# f=open("id_changCompanyOverSamCategory.csv","w")

# fl=True

# for _ in range(11):
#     f1=open("id_changCompanyOverSamCategory"+str(_)+".csv","r")
#     line = f1.readline()
#     while line:
#         if fl:
#             f.write(line)
#             fl=False
#         else:
#             if line != "id,changCompanyOverSamCategory\n":
#                 f.write(line)
#         line = f1.readline()
#     f1.close()

# f.close()

# =============================================================================
# 8) Is there is a fixed or almost same duration between repeat purchases by customers for a specific product
# =============================================================================

# =============================================================================
# 9) What is percentage of product returns?
# =============================================================================

#NO ANSWER

# =============================================================================
# 10)   Are the product returns from the similar customers , similar category, or a similar brand?
# =============================================================================

#NO ANSWER

# =============================================================================
# 11) How many repeat transaction of set of category, company, brand are done at same chain
# =============================================================================
import os
import pandas as pd

'''oneGbBrand'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbBrand.csv", usecols = ['id','category','company','brand','chain'])
print("Data is loaded")

print("Data info")
transactions_data.info()

print("Data Size")
transactions_data.size

print("Data Shape")
transactions_data.shape

print("Data Containg Null values count by columns")
print(transactions_data.isnull().sum())

listp=[]

for i,t_df_id in transactions_data.groupby(['id']):
    for j,t_df_category in t_df_id.groupby(['category']):
        for k,t_df_company in t_df_category.groupby(['company']):
            for l,t_df_brand in t_df_company.groupby(['brand']):
                T=len(t_df_brand.chain)
                U=len(t_df_brand.chain.unique())
                listp.append((T-U)/T)

print(str((sum(listp)/len(listp))*100)+"%")
#34.58962092272587%
'''oneGbCategory'''

print("data is loading...") 
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCategory.csv", usecols = ['id','category','company','brand','chain'])
print("Data is loaded")

print("Data info")
transactions_data.info()

print("Data Size")
transactions_data.size

print("Data Shape")
transactions_data.shape

print("Data Containg Null values count by columns")
print(transactions_data.isnull().sum())

listp=[]

for i,t_df_id in transactions_data.groupby(['id']):
    for j,t_df_category in t_df_id.groupby(['category']):
        for k,t_df_company in t_df_category.groupby(['company']):
            for l,t_df_brand in t_df_company.groupby(['brand']):
                T=len(t_df_brand.chain)
                U=len(t_df_brand.chain.unique())
                listp.append((T-U)/T)

print(str((sum(listp)/len(listp))*100)+"%")
#33.271037105467194%
'''oneGbCompany'''

print("data is loading...")
os.chdir("D:\\Final project\\Datasets\\acquire-valued-shoppers-challenge\\transactions\\One GB parts")
transactions_data = pd.read_csv("oneGbCompany.csv", usecols = ['id','category','company','brand','chain'])
print("Data is loaded")

print("Data info")
transactions_data.info()

print("Data Size")
transactions_data.size

print("Data Shape")
transactions_data.shape

print("Data Containg Null values count by columns")
print(transactions_data.isnull().sum())

listp=[]

for i,t_df_id in transactions_data.groupby(['id']):
    for j,t_df_category in t_df_id.groupby(['category']):
        for k,t_df_company in t_df_category.groupby(['company']):
            for l,t_df_brand in t_df_company.groupby(['brand']):
                T=len(t_df_brand.chain)
                U=len(t_df_brand.chain.unique())
                listp.append((T-U)/T)

print(str((sum(listp)/len(listp))*100)+"%")
#34.1923108100886%