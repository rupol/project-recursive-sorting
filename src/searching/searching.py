# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # make sure the array has a length
    if start <= end:
        middle_index = (start + end) // 2
        # base case: target is the middle
        if arr[middle_index] == target:
            return middle_index
        # recursive case: target is not the middle (move low or high)
        elif arr[middle_index] < target:
            # middle is less than target: item right of middle becomes new start (look to RHS)
            return binary_search(arr, target, middle_index + 1, end)
        else:
            # middle is greater than target: item left of middle becomes new end (look to LHS)
            return binary_search(arr, target, start, middle_index - 1)
    else:
        return -1  # not found


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, -2, 0, len(arr1)-1))
print(binary_search(arr1, 0, 0, len(arr1)-1))
print(binary_search(arr1, 1, 0, len(arr1)-1))
print(binary_search(arr1, 4, 0, len(arr1)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    return -1
