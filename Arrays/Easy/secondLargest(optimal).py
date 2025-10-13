arr = [3, 2, 1, 5, 2, 7, 9]

largest = arr[0]
secondLargest = -1

for i in range(1, len(arr)):
    if(arr[i]>largest):
        secondLargest = largest
        largest = arr[i]
    elif(arr[i]<largest and arr[i]>secondLargest):
                secondLargest = arr[i]
        
print(secondLargest)    