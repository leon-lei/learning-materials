import sqlite3
import datetime
import random
import time

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(34343433, '2018-07-08 00:00:01', 'Java', 42)")
    conn.commit()    #call anytime you update db
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())   # seconds since epoch 1970-01-01
    date = datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
    (unix, date, keyword, value))

    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    for row in data:
        print(row)

def graph_data():
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-1')
    plt.show()

def del_and_update():
    print('Updating')
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 9')
    conn.commit()

    print('Printing all after update')
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(len(data))
    [print(row) for row in data]

    print(35 * '#')
    print('Deleting')
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(len(data))
    [print(row) for row in data]



# Main
create_table()

# Manual data entry
# data_entry()

# Dynamic data entry
# for i in range(50):
#     dynamic_data_entry()
#     time.sleep(1)

# read_from_db()
# graph_data()
del_and_update()

c.close()
conn.close()

