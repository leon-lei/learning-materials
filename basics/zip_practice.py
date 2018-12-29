# The zip function iterates through multiple iterables, and aggregates them.
# Consider you have two lists, and you instead want them to be one list,
# where elements from the shared index are together.

x = [1, 2, 3, 4]
y = [7, 6 ,2 ,1]
z = ['a', 'b', 'c', 'd']

for a,b,c in zip(x,y,z):
    print(a,b,c)
#
# # zip() is a zip object
# # you can iterate through the items of the zip object
print(zip(x,y,z))
for i in zip(x,y,z):
    print(i)
#
# # you can make it a list as well
print(list(zip(x,y,z)))
#
# # or you can make it into a dictionary with 2 values
print(dict(zip(x,y)))
#
# # list comprehension is possible
print('List Comprehension')
[print(a,b,c) for a,b,c in zip(x,y,z)]
#
# # For Loops stores the variable
# # List Comprehension does not store the variable
print('For Loops vs List Comprehension')
[print(x,y) for x,y in zip(x,y)]
print(x)
# x is still the original list

# change the name of the iterable
# in a list comprehension, a is not stored
[print(a,b) for a,b in zip(x,y)]

# in a for loop, a is stored
for a,b in zip(x,y):
    print(a,b)

print(x)

# thus if your iterable is the same text as your variables being zipped,
# your original variable will be replaced by the iterable
# x is no longer a list, it is the last item within list x being zipped
for x,y in zip(x,y):
    print(x,y)
print(x)
