# Code being referenced from pynative.com
import mysql.connector

from decouple import config
from mysql.connector import Error
from typing import Optional

MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')

# Use dict to keep MySQL Connection arguments
connection_config_dict = {
    'host': '127.0.0.1',
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'database': 'pets',
    'raise_on_warnings': True,
    'use_pure': False,
    'autocommit' : False,
    'pool_size' : 5,
    'connection_timeout': 180
}

def main(run:str, params: Optional[dict] = None):
    try:
        connection = mysql.connector.connect(**connection_config_dict)
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print(f'Connected to MySQL database... MySQL Server version on {db_Info})')

            # cursor = connection.cursor(buffered=True) # need to set True to avoid MySQL Unread result error
            cursor = connection.cursor(prepared=True)

            if run == 'global_connect':
                # global connection timeout args 
                global_connect_timeout = 'SET GLOBAL connect_timeout=180'
                global_wait_timeout = 'SET GLOBAL connect_timeout=180'
                global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

                cursor.execute(global_connect_timeout)
                cursor.execute(global_wait_timeout)
                cursor.execute(global_interactive_timeout)

                connection.commit()

            elif run == 'vars_query_params':
                # use variables as query parameters
                sql_query = '''select * from python_developers where id = %s'''
                _id = params['id']
                cursor.execute(sql_query, (_id, ))
                records = cursor.fetchall()
                print(records)

            elif run == 'fetchmany':
                sql_query = 'select * from python_developers'
                cursor.execute(sql_query)
                
                fetching_size = params['fetching_size']
                records = cursor.fetchmany(fetching_size)
                for r in records:
                    print(f'Id = {r[0]}')
                    print(f'Name = {r[1]}')
                    print(f'Join Date = {r[2]}')
                    print(f'Salary = {r[3]}','\n')
                
            elif run == 'fetchone':
                sql_query = 'select * from python_developers'
                cursor.execute(sql_query)
                
                record = cursor.fetchone()
                salary = float(record[3])
                print(f'Salary: {salary}')

            elif run == 'insert_record':
                sql_query = 'INSERT INTO python_developers (name, join_date, salary) VALUES (%s, %s, %s)'

                insert_tuple = (params['name'], params['join_date'], int(params['salary']))
                result = cursor.execute(sql_query, insert_tuple)
                connection.commit()
                print('Record inserted successfully')
    except Error as e:
        print(f'Error while connection to MySQL {e}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed')

if __name__ == '__main__':

    params = {
        'id': 1,
        'name': 'Beta',
        'join_date': '2018-11-11',
        'salary': '69000',
        'fetching_size': 8
    }

    main(run='fetchmany', params=params)
