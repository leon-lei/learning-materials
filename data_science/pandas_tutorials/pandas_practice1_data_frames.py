import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from matplotlib import style

# plots data frame of yahoo data using matplotlib
style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader("XOM", "yahoo", start, end)
print(df.head())
df['Adj Close'].plot()
plt.show()

# create a data frame from dictionary

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,55,33,64,23,52],
             'Bounce_Rate':[76,47,54,65,66,75]}

df = pd.DataFrame(web_stats)

# head first 5, tail last 5, can set parameter
print(df)
print(df.head())
print(df.tail())
print(df.tail(2))

# set_index creates a new data frame
# can assign it to a variable, df2 = df.set_index('Day')
# or replace the original data frame with inplace
df.set_index('Day', inplace=True)
print(df.head())

# reference a single column of the data frame
print(df['Visitors'])   # or print(df.Visitors)

# reference multiple columns of the data frame. Use list as input
print(df[['Visitors', 'Bounce_Rate']])

# convert to list
print(df.Visitors.tolist())
