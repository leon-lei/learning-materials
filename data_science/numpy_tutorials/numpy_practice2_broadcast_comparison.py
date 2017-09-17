import numpy as np

# numpy arrays differ from lists in the ability to broadcast
print('Demo array broadcast')
print('Creating an array of 25 elements with np.arange')
arr = np.arange(0,25)
print(arr)

print('\n Slice of the array[:6]')
slice = arr[:6]
print(slice)

print('\n Broadcasting 99 to the slice')
slice[:] = 99
print(slice)

print('\n Now display the OG array, which has been modified because of the slice')
print(arr)

# create a copy of the OG array using array.copy
print('\n Copy the original array into its own variable')
arr_copy = arr.copy()
print(arr_copy)

print('\n Edit the copy array now without fear of affecting the OG')
arr_copy[:] = 100
print(arr_copy)

print('\n Displaying the OG')
print(arr)

# indexing a 2D array (matrix)
arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print('\n Displaying a 2D array/matrix \n{}'.format(arr_2d))

# 2 methods of grabbing elements from a matrix
# double bracket
# single bracket with comma
print('\n Double bracket method of grabbing elements from a matrix')
print('arr_2d[0][0]')
print(arr_2d[0][0])

print('\n Single bracket method with comma')
print('arr_2d[1,2]')
print(arr_2d[1,2])

# Slice notation to grab sections of array
print('\n Slice notation to grab sections of array')
print('arr_2d[:3,:2]')
print(arr_2d[:3,:2])

# Comparison operators on arrays
# by assigning the comparison to a boolean array to be passed into the OG array instead of a slice
print('\n Using comparison operators on an array')
arr = np.arange(0,25)
print(arr)
print('\n arr > 5')
print(arr > 5)

# assign the comparison to a boolean array
print('\n Comparison is assigned to a boolean array that is now passed in')
print('arr[bool_arr]')
bool_arr = arr > 5
print(arr[bool_arr])

# alternative and quicker notation
print('\n Alternative notation, arr[arr>5]')
print(arr[arr>5])
