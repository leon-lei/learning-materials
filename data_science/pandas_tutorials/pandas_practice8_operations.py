import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})

print(df.head())

# Returns all unique values in the column
# array([444, 555, 666])
print('\ndf["col2"].unique()')
print(df['col2'].unique())

# Returns number of unique values in the column
# 3
print('\ndf["col2"].nunique()')
print(df['col2'].nunique())

# Returns the count of each unique value
print('\ndf["col2"].value_counts()')
print(df['col2'].value_counts())

#Select from DataFrame using criteria from multiple columns
print('\ndf[(df["col1"]>2) & (df["col2"]==444)]')
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)

# Applying functions
def times2(x):
    return x*2

df['col1'].apply(times2)

# Alternate method is to use lambdas
print('\ndf["col1"].apply(lambda x: x*2)')
print(df['col1'].apply(lambda x: x*2))

# Deleting a column permanently
del df['col1']

# Columns info
print('\ndf.columns')
print(df.columns)

# Index info
print('\ndf.index')
print(df.index)

# Sort
print('\ndf.sort_values(by="col2", inplace=True)')
print(df.sort_values(by='col2', inplace=True))

# Find Null Values
print('\ndf.isnull()')
print(df.isnull())

# Drop rows with NaN Values
print('\ndf.dropna()')
print(df.dropna())

