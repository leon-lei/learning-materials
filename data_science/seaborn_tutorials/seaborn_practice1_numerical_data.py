import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# total_bill | tip | sex | smoker | day | time | size
# 16.99 | 1.01 | Female | No | Sun | Dinner | 2
print(tips.head())

# Looks at distribution of 1 variable (univariate)
# Draws a histogram and fit a kernel density estimate (KDE)
sns.distplot(tips['total_bill'], kde=False, bins=30)

# Matches up 2 distplots by bivariate data
# X,Y are 2 column names from the dataset
# Draws 2 histograms on the sides for their respective axes
# Middle is a scatter plot
# kind=parameters 'hex','reg','kde'
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

# Plots all combo of pairwise relationships across an entire dataframe for numerical columns
# hue=parameter pass in column name of a categorical column
sns.pairplot(tips, hue='sex', palette='coolwarm')

# Draws a dash mark for every point on univariate distribution
# Normal distribution for each rugplot is summed to draw a KDE plot
sns.rugplot(tips['total_bill'])

plt.show()
