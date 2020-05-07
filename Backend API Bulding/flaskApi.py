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
model=pickle.load(open('D:\\Final project\\Program\\MLModel\\finalized_Decision_Tree_80+20_split.sav','rb'))

@app.route("/discount",methods=['POST'])
def test():
    print (request.is_json)
    woocomm=request.get_json()
    print(woocomm)
    
    x =  '{"response":'+str(random.randrange(0,3,1))+'}'
    y = json.loads(x)
    return y
    
@app.route("/discount_model",methods=['POST'])
def dis_prediction_model():
    pidDic={31:100,32:101,33:102,34:103,35:104,36:105,37:106,38:107,39:108,40:109,41:110,42:111}
    #get input
    woocomm=request.get_json()
    user = 'ZDEzZWRkNTllZDk0NjQxN2RjYWZhNmIy'
    #pythonapp = 'G4kN hBNh r35J luXk aXyd n6Lm'
    url = 'http://localhost/wordpress/wp-json/ld/v1'
    #token = base64.standard_b64encode(user + ':' + pythonapp)
    #headers = {'SecurityKey': 'Basic ' + token}
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
        result=model.predict(tdf)
        r = requests.post(url + '/discount/'+str(woocomm['product_c']), headers=headers)
        rlt=r.json()
        print(result,"RESULT")
        resp=0
        if result[0]==3:
            code=int(ip[0]['lastOfferCode'])
            resp=0
        elif result[0]==1 and int(ip[0]['lastOfferCode'])%10<3:
            code=int(ip[0]['lastOfferCode'])+1
            resp=rlt[0][str(result[0])]
        elif result[0]==2 and (int(ip[0]['lastOfferCode'])//10)%10<2:
            code=int(ip[0]['lastOfferCode'])+10
            resp=rlt[0][str(result[0])]
        elif result[0]==0 and (int(ip[0]['lastOfferCode'])//100)%10<1:
            code=int(ip[0]['lastOfferCode'])+100
            resp=rlt[0][str(result[0])]
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
    


# running web app in local machine
if __name__ == '__main__':
    app.run(host='192.168.1.107', port='8099')#in plasc of ... use your ip or domain name to host your server
