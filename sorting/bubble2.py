#optimized approach
#swapped is set to True if any element is swapped 
#else it's False, which means array is already sorted

arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if (arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    
    if not swapped:
        break
    
print(arr)