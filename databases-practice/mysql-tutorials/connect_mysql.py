# Code being referenced from pynative.com
import mysql.connector

from decouple import config
from mysql.connector import Error

MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')


try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                        user=MYSQL_USER,
                                        password=MYSQL_PASSWORD)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(f'Connected to MySQL database... MySQL Server version on {db_Info})')

        cursor = connection.cursor()
        cursor.execute('SHOW databases;')
        dbs = cursor.fetchall()
        print('Listing all databases')
        for db in dbs:
            print('\t', db)

except Error as e:
    print(f'Error while connection to MySQL {e}')
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print('MySQL connection closed')
