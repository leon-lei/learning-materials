# Python MySQL commands

## Connect to a database
```
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='foobar',
    database='mydatabase' # throws error if doesn't exist
)

mycursor = mydb.cursor()
```

## Create a database
```
mycursor.execute('CREATE DATABASE mydatabase')
```

## Return list of databases
```
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)
```

## Create a table
```
mycursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')
```

## Check if the table exists
```
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)
```

## Delete the table
```
mycursor.execute('DROP TABLE customers')
```

## Alter an existing table
```
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
```

## Insert a record into 'customers' table
```
mycursor = mydb.cursor()

sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('John', 'Highway 21')

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, 'record inserted.')
print(f'ID: {mycursor.lastrowid}')
```

## Insert multiple rows into a table
```
sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = [
    ('Leon', '155 Borden'),
    ('Shawn', '199 Court'),
    ('Jimmy', '1681 East'),
    ('Stephen', '75 Varick'),
    ('Ibrahim', '1 World Trade'),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, 'was inserted.')
```

## Return all records from table (fetchall)
```
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM customers')
myresult = mycursor.fetchall()

for x in myresult:
    print(x
```

## Return one record from table (fetchone)
```
mycursor.execute('SELECT * FROM customers')
myresult = mycursor.fetchone()
```