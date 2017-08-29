import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from matplotlib import style

# importing from csv and outputting to csv
df = pd.read_csv('ZILLOW-Z77002_ZRISFRR.csv')
df.set_index('Date', inplace=True)
print(df.head())
df.to_csv('newcsv2.csv')

# set the index column when opening a csv
df = pd.read_csv('newcsv2.csv', index_col=0)

# renaming original column in data frame
df.columns = ['Houston_SFR']

# rename column in data frame
df.rename(columns={'Houston_SFR':'Houston_family'})

# create csv with no headers
# read a csv with no headers and assign headers and index_col
df.to_csv('newcsv3.csv', header=False)
df = pd.read_csv('newcsv3.csv', names=['Date','Houston_SFR'], index_col=0)

# rename column in data frame
df.rename(columns={'Houston_SFR':'Houston_family'}, inplace=True)

print(df.head())

# save data frame to html
df.to_html('csv_file.html')