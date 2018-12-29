# Code being referenced from pynative.com
import argparse
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

def main(operation:str, params: Optional[dict] = None):
    try:
        connection = mysql.connector.connect(**connection_config_dict)
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print(f'Connected to MySQL database... MySQL Server version on {db_Info})')

            # cursor = connection.cursor(buffered=True) # need to set True to avoid MySQL Unread result error
            cursor = connection.cursor(prepared=True)

            if operation == 'global_connect':
                # global connection timeout args 
                global_connect_timeout = 'SET GLOBAL connect_timeout=180'
                global_wait_timeout = 'SET GLOBAL connect_timeout=180'
                global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

                cursor.execute(global_connect_timeout)
                cursor.execute(global_wait_timeout)
                cursor.execute(global_interactive_timeout)

                connection.commit()

            elif operation == 'parameterized':
                # parameterized query
                sql_query = '''SELECT * FROM python_developers WHERE id = %s'''
                _id = params['id']
                cursor.execute(sql_query, (_id, ))

                records = cursor.fetchall()
                print(records)

            elif operation == 'fetchmany':
                sql_query = 'SELECT * FROM python_developers'
                cursor.execute(sql_query)
                
                fetching_size = params['fetching_size']
                records = cursor.fetchmany(fetching_size)
                for r in records:
                    print(f'Id = {r[0]}')
                    print(f'Name = {r[1]}')
                    print(f'Join Date = {r[2]}')
                    print(f'Salary = {r[3]}','\n')
                
            elif operation == 'fetchone':
                sql_query = 'SELECT * FROM python_developers'
                cursor.execute(sql_query)
                
                record = cursor.fetchone()
                salary = float(record[3])
                print(f'Salary: {salary}')

            elif operation == 'insert_record':
                try:
                    sql_query = 'INSERT INTO python_developers (name, join_date, salary) VALUES (%s, %s, %s)'
                    insert_tuple = (params['name'], params['join_date'], int(params['salary']))
                    result = cursor.execute(sql_query, insert_tuple)

                    connection.commit()
                    print('Record inserted successfully')
                except mysql.connector.Error as e:
                    connection.rollback()    # rollback if any exception occurred
                    print(f'Failed inserting record into python_developers table {e}')

            elif operation == 'insert_many_records':
                try:
                    records_to_insert = params['records']
                    sql_query = 'INSERT INTO python_developers (name, join_date, salary) VALUES (%s, %s, %s)'
                    result = cursor.executemany(sql_query, records_to_insert)

                    connection.commit()
                    print(f'{cursor.rowcount} records inserted successfully into python_developer table')
                except mysql.connector.Error as e:
                    connection.rollback()    # rollback if any exception occurred
                    print(f'Failed inserting multiple records into python_developers table {e}')

            elif operation == 'update_record':
                try:
                    salary, _id = params['update_inputs']
                    print('Before updating record')
                    sql_query = 'SELECT * FROM python_developers WHERE id = %s'
                    cursor.execute(sql_query, (_id,))
                    print(cursor.fetchone())

                    print('Updating record')
                    sql_query = '''UPDATE python_developers SET salary = %s WHERE id = %s'''
                    cursor.execute(sql_query, (salary, _id))
                    connection.commit()

                    print('After updating record')
                    sql_query = 'SELECT * FROM python_developers WHERE id = %s'
                    cursor.execute(sql_query, (_id,))
                    print(cursor.fetchone())
                except mysql.connector.Error as e:
                    connection.rollback()    # rollback if any exception occurred
                    print(f'Failed updating record into python_developers table {e}')


    except Error as e:
        print(f'Error while connection to MySQL {e}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection closed')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Execute a command to the MySQL database')
    parser.add_argument('operation', help='parameterized, fetchmany, fetchone, insert_record')
    args = parser.parse_args()

    params = {
        'id': 5,
        'name': 'Gamma',
        'join_date': '2018-12-27',
        'salary': '80000',
        'fetching_size': 20,
        'records': [
            ('delta', '2011-11-11', 100000),
            ('epsilon', '2015-05-23', 120000),
            ('zeta', '2018-12-30', 50000),
        ],
        'update_inputs': (55000, 1),
    }

    main(operation=args.operation, params=params)
