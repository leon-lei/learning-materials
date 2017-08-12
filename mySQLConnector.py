import pymysql

conn = pymysql.connect(user='root',password='3510',
                        host='127.0.0.1',port=3306,database='mysql')

print('fine')
