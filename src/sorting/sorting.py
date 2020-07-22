# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
    # Your code here
    # compare the smallest of A and B, and drop the smallest in merged_arr[0]:

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case: only two elements:
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        # find the mid of array
        mid = len(arr)//2
        # divide in half
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0
        # copy data to temp arrays L and R
        while i < len(L) and j< len(R):
            if L[i] < R[i]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

