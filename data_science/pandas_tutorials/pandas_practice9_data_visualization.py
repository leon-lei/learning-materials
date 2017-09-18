import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')

# Plot Styles
# http://matplotlib.org/gallery.html#style_sheets
# plot_bmh,plot_fivethirtyeight,plot_ggplot
plt.style.use('fivethirtyeight')

# Histogram Plot with pandas
df1['A'].plot.hist(bins=30)

# Area Plot with some transparency through alpha param
df2.plot.area(alpha=0.4)

# Bar Plot
df2.plot.bar(stacked=True)

# Line plot
df1.plot.line(x=df1.index, y='B', figsize=(12,3), lw=1)

# Scatter Plot
# c param setting Color with df1['C']
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')

# Alternate is to show relationship with size and not color
df1.plot.scatter(x='A', y='B', s=df1['C']*100)

# Box Plot
df2.plot.box()

# Hex Bin with bivariate data
df = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])
df.plot.hexbin(x='a', y='b', gridsize=25)

# KDE or Density Plot
df1.plot.kde()

# Same as KDE except now we're plotting just 1 column
df1['A'].plot.density()

plt.show()