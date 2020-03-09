f = open("oneGbTransactionsBrand.csv","r")
f1 = open("oneGbBrand.csv","w")
line = f.readline()
while line:
    if len(line)>1:
        f1.write(line)
    line=f.readline()
f.close()
f1.close()
f = open("oneGbTransactionsCategory.csv","r")
f1 = open("oneGbCategory.csv","w")
line = f.readline()
while line:
    if len(line)>1:
        f1.write(line)
    line=f.readline()
f.close()
f1.close()
f = open("oneGbTransactionsCompany.csv","r")
f1 = open("oneGbCompany.csv","w")
line = f.readline()
while line:
    if len(line)>1:
        f1.write(line)
    line=f.readline()
f.close()
f1.close()
