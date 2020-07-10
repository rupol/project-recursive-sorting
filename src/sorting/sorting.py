# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * (elements)
    left = right = index = 0
    # for each item in the subarrays
    while left < len(arrA) and right < len(arrB):
        # compare each value of each subarray, starting with the first
        # if the value in the left array is lower, put that value in the merged array
        if arrA[left] <= arrB[right]:
            merged_arr[index] = arrA[left]
            left += 1
        # if the value in the right array is lower, put that value in the merged array
        else:
            merged_arr[index] = arrB[right]
            right += 1
        index += 1
    # add the leftovers in left and right to the merged array
    while left < len(arrA):
        merged_arr[index] = arrA[left]
        left += 1
        index += 1
    while right < len(arrB):
        merged_arr[index] = arrB[right]
        right += 1
        index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # base case: array with one element
    if len(arr) <= 1:
        return arr

    # recursive case: divide in half until subarrays have only one element
    # find the middle point
    # divide the array in half
    arrA = arr[:len(arr)//2]
    arrB = arr[len(arr)//2:]
    # call merge on each half, recursively
    # the recursion will break the arrays up until they are only one value
    return merge(merge_sort(arrA), merge_sort(arrB))


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    return start, mid, end


def merge_sort_in_place(arr, l, r):
    # Your code here
    return arr
