'''
Created on 2021年3月14日

@author: Harry
'''
# -*- coding=UTF-8 -*-

import numpy as np
import tushare as ts
from datetime import datetime

def GetProObject():
    ts.set_token('f525ae8bdefeb8cff71d99a27dd637d89b98ea966a65c798ff8c3549')
    pro = ts.pro_api()
    return pro
       
def DataformToList(data):
    return np.array(data).tolist()

def StrToDate(str):
    return datetime.strptime(str,'%Y%m%d')
    
    