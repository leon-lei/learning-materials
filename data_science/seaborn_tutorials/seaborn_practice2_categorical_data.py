import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Categorical Plots

# Data Set
tips = sns.load_dataset('tips')
# total_bill | tip | sex | smoker | day | time | size
# 16.99 | 1.01 | Female | No | Sun | Dinner | 2

# Bar Plot
# To aggregate categorical data based off of some function
# X=Categorical Y=Numerical
# Plot shows mean value for each category
# Estimator=parameter Pass in aggregator function (default=mean)
sns.barplot(x='day', y='tip', data=tips, estimator=np.std)

# Count Plot
# Shows number of occurrences for the categorical column
sns.countplot(x='sex', data=tips)

# Box and Whisker Plot
# Show relationships btwn categorical data
# Hue=parameter Pass in additional categorical column
sns.boxplot(x='day',y='total_bill', data=tips, hue='smoker')

# Violin Plot
# Plots all components that correspond to actual data points
# Essentially showing KDE of underlying distribution
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True, inner='box', scale='count')

# Strip Plot
# Scatter plot base off of the category
# Jitter=parameter Adds some random noise to separate the stack points to allow for clearer view
# Split was renamed to Dodge
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue='sex', dodge=True)

# Swarm Plot
# Combines strip plot and violin plot
# Points are adjusted for no overlap
# Does not scale well for large number and large data sets
# You can overlap a violin plot on top, setting the color of the swarmplot to better outline it
# sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='black')


# Factor Plot
# Most general form, passing in kind parameter adjusts it to the above plots
# Kind=parameter 'bar', 'violin', 'box'
sns.factorplot(x='day', y='total_bill', data=tips, kind='box')

plt.show()