import pymysql

# host/server, user, password, database
conn = pymysql.connect('localhost', 'root', '####', 'beginnerwork')
cur = conn.cursor()

# using variables for inserting into table
timea = 15856605
username = 'pythonista'
tweet = "live from new york, it's SNL"

cur.execute("INSERT INTO ham (time, username, tweet) VALUES (%s,%s,%s)",
                (timea, username, tweet))

cur.execute("""
    CREATE TABLE menu (
        ID INT NOT NULL AUTO_INCREMENT,
        Food VARCHAR(255) NOT NULL,
        Price INT(5) NOT NULL,
        PRIMARY KEY (ID)
    )
""")

conn.commit()

# 2 ways to input the SQL commands
# sql = 'SELECT * FROM ham'
# cur.execute(sql)
cur.execute("SELECT * FROM ham")

# 2 ways to print out the query
# for row in cursor:
#     print(row)
rows = cur.fetchall()
for eachRow in rows:
    print(eachRow)

# always close the database connection
conn.close()

print('\nProgram Complete')
