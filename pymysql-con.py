#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pymysql
#import pymysql.cursors

con=pymysql.connect(
                        host='localhost',
                        user='root',
                        db='test',
                        passwd='123',
                        port=3306
                        )

cursor=con.cursor()
data=[]
try:
        sql = "select * from class"
        cursor.execute(sql)
        date=cursor.fetchall()
        print(cursor.rowcount)
        for tmp in date:
            print(tmp)
except Exception as e:
        print("%s"%e)


cursor.close()
con.close()
