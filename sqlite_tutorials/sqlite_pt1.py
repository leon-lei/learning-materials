import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(34343433, '2018-07-08 00:00:01', 'Java', 42)")
    conn.commit()    #call anytime you update db
    c.close()
    conn.close()

create_table()
data_entry()