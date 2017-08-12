import pickle

# create a dictionary object for pickling
example_dict = {1:'curry',
                2:'ramen',
                3:'nikuman'}

# create a pickle file with write binary
pickle_out = open('dict.pickle','wb')

# dump the object into the pickle file
pickle.dump(example_dict, pickle_out)

# close the pickle file
pickle_out.close()

# opening a pickle file with read binary
pickle_in = open('dict.pickle','rb')

# load the content of the pickle file into an object
example_dict = pickle.load(pickle_in)

print(example_dict)
print(example_dict[2])