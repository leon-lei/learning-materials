# string concatenation and formatting

##########
names = ['Leon', 'Shawn', 'Stephen', 'Ibrahim']

# Harrison recommending to use join for 2+ string concatenation
for name in names:
    print('Hello there, ' + name)
    print('-'.join(['Hello there,', name, '5']))


# The reason for this is it scales better. When we use the +, we're creating new strings.
# A more impactful example of this might be if we're just trying to print out a string list of all of the names:
print(', '.join(names))

########## joining file paths
import os

location_of_files = 'C:\\Users\\leonl\\Desktop'
file_name = 'example.txt'

print(location_of_files + '\\' + file_name)

# joins the 2 paths and read the content
with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())


############ string formatting
who = 'Gary'
how_many = 12

# Gary bought 12 apples today!

# incorrect method
print(who, 'bought', how_many, 'apples today!')

# correct method
print('{} bought {} apples today!'.format(who, how_many))