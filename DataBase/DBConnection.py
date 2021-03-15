'''
Created on 2021年3月15日

@author: harry
'''

from dbutils.pooled_db import PooledDB
import pymysql
import string
import datetime
import time

class DBConnection:

    def __init__(self):
        self.__hostname = '127.0.0.1'
        self.__username = 'root'
        self.__password = 'SHr1ng3r'
        self.__port = 3306
        self.__db = 'pystock'
        self.__charset = 'utf8'
        self.__mincached = 5  
        self.__maxcached = 3000 
        self.__maxshared = 3000 
        self.__maxconn = 3000 
        
        try:
            self.pool = PooledDB(pymysql,mincached=self.__mincached, maxconnections=self.__maxconn, maxcached=self.__maxcached,
                                     user=self.__username, passwd=self.__password, host=self.__hostname, port=self.__port, db=self.__db,charset=self.__charset)
        except Exception as e:
#             LoggerFactory.error("CreateConnectionPool", "Failed to create connection pool with exception: " + str(e))
            print("Failed to create connection pool with exception: " + str(e) )
                    
            
    def execute_sql(self,sql):
        
        try:
            conn = self.pool.connection()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            
        except Exception as e:
            cur.close()
            conn.close()
            print("Failed to excute sql statement with exception: " + str(e) )
            print("SQL is: " + sql)
     
    def query_all_data(self,sql):

        try:
            conn = self.pool.connection()
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            
            cur.close()
            conn.close()
            
            return results
            
        except Exception as e:
            cur.close()
            conn.close()
            print("Failed to execute query all data with exception: " + str(e) )
            
            return None
   
    def query_one_data(self,sql):  
        try:
            conn = self.pool.connection()
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchone()
            
            cur.close()
            conn.close()
            
            return results
            
        except Exception as e:
            cur.close()
            conn.close()
            print("Failed to execute one data with exception: " + str(e) )
            
            return None
   
   
if __name__=='__main__':

    sqldbhandle = DBConnection()
      
    pool = sqldbhandle.CreateConnectionPool()
    
    mytime = "str_to_date('%s'," % time.strftime('%Y-%m-%d') + "'%Y-%m-%d')"
    
    sql_rtstock = "select count(*) from ts_stock_basic_info"
    
    if pool is not None: 
         
        conn = pool.connection()
            
        cur = conn.cursor()
               
        cur.execute(sql_rtstock)
                 
        results = cur.fetchall()
                 
        print(results) 
                 
        cur.close()
        conn.close()
     

