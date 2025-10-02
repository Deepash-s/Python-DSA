arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

def bubbleSort(arr, n):
    swapped = False 
    if n == 1:
        return arr
    for i in range(n-1):
        if (arr[i]>arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True 
    if swapped:
        return bubbleSort(arr, n-1)
    else:
        return arr
    
print(bubbleSort(arr, n))