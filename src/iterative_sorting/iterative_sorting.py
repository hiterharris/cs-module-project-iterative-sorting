# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # Loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Find next smallest element
        for j in range(i + 1, len(arr)): 
            if arr[smallest_index] > arr[j]: 
                smallest_index = j  

        # Swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1)  :
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    output = [0 for i in range(256)] 
    count = [0 for i in range(256)] 
    ans = ["" for _ in arr] 
  
    for i in arr: 
        count[ord(i)] += 1
  
    for i in range(256): 
        count[i] += count[i-1] 
  
    for i in range(len(arr)): 
        output[count[ord(arr[i])]-1] = arr[i] 
        count[ord(arr[i])] -= 1
  
    for i in range(len(arr)): 
        ans[i] = output[i] 


    return arr
