import quandl
import pandas as pd
import pickle

api_key = 'ixQ8osz5dtLHpjnuWj51'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = 'FMAC/HPI_' + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(abbv)}, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    # pickling is similar to creating and writing onto a csv
    # pickle_out is the new file, in byte code
    # pickle.dump is the writer
    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state_data()

# pickling using og python module
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
# print(HPI_data)

# pickling using panda module
HPI_data.to_pickle('pandas_pickle.pickle')
HPI_data2 = pd.read_pickle('pandas_pickle.pickle')
print(HPI_data2)