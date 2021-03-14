'''
Created on 2021年3月14日

@author: harry
'''

import TuShare.TSFetchData
from Common import Utility
import tushare as ts

def InsertStockBasicInfo(proObject):
    data = TuShare.TSFetchData.ts_get_StockBasic(proObject)
    for index,row in data.iterrows():
        ts_code=row['ts_code']
        ts_exchange=row['exchange']
        ts_symbol=row['symbol']
        ts_name=row['name']
        ts_fullname=row['fullname']
        ts_market=row['market']
        ts_area=row['area']
        ts_industry=row['industry']
        ts_is_hs=row['is_hs']  
        ts_list_date=Utility.StrToDate(row['list_date'])
        
        print(ts_code,ts_exchange,ts_symbol,ts_name,ts_fullname,ts_market,ts_area)
        
        
if __name__=='__main__':
    
    ts.set_token('f525ae8bdefeb8cff71d99a27dd637d89b98ea966a65c798ff8c3549')
    pro = ts.pro_api()
      
    InsertStockBasicInfo(pro)