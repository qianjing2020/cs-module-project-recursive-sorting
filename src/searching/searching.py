# TO-DO: Implement a recursive implementation of binary search
import random
import time

def binary_search(arr, target, start, end):
    # assuming arr is ordered ascendingly    
    # special case
    if start+1 == end:
        if target == arr[start]:
            return start
        elif target ==arr[end]:
            return end      
    # use while loop recursion to search
    while start+1 < end:
        # define middle point
        mid = (start + end) // 2
        # base case
        if target == arr[mid]:
            return mid
        # other cases:
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid)            
        else:
            return binary_search(arr, target, mid, end)
    return -1
        
def descending_binary_search(arr, target, start, end):
    # assume arry is desceinding in order
    # assuming arr is ordered ascendingly
    # special case
    if start+1 == end:
        if target == arr[start]:
            return start
        elif target == arr[end]:
            return end
    while start+1 < end:
        mid = (start + end) // 2
        # base case
        if target == arr[mid]:
            return mid
        # other cases:
        elif target < arr[mid]:
            return descending_binary_search(arr, target, mid, end)            
        else:
            return descending_binary_search(arr, target, start, mid)
    return -1

# lst = list(range(0, 10))
# print(lst)
# random.shuffle(lst)
# target = 4

# start_time = time.time()
# print(binary_search(lst, target, 0, len(lst)))
# print(f'Runtime for recursive binary search is {time.time()-start_time} seconds')

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # question: how to update start end without updating arr? 
    # recursive algorithm
    # decide if the array is ascending or descending    
    start = 0
    end = len(arr)-1
    isascending = (arr[0] <= arr[end])
    # define middle point
    # ascending order, then use above binary search code
    if isascending == True:
        return binary_search(arr, target, start, end)
        
    # else: descending order, different update of start and end
    else:
        return descending_binary_search(arr, target, start, end)
        
    


