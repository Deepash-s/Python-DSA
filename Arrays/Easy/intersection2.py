arr1 = [1, 2, 2, 3, 3, 4, 5, 6]
arr2 = [2, 3, 3, 5, 6, 6, 7]
n1 = len(arr1)
n2 =  len(arr2)
intersection  = []
i, j = 0, 0

while i<n1 and j<n2:
    if arr1[i] == arr2[j]:
        intersection.append(arr1[i])
        i += 1
        j += 1
    elif(arr1[i]<arr2[j]):
        i += 1
    elif(arr1[i]>arr2[j]):
        j += 1
        
        
print(intersection)