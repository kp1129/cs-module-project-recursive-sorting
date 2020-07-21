# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here

    # return merged_arr


    result = []
    i = 0
    j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            result.append(arrA[i])
            i += 1
        else:
            result.append(arrB[j])
            j += 1
    while i < len(arrA):
        result.append(arrA[i])
        i += 1
    while j < len(arrB):
        result.append(arrB[j])
        j += 1    

    print('merge result', result)
    return result            


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    else:
        mid  = len(arr) // 2

        arrA = merge_sort(arr[:mid])
        arrB = merge_sort(arr[mid:])

        return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

