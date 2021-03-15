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
        
#         self.logger = LoggerFactory.getLogger("DBConnection")
            
            
    def CreateConnectionPool(self):
        
        try:
            PooledDB.
            pool = PooledDB.PooledDB(pymysql,mincached=self.__mincached, maxconnections=self.__maxconn, maxcached=self.__maxcached,
                                     user=self.__username, passwd=self.__password, host=self.__hostname, port=self.__port, db=self.__db,charset=self.__charset)

                               
            return pool
         
        except Exception, e:
            
            LoggerFactory.error("CreateConnectionPool", "Failed to create connection pool with exception: " + str(e))
#             self.logger.error("Failed to create connection pool with exception: " + str(e) )
              
            return None
 
     
    def CreateConnection(self):
              
        try: 
            conn = pymysql.connect(host=self.__hostname, user=self.__username, passwd=self.__password, db=self.__db, port=self.__port)
           
            return conn
        
        except Exception, e: 
            
            LoggerFactory.error("CreateConnection", "Failed to create DB connection with exception error: " + str(e))
#             self.logger.error( "Failed to create DB connection with exception error: " + str(e) )
            
            return None
    
        
   
if __name__=='__main__':

    sqldbhandle = DBConnection()
      
    pool = sqldbhandle.CreateConnectionPool()
    
    mytime = "str_to_date('%s'," % time.strftime('%Y-%m-%d') + "'%Y-%m-%d')"
    
    sql_rtstock = "select count(*) from rtstocks where mtime >= %s" % mytime
    
    if pool is not None: 
         
        conn = pool.connection()
            
        cur = conn.cursor()
               
        cur.execute(sql_rtstock)
                 
        results = cur.fetchall()
                 
        print results 
                 
        cur.close()
        conn.close()
     

