'''
Created on 2021年3月14日

@author: harry
'''

import TuShare.TSFetchData
from Common import Utility
import tushare as ts
from DataBase.DBConnection import DBConnection

def InsertStockBasicInfo(proObject):
    
    dbops = DBConnection()
        
    data = TuShare.TSFetchData.ts_get_StockBasic(proObject)
    count = 1
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
        
        sql = "insert into ts_stock_basic_info(ts_code,symbol,exchange,name,fullname,market,area,industry,is_hs,list_date)  values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )" \
            %(row['ts_code'], row['exchange'], row['symbol'], row['name'], row['fullname'], row['market'], row['area'], row['industry'], row['is_hs'], ts_list_date) 
            
        dbops.execute_sql(sql)
        
        count = count + 1
        print("have already executed: " + str(count))
        
if __name__=='__main__':
    
    ts.set_token('f525ae8bdefeb8cff71d99a27dd637d89b98ea966a65c798ff8c3549')
    pro = ts.pro_api()
      
    InsertStockBasicInfo(pro)