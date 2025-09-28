arr = [1,3,2,6,3,5]

    
for i in range(len(arr)):
    min_index = i + arr[i:].index(min(arr[i:]))
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
print(arr) 