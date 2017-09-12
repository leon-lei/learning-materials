import quandl
import pandas as pd

# use the api key from the account to access a Freddie Mac database through quandl api
# assign the dataset to a data frame for viewing
api_key = ''
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())

# fiddy_states is a list of data frames
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# printing just the 1st data frame from the list, which contains the state abbreviations
print(fiddy_states[0])

# printing just the 1st column from the 1st data frame
print(fiddy_states[0][0])

# creating the name of the data sets by concatenating
for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_' + str(abbv))
