# list comprehension and generator expressions

# example of a list comprehension (one liner for loops)
xyz = [i for i in range(5)]
print(xyz)

# which can also be written out as
abc = []
for i in range(5):
    abc.append(i)
print(abc)

# to go from list comprehension to generator
# change the brackets to parenthesis

xyz = [i for i in range(5)]
print(xyz)
xyz = (i for i in range(5))    # print statement will show a generator object
print(xyz)

# to test the speed of both
xyz = [i for i in range(50000000)]
print('done')
xyz = (i for i in range(50000000))
print(xyz)

# First, with a generator, the values are generated from an original input,
# but the values are not copied and instead are generated on-the-fly.
# This means we will use far less memory, since the entire list is not processed all at once,
# but also means the process is a bit slower, since things are indeed generated as we go.
#
# The list comprehension puts the entire list into memory, so it is faster, but the penalty is memory use

input_list = [5,6,3,15,10,3,7,40,25,33,98,77]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

# note the use of parenthesis instead of brackets to create the generator
xyz = (i for i in input_list if div_by_five(i))

# list comprehension to print. One liner for loops
[print(i) for i in xyz]
