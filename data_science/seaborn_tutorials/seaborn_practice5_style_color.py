import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

# Data Set
tips = sns.load_dataset('tips')
# total_bill | tip | sex | smoker | day | time | size
# 16.99 | 1.01 | Female | No | Sun | Dinner | 2

# Style
# {darkgrid, whitegrid, dark, white, ticks}
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)

# Removing spines from the plot
sns.despine()

# Setting Context
# "paper", "talk", and "poster"
sns.set_context('poster', font_scale=3)

# Colormap
# https://matplotlib.org/examples/color/colormaps_reference.html
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', size=2, aspect=4,
           palette='inferno')

plt.show()
