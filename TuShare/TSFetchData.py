'''
Created on 2021年3月14日

@author: Harry
'''
# -*- coding=UTF-8 -*-

import tushare as ts
import numpy as np


def ts_get_StockBasic( proOjbect ):
    data = proOjbect.stock_basic(list_status='L',fields='ts_code,exchange,symbol,name,fullname,market,area,industry,is_hs,list_date')
    return data
 

def ts_get_trade_cal(proObject,startdate,enddate):
    data = proObject.trade_cal(start_date=startdate,end_date=enddate)
    return data
 
 
def ts_get_daily_by_tradeDay(proObject,tscode,trade_day):
    data = proObject.daily(ts_code=tscode,trade_date=trade_day)
    return data
 
 
def ts_get_daily_by_timePeriod(proObject,tscode,startdate,enddate):
    data = proObject.daily(ts_code=tscode,start_date=startdate,end_date=enddate)
    return data
 
 
if __name__=='__main__':
    
    ts.set_token('f525ae8bdefeb8cff71d99a27dd637d89b98ea966a65c798ff8c3549')
    pro = ts.pro_api()
    
    stock_code=['603005.SH','603002.SH']
    
    for code in stock_code:
    
        print( ts_get_daily_by_timePeriod(pro,code,'20210301','20210310')) 
    
#     datalist = Utility.DataformToList(ts_get_StockBasic(pro))
    
#     print(datalist)
    
    
    
    