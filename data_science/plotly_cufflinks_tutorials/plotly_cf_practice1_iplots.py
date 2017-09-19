# https://github.com/santosjorge/cufflinks

import pandas as pd
import numpy as np
import plotly
import cufflinks as cf

# For offline use
cf.go_offline()

# Setting up 2 dataframes
df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Category':['A','B','C'], 'Values':[32,43,50]})
print(df2.head())

# Creates an interactive temporary plot html file in the working directory
plotly.offline.plot(df.iplot(asFigure=True))

# Scatter Plot
plotly.offline.plot(df.iplot(kind='scatter', x='A', y='B', mode='markers', size=10, asFigure=True))

# Bar Plots
plotly.offline.plot(df2.iplot(kind='bar', x='Category', y='Values', asFigure=True))
# With aggregator function
plotly.offline.plot(df.sum().iplot(kind='bar', asFigure=True))

# Box Plot
plotly.offline.plot(df.iplot(kind='box', asFigure=True))

# 3D Surface
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
plotly.offline.plot(df3.iplot(kind='surface', colorscale='rdylbu', asFigure=True))

# Spread
# Good for financial data and comparing between 2 stocks
plotly.offline.plot(df[['A','B']].iplot(kind='spread', asFigure=True))

# Histogram
# Single Column
plotly.offline.plot(df['A'].iplot(kind='hist', bins=25, asFigure=True))
# All of the dataframe
plotly.offline.plot(df.iplot(kind='hist', bins=25, asFigure=True))

# Bubble Plot
plotly.offline.plot(df.iplot(kind='bubble', x='A', y='B', size='C', asFigure=True))

# Scatter Matrix
# Similar to Seaborn's PairPlot
plotly.offline.plot(df.scatter_matrix(asFigure=True))