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

from flask import Flask, request,render_template,jsonify

app = Flask(__name__,template_folder='template')
model=pickle.load(open('D:\\Final project\\Program\\MLModel\\finalized_model_with_80+20_split.sav','rb'))

@app.route("/discount",methods=['POST'])
def main():
    print (request.is_json)
    woocomm=request.get_json()
    print(woocomm)
    x =  '{"response":'+str(random.randrange(0,3,1))+',"status":200,"mimetype":"application/json"}'
    y = json.loads(x)
    return y
    
@app.route("/discount_model",methods=['POST'])
def predict():
    #get input
    ip=request.get_json(force=True)
    LstPD=[]
    Pamt=0
    Freq=0
    for i in ip['product_h']:
        LstPD.append(i['purchase_date'])
        Pamt+=i['purchase_amount']
        Freq+=1
    df=pd.DataFrame({'Date':LstPD})
    df['Date'] =pd.to_datetime(df.Date)
    df.Date=df.sort_values(by='Date')
    Todydf=pd.DataFrame({"date":[pd.datetime.now().date()]})
    Todydf['date'] =pd.to_datetime(Todydf.date)
    Todydf.date=Todydf.sort_values(by='date')
    r=(Todydf.date.sub(df.iloc[Freq-1].Date)/np.timedelta64(1,'D')).iloc[0]
    tdf=pd.DataFrame({"R":[r],"F":[Freq],"M":[Pamt]})
    result=model.predict(tdf)
    if int(result[0])==0:
        result_L='LOW'
    elif int(result[0])==1:
        result_L='MEDIUM'
    elif int(result[0])==2:
        result_L='HIGH'
    print(result_L)
    output = {'results': result_L}
    print(result)
    return jsonify(results=output)
    


# running web app in local machine
if __name__ == '__main__':
    app.run(host='192.168.43.68', port='8099')#in plasc of ... use your ip or domain name to host your server
