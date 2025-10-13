arr = [3, 2, 1, 5, 2, 7, 9]

largest = arr[0]
secondLargest = -1

for i in range(1, len(arr)):
    if(arr[i]>largest):
        largest = arr[i]

for i in range(len(arr)):
    if(arr[i]>secondLargest and arr[i]!=largest):
        secondLargest = arr[i]
        
print(secondLargest)