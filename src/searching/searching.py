def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Figure out size of the array
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Find midpoint
        mid = (left + right) // 2

        # Check if midpoint is our target
        if arr[mid] == target:
            return mid

        # Check to see if target is on the left or right
        if arr[mid] < target:
            # Remove left side and update index
            left = mid + 1

        else:
            # Remove right side and update index
            right = mid -1
    

    return -1  # not found
