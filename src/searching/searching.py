def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)
    return -1   # not found
# array = [2,3,4,1,8,9,0]
# print(linear_search(array,9))

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    # Your code here
    lower_index = 0  # set the lower index
    highest_index = len(arr)-1 # set the higher index 
    print(len(arr)) # 8
    print(highest_index) # 7
    while lower_index <= highest_index: # until there is only one item in the list do:
        #  used // that divides with integral result (discard remainder)
        middle_index = (lower_index + highest_index) // 2 
        # check if the element of the arr with the middle_index is equal to the target
        if arr[middle_index] == target:
            # if it is return the index
            return middle_index
        # because we use a binary tree the values are sorted 
        # else check if if the value of the element at arr[middle index] is biger than the target
        elif arr[middle_index] > target:
            # set the highest_index to be equal to the middle_index - 1 to go left
            highest_index = middle_index - 1
        else:
            # set the lower_index to be equal to the middle_index + 1 to go right
            lower_index = middle_index + 1
    return -1 # not found 

array = [2, 3, 4, 1, 8, 9, 0, 7]
print(binary_search(array, 9))
