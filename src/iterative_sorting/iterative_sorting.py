# WILL-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            # If a smaller element than the cur_index element is found, we re-assign the cur_index element and the minimum index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        # If cur_index index has changed, i.e, a smaller  element has been found, then we swap that element with the ith element
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

# --------Method 2 -----------(selecting by the maximum value)
# def selection_sort(arr):
#     for i in range(len(arr)-1,0,-1):
#         positionOfMax=0
        
#         # For every set of 0 to i+1
#         for location in range(1,i+1):
#             # Set maximum's location
#             if arr[location]>arr[positionOfMax]:
#                 positionOfMax = location

#         temp = arr[i]
#         arr[i] = arr[positionOfMax]
#         arr[positionOfMax] = temp

#     return arr

array = [3,2,5,1,0,4]
print(selection_sort(array))




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("bubble_sort")
array = [3,2,5,1,0,4]
print(bubble_sort(array))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr):
    if len(arr) == 0:
        return []

    max_element = int(max(arr)) 
    min_element = int(min(arr)) 
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual 
    # elements and initialize count array as 0 
    count_arr = [0 for _ in range(range_of_elements)] 
    output_arr = [0 for _ in range(len(arr))] 
  
    # Store count of each character 
    for i in range(0, len(arr)): 
       count_arr[arr[i]-min_element] += 1
  
    # Change count_arr[i] so that count_arr[i] now contains actual 
    # position of this element in output array 
    for i in range(1, len(count_arr)): 
        count_arr[i] += count_arr[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)-1, -1, -1): 
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i] 
        count_arr[arr[i] - min_element] -= 1
  
    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(0, len(arr)): 
        arr[i] = output_arr[i] 
  
    return arr 
print('count')
# array =[]
array = [-3,2,5,1,0,4]
print(counting_sort(array))