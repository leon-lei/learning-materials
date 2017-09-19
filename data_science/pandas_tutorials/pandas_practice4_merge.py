import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# Concat does not merge data, simply adds the data frames on top of each other
concat = pd.concat([df1, df2, df3])
print(concat)

# Append will still not merge the data to share the same index
df4 = df1.append(df3)
print(df4)
# Appends the series/row into the data frame
s = pd.Series([80, 2, 50], index = ['HPI', 'Int_rate', 'US_GDP_Thousands'])
df5 = df1.append(s, ignore_index = True)
print(df5)

# Join will still create some duplicate data
joined = df1.join(df3)
print(joined)


# Merge will effectively combine both dataframes
df_merged1 = pd.merge(df1,df3)    # Not specifying what to merge on will merge on intersection of columns

df_merged2 = pd.merge(df1,df3,    # If you want to specify with the on=parameter, only pass in values that both dataframes share
                      on=['HPI','Int_rate'])

df_merged3 = pd.merge(df1, df3, on = 'HPI', how='inner')
df_merged3.set_index('HPI', inplace=True)
print(df_merged3)
