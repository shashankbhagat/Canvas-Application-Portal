"""
File Name: DataAccess.py
Author: Bhavana Vankhede
Date: 12/14/2018
Notes: This implementation file serves as the Data Access layer. The db is contacted for extracting results.
"""
import sqlite3
from contextlib import closing

class DbAccess:
    def __init__(self):         #establishing connection with Db
        try:
            self.conn=sqlite3.connect("CanvasDb.db")            
        except Exception as e:
            print("Error accessing database.\n",str(e))

    def getSingleAnswer(self,query,parameter=()):           #Method for returning only a single record from the Db.
        single_record=()
        with closing(self.conn.cursor()) as cur:
            try:
                
                cur.execute(query,parameter)
                single_record=cur.fetchone()                
            except Exception as e:
                print("error while extracting single record.\n",e)
            return single_record

    def getMultipleAnswers(self,query,parameter=()):            #Method for returning multiple records from the Db.
        multiple_record=()
        with closing(self.conn.cursor()) as cur:
            try:
                print('query:',query,parameter)
                cur.execute(query,parameter)
                multiple_record=cur.fetchall()
            except Exception as e:
                print("error while extracting multiple records.\n",e)
            return multiple_record

    def insertUpdateDelete(self,query,parameter):            #Method for returning multiple records from the Db.
        count_record=0
        #parameter=('11','11',3,1234)
        with closing(self.conn.cursor()) as cur:
            try:
                print('data access',query,parameter)
                x=cur.execute(query,parameter)
                print('x:',x)
                
                return cur.rowcount
                #return cur.lastrowid
                
            except Exception as e:
                print("error while insert records.\n",e)
            finally:
                print('insert success')
            