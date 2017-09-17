import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Categorical Plots
tips = sns.load_dataset('tips')
# total_bill | tip | sex | smoker | day | time | size
# 16.99 | 1.01 | Female | No | Sun | Dinner | 2

flights = sns.load_dataset('flights')
# year | month | passengers
# 1949 | January | 112

# Heatmap
# Requires Matrix form, which we'll create through correlation data
print(tips.corr())
sns.heatmap(tips.corr(), cmap='coolwarm', annot=True)

# We can also achieve Matrix form through pivot table
pvflights = flights.pivot_table(values='passengers', index='month', columns='year')
sns.heatmap(pvflights, cmap='coolwarm', linecolor='white', linewidths=1)

# Clustermap
# Uses hierarchal clustering to produce a clustered version of the heatmap
# Columns will no longer be in order as they are group by similar values (passenger count)
sns.clustermap(pvflights, cmap='coolwarm', standard_scale=1)

plt.show()