# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:43:52 2020

@author: outsi
"""

import os
import json
import random
import pickle
import pandas as pd
import numpy as np
import requests
from flask import Flask, request,render_template,jsonify

app = Flask(__name__,template_folder='template')
model = pickle.load(open('.\\MLModel\\NuralNetworkModel.sav','rb'))
model2 = pickle.load(open('.\\MLModel\\finalized_Decision_Tree_80+20_split.sav','rb'))

@app.route("/discount_model",methods=['POST'])
def dis_prediction_model():
    pidDic={31 : 101,32 : 107,33 : 112,34 : 108,35 : 106,36 : 102,37 : 109,38 : 103,39 : 111,40 : 104,41 : 110,42 : 105}
    woocomm=request.get_json()
    user = '' #add security code.
    url = 'http://localhost/wordpress/wp-json/ld/v1'
    headers = {'SecurityKey':user}
    r = requests.post(url + '/posts/'+str(woocomm['id'])+'?pid='+str(woocomm['product_c']), headers=headers)
    ip=r.json()
    print(ip)
    Freq=len(ip)
    code=0
    if Freq!=0:
        LstPD=[]
        Pamt=0
        for i in ip:
            LstPD.append(i['date_time'])
            Pamt+=int(i['price'])
        
        df=pd.DataFrame({'Date':LstPD})
        df['Date'] =pd.to_datetime(df.Date)
        df.Date=df.sort_values(by='Date')
        Todydf=pd.DataFrame({"date":[pd.datetime.now().date()]})
        Todydf['date'] =pd.to_datetime(Todydf.date)
        Todydf.date=Todydf.sort_values(by='date')
        r=(Todydf.date.sub(df.iloc[Freq-1].Date)/np.timedelta64(1,'D')).iloc[0]
        tdf=pd.DataFrame({"Recency":[r],"Frequency":[Freq],"Monetary":[Pamt],"CCategory_int":[pidDic[int(woocomm['product_c'])]]})
        result1 = model.predict(tdf)
        result = model2.predict(tdf)
        r = requests.post(url + '/discount/'+str(woocomm['product_c']), headers=headers)
        rlt=r.json()
        print(result1,"Nural Network")
        print(result,"RESULT")
        resp=0
        if result[0]==3:
            code=int(ip[0]['lastOfferCode'])
            resp=0
        elif result[0]==1 and int(ip[0]['lastOfferCode'])%10<3:
            code=int(ip[0]['lastOfferCode'])+1
            resp=rlt[0]["0"]
        elif result[0]==2 and (int(ip[0]['lastOfferCode'])//10)%10<2:
            code=int(ip[0]['lastOfferCode'])+10
            resp=rlt[0]["1"]
        elif result[0]==0 and (int(ip[0]['lastOfferCode'])//100)%10<1:
            code=int(ip[0]['lastOfferCode'])+100
            resp=rlt[0]["2"]
        elif int(ip[0]['lastOfferCode'])>100:
            code=0
            resp=0
        return jsonify({"response":resp,"code":code})
    r = requests.post(url + '/code/'+str(woocomm['id'])+'?pid='+str(woocomm['product_c']), headers=headers)
    rlt=r.json()
    print(rlt,"CODE")
    code=0
    if len(rlt)>=1:
        code=rlt[0]['lastOfferCode']
    return jsonify({"response":0,"code":code})
    


if __name__ == '__main__':
    app.run()
        
    
