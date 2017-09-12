import numpy as np
# from numpy.random import randint

my_list = [1,2,3,4,5,6]

new_list = [[1,2,3], [4,5,6], [7,8,9]]

# 1D array
print('Casting a premade list into a 1D numpy array')
print(np.array(my_list))

# 2D array, note the extra brackets being displayed
print('\nCasting a list of lists into a 2D numpy array')
print(np.array(new_list))

# similar to regular range function
# (start, stop, step)
print('\n np.arange to create a 1D array from (start, stop, step)')
print(np.arange(0,10,2))

# returns evenly space points between (start, stop, num=50)
# only a 1D array
# example below returns 30 evenly space pts between 0 and 5
print('\n np.linspace to return evenly space arrays from (start, stop, num)')
print(np.linspace(0,5,30))

# arrays of zeros and ones
# 2D arrays as we're passing in tuples
print('\n Zeros and Ones')
print(np.zeros((3,3)))
print()
print(np.ones((3,3)))

# identity matrix - for linear algebra problems
# returns a 2D array with ones on the diagonal and zeros elsewhere
# will square the argument, thus example below is returning a 7x7 array
print('\n Identity Matrix')
print(np.eye(7))

# random.rand
# returns random values in a given shape, not ints
# 1st example is 1D array
# 2nd example is 2D array, note we don't have to pass in tuples as like before
print('\n random.rand as a 1D array')
print(np.random.rand(5))
print('\n random.rand as a 2D array')
print(np.random.rand(5,5))

# random.randn
# returns sample from "Standard Normal"/ Gaussian distribution
# 2D plus arrays no need to pass in tuples either
print('\n Standard Normal/ Gaussian distribution in a 1D array')
print(np.random.randn(7))
print('\n Same Gaussian except in a 2D array if 2 arguments were passed in')
print(np.random.randn(4,4))

# random.randint
# returns 1 random int if size is not specified
# (low, high, size)
print('\n random.randint to return n random ints from (low, high, size)')
print(np.random.randint(0,10,5))

# reshaping an array
# first build a 1D array using np.arange
# then reshape and assign to a new variable
# note that total size of new array must remain the same
# if OG array was only 25 elements, we cannot reshape it into a 5x10 array
print('\n array.reshape on an array created with np.arange(0, 25)')
arr =  np.arange(0,25)
print(arr)
arr2 = arr.reshape(5,5)
print('\n Note reshaping does not alter the original array,\n so we assigned it to a new variable')
print(arr2)
# shape attribute
print('\n the shape of the array is {}'.format(arr2.shape))

# finding max and min
# finding position of the max and min
# finding the type of the array with dtype attribute
randr = np.random.randint(0,100,20)
print('\n finding the max/min of a random array')
print(randr)
print('\nThe max is {} and min is {}'.format(randr.max(), randr.min()))
print('The max of {} is located at position {}'.format(randr.max(), randr.argmax()))
print('The min of {} is located at position {}'.format(randr.min(), randr.argmin()))
print('\nThe type of the array is {}'.format(randr.dtype))