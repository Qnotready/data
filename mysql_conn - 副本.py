import pymysql
#import pymysql.cursors

connect=pymysql.Connect(
			host='localhost',
			user='test',
			db='test',
			passwd='test',
			port=3306
			)

cursor=connect.cursor()
data=[]
try:
	sql = "select username,password from auth where success=0"
	cursor.execute(sql)
	f=open('ssh密码字典.txt','a+')
	txt=[]
	for tx in open('ssh密码字典.txt'):
		tx1=tx.strip()#去除首尾的空格
		txt.append(tx1)
	data=cursor.fetchall()
	num=cursor.rowcount
	print(num)
	print(40*"-")
	result=[]
	for tmp in data:
		a=tmp[0]+":"+tmp[1]
		result.append(a)
	for temp in list(set(result)):
		if temp not in txt:
			f.write(temp+"\n")
	print(result)
	f.close()
except Exception as e:
	print("%s"%e)


cursor.close()
connect.close()
