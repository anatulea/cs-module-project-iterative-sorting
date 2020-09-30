# WILL-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = arr[i]
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(array)):
            # If a smaller element than the cur_index element is found, we re-assign the cur_index element and the minimu index
            if array[j] < cur_index:  
                cur_index = array[j]
                smallest_index = j
         # If cur_index index has changed, i.e, a smaller  element has been found, then we swap that element with the ith element
        if smallest_index  != i: 
            array[smallest_index ], array[i] = array[i], array[smallest_index ]
        # TO-DO: swap
        # Your code here

    return arr

array = [3,2,5,1,0,4]
print(selection_sort(array))




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr

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
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
