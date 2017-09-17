import seaborn as sns
import matplotlib.pyplot as plt

# Data Set
tips = sns.load_dataset('tips')
# total_bill | tip | sex | smoker | day | time | size
# 16.99 | 1.01 | Female | No | Sun | Dinner | 2

# Linear Model Plot
# scatter_kws parameter to adjust size of markers
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','v'],
           scatter_kws={'s':100})

# Create additional plots by column and/or row based on the categorical data selected
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex',row='time')

# Aspect parameter is L x W
sns.lmplot(x='total_bill', y='tip', data=tips, col='day',hue='sex',
           aspect=0.4, size=7)

plt.show()