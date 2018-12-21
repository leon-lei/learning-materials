# It returns location of x in given array arr if present,
# else returns -1

def binarySearch(arr, left, right, x):

    while left <= right:

        mid = int(left + (right - left)/2)

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1

        # if x is smaller, ignore right half
        else:
            right = mid - 1

    # if we reach here, then the element was not present
    return -1

### Test
arr = [2, 3, 4, 10, 40, 55, 90, 122, 199]
x = 122

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print('Element is present at index {}'.format(result))
else:
    print('Element is not present in array')

print('Done')