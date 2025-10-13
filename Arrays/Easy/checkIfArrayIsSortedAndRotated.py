arr = [3, 4, 5, 1, 2]

def sortedArray(arr):
    n = len(arr)
    rotation = 0
    
    for i in range(n-1):
         if arr[i] > arr[i+1]:
             rotation += 1
        
    if rotation > 1:
        return False
    
    if rotation == 1:
        if arr[n-1] <= arr[0]:
            return True
        else:
            return False
    
    return True
    
    
print(sortedArray(arr))