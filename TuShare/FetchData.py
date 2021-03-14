'''
Created on 2021年3月14日

@author: Harry
'''
# -*- coding=UTF-8 -*-

import tushare as ts
import numpy as np
from TuShare import Utility


def Get_StockBasic( proOjbect ):
    data = proOjbect.stock_basic()
    return data
 
if __name__=='__main__':
    
    ts.set_token('f525ae8bdefeb8cff71d99a27dd637d89b98ea966a65c798ff8c3549')
    pro = ts.pro_api()
    
    datalist = Utility.DataformToList(Get_StockBasic(pro))
    
    print(datalist)
    
    
    
    