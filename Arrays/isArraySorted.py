arr1 = [3, 2, 1, 5, 2, 7]
arr2 = [1, 2, 3, 4, 5, 6]

def isArraySorted(arr1):
    for i in range(1, len(arr1)):
        if(arr1[i]>=arr1[i-1]):
            pass
        else:
            return False
    return True
        
print(isArraySorted(arr2))