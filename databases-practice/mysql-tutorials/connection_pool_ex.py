# Code being referenced from pynative.com
import mysql.connector

from mysql.connector import Error
from mysql.connector import pooling
from decouple import config

import pprint
pp = pprint.PrettyPrinter(indent=4)


MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')


try:
	connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name='distinct_pool',
																pool_size=1,
																pool_reset_session=True,
																host='localhost',
																database='pets',
																user=MYSQL_USER,
																password=MYSQL_PASSWORD)

	# details about pool
	pp.pprint(connection_pool.__dict__)

	# Get connection object from a pool
	connection_obj = connection_pool.get_connection()

	if connection_obj.is_connected():
		db_Info = connection_obj.get_server_info()
		print(f'Connected to MySQL database using connection pool ... MySQL Server version on {db_Info}')

		cursor = connection_obj.cursor()
		cursor.execute('select database();')
		record = cursor.fetchone()
		print(f'Connected to {record}')

except Error as e:
	print(e)
finally:
	if connection_obj.is_connected():
		cursor.close()
		connection_obj.close()
		print('MySQL connection closed')

								

