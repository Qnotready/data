#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import mysql.connector

def connect():
    conn=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="123",
        db="test",
        charset="utf8"
    )
    mycursor=conn.cursor()
    return conn,mycursor

def display():
    print("*"*50)
    print("=                银行管理系用 V999                ")
    print("=                    存款(11)                  =")
    print("=                    取款(22)                  =")
    print("=                    查询余额(33)              =")
    print("=                    退出(44)                  =")
    print("*"*50)


def login():
    print("*"*50)
    print("=                    登录(11)                  =")
    print("=                    注册(22)                  =")
    print("=                    退出(33)                  =")
    print("*"*50)
    key=int(input("请输入你的选项：\n"))
    return key

def login_in(conn,mycursor):
    try:
        account=int(input("请输入你的账号："))
        passwd=int(input("请输入你的密码："))
        sql_passwd="select passwd from persion where account=%s"
        mycursor.execute(sql_passwd,(account,))
        results=mycursor.fetchall()
        passwd_re=None
        for tmp in results:
            for passwd_re in tmp:
                pass
        return passwd_re,passwd,account
    except Exception as e:
        print("%s"%e)
        print("请输入正确的格式！！")

def register(conn,mycursor):
    try:
        account = int(input("请输入你要创建的账号："))
        passwd = int(input("请输入你要创建的密码："))
        money=int(input("请输入你初始存入的钱的数量："))
        sql_insert="insert into persion (account,passwd,money) values (%s,%s,%s)"
        value=(account,passwd,money)
        #print(value)
        mycursor.execute(sql_insert,value)
        conn.commit()
        result=mycursor.rowcount
        print(result)
        if result!=0:
            print("恭喜！用户创建成功！！")

    except Exception as e:
        print("%s"%e)
        print("请输入正确的格式！！")


def insert(conn,mycursor,account):
    try:
        money=int(input("请输入你想要存的数字："))
        sql_select="select money from persion where account=%s"
        mycursor.execute(sql_select,(account,))
        results=mycursor.fetchall()
        result=None
        for tmp in results:
            for result in tmp:
                pass
        l_money=money+result
        sql_insert="update persion set money=%s where account=%s"
        value=(l_money,account)
        mycursor.execute(sql_insert,value)
        mycursor.execute(sql_select, (account,))
        conn.commit()
        last_moneys=mycursor.fetchall()
        last_money=None
        for tmp in last_moneys:
            for last_money in tmp:
                pass
        print("你的余额为：%s"%last_money)
    except:
        print("请输入数字！！")

def out_money(conn,mycursor,account):
    try:
        money=int(input("请输入你想要取的钱数量："))
        sql_select="select money from persion where account=%s"
        mycursor.execute(sql_select,(account,))
        results=mycursor.fetchall()
        result=None
        for tmp in results:
            for result in tmp:
                pass
        l_money=result-money
        sql_insert="update persion set money=%s where account=%s"
        value=(l_money,account)
        mycursor.execute(sql_insert,value)
        conn.commit()
        mycursor.execute(sql_select, (account,))
        last_moneys=mycursor.fetchall()
        last_money=None
        for tmp in last_moneys:
            for last_money in tmp:
                pass
        print("恭喜！取款成功！！")
        print("取款数为：%s"%money)
        print("你的余额为：%s"%last_money)
    except:
        print("请输入数字！！")

def select(conn,mycursor,account):
    sql_select = "select money from persion where account=%s"
    mycursor.execute(sql_select, (account,))
    results = mycursor.fetchall()
    result = None
    for tmp in results:
        for result in tmp:
            pass
    print("你的余额为：%s" % result)

def main():
    conn,mycursor=connect()
    while True:
        try:
            display()
            print("请先登录！")
            key=login()
            if key==11:
                passwd_re,passwd,account=login_in(conn,mycursor)
                if passwd_re==passwd:
                    print("恭喜！登录成功！")
                    display()
                    choice = int(input("请输入你的选项：\n"))
                    if choice==11:
                        insert(conn,mycursor,account)
                    elif choice==22:
                        out_money(conn,mycursor,account)
                    elif choice==33:
                        select(conn,mycursor,account)
                    elif choice==44:
                        print("退出成功！谢谢你的使用！")
                        main()
            elif key==22:
                register(conn,mycursor)
            elif key==33:
                break
        except Exception as e:
            print("%s"%e)
            print("请输入正确的选项！！！")


if __name__ == '__main__':
    main()