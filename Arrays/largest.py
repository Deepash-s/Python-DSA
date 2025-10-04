arr = [3, 2, 1, 5, 2, 7]

largest = arr[0]

for i in range(1, len(arr)):
    if(arr[i]>largest):
        largest = arr[i]
        
print("Largest:",largest)